from flask import Flask, render_template , session , request, url_for, g, request, redirect ,flash,send_from_directory
from database import get_db,close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps 

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"]= "this-isn't-my-secret-key"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


@app.before_request
def logged_in_user():

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login",next=request.url) )
        return view(*args, **kwargs)
    return wrapped_view

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id= form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db=get_db()
        possible_clashing_user = db.execute("""SELECT *
                                            FROM user
                                            WHERE user_id=?;""",(user_id,)).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("User is already taken!")
        else:
            db.execute("""INSERT INTO user(user_id,password)
                       VALUES(?,?); """,
                       (user_id,generate_password_hash(password)))
            db.commit()
            return redirect( url_for("login"))
    return render_template("register.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user_id= form.user_id.data
        password= form.password.data
        db= get_db()
        possible_clashing_user = db.execute("""SELECT *
                                            FROM user
                                            WHERE user_id = ?;""",
                                            (user_id,)).fetchone()
        if possible_clashing_user is None:
            form.user_id.errors.append("Account is not exists! ")
        elif not check_password_hash(possible_clashing_user["password"],password):
            form.user_id.errors.append("Incorrect password!")
        else:
            session.clear()
            session["user_id"] = user_id
            next_page= request.args.get("index")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)
    return render_template("login.html",form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index") )

@app.route("/energy_use",methods=["GET","POST"])
def energyUse():
    form = EnergyUseForm()
    if form.validate_on_submit():
        selections = form.selections.data
        total = 0 
        for i in selections :
            print(i)
            if i == "lighting":
                total += 100
            elif i == "heating":
                total += 1000
            elif i == "landry":
                total += 1000
            elif i == "entertainment equipments":
                total +=  1100
            elif i == "fridge":
                total += 1000
            else:
                total += 1200
                
        if total >= 5000 :    
            return render_template("advices.html")
                    
            
    return render_template("energyUse.html", form = form)


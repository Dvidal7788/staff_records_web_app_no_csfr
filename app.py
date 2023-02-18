from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_mail import Mail, Message
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure e-mail
app.config['MAIL_DEFAULT_SENDER'] = 'dvidal7788@gmail.com'
app.config['MAIL_USERNAME'] = 'dvidal7788@gmail.com'
app.config['MAIL_PASSWORD'] = 'oxbbivllbzottirw'
app.config['MAIL_PORT'] = 587 # TCP port
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = True # Use encryption
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


class ExportCriteria():
    def __init__(self, department, sort_by):
        self.department = department
        self.sort_by = sort_by

# Globals
export_criteria = ExportCriteria('all', 'emp_id')
departments_all = False
staff_added = False
email_sent = False

def login_required(f):
    # Decorate routes to require login.
    # https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    else:
        return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():

    # GET
    if request.method == 'GET':
        return render_template('register.html')

    # POST
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # Confirm form filled out
        if not username and not password and not confirmation:
            return render_template('error.html', message="You left the form blank")
        elif not username:
            return render_template('error.html', message="Username field left blank")
        elif not password:
            return render_template('error.html', message="Password field left blank")
        elif not confirmation:
            return render_template('error.html', message="Password Confirmation field left blank")

        # Make sure username is not already taken
        db = sqlite3.connect("staff.db")
        tmp_cursor = db.execute("SELECT username FROM users")

        for tmp_tuple in tmp_cursor:
            if username == tmp_tuple[0]:
                return render_template('error.html', message="The username you entered is already taken")

        # Verify password meets criteria
        pw_criteria1 = 'Password must have at least 8 characters.'
        pw_criteria2 = '(At least 1 uppercase letter, 1 lowercase letter, 1 number & 1 special character.)'

        if len(password) < 8:
            return render_template('error.html', message=pw_criteria1, message2=pw_criteria2)

        pw_letter = False
        pw_number = False
        pw_special_char = False
        pw_upper = False
        pw_lower = False

        for char in password:
            if char.isalpha():
                pw_letter = True
                if char.isupper():
                    pw_upper = True
                else:
                    pw_lower = True
            elif char.isnumeric():
                pw_number = True
            elif not char.isalnum():
                pw_special_char = True

        if not pw_letter or not pw_number or not pw_special_char or not pw_upper or not pw_lower:
            return render_template('error.html', message=pw_criteria1, message2=pw_criteria2)


        # Password matches confirmation
        if password != confirmation:
            return render_template('error.html', message="The password you entered does not match your confirmation")

        # --- Add user to database ---
        # Create new user_id
        tmp_cursor = db.execute("SELECT MAX(user_id) FROM users")
        for tmp_tuple in tmp_cursor:
            if tmp_tuple[0] == None:
                new_id = 0
            else:
                new_id = tmp_tuple[0] + 1

        cur = db.cursor()
        cur.execute("INSERT INTO users VALUES(?,?,?)", (new_id, username, generate_password_hash(password)))
        db.commit()

        return render_template('confirmation.html', message='Registration Successful!', message2='You may now log in.')


@app.route("/login", methods=['GET', 'POST'])
def login():

    # GET
    if request.method == 'GET':
        return render_template('login.html')

    # POST
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        db = sqlite3.connect("staff.db")
        tmp_cursor = db.execute("SELECT * FROM users WHERE username = ?", (username,))

        user_found = False
        for tmp_tuple in tmp_cursor:
            if username == tmp_tuple[1]:
                user_found = True
                session['user_id'] = tmp_tuple[0]
                session['username'] = tmp_tuple[1]
                hash = tmp_tuple[2]

        if not user_found:
            return render_template('error.html', message='Username incorrect.', message2='Try again.')

        if not check_password_hash(hash, password):
            session.clear()
            return render_template('error.html', message='Password incorrect.', message2='Try again.')

        return redirect("/")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


@app.route("/add_new_staff", methods=['GET', 'POST'])
@login_required
def add_new_staff():
    global staff_added

    # GET
    if request.method == 'GET':
        if staff_added:
            # Reset staff_added before rendering template
            staff_added = False

            return render_template('add_new_staff.html', staff_added=True, username=session['username'])
        else:
            return render_template('add_new_staff.html', staff_added=False, username=session['username'])


    # POST
    else:
        name = request.form.get('name')
        department = request.form.get('department')
        start_date = request.form.get('start_date')

        if not name and not department and not start_date:
            return render_template('error.html', message="Form blank", username=session['username'])
        elif not name:
            return render_template('error.html', message="Please enter name of new staff member", username=session['username'])
        elif not department:
            return render_template('error.html', message="Please enter department", username=session['username'])
        elif not start_date:
            return render_template('error.html', message="Please enter start date", username=session['username'])

        print(start_date)

        # Get max emp_id
        db = sqlite3.connect("staff.db")
        tmp_cursor = db.execute("SELECT MAX(emp_id) FROM staff")
        for tmp_tuple in tmp_cursor:
            if tmp_tuple[0] == None:
                new_id = 0
            else:
                new_id = tmp_tuple[0] + 1

        cur = db.cursor()
        cur.execute("INSERT INTO staff VALUES (?,?,?,?)", (new_id, name, department, start_date))
        db.commit()

        staff_added = True

        return redirect("/add_new_staff")


@app.route("/all_staff")
@login_required
def all_staff():
    global departments_all

    departments_all = True
    return redirect("/departments")


@app.route("/departments", methods=['GET', 'POST'])
@login_required
def departments():
    global departments_all
    global export_criteria
    global email_sent

    # Retrieve departments from database
    db = sqlite3.connect("staff.db")
    tmp_cursor = db.execute("SELECT DISTINCT(department) FROM staff")
    departments = []
    for tmp_tuple in tmp_cursor:
        departments.append(tmp_tuple[0])

    departments.sort()

    # GET
    if request.method == 'GET' and not departments_all:
        if email_sent:
            email_sent = False
            return render_template('departments.html', departments=departments, username=session['username'], email_sent=True)
        else:
            return render_template('departments.html', departments=departments, username=session['username'], email_sent=False)

    # POST
    elif request.method == 'POST' or departments_all:
        department = request.form.get('department')
        if departments_all:
            department = 'all'
            departments_all = False

        # SQL
        staff = access_sql_db(department)

        # Sort
        sort_by = request.form.get('sort_by')
        if sort_by:
            staff.sort(key=lambda x: x[sort_by])
        else:
            sort_by = 'emp_id'

        # Update export criteria
        export_criteria.department = department
        export_criteria.sort_by = sort_by

        return render_template('departments.html', departments=departments, staff=staff, department_selected=department, sort_by=sort_by, display_results=True, username=session['username'])


@app.route("/csv_export", methods=['POST'])
@login_required
def csv_export():
    global export_criteria
    global email_sent

    # Retrieve info from database
    staff = access_sql_db(export_criteria.department)

    # Create filename
    filename = f'{export_criteria.department}_{datetime.now()}.csv'

    # Create list of columns
    columns = []
    for key in staff[0]:
        columns.append(key)

    num_of_columns = len(columns)
    # Write to new csv file
    with open(filename, 'w') as file:
        # Write header
        for i in range(num_of_columns):
            if i < num_of_columns-1:
                file.write(f'{columns[i]},')
            else:
                file.write(f'{columns[i]}\n')

        # Write rest of file
        for person in staff:
            i = 0
            for key in person:
                if i < len(columns)-1:
                    file.write(f'{person[key]},')
                else:
                    file.write(f'{person[key]}\n')
                i += 1

    # E-mail
    email = request.form.get('email')
    message = Message('The csv file you requested', recipients=[email])

    if export_criteria.department != 'all':
        message.body = f"Here is the csv file you requested of:\nThe '{export_criteria.department}' Department sorted by '{export_criteria.sort_by}'."
    else:
        message.body = f"Here is the csv file you requested of:\n'{export_criteria.department} departments' sorted by '{export_criteria.sort_by}'."

    # Attach
    with app.open_resource(filename) as csv_fp:
        message.attach(filename, 'application/csv', csv_fp.read())

    # Send e-mail
    mail.send(message)

    # Remove csv
    os.remove(filename)

    # Email confirmation
    email_sent = True

    return redirect("/departments")



def access_sql_db(department):

    # Retrieves info from selected department
        db = sqlite3.connect("staff.db")

        if department == 'all':
            tmp_cursor = db.execute("SELECT * FROM staff")
        else:
            tmp_cursor = db.execute("SELECT * FROM staff WHERE department = ?", (department,))

        staff = []
        for tmp_tuple in tmp_cursor:
            staff.append({'emp_id': tmp_tuple[0], 'name': tmp_tuple[1], 'department': tmp_tuple[2], 'start_date': tmp_tuple[3]})

        # Return list of dicts
        return staff

#import flask_mysqldb
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from mysql.connector import cursor

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

"""conn = connector.connect(host="localhost",
                         user="root",
                         password="",
                         database="users",
                         auth_plugin='mysql_native_password')"""
#cursor = conn.cursor()
#mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('loginp.html')


@app.route("/login")
def login():
    return render_template('loginp.html')


@app.route("/signupP", methods=['POST', 'get'])
def signup():
    if request.method == "POST":
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['cpassword']
        """cursor = conn.cursor()"""
        cursor = mysql.connect().cursor()
        cursor.execute(f"insert into users values('{firstname}','{lastname}','{email}','{password}','{confirmpassword}')")
        #mysql.connect().commit()
        cursor.connection.commit()
        cursor.close()
        #mysql.connect().cursor()
        return render_template('loginp.html')
    else:
        return render_template('signupP.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mysql.connect().cursor()
        cursor.execute(" SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}' ".format(email, password))
        users = cursor.fetchall()
        print(users)
        if not users:
            cursor.close()
            return "Username or Password is wrong"
        else:
            #return "Logged in successfully"
            return render_template('landing.html')
    else:
        return render_template('loginp.html')

@app.route("/forgotpasswd")
def forgotpasswd():
    return render_template('forgotpassP.html')

@app.route("/email_validation" , methods=['POST'])
def email_valid():
    if request.method == "POST":
        email = request.form.get('email')
        cursor = mysql.connect().cursor()
        cursor.execute(" select email from users where 1 ".format(email))
        users = cursor.fetchall()
        print(users)
        if not users :
            cursor.close()
            return render_template('signupP.html')
        else:
            #return "Logged in successfully"
            return render_template('passwd_reset.html')
    

@app.route("/passwd_reset" , methods=['POST', 'GET'])
def passwd_reset():
    if request.method == "POST":
        
        password = request.form['password']
        confirmpassword = request.form['cpassword']
        """cursor = conn.cursor()"""
        cursor = mysql.connect().cursor()
        cursor.execute(" UPDATE `users` SET `password`='4321',`cpassword`='4321' WHERE 1")
        
        mysql.connect().commit()
        #mysql.connect().commit()
        cursor.connection.commit()
        cursor.close()
        #mysql.connect().cursor()
        return render_template('loginp.html')
    else:
        return render_template('signupP.html')


# add patient user
app.route('/add_user', methods=['POST', 'GET'])


def add_user():

    if request.method == 'POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['cpassword']
        cursor = mysql.connect().cursor()
        cursor.execute(''' INSERT INTO `users` (`firstname`,`lastname`,`email`,`password`,`confirmpassword`)
        5 VALUES(`{}`,`{}`,`{}`,`{}`,`{}`)'''.format(firstname, lastname, email, password, confirmpassword))
        mysql.connect().commit()
        cursor.close()
        return f"Done!!"
    else:
        return render_template('loginp.html')

# add doctor

app.run(debug=True)

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


@app.route("/index")
def home():
    return render_template('index.html')


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
        cursor.execute(
            f"insert into users values('{firstname}','{lastname}','{email}','{password}','{confirmpassword}')"
        )
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
        cursor.execute(
            " SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}' "
            .format(email, password))
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


@app.route("/email_validation", methods=['POST'])
def email_valid():
    if request.method == "POST":
        email = request.form.get('email')
        cursor = mysql.connect().cursor()
        cursor.execute(" select email from users where 1 ".format(email))
        users = cursor.fetchall()
        print(users)
        if not users:
            cursor.close()
            return render_template('signupP.html')
        else:
            #return "Logged in successfully"
            return render_template('passwd_reset.html')


@app.route("/passwd_reset", methods=['POST', 'GET'])
def passwd_reset():
    if request.method == "POST":

        password = request.form['password']
        confirmpassword = request.form['cpassword']
        """cursor = conn.cursor()"""
        cursor = mysql.connect().cursor()
        cursor.execute(
            " UPDATE `users` SET `password`='4268',`cpassword`='4268' WHERE 1")

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
        cursor.execute(
            ''' INSERT INTO `users` (`firstname`,`lastname`,`email`,`password`,`confirmpassword`)
        5 VALUES(`{}`,`{}`,`{}`,`{}`,`{}`)'''.format(firstname, lastname,
                                                     email, password,
                                                     confirmpassword))
        mysql.connect().commit()
        cursor.close()
        return f"Done!!"
    else:
        return render_template('loginp.html')


# add doctor
@app.route("/signupd", methods=['POST', 'get'])
def signupd():
    if request.method == "POST":
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['cpassword']
        """cursor = conn.cursor()"""
        cursor = mysql.connect().cursor()
        cursor.execute(
            f"insert into docusers values('{firstname}','{lastname}','{email}','{password}','{confirmpassword}')"
        )
        #mysql.connect().commit()
        cursor.connection.commit()
        cursor.close()
        #mysql.connect().cursor()
        return render_template('logind.html')
    else:
        return render_template('signupd.html')


@app.route("/logind")
def logind():
    return render_template('logind.html')


@app.route('/login_validation_doc', methods=['POST'])
def login_validation_doc():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        cursor = mysql.connect().cursor()
        cursor.execute(
            " SELECT * FROM docusers WHERE email LIKE '{}' AND password LIKE '{}' "
            .format(email, password))
        users = cursor.fetchall()
        print(users)
        if not users:
            cursor.close()
            return "Username or Password is wrong"
        else:
            #return "Logged in successfully"
            return render_template('doctorlanding.html')
    else:
        return render_template('logind.html')


app.route('/add_user_doc', methods=['POST', 'GET'])


def add_user_doc():

    if request.method == 'POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['cpassword']
        cursor = mysql.connect().cursor()
        cursor.execute(
            f"insert into docusers values('{firstname}','{lastname}','{email}','{password}','{confirmpassword}')"
        )
        mysql.connect().commit()
        cursor.close()
        return f"Done!!"
    else:
        return render_template('logind.html')


#contact us
@app.route("/contactus", methods=['POST','GET'])
def contactus():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor = mysql.connect().cursor()
        cursor.execute(
            f"insert into contactus values('{name}','{email}','{message}')"
        )

        cursor.connection.commit()
        cursor.close()

        #cursor.execute(
        #    f"insert into docusers values('{name}','{email}','{message}')"
        #)
        return f"done!!"
    else:
        return render_template('contact.html')

@app.route("/about")
def home1():
    return render_template('about.html')

@app.route("/services")
def home2():
    return render_template('services.html')

@app.route("/contact")
def home3():
    return render_template('contact.html')

@app.route("/covid")
def home4():
    return render_template('covid.html')

@app.route("/covidlandig")
def home5():
    return render_template('covidlandig.html')

@app.route("/doctorlanding")
def home6():
    return render_template('doctorlanding.html')

@app.route("/general")
def home7():
    return render_template('general.html')




app.run(debug=True)

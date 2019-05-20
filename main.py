from flask import Flask, flash , redirect, request, render_template

app = Flask(__name__)
app.secret_key = 'abc123'

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html', title='User SignUp!')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    error_msg = False
    
    username_error = "Please enter a valid username!"
    password_error = "Must contain 3-20 characters!"
    verify_error = "Password does not match!"
    email_error = "Please enter a valid email!"

    #if not username or not password or not verify:
        #return username_error
    #elif not '@' in email or not '.' in email:
        #return email_error
    #else:
        #return "<H1>Welcome " + username + "!</H1>"
    if username == "" :
        error_msg = True
        flash(username_error)
    elif len(username)<=3 or len(username) > 20:
        error_msg = True
        flash(username_error)
    elif " " in username:
        flash("Username can't contain spaces")


    if password == "":
        error_msg = True
        flash(password_error)
    elif len(password)<3 or len(password) > 20:
        error_msg = True
        flash(password_error)
    elif " " in password:
        error_msg = True
        flash("Password can't contain spaces")


    if verify == "" or verify !=password:
        error_msg = True
        flash(verify_error)

    if email != "":
        if not "@" in email or not "." in email:
            # return email_error
            error_msg = True
            flash(email_error)
    if error_msg==True:
        return redirect('/')
    
    else:
        return render_template('welcome.html',username=username)
#if error_msg:
    #redir
#el
    #template
app.run()
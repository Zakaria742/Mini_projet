from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/submit-form", methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    msg = request.form['msg']
    print(f'Name: {name}\nEmail: {email}\nmsg: {msg}\n')
    return render_template("submit-success.html", name=name, email=email, msg=msg)

if __name__ == '__main__':
    app.run(debug = True)

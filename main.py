from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route('/create', methods=['GET', 'POST'])
def homepage():
  if request.method == 'GET':
    return render.template('home.html')
  
  else:
    name = request.form['name']
    password = request.form['pass']
    email = request.form['mail']

    add_user(name, email, password)
    return render_template('home.html', n=name, p=password, e=email)

@app.route('/log', methods=['GET', 'POST'])
def pagehome():
  if request.method == 'GET':
    return render_template(home.html)
  
  else:

    email = request.form['mailo']
    password = request.form['passo']
    print(password)

    user = get_user_by_email(email)
    print(user)
    print(user.password)
    if (user != None) and (user.password == password):
        return render_template('home.html',ea=email, ps=password)
    else:
      return render_template('signlog.html', ea=email, ps=password)
 


@app.route("/")
def singlog():
  return render_template("singlog.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/ringring")
def ringring():
    return render_template("ringring.html")

@app.route("/waterloo")
def waterloo():
    return render_template("waterloo.html")

@app.route("/abba")
def abba():
    return render_template("abba.html")

@app.route("/arrival")
def arrival():
    return render_template("arrival.html")

@app.route("/abbathealbum")
def abbathealbum():
    return render_template("abbathealbum.html")

@app.route("/voulezvous")
def voulezvous():
    return render_template("voulezvous.html")

@app.route("/supertrouper")
def supertrouper():
    return render_template("supertrouper.html")

@app.route("/thevisitors")
def thevisitors():
    return render_template("thevisitors.html")

@app.route("/voyage")
def voyage():
    return render_template("voyage.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
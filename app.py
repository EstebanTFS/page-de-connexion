from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validation des informations de connexion
    if username == 'mon_nom_utilisateur' and password == 'mon_mot_de_passe':
        return redirect('/success')
    else:
        print("Nom d'utilisateur entré :", username)
        print("Mot de passe entré", password)
        return redirect('/error')
@app.route('/success')
def success():
	return 'Connexion réussie!'

@app.route('/error')
def error():
	return 'Erreur de connexion! Veuillez vérifier vos informations de connexion.'

if __name__ == '__main__':
	app.run(debug=True)

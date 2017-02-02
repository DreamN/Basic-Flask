##############################################################
#         Basic Flask Course @tedESL ESL, KMITL              #
#              Github:https://github.com/DreamN/Basic-Flask  #
##############################################################

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
	y = "foo"
	return render_template('home.html', x=y)

@app.route('/game')
def myFavGame():
	game_list = ['Mario', 'Pokemon', 'Pacman', 'Rockman', 'Megaman']
	return render_template('favGame.html', game_list=game_list)

@app.route('/greeting/<string:name>/')
def greeting(name):
	name = name[::-1]
	return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)

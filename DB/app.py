from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<string:artist>/<string:album>', methods=['GET'])
def get_review(artist, album):
	
	return artist + " " + album 

@app.route('/')
def index():
	return "Hi there\n"

if __name__ == '__main__':
	app.run(debug=True)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}), 404)
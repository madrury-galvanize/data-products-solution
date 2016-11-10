from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET'])
def submit():
    return render_template('submit.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

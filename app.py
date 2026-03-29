from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/world')
def world():
    return render_template('world.html')

@app.route('/future')
def future():
    return render_template('future.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

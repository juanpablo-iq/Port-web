from flask import Flask
from flask import render_template
from data import Data, Experience, Education, Skills, Interests, Awards

app = Flask(__name__ )

@app.route('/')
def index():
    return render_template('/index.html',Data=Data,Experience=Experience,Education=Education, Skills=Skills, Interests=Interests,Awards=Awards)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
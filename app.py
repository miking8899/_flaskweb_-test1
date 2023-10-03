from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    
    return  "<p>Hello, first test S flask World!</p><h2></h2><p> 這是另外一個段落,還有個段落</p><h3></h3><p>第2個段落</p>"

@app.route("/hello_world")
def hello_world():
    return "<p>第2個網頁</p> <h1></h1><p>另一個天地,天公仔</p>"
    
    

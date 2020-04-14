from flask import Flask

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/home")
def hello_world2():
    return "Hello home"

if __name__=="__main__":
    app.run(debug=True)


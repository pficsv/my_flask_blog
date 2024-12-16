from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Welcome to My Blog.\nThis is a cool place to fuckin chill and drink. I welcome you with open arms."

if __name__ == '__main__':
    app.run(debug=True)

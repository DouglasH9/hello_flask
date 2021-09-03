from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:phrase>')
def number_phrase(num, phrase):
    message = ""
    for i in range (0, num):
        message += phrase
    return message


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
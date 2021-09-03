from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play/<int:times>")
def displayBox():
    return render_template('playground.html', 'times')

# @app.route('/play/<int:times>')
# def mult_boxes():
#     return render_template('playground.html', times)

if __name__=="__main__":
    app.run(debug=True)
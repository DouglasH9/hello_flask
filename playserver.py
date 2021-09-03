from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def displayBox():
    return render_template('playground.html', times=3, color= 'blue')

@app.route('/play/<int:times>')
def mult_boxes(times):
    return render_template('playground.html', times=times, color= 'blue')

@app.route('/play/<int:times>/<string:color>')
def num_color_boxes(times, color):
    return render_template('playground.html', times=times, color=color)

if __name__=="__main__":
    app.run(debug=True)
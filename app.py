from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
@app.route("/analyze")
def analyze():
    plot = '<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plot.ly/~misaeljonathann/1.embed"></iframe>'
    return render_template("index.html", data=plot)

@app.route("/")
def main():
    return "HOME"

@app.route("/get_text", methods=['POST'])
def get_text():
    text = request.form.get('text')
    data = {'text' : text }
    data = jsonify(data)
    return data

if __name__ == "__main__":
    app.run(debug=True) #jangan lupa hapus debug
 
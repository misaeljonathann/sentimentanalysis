from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from Analisis import analysis

app = Flask(__name__)
CORS(app)
 
@app.route("/")
def analyze():
    dictio = {}
    dictio["jambu"] = 100
    dictio["wombo"] = 30
    dictio["gilo"] = 10
    return render_template("index.html", dict=dictio)

@app.route("/get_text", methods=['POST'])
def get_text():
    text = request.form.get('text')
    obj = analysis.SentimentAnalyzer()
    returnedText = obj.main(str(text).lower())
    if int(returnedText) > 0:
        hasil = "Positif"  
    elif int(returnedText) < 0:
        hasil = "Negatif"
    else:
        hasil = "Netral"
    data = {'nilai' : returnedText, 'hasil' : hasil}
    data = jsonify(data)
    return data

if __name__ == "__main__":
    app.run(debug=True) #jangan lupa hapus debug
 
from flask import Flask, request, render_template

app = Flask(__name__)

def analyze_sentiment(text):
    if "good" in text.lower():
        return "Positivee"
    else:
        return "Negative"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        sentiment = analyze_sentiment(text)
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
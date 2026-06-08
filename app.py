from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)
UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    uploaded_file = request.files.get("image")
    if uploaded_file and uploaded_file.filename:
        save_path = UPLOAD_DIR / uploaded_file.filename
        uploaded_file.save(save_path)
        return render_template("result.html", filename=uploaded_file.filename, prediction="Tumor detected")
    return render_template("result.html", filename=None, prediction="No image uploaded")


if __name__ == "__main__":
    app.run(debug=True)

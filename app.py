from flask import Flask, render_template, request
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

classes = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

model = models.resnet50(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(classes)
)

model.load_state_dict(
    torch.load(
        "model/brain_tumor_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)

    with torch.no_grad():

        outputs = model(image)

        _, predicted = torch.max(outputs, 1)

    return classes[predicted.item()]

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["image"]

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(file_path)

        prediction = predict_image(file_path)

        return render_template(
            "result.html",
            prediction=prediction,
            image=file.filename
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
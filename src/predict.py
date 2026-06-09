import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# --------------------------------------------------
# Classes
# --------------------------------------------------

classes = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]

# --------------------------------------------------
# Device
# --------------------------------------------------

device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

print("Using Device:", device)

# --------------------------------------------------
# Load ResNet50 Model
# --------------------------------------------------

model = models.resnet50(weights=None)

model.fc = nn.Linear(
    model.fc.in_features,
    len(classes)
)

# --------------------------------------------------
# Load Trained Weights
# --------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "brain_tumor_model.pth"
)

print("Loading Model From:")
print(MODEL_PATH)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)

model.to(device)
model.eval()

# --------------------------------------------------
# Image Transform
# --------------------------------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)

    with torch.no_grad():

        outputs = model(image)

        _, predicted = torch.max(outputs, 1)

    return classes[predicted.item()]

# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    image_path = input("Enter Image Path: ").strip().replace('"', '')

    print("Image Path:", image_path)
    print("File Exists:", os.path.exists(image_path))
    
    prediction = predict_image(image_path)

    print("\nPrediction:", prediction)
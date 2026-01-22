from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision import models

# Load ResNet WITHOUT pretrained weights (offline-safe)
model = models.resnet18(weights=None)
model.eval()

# Remove final classification layer
model = torch.nn.Sequential(*list(model.children())[:-1])

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def image_to_vector(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        vector = model(image)

    return vector.squeeze().tolist()

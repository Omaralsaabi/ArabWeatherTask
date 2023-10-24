import torch 
import torchvision 
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
from PIL import Image
import os
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model_path = os.path.join(os.getcwd(), 'model/resnet18_finetuned.pth')

class_names = ['dew', 'fogsmog', 'frost', 'glaze', 'hail', 'lightning', 'rain', 'rainbow', 'rime', 'sandstorm', 'snow']

def load_fine_tuned_resnet():
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.eval()
    model.to(DEVICE)
    return model

def predict_image(image):
    transform = transforms.Compose([
    transforms.Resize((300, 400)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
    image = Image.open(image)
    image = transform(image).unsqueeze(0).to(DEVICE)
    model = load_fine_tuned_resnet()
    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
        return class_names[preds[0].item()]
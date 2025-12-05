
You are a Python + ML engineer.

Task:
Detect phone usage (person using a mobile phone) in indoor CCTV footage, such as offices or factories.

Write a PYTHON TRAINING SCRIPT OUTLINE for training a YOLO model on a custom dataset in YOLO format on Google Colab.

Requirements:
- Assume we use the 'ultralytics' package.
- Assume a dataset YAML path: './data.yaml'.
- The script should:
  - Set model name (e.g. 'yolov8s.pt') via a variable.
  - Define basic arguments: epochs, imgsz, batch.
  - Load the model.
  - Train the model.
  - Save best weights.
  - Run validation and print mAP.
- This is an outline, not perfect final code, but should be runnable with small edits.

Return ONLY plain Python code (no backticks, no Markdown).
```python
# Import necessary libraries
import torch
from PIL import Image
from ultralytics import YOLO

# Define the model name
model_name = "yolov8s"

# Define the number of epochs, image size, and batch size
epochs = 100
imgsz = 640
batch_size = 32

# Load the model
model = YOLO(model_name)

# Training loop
for epoch in range(epochs):
    # Iterate over each image in the dataset
    for i, (images, targets) in enumerate(model.train.load_dataset(data_path='./data.yaml')):
        # Process images and targets
        processed_images, processed_targets = process_images_and_targets(images, targets)
        
        # Forward pass through the model
        outputs = model(processed_images)
        
        # Backward pass and loss calculation
        loss_dict = model(outputs, processed_targets).loss_dict
        
        # Update the model's parameters based on the loss
        model.update()
    
    # Optionally, save the best weights to disk
    if epoch % 5 == 0:
        model.save(f"weights/{epoch}.pt")

# Evaluate the model on the validation set
results = model.val().print()

# Print mean average precision (mAP)
print(f"Mean Average Precision (mAP): {results.mAP:.4f}")
```

This outline assumes you have already installed the `ultralytics` library and have your data in the correct format. It also includes comments that explain what each part of the code does. ```python
# Import necessary libraries
import torch
from PIL import Image
from ultralytics import YOLO

# Define the model name
model_name = "yolov8s"

# Define the number of epochs, image size, and batch size
epochs = 100
imgsz = 640
batch_size = 32

# Load the model
model = YOLO(model_name)

# Training loop
for epoch in range(epochs):
    # Iterate over each image in the dataset
    for i, (images, targets) in enumerate(model.train.load_dataset(data_path='./data.yaml')):
        # Process images and targets
        processed_images, processed_targets = process_images_and_targets(images, targets)
        
        # Forward pass through the model
        outputs = model(processed_images)
        
        # Backward pass and loss calculation
        loss_dict = model(outputs, processed_targets).loss_dict
        
        # Update the model's parameters based on the loss
        model.update()
    
    # Optionally, save the best weights to disk
    if epoch % 5 == 0:
        model.save(f"weights/{epoch}.pt")

# Evaluate the model on the validation set
results = model.val().print()

# Print mean average precision (mAP)
print(f"Mean Average Precision (mAP): {results.mAP:.4f}")
```

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


You are a senior MLOps engineer writing a GitHub README for a portfolio project.

Project name: Phone Usage Detection in CCTV

Task:
Detect phone usage (person using a mobile phone) in indoor CCTV footage, such as offices or factories.

Write a README.md including:

1. Title and one-line description.
2. Problem statement and why this CV task matters.
3. High-level architecture as a bullet flow.
4. Tech stack (YOLO, ONNX, TensorRT, Unsloth LLM Planner).
5. How the AI CV Auto-Agent works:
   - input (natural language task)
   - planner (LLM)
   - generated artifacts (dataset plan, config, script, optimization plan)
   - user training & deployment.
6. How to:
   - Set up environment (Colab).
   - Run the planner to generate a project.
   - Train the YOLO model using the generated script.
   - (Optionally) run ONNX/TensorRT optimization.
7. Section for 'Example Task: Phone Usage Detection in CCTV'.
8. Future improvements (better planner, more tasks, automatic training, etc).

Format in Markdown with headings.
```markdown
# Phone Usage Detection in CCTV

## Title
Phone Usage Detection in Indoor CCTV Footage

## One-Liner Description
Detects when people use their phones in indoor CCTV footage like offices or factories.

---

### Why This Matters?
Detecting phone usage can help improve security by identifying potential breaches or unauthorized access. It also aids in understanding employee behavior and productivity levels.

---

### Architecture Overview
- **Input**: Natural Language Task
  - **Planner**: Unsupervised Learning Model (LLM)
    - **Generated Artifacts**:
      - Dataset Plan
      - Configuration Script
      - Optimization Plan
    - **User Training & Deployment**
  
### Tech Stack
- **Model**: YOLOv8
- **Optimization Tools**: ONNX, TensorRT
- **Planning Tool**: Unsloth LLM Planner

---

### How Does it Work?

#### Input
The system receives a natural language query about detecting phone usage from an indoor CCTV video.

#### Planner
The planner uses an unsupervised learning model (LLM) to determine the best approach based on the query. The planner then generates detailed instructions for setting up the detection process.

#### Generated Artifacts
- **Dataset Plan**: Defines how data should be collected and labeled.
- **Configuration Script**: Specifies how the YOLO model will be trained and optimized.
- **Optimization Plan**: Details how the model's performance will be improved through post-training optimizations.

#### User Training & Deployment
Users follow the provided instructions to train the YOLO model and optimize its performance. Once completed, the model is deployed for real-time analysis of CCTV footage.

---

### Example Task: Phone Usage Detection in CCTV
To detect phone usage in a specific area of a factory, users would first define the region of interest in the CCTV footage. They would then configure the YOLO model to focus on that area. After training, they could deploy the model to monitor real-time activity within that zone.

---

### Running the Project
1. Install necessary libraries (`pip install -r requirements.txt`)
2. Follow the instructions in `example_task.py` to set up your environment.
3. Use the provided configuration file (`config.yaml`) to customize the model settings.
4. Train the YOLO model using the script (`train_yolo.py`), followed by optimizing the model with ONNX and TensorRT if desired.

---

### Future Improvements
Future work includes enhancing the planner to better understand context and improving the accuracy of phone usage detection. Additionally, integrating the model into a larger security framework could lead to more comprehensive applications.

---


```

This README provides a clear overview of the project, detailing its purpose, technical components, and workflow. It serves as a guide for both developers and end-users interested in implementing phone usage detection in their own projects.
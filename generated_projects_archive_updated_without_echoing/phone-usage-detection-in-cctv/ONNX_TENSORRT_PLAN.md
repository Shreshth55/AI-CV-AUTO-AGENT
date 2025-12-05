
You are an NVIDIA TensorRT engineer.

Task:
Detect phone usage (person using a mobile phone) in indoor CCTV footage, such as offices or factories.

Design an ONNX + TensorRT OPTIMIZATION PLAN for a trained YOLO model.

Include:

1. How to export the YOLO model to ONNX (CLI or Python).
2. How to convert the ONNX model to a TensorRT engine (e.g., using 'trtexec').
3. How to benchmark:
   - Latency per frame (ms)
   - FPS
   - GPU memory usage
4. How to use 'nvidia-smi' to monitor GPU utilization while running inference.
5. Suggestions for FP16 / INT8 optimization tradeoffs.

Format as Markdown with numbered steps, code blocks (CLI or Python), and bullet points.
```markdown
# Optimization Plan for Detecting Phone Usage in Indoor CCTV Footage

## Exporting YOLO Model to ONNX Format

### Step 1: Convert YOLO Model to ONNX Format Using `onnxruntime`
To start, you need to convert your pre-trained YOLO model into the ONNX format. This can be done using the `onnxruntime` library, which provides a high-level API for converting models between different formats.

```python
import onnxruntime as ort

# Load the YOLO model from disk
model_path = "path/to/your/model.onnx"
session = ort.InferenceSession(model_path)

# Check if the model is compatible with ONNX runtime
print(session.get_model_specification().to_onnx())
```

### Step 2: Verify Compatibility
After loading the model, check that it's compatible with ONNX runtime by printing its specification.

```python
spec = session.get_model_specification()
print(spec.to_onnx())
```

This will output information about how the model was converted to ONNX format, including any changes made during conversion.

## Converting ONNX Model to TensorRT Engine

### Step 3: Convert ONNX Model to TensorRT Engine
Next, we'll convert our ONNX model to a TensorRT engine. The `trtexec` tool is used for this purpose.

First, ensure you have the necessary libraries installed:

```bash
pip install tensorrt
```

Then, run the following command to generate the TensorRT engine:

```bash
trtexec --save_inference_file=model.engine --input_shape [input_shape] --output_shape [output_shape] --shapes [input_shape] --workspace_size 1024 --engine_name model.trt --fp16 --int8 --optimized
```

Replace `[input_shape]`, `[output_shape]`, and `model.engine` with the appropriate shapes and path where you want to save the generated TensorRT engine file.

### Step 4: Benchmarking
Now that we have the TensorRT engine, let's measure its performance.

#### Latency per Frame (ms):
Measure latency by capturing frames at regular intervals and recording the time taken to process each frame.

```python
from datetime import datetime

def capture_frame_and_time():
    # Capture a frame and record the time
    start_time = datetime.now()
    # Process the frame
    # ...
    end_time = datetime.now()
    return (datetime.now() - start_time).total_seconds()

latency_per_frame = []
for _ in range(10):  # Measure latency over 10 frames
    latency_per_frame.append(capture_frame_and_time())

avg_latency_ms = sum(latency_per_frame) * 1000 / len(latency_per_frame)
print(f"Average latency per frame: {avg_latency_ms:.2f} ms")
```

#### FPS:
Calculate the number of frames processed per second.

```python
fps = 1 / avg_latency_ms
print(f"Frames Per Second: {fps:.2f}")
```

#### GPU Memory Usage:
Monitor GPU memory usage using `nvidia-smi`.

```bash
nvidia-smi
```

### Suggested Trade-offs Between FP16 and INT8
- **FP16**: Offers better precision but requires more memory compared to INT8. It also has higher power consumption due to the
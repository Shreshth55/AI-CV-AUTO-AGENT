
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

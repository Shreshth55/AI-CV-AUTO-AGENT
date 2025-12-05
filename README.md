# AI CV Auto-Agent

## Overview
A system that takes a natural-language description of a computer vision task
(e.g., "detect workers using phones in CCTV footage") and automatically generates:

- A dataset plan
- A YOLO model configuration
- A training script outline
- An ONNX/TensorRT optimization plan
- A ready-to-publish README for that task

Powered by an LLM that can later be fine-tuned with Unsloth.

## Key Features
- Converts natural-language CV tasks into structured ML project files.
- Generates dataset strategy, hyperparameters, and augmentations.
- Produces YOLO training script skeletons.
- Creates GPU optimization plans using ONNX + TensorRT.
- Includes architecture-aware README for each generated project.
- Can be improved by fine-tuning the LLM using Unsloth.
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

# FLOW DIAGRAM
                ┌──────────────────────────────┐
                │         User Input            │
                │  "Detect phone usage in CCTV" │
                └───────────────┬───────────────┘
                                │
                                ▼
                ┌────────────────────────────────┐
                │   LLM Planner (Unsloth-ready)   │
                │  - dataset plan                 │
                │  - YOLO config                  │
                │  - training script outline      │
                │  - ONNX/TensorRT plan           │
                │  - project README               │
                └───────────────┬────────────────┘
            ┌────────────────────┼──────────────────────────┐
            ▼                    ▼                          ▼
   ┌────────────────┐   ┌─────────────────────┐   ┌──────────────────────┐
   │ Dataset Plan    │   │ YOLO Config (YAML) │   │ Training Script (.py) │
   └────────────────┘   └─────────────────────┘   └──────────────────────┘
            │                    │                          │
            └───────────────┬────┴───────────────┬────────┘
                            ▼                    ▼
                ┌──────────────────────────────────────────┐
                │ ONNX/TensorRT Optimization Plan (Markdown)│
                └──────────────────────────────────────────┘
                                │
                                ▼
                ┌──────────────────────────────────────────┐
                │  Final Generated Project Folder           │
                │  (ready for user to train & optimize)     │
                └──────────────────────────────────────────┘



```mermaid
graph TD
    %% Nodes
    A[User Input<br/>'Detect phone usage in CCTV']
    B[LLM Planner Unsloth-ready<br/>• dataset plan<br/>• YOLO config<br/>• training script outline<br/>• ONNX/TensorRT plan<br/>• project README]
    C[Dataset Plan]
    D[YOLO Config YAML]
    E[Training Script .py]
    F[ONNX/TensorRT Optimization<br/>Plan Markdown]
    G[Final Generated Project Folder<br/>ready for user to train & optimize]

    %% Edge connections
    A --> B
    B --> C
    B --> D
    B --> E
    C --> F
    D --> F
    E --> F
    F --> G

    %% Styling (Optional - makes it look cleaner)
    style A fill:#f9f,stroke:#333,stroke-width:2px,color:black
    style B fill:#bbf,stroke:#333,stroke-width:2px,color:black
    style G fill:#9f9,stroke:#333,stroke-width:2px,color:black
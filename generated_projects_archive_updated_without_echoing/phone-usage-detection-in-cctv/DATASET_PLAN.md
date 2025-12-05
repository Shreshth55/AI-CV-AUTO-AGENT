
You are an expert computer vision data scientist.

Task:
Detect phone usage (person using a mobile phone) in indoor CCTV footage, such as offices or factories.

Design a DATASET PLAN for this task. Include:

1. Classes (with short explanations).
2. Recommended data sources (e.g., Roboflow keywords or types of images).
3. Approximate number of images per class for an MVP and for a stronger model.
4. Train/validation/test split percentages.
5. Recommended data augmentations (and why).
6. Notes specific to CCTV-style footage and phone usage.

Format your answer as clear Markdown with headings and bullet points.
```
# Dataset Plan: Detecting Phone Usage in Indoor CCTV Footage

## Classes
- **Phone**: A person is actively using their mobile phone.
- **No Phone**: No one is using a mobile phone.
- **Background**: The scene has no people or phones visible.

## Data Sources
- **Roboflow Keywords**:
  - "mobile phone detection"
  - "indoor surveillance"
  - "office environment"
  - "factory setting"

- **Image Types**:
  - High-resolution photos from various angles.
  - Videos captured at different times of day.
  - Images taken during different weather conditions.
  - Scenes with varying levels of background clutter.

## Image Count Per Class
- **MVP (Minimum Viable Product)**:
  - **Phone**: 1000 images
  - **No Phone**: 1000 images
  - **Background**: 1000 images

- **Stronger Model**:
  - **Phone**: 5000 images
  - **No Phone**: 5000 images
  - **Background**: 5000 images

## Training/Validation/Test Split
- **Training**: 80%
- **Validation**: 10%
- **Test**: 10%

## Data Augmentations
- **Rotation**: Rotate the image by 90 degrees randomly to simulate camera movement.
- **Flip**: Randomly flip the image horizontally to account for camera motion.
- **Resize**: Resize the image to a random scale between 0.7 and 1.3 to simulate changes in distance.
- **Crop**: Crop the image to a random size within the original dimensions to simulate object occlusion.
- **Color Jitter**: Adjust the brightness, contrast, saturation, and hue of the image slightly to simulate lighting variations.

## Notes Specific to CCTV Style Footage and Phone Usage
- **CCTV Style Footage**: Ensure that the dataset includes scenes where the subject's face is clearly visible, even if partially obscured by objects like desks or chairs. This will help in accurately detecting when someone is holding a phone.
- **Phone Usage Context**: Focus on scenarios where the phone is held vertically, such as taking pictures or making calls, rather than horizontal use cases like texting or browsing.
- **Variability**: Include diverse backgrounds and lighting conditions to ensure robustness against real-world variations.
```
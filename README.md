Team 22471A05 — Neuro-Diagnosis: YOLO-Based Brain Tumor Detection
Team Info
22471A0553 — Shaik Mohammad Khaleel ( LinkedIn )
Work Done: Model development, YOLOv5/v7/v8 training, evaluation, documentation
22471A0505 — Bontha John Babu ( LinkedIn )
Work Done: Dataset preprocessing, annotation, mask alignment
22471A0566 — Yannakula Shiva Sai ( LinkedIn )
Work Done: GUI development, visualization, result analysis
22471A0514 — Chowdari Rama Krishna ( LinkedIn )
Work Done: Literature review, testing, performance comparison

Abstract

This project proposes an automated deep learning pipeline for brain tumor detection, segmentation, and classification using MRI images. A YOLO-based framework (YOLOv5, YOLOv7, YOLOv8) is used to detect tumor boundaries and classify tumor types. Preprocessing techniques such as mask alignment, noise reduction, and normalization significantly improve performance. Among all models, YOLOv8 achieved the best results with high precision, recall, and mAP, making it suitable for real-time clinical applications.

Paper Reference (Inspiration)

👉 [Neuro-diagnosis: A YOLO-Inspired Pipeline for Automated Tumor Boundary Extraction and MRI-Based Classification and Segmentation
– K.V. Narasimha Reddy, Shaik Mohammad Khaleel, et al.](Paper URL here)

Original IEEE conference paper used as the base work.

Our Improvement Over Existing Paper
Compared three YOLO variants (v5, v7, v8) instead of a single model
Added detailed preprocessing impact analysis (before vs after)
Included failure case analysis (mask misalignment, over-smoothing)
Achieved higher accuracy with YOLOv8 (mAP = 0.934)
Implemented real-time GUI for prediction
About the Project
What the project does

Detects and classifies brain tumors from MRI images automatically.

Why it is useful
Reduces manual effort for radiologists
Provides fast and consistent diagnosis
Helps in early detection of tumors
Workflow

Input (MRI images)
→ Preprocessing (mask alignment, normalization)
→ YOLO Model (v5/v7/v8 training)
→ Detection & Classification
→ Output (Tumor location + type prediction)

Dataset Used

👉 [MRI Brain Tumor Dataset](Dataset URL)

Dataset Details:
MRI brain scan images (.MAT format converted to .PNG)
Includes tumor masks for segmentation
Tumor types:
Meningioma
Glioma
Pituitary
Contains annotated bounding boxes for YOLO training
Dependencies Used
Python
PyTorch
OpenCV
NumPy
Matplotlib
YOLOv5 / YOLOv7 / YOLOv8 frameworks
EDA & Preprocessing
Converted .mat → .png format
Aligned tumor masks with MRI images
Applied:
Noise reduction
Morphological operations (erosion, dilation)
Normalization
Created YOLO annotations (bounding boxes)

✔ Preprocessing improved:

Precision from ~0.4 → ~0.9
Significant boost in detection accuracy
Model Training Info
Models used:
YOLOv5
YOLOv7
YOLOv8
Training includes:
Feature extraction
Bounding box prediction
Non-Max Suppression (NMS)
Evaluation metrics:
Precision
Recall
mAP
Model Testing / Evaluation

Performance comparison:

Model	Precision	Recall	mAP
YOLOv5	0.903	0.876	0.914
YOLOv7	0.805	0.764	0.821
YOLOv8	0.914	0.886	0.934

✔ YOLOv8 performed best across all metrics

Results
Overall Accuracy: 87%
Best class performance: Pituitary tumor (F1 ≈ 0.96)
Real-time detection achieved (~65 FPS)
Improved tumor boundary detection using preprocessing
Limitations & Future Work
Limitations
Class imbalance (Background class = poor performance)
Works mainly on 2D MRI slices
Sensitive to preprocessing errors
Future Work
Use 3D MRI volumetric analysis
Apply Explainable AI (XAI)
Improve dataset diversity
Deploy in real hospital environments
Deployment Info
GUI-based system for real-time tumor detection
Users can upload MRI images and get:
Tumor location
Tumor classification
Can be extended as a web app or hospital tool

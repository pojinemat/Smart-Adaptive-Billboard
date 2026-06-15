# Smart Targeted Billboard Advertising System - An ML Project

## Overview

Traditional billboards display the same advertisement to everyone, regardless of who is viewing them. This project explores a smarter approach by using **Machine Learning and Computer Vision** to classify vehicle types and dynamically display targeted advertisements.

The system identifies the body type of a vehicle from an image and recommends a suitable advertisement based on the detected vehicle category. This demonstrates how AI can be applied to improve outdoor advertising by making it more personalized, efficient, and adaptive.

This project was developed as part of the **Machine Learning (CSCI 4340) Group Project**.

---

## Features

- 🚘 **Vehicle Image Classification**
  - Detects different vehicle body types using a deep learning model.

- 🧠 **CNN-Based Machine Learning Model**
  - Uses transfer learning with **EfficientNetB0** for image classification.

- 🎯 **Targeted Advertisement System**
  - Displays advertisements based on detected vehicle categories.

- 🖥️ **Desktop GUI Application**
  - Built using Python Tkinter for easy testing and demonstration.

- 📊 **Model Evaluation**
  - Includes accuracy analysis, precision, recall, F1-score, and confusion matrix evaluation.

---

## 🎯 Objectives

The main objectives of this project are:

- Develop an image classification model capable of recognizing vehicle body types.
- Apply deep learning techniques for practical real-world applications.
- Demonstrate how AI can improve traditional advertising methods.
- Create a prototype system that adapts advertisements based on detected vehicles.

---

## 🏗️ System Workflow

1. User uploads a vehicle image.
2. The image is preprocessed and resized.
3. The trained CNN model analyzes the image.
4. The model predicts the vehicle body type.
5. The system displays a suitable advertisement.

---

## 🧠 Machine Learning Approach

The project uses **Convolutional Neural Networks (CNNs)** because CNNs are highly effective for image recognition tasks.

A pretrained model, **EfficientNetB0**, is used through transfer learning.

### Model Architecture

- Base Model:
  - EfficientNetB0 (pretrained on ImageNet)

- Custom Classification Layers:
  - Global Average Pooling
  - Dense Layer (128 neurons)
  - Dropout Layer
  - Output Layer (7 classes)

### Frameworks Used

- TensorFlow
- Keras

---

## 📂 Dataset

The model is trained using the **Car Body Type Images Dataset**.

The dataset contains approximately **7,000 vehicle images** divided into 7 categories:

| Class | Description |
|---|---|
| Convertible | Cars with a removable or folding roof |
| Coupe | Two-door cars with a fixed roof |
| Hatchback | Cars with a rear lift-up door |
| Pick-Up | Vehicles with an open cargo area |
| SUV | Sport utility vehicles |
| Sedan | Passenger cars with separate compartments |
| Van | Vehicles designed mainly for transporting passengers/goods |

Dataset split:

- Training set
- Validation set
- Testing set

---

## 🔄 Data Preprocessing

Before training, images are processed using:

- Image resizing to `224 x 224`
- Pixel normalization
- Data augmentation

Training images are augmented using:

- Rotation
- Width/height shifting
- Brightness adjustment
- Zooming
- Horizontal flipping

These techniques improve model generalization and reduce overfitting.

---

## 📈 Results

The final model achieved approximately:

**96% classification accuracy**

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The model performs well across most vehicle categories, with minor confusion between visually similar classes such as SUVs and Sedans.

---

## 🚀 Deployment

A simple desktop application was created using **Tkinter**.

The application allows users to:

1. Select a vehicle image.
2. Run prediction.
3. View:
   - Predicted vehicle category
   - Corresponding advertisement

Examples:

Sedan

<img width="500" height="252" alt="image" src="https://github.com/user-attachments/assets/c1351cf2-eb5a-48c3-94a9-d6453c001f75" />

Van

<img width="500" height="252" alt="image" src="https://github.com/user-attachments/assets/52a0bb8e-697c-471b-a9d1-e3c0dee4793d" />



---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow | Deep learning framework |
| Keras | Neural network development |
| EfficientNetB0 | Image classification model |
| Tkinter | GUI development |
| Google Colab | Model training environment |

---

## 📌 Future Improvements

Possible improvements include:

- Real-time vehicle detection using camera input.
- Better handling of different lighting/weather conditions.
- Hyperparameter tuning for improved accuracy.
- More diverse vehicle datasets.
- Privacy-aware deployment strategies.

---

## 👥 Contributors

- Irfan Adib Bin Sahak
- Amir Fauzi Bin Ne'mat
- Ali Ilhan Thani Bin Jalaludin

---

## 📚 References

Dataset:
- Car Body Type Images Dataset (Kaggle) | Link: [https://www.kaggle.com/datasets/ademboukhris/cars-body-type-cropped](url)

Machine Learning:
- TensorFlow / Keras Documentation
- EfficientNet Architecture

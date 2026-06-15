import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import os

# Load the pre-trained Keras model
model_path = 'car_body_type_classifier.keras'
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    print(f"Error loading model from {model_path}: {e}")
    model = None

# Define class names corresponding to the model's output indices
class_names = ["Convertible", "Coupe", "Hatchback", "Pick-Up", "SUV", "Sedan", "VAN"]

# Path to advertisements folder
advert_folder = 'Advertisement'

# Initialize the main window
root = tk.Tk()
root.title("Car Body Type Classifier")
root.geometry("750x350")

# Function to handle image selection and prediction
def select_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename(title="Select Car Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if not file_path:
        return

    try:
        # Open the image using PIL
        selected_image = Image.open(file_path).convert('RGB')
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Display the selected image (resize for display)
    display_image = selected_image.copy()
    display_image.thumbnail((300, 300))
    display_imgtk = ImageTk.PhotoImage(display_image)
    original_label.config(image=display_imgtk)
    original_label.image = display_imgtk

    # Preprocess the image for model prediction
    model_image = selected_image.resize((224, 224))
    img_array = np.array(model_image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class
    if model:
        predictions = model.predict(img_array)
        predicted_idx = np.argmax(predictions[0])
        predicted_class = class_names[predicted_idx]
    else:
        predicted_class = "Unknown (model not loaded)"

    # Update predicted label
    result_label.config(text=f"Predicted: {predicted_class}")

    # Load and display the corresponding advertisement image
    advert_path = os.path.join(advert_folder, f"{predicted_class}_ad.jpg")
    if os.path.exists(advert_path):
        try:
            advert_image = Image.open(advert_path).convert('RGB')
            advert_image.thumbnail((300, 300))
            advert_imgtk = ImageTk.PhotoImage(advert_image)
            advert_label.config(image=advert_imgtk)
            advert_label.image = advert_imgtk
        except Exception as e:
            print(f"Error loading advertisement image: {e}")
    else:
        # If no advertisement image found, clear the label
        advert_label.config(image='')
        advert_label.image = None

# Button to select image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Labels to display images
original_label = tk.Label(root)
original_label.grid(row=1, column=0, padx=10, pady=10)

advert_label = tk.Label(root)
advert_label.grid(row=1, column=1, padx=10, pady=10)

# Label to show predicted class
result_label = tk.Label(root, text="Please select an image", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

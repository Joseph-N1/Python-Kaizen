from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Path to your images folder
image_folder = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Images"
# Path to the folder where you want to save the modified images
save_folder = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Modified Images\main3.0"

# Ensure save folder exists
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

def randomize_and_obscure_horizontal_slices(image_path, num_slices=60, min_slice_height=60, max_slice_height=60):
    # Open the image and convert to numpy array
    img = Image.open(image_path)
    img_array = np.array(img)
    h, w, _ = img_array.shape
    
    # Calculate slice height based on desired number of slices
    min_slice_height = h // num_slices
    max_slice_height = min_slice_height  # Keep all slices the same height

    # Initialize slices and slice position
    slices = []
    y = 0
    
    # Create slices of equal height
    while y < h:
        slice_section = img_array[y:y + min_slice_height, :]
        slices.append(slice_section)
        y += min_slice_height
    
    # Shuffle the slices more randomly
    def advanced_shuffle(slices):
        slice_copy = slices[:]
        random.shuffle(slice_copy)
        return slice_copy
    
    shuffled_slices = advanced_shuffle(slices)

    # Add obscuring effects to some slices for added difficulty
    for i, slice_section in enumerate(shuffled_slices):
        # Apply a blur effect randomly to a subset of slices
        if random.random() < 0.3:
            slice_img = Image.fromarray(slice_section)
            blurred_slice = slice_img.filter(ImageFilter.GaussianBlur(radius=5))
            shuffled_slices[i] = np.array(blurred_slice)

    # Reassemble the image
    randomized_img_array = np.vstack(shuffled_slices)
    
    # Convert back to PIL image
    randomized_img = Image.fromarray(randomized_img_array)

    return randomized_img

def process_images_in_folder(image_folder, save_folder, num_slices=10):
    # Loop through all images in the image folder
    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        
        # Check if the file is a valid image
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Processing image: {image_name}")
            
            # Apply randomization and obscuring to the image
            randomized_img = randomize_and_obscure_horizontal_slices(image_path, num_slices)
            
            # Save the modified image to the new folder
            save_path = os.path.join(save_folder, f"modified_{image_name}")
            randomized_img.save(save_path)
            print(f"Saved modified image to: {save_path}")

# Run the process on all images in the folder
process_images_in_folder(image_folder, save_folder, num_slices=15)

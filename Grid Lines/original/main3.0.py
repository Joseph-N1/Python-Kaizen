from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import random

# Path to your test image
image_path = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images\AOT.jpg"

# Path to your images folder
image_folder = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images"

def randomize_and_obscure_horizontal_slices(image_path, min_slice_height=15, max_slice_height=30):
    img = Image.open(image_path)
    img_array = np.array(img)
    h, w, _ = img_array.shape
    
    # Initialize slices and slice position
    slices = []
    y = 0
    
    # Create variable height slices
    while y < h:
        slice_height = random.randint(min_slice_height, max_slice_height)
        if y + slice_height > h:
            slice_height = h - y  # adjust for last slice
        slice_section = img_array[y:y + slice_height, :]
        slices.append(slice_section)
        y += slice_height
    
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
    
    # Display the image
    plt.imshow(randomized_img_array)
    plt.axis('off')
    plt.show()

# Run the function on the test image
randomize_and_obscure_horizontal_slices(image_path)

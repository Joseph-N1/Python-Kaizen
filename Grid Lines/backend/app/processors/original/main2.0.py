from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to your test image
image_path = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images\Sums.jpg"

# Path to your images folder
image_folder = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images"

def randomize_image_grid(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)

    # Define the grid size (adjust as needed)
    grid_size = 3
    h, w, _ = img_array.shape
    grid_h, grid_w = h // grid_size, w // grid_size

    # Create grid sections
    grid_sections = []
    for i in range(grid_size):
        for j in range(grid_size):
            section = img_array[i*grid_h:(i+1)*grid_h, j*grid_w:(j+1)*grid_w]
            grid_sections.append(section)

    # Randomize the sections
    np.random.shuffle(grid_sections)

    # Reassemble the shuffled grid
    new_img_array = np.zeros_like(img_array)
    count = 0
    for i in range(grid_size):
        for j in range(grid_size):
            new_img_array[i*grid_h:(i+1)*grid_h, j*grid_w:(j+1)*grid_w] = grid_sections[count]
            count += 1

    # Display the shuffled image
    plt.imshow(new_img_array)
    plt.axis('off')
    plt.show()

# Run the function on the test image
randomize_image_grid(image_path)


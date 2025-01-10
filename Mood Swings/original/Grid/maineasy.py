from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to your test image
image_path = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Mood Swings\Images\FN 1.jpg"

# Path to your images folder
image_folder = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images"

def randomize_image_grid(image_path, grid_size=5):
    if not os.path.exists(image_path):
        print("Image file does not exist. Please check the path.")
        return
    
    try:
        # Open the image
        img = Image.open(image_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')  # Ensure compatibility with RGB
        img_array = np.array(img)
    except Exception as e:
        print(f"Error opening the image: {e}")
        return

    h, w, _ = img_array.shape
    grid_h, grid_w = h // grid_size, w // grid_size
    remaining_h, remaining_w = h % grid_size, w % grid_size

    # Create grid sections, accounting for remaining pixels
    grid_sections = []
    for i in range(grid_size):
        for j in range(grid_size):
            start_h = i * grid_h
            end_h = (i + 1) * grid_h if i < grid_size - 1 else h
            start_w = j * grid_w
            end_w = (j + 1) * grid_w if j < grid_size - 1 else w
            section = img_array[start_h:end_h, start_w:end_w]
            grid_sections.append(section)

    # Randomize the sections
    np.random.shuffle(grid_sections)

    # Reassemble the shuffled grid
    new_img_array = np.zeros_like(img_array)
    count = 0
    for i in range(grid_size):
        for j in range(grid_size):
            start_h = i * grid_h
            end_h = (i + 1) * grid_h if i < grid_size - 1 else h
            start_w = j * grid_w
            end_w = (j + 1) * grid_w if j < grid_size - 1 else w
            new_img_array[start_h:end_h, start_w:end_w] = grid_sections[count]
            count += 1

    # Display the shuffled image
    plt.imshow(new_img_array)
    plt.axis('off')
    plt.show()

# Run the function on the test image
randomize_image_grid(image_path, grid_size=5)

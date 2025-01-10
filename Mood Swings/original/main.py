from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import random
import os

# Load the image
def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Add grid lines (A1-A10, B1-B5) and display
def add_grid_lines(image, grid_rows=5, grid_cols=10):
    img_width, img_height = image.size
    draw = ImageDraw.Draw(image)

    # Calculate cell size
    cell_width = img_width // grid_cols
    cell_height = img_height // grid_rows

    # Add horizontal and vertical lines
    for i in range(1, grid_cols):
        draw.line([(i * cell_width, 0), (i * cell_width, img_height)], fill='black', width=2)
    for j in range(1, grid_rows):
        draw.line([(0, j * cell_height), (img_width, j * cell_height)], fill='black', width=2)

    # Add labels A1-A10 and B1-B5
    for i in range(grid_cols):
        for j in range(grid_rows):
            label = f"A{i+1}" if i < 5 else f"B{j+1}"
            draw.text((i * cell_width + 5, j * cell_height + 5), label, fill="yellow")
    
    return image

# Rearrange grid sections to make the image unrecognizable
def rearrange_grid(image, grid_rows=5, grid_cols=10):
    img_width, img_height = image.size
    cell_width = img_width // grid_cols
    cell_height = img_height // grid_rows
    
    # Crop each grid section and store it
    grid_pieces = []
    for i in range(grid_cols):
        for j in range(grid_rows):
            box = (i * cell_width, j * cell_height, (i + 1) * cell_width, (j + 1) * cell_height)
            grid_pieces.append(image.crop(box))
    
    # Shuffle the grid sections
    random.shuffle(grid_pieces)
    
    # Create a new blank image to paste the shuffled sections
    shuffled_image = Image.new('RGB', (img_width, img_height))
    idx = 0
    for i in range(grid_cols):
        for j in range(grid_rows):
            shuffled_image.paste(grid_pieces[idx], (i * cell_width, j * cell_height))
            idx += 1
    
    return shuffled_image

# Display the original and modified images side by side
def display_images(original, modified):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(modified)
    axes[1].set_title("Shuffled Image")
    axes[1].axis('off')

    plt.show()

if __name__ == "__main__":
    # Path to your image
    image_path = r"C:\Users\Joseph N Nimyel\OneDrive\Documents\Python-Kaizen\Grid Lines\images\Gojo.jpg"

    # Load and process the image
    original_image = load_image(image_path)
    if original_image:
        # Add grid lines and rearrange sections
        grid_image = add_grid_lines(original_image.copy())
        shuffled_image = rearrange_grid(original_image.copy())

        # Display both images
        display_images(grid_image, shuffled_image)

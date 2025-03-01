import os
import sys
from PIL import Image  # To merge images into one PDF

# Function to merge images into a single PDF
def merge_images_to_pdf(image_paths, output_pdf):
    # Open the first image
    image_list = [Image.open(image_paths[0])]
    # Append the remaining images
    for image_path in image_paths[1:]:
        print(f"\n merging image {image_path}")
        image_list.append(Image.open(image_path))
    
    # Save the images as a single PDF
    image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:], resolution=100.0, quality=95, optimize=True)

# Main function to process and merge images into a PDF
def merge_images(input_images_dir, output_pdf):
    # Get all image file paths in the directory
    image_paths = [os.path.join(input_images_dir, f) for f in os.listdir(input_images_dir) if f.endswith('.png')]

    # Ensure the images are sorted in ascending order based on filenames (assumes filenames have page numbers)
    image_paths.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1]))

    # Check if there are images to process
    if not image_paths:
        print(f"No images found in the directory: {input_images_dir}")
        return

    # Merge the images into a single PDF
    print(f"Merging {len(image_paths)} images into a single PDF...")
    merge_images_to_pdf(image_paths, output_pdf)
    print(f"PDF saved as {output_pdf}")

# Entry point for the script
if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 3:
        print("Usage: python merge_images_to_pdf.py <input_images_dir> <output_pdf>")
        sys.exit(1)

    # Get input images directory and output PDF path from command line arguments
    input_images_dir = sys.argv[1]
    output_pdf = sys.argv[2]

    # Start merging the images into a PDF
    merge_images(input_images_dir, output_pdf)

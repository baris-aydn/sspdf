import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pdf2image import convert_from_path
from PyPDF2 import PdfReader  # Use PdfReader instead of PdfFileReader

# Function to convert a single page to an image
def convert_page(page_number, input_pdf, output_images_dir):
    try:
        # Convert single page to image
        images = convert_from_path(input_pdf, first_page=page_number, last_page=page_number, dpi=300)
        image_path = os.path.join(output_images_dir, f"page_{page_number}.png")
        images[0].save(image_path, "PNG")
        return page_number, image_path
    except Exception as e:
        print(f"Error processing page {page_number}: {e}")
        return page_number, None

# Main function to process PDF to images with progress
def process_pdf(input_pdf, output_pdf):
    # Create a directory for storing page images
    output_images_dir = "output_images"
    os.makedirs(output_images_dir, exist_ok=True)

    # Get the number of pages in the PDF
    with open(input_pdf, "rb") as f:
        reader = PdfReader(f)  # Use PdfReader instead of PdfFileReader
        num_pages = len(reader.pages)  # Get number of pages using PdfReader

    # Use ThreadPoolExecutor to process pages concurrently
    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers as needed
        futures = []
        
        # Submit all pages for conversion
        for i in range(1, num_pages + 1):
            futures.append(executor.submit(convert_page, i, input_pdf, output_images_dir))
        
        # Wait for all threads to complete and handle progress
        for i, future in enumerate(futures):
            page_number, image_path = future.result()
            if image_path:
                print(f"Converted page {page_number}/{num_pages} to image: {image_path}")
            else:
                print(f"Failed to convert page {page_number}/{num_pages}")

    # Final message after processing all pages
    print(f"All pages processed. Images are saved in the '{output_images_dir}' directory.")

# Entry point for the script
if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_image.py <input_pdf> <output_pdf>")
        sys.exit(1)

    # Get input and output PDF paths from command line arguments
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]

    # Start processing the PDF
    process_pdf(input_pdf, output_pdf)

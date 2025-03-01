PDF to Image Conversion and Image Merging Scripts

This project contains two Python scripts designed for converting PDF pages to images and merging those images into a single PDF.
Scripts Overview

    pdf_to_image.py:
        Converts each page of a PDF into individual images (PNG format).
        It processes the PDF file and saves each page as a separate image file.

    merge_images_to_pdf.py:
        Merges all images (converted from PDF) into a single PDF file.
        It takes a directory of image files and combines them into a PDF, preserving the correct order based on image filenames.

Requirements

Before running these scripts, ensure that you have the following installed:

    Python 3.x
    Python libraries:
        pdf2image (for PDF to image conversion)
        Pillow (for merging images into a PDF)
        poppler-utils (for PDF utilities like pdfinfo)

Install required Python packages:

pip install pdf2image Pillow

For pdf2image, you also need to install Poppler on your system:

    Download Poppler for Windows
    Make sure to add the Poppler bin directory to your PATH.

Script 1: pdf_to_image.py
Description

This script converts each page of a PDF into individual PNG images.
Usage

python pdf_to_image.py <input_pdf> <output_images_directory>

    <input_pdf>: Path to the input PDF file.
    <output_images_directory>: Directory where the PNG images will be saved.

Example:

python pdf_to_image.py input.pdf output_images

This command will take the input.pdf file and convert each page into a separate PNG file, saving them in the output_images directory.
Script 2: merge_images_to_pdf.py
Description

This script merges PNG images into a single PDF file. It assumes the images are sequentially numbered to maintain the correct page order.
Usage

python merge_images_to_pdf.py <input_images_directory> <output_pdf>

    <input_images_directory>: Directory containing the PNG images to be merged.
    <output_pdf>: Path to the resulting PDF file.

Example:

python merge_images_to_pdf.py output_images final_output.pdf

This command will take all the PNG images from the output_images directory and merge them into a single PDF file named final_output.pdf.
Notes

    Filename Convention: The script merge_images_to_pdf.py sorts images based on the numeric part of the filenames. Ensure that your images are named in a way that allows proper sorting (e.g., page_1.png, page_2.png, or 001.png, 002.png, etc.).
    Image Quality: You can adjust the quality and resolution of images by modifying the dpi parameter in pdf_to_image.py or the quality parameter in merge_images_to_pdf.py.

Example Workflow

    Step 1: Convert a PDF to images.

python pdf_to_image.py input.pdf output_images

Step 2: Merge the converted images into a single PDF.

    python merge_images_to_pdf.py output_images final_output.pdf

After following these steps, you'll have a single PDF file (final_output.pdf) containing all the pages from the original PDF.
Troubleshooting

    Poppler is not found: If the script is unable to locate poppler, ensure that you have installed Poppler and added its bin directory to your system's PATH.
    Images not sorted correctly: If the images are not in the correct order, check the filenames. The script sorts files based on the numeric part of the filename (e.g., page_1.png, page_2.png). Ensure that the filenames follow a consistent naming pattern.


from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def images_to_pdf(image_files, output_pdf):

    # Create a new PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=letter)
    
    # Set the title of the PDF
    c.setTitle(os.path.basename(output_pdf))
    
    for i, image_file in enumerate(image_files):

        # Open the image
        img = Image.open(image_file)
        # Resize the image to fit the letter page
        img = img.convert('RGB')
        width, height = letter
        img.thumbnail((width, height), Image.ANTIALIAS)
        
        # Save image as temporary file for ReportLab to add it to PDF
        temp_image_path = f"temp_image_{i}.jpg"
        img.save(temp_image_path)
        c.drawImage(temp_image_path, 0, 0, width, height)
        c.showPage()  # Create a new page in the PDF

        # Delete the temporary image file
        os.remove(temp_image_path)

    c.save()  # Save the PDF document

# Image files and pdf output location
images = [
    # Full file paths go here 
]
output_pdf = ''

# Convert images to PDF
images_to_pdf(images, output_pdf)

print("PDF created successfully!")
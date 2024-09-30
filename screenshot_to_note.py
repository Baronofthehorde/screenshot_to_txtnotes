import os
import pytesseract

# Set the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r'E:\Users\Owner\Downloads\tesseract.exe'

# Specify the input folder and output file name
input_folder = 'E:\\code\\AI_python_JS_teacher\\courserassnotes'
output_file = 'classnotes.txt'

# Open the output file in append mode
with open(output_file, 'a') as f:
    # Iterate through the files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (assuming images have .jpg or .png extension)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Extract the text from the image using Tesseract OCR
            try:
                text = pytesseract.image_to_string(os.path.join(input_folder, filename))
                print(filename, '\n', text)
                # Append the extracted text to the output file
                f.write(text + '\n')
            except Exception as e:
                print(f"Error processing {filename}: {e}")

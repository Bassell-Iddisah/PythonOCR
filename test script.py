from PIL import Image
import pytesseract
import csv

def extract_text_from_image(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Use Tesseract to extract text from the image
    text = pytesseract.image_to_string(img)

    return text

def process_text_and_save_tsv(text, output_tsv):
    # Split the text into rows based on newline characters
    rows = text.strip().split('\n')

    # Create a TSV file and write the extracted data
    with open(output_tsv, 'w', newline='') as tsvfile:
        tsv_writer = csv.writer(tsvfile, delimiter='\t')

        # Iterate through each row and split the values based on tab characters
        for row in rows:
            values = row.split('\t')
            # Write each row to the TSV file
            tsv_writer.writerow(values)

if __name__ == "__main__":
    # Path to the input image containing the printed document
    input_image_path = "test.png"

    # Path to the output TSV file
    output_tsv_path = "output_data.tsv"

    # Extract text from the image
    extracted_text = extract_text_from_image(input_image_path)

    # Process the extracted text and save it to a TSV file
    process_text_and_save_tsv(extracted_text, output_tsv_path)
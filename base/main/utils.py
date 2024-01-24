import os
import csv
import secrets
import pytesseract
import os.path as path
from PIL import Image
from flask import current_app


def save_pic(form_picture):
    '''Save an image on local storage using Image from PIL'''
    _, f_ext = path.splitext(form_picture.filename)  # Extract extension and filename from image
    ran_hex = secrets.token_hex(5)  # Generate a random string
    picture_fn = f'{ran_hex}_toextract{f_ext}'  # Use generated string as new filename

    # Setting picture save path
    if path.exists(path.join(current_app.root_path, 'static/images/results/')):  # check if save path exists
        picture_path = path.join(current_app.root_path, f'static/images/results/{picture_fn}')  # Set save path to
        # picture_path
    else:
        os.makedirs(path.join(current_app.root_path, 'static/images/results/'))  # Create save path folder
        picture_path = path.join(current_app.root_path, f'static/images/results/{picture_fn}')  # set save path

    image = Image.open(form_picture)  # Open the image
    image.save(picture_path)  # Save the image
    return picture_fn,picture_path  # return the image name to be saved in database



def extract_text_from_image(image_path):
    
    img = Image.open(image_path) # Open the image using Pillow

    text = pytesseract.image_to_string(img) # Open the image using Pillow

    return text


def process_text_and_save_tsv(text, output_tsv):
    
    rows = text.strip().split('\n') # Split the text into rows based on newline characters

    write_path = path.join(current_app.root_path, 'files')
    os.chdir(write_path)
    with open(output_tsv, 'w', newline='') as tsvfile: # Create a TSV file and write the extracted data
        tsv_writer = csv.writer(tsvfile, delimiter='\t')

        
        for row in rows: # Iterate through each row and split the values based on tab characters
            values = row.split('\t')
            
            tsv_writer.writerow(values) # Write each row to the TSV file
    return 0
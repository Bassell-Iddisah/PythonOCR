import os
import os.path as path
from flask import current_app
import secrets
from PIL import Image


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
    return picture_fn  # return the image name to be saved in database

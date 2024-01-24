from flask import render_template, Blueprint, redirect, url_for, request, current_app, session, flash, send_file
from base.main.utils import extract_text_from_image, process_text_and_save_tsv
from base.main.forms import TakeImageForm
from base.main.utils import save_pic
import os


main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', form=TakeImageForm())


@main.route('/p', methods=['GET', 'POST'])
def processing():
    form = TakeImageForm()
    output_tsv_path = "output_file.tsv" # Name the output file

    picture_det = save_pic(form.image.data) # Save the image to the storage and return filename and saved path
    session["picture_fn"] = picture_det[0]
    extracted_text = extract_text_from_image(picture_det[1])

    process_text_and_save_tsv(extracted_text, output_tsv_path) # Process the extracted text and save to tsv file
    
    #flash("The task was completed successfully", "success") # Display a successfully complete notification

    return redirect(url_for("main.results"))


@main.route('/results', methods=['GET', 'POST'])
def results():
    form = TakeImageForm()
    file_name = session['picture_fn']

    #_, fixed_path = file_path.split("static")
    #actual_path = pacurrent_app.root_path
    path = os.path.join(current_app.root_path, "files/output_file.tsv")
    return send_file(path, as_attachment=True)

    #return render_template('results.html', path=file_path)


@main.route('/faqs')
def faqs():
    return render_template('faqs.html')


@main.route('/about')
def about():
    return render_template('about.html')

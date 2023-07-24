from flask import render_template, Blueprint, request, redirect, url_for
from base.main.forms import TakeImageForm
from base.main.utils import save_pic
from base.extractor import extract_text_from_image


main = Blueprint("main", __name__)


@main.route('/')
@main.route('/index')
@main.route('/home')
def home():
    return render_template('index.html', form=TakeImageForm())


@main.route('/faqs')
def faqs():
    return render_template('faqs.html', form=TakeImageForm())


@main.route('/about')
def about():
    return render_template('about.html', form=TakeImageForm())


@main.route('/results', methods=['GET', 'POST'])
def results(extracted_text=""):
    form = TakeImageForm()
    if request.method == "POST":
        if form.validate_on_submit():
            picture = save_pic(form.image.data)
            extracted_text = extract_text_from_image(f"C:/Users/Bassell Iddisah/Projects/Final "
                                                     f"Year/PythonOCR/base/static/images/results/{picture}")  # Call
            # the function to extract text
            return redirect(url_for("main.results", extracted_text=extracted_text))
        else:
            return "Not submitting"
    extracted_text = request.args.get('extracted_text')
    return render_template('results.html', extracted_text=extracted_text)

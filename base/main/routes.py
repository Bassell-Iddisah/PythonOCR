from flask import render_template, Blueprint, redirect, url_for, request, current_app
from base.main.forms import TakeImageForm
from base.main.utils import save_pic
from base.extractor import extract_text


main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', form=TakeImageForm())


@main.route('/p', methods=['GET', 'POST'])
def processing():
    form = TakeImageForm()
    picture = save_pic(form.image.data)
    extracted_text = extract_text(f"{current_app.root_path}/static/images/results/{picture}")
    return redirect(url_for("main.results", extracted_text=extracted_text))


@main.route('/results<string:extracted_text>', methods=['GET', 'POST'])
def results(extracted_text):
    return render_template('results.html', extracted_text=extracted_text)


@main.route('/faqs')
def faqs():
    return render_template('faqs.html')


@main.route('/about')
def about():
    return render_template('about.html')

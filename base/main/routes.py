from flask import render_template, Blueprint, redirect, url_for, request, current_app, session
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
    session['text'] = extracted_text
    return redirect(url_for("main.results"))


@main.route('/results', methods=['GET', 'POST'])
def results():
    form = TakeImageForm()
    extracted_text = session.pop('text', "Nothing saved in sessions")
    # with open(F"")
    return render_template('results.html', extracted_text=extracted_text, word=form.image.data)


@main.route('/faqs')
def faqs():
    return render_template('faqs.html')


@main.route('/about')
def about():
    return render_template('about.html')

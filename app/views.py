from app import appl
from flask import render_template, request
from .python.random_return import return_random
from .python.rhyme import get_rhymes

@appl.route('/index')
def index():
	return render_template("index.html")


@appl.route('/random', methods=['GET'])
def random():
	return render_template("random.html"
							, chosen = "")

@appl.route('/random', methods=['POST'])
def random_post():
    text = request.form['word_list']
    processed_text = return_random(text)
    return render_template("random.html"
							, chosen = processed_text)


@appl.route('/rhyme', methods=['GET'])
def rhyme():
	return render_template("rhyme.html"
							, chosen = "")

@appl.route('/rhyme', methods=['POST'])
def rhyme_post():
	text = request.form['word_rhyme']
	processed_text = get_rhymes(text)
	return render_template("rhyme.html"
							, chosen = processed_text)
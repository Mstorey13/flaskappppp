from flask import Blueprint, render_template 

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/collection')
def collection():
    return render_template('collection.html')
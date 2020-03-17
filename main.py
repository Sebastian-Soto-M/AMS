import os
import utils
import jinja2
from flask import Flask, render_template

app = Flask(__name__)

template_dir = os.path.join('.', 'templates')
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)


@app.context_processor
def inject_dict_for_all_templates():
    nav_info = utils.readJson(os.path.join('content', 'nav.json'))
    return dict(nav_bar=nav_info)


@app.route('/')
def index():
    clients_info = utils.readJson(os.path.join('content','clients.json'))
    return render_template('views/index/index.html', index=True, clients=clients_info)


# @app.route('/about')
# def about():
#     return render_template('views/about/about.html', dir_title='About')


@app.route('/contact')
def contact():
    return render_template('views/contact/contact.html', dir_title='Contact')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('views/404.html', dir_title='Not Found'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
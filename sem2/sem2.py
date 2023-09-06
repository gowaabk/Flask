from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_site():
    # context = {
    #     'title': 'Главная',
    # }
    return render_template('base.html')


@app.route('/page1/')
def page_1():

    return "hi Vasya"


@app.route('/load_image/',  methods=['GET', 'POST'])
def load_image():

    return render_template('page_1.html')


if __name__ == '__main__':
    app.run(debug=True)

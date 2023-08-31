from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_site():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes_site():
    context = {
        'title': 'Одежда'
    }
    # context = {
    #     'title': 'Одежда',
    #     'image': "<img src="{{ url_for('static', filename='../static/img/clothes.jpg') }}" alt="clothes" class="img_content">"
    # }

    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes_site():
    context = {
        'title': 'Обувь'
    }
    return render_template('shoes.html', **context)


@app.route('/jackets/')
def jackets_site():
    context = {
        'title': 'Куртки'
    }
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

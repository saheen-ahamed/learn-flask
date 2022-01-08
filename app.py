from flask import Flask, render_template
app = Flask(__name__)

data = [
    {
        'author': 'Saheen',
        'book': 'Atomic Habits',
        'published': '2022'
    },
    {
        'author': 'Jia lisa',
        'book': 'Midnight vibes',
        'published': '2021'
    }
]


# render templates
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", data=data)


@app.route('/about')
def about():
    return render_template("about.html", title='About us')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)


posts = [
    {
        "name": "Emeka Manuel",
        "title": "Chronicles of Tommy Shelby",
        "content": "First Post Content",
        "data_posted": "April 20, 2020",
    },
    {
        "name": "Chioma Okafor",
        "title": "Chronicles of The Okafors",
        "content": "Third Post Content",
        "date_posted": "April 13, 2023",
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)

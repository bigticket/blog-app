from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'content': 'Post 1 content',
        'date': 'May 3, 1997'
    },
    {
        'author': 'Betty Doe',
        'title': 'Post 2',
        'content': 'Post 2 content',
        'date': 'May 5, 1997'
    }
]

@app.route("/")
@app.route("/home/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)
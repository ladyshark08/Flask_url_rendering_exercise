from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_api = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    response = requests.get(blog_api).json()
    return render_template("index.html", blog_posts=response)


@app.route("/post/<int:num>")
def get_blog(num):
    response = requests.get(blog_api).json()[num - 1]
    return render_template("post.html", message=response)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/k<book_id>")
def book_view(book_id):
    return render_template(f"k{book_id}.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 59.99, "category": "Electronics"},
    {"id": 2, "name": "Running Shoes", "price": 79.99, "category": "Fashion"},
    {"id": 3, "name": "Coffee Maker", "price": 49.99, "category": "Home"},
]


@app.route("/")
def home():
    query = request.args.get("q", "").strip().lower()
    filtered = [
        p for p in PRODUCTS if query in p["name"].lower() or query in p["category"].lower()
    ] if query else PRODUCTS
    return render_template("home.html", products=filtered, query=query)


if __name__ == "__main__":
    app.run(debug=True)

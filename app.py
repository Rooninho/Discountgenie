# app.py
from flask import Flask, request, jsonify
from discount import calculate_discount

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    try:
        price = float(data.get("price"))
        discount_percent = float(data.get("discount_percent"))
        final_price = calculate_discount(price, discount_percent)
        return jsonify({
            "original_price": price,
            "discount_percent": discount_percent,
            "final_price": final_price
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)

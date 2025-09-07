# DiscountGenie

![DiscountGenie Logo](https://img.shields.io/badge/DiscountGenie-Python-blue?style=flat-square)

**DiscountGenie** is a Python project that calculates the final price of items after applying discounts. It supports **CLI**, **GUI**, and **Web API** interfaces, making it a versatile and professional mini-software engineering project.

---

## Features

- ✅ Calculate final price with discounts (applied only if 20% or higher)  
- ✅ Command-Line Interface (CLI) for quick usage  
- ✅ Graphical User Interface (GUI) using Tkinter  
- ✅ Web API backend using Flask  
- ✅ Handles multiple items and summarizes totals  
- ✅ Input validation and error handling  
- ✅ Unit tests included to ensure correctness

---

## Screenshots

**CLI Version**  

**GUI Version**  
![GUI Screenshot](screenshot.png)

**Web API Version (POST /calculate)**  
```json
{
  "original_price": 100,
  "discount_percent": 25,
  "final_price": 75
}



**GUI Version**  
![GUI Screenshot](screenshot.png)

**Web API Version (POST /calculate)**  
```json
{
  "original_price": 100,
  "discount_percent": 25,
  "final_price": 75
}

Installation

Clone the repository
git clone https://github.com/YourUsername/DiscountGenie.git
cd DiscountGenie

(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies
pip install -r requirements.txt

Usage🤖
python main.py
python gui.py
python app.py

project structure

DiscountGenie/
│
├── discount.py         # Core logic
├── main.py             # CLI version
├── gui.py              # GUI version
├── app.py              # Flask Web API
├── tests/
│   └── test_discount.py
├── README.md
└── requirements.txt

Running tests

python -m unittest tests/test_discount.py

Future Improvements

Support for tiered discounts and category-specific rules

Persistent storage for multiple carts (SQLite/JSON)

Enhanced GUI styling and better UX

Deployment as a cloud web app (Heroku, Render)


Option to generate discount reports for businesses

Author

Rooney wandeto Maina

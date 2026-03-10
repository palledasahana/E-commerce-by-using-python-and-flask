# E-commerce-by-using-python-and-flask
# 🛍️ ShopWave — Full-Stack E-Commerce Platform

A complete, production-ready **E-Commerce web application** built with Python (Flask) and SQLite. Features a dark-themed, modern UI with a full shopping experience — from browsing to checkout.

---

## 🚀 Features

### 🛒 Customer Features
| Feature | Description |
|--------|-------------|
| 🏠 Home Page | Hero banner, featured products, category navigation |
| 🔍 Product Search | Search by name, filter by category, sort by price/rating |
| 📄 Product Detail | Full product page with related items |
| 🛒 Shopping Cart | Add, update quantity, remove items |
| ♡ Wishlist | Save products for later |
| 💳 Checkout | Address, payment method selection, order placement |
| 📦 Order History | Track all past orders |
| 👤 Profile | Update name, address, phone |

### 🔐 Admin Features
| Feature | Description |
|--------|-------------|
| 📊 Dashboard | Revenue, orders, user stats |
| 📦 Product Management | Add, delete, mark as featured |
| 🛒 Order Management | View all orders, update status |
| 👥 User Management | View all registered customers |

---

## 🗂️ Project Structure

```
ecommerce/
│
├── app.py                    # Flask app — all routes
├── requirements.txt
├── README.md
│
├── database/
│   └── db.py                 # SQLite schema, connection, seed data
│
├── models/
│   └── models.py             # All data models (Product, User, Cart, Order, Wishlist)
│
└── templates/
    ├── base.html             # Navbar, footer, flash messages
    ├── home.html             # Landing page
    ├── products.html         # Product listing with filters
    ├── product_detail.html   # Single product view
    ├── auth.html             # Login & Register
    ├── cart.html             # Shopping cart
    ├── checkout.html         # Checkout form
    ├── order_success.html    # Order confirmation
    ├── orders.html           # Order history
    ├── wishlist.html         # Saved products
    ├── profile.html          # User profile editor
    └── admin/
        ├── dashboard.html    # Admin overview
        ├── products.html     # Manage products
        ├── orders.html       # Manage orders
        └── users.html        # View users
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.8+, Flask 3.x |
| Database | SQLite (built-in) |
| Frontend | HTML5, CSS3, Vanilla JS |
| Fonts | Google Fonts (Playfair Display + DM Sans) |
| Auth | Flask sessions |

---

## ⚙️ Installation & Running

### 1. Clone the repo
```bash
git clone https://github.com/palledasahana/ecommerce.git
cd ecommerce
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

Visit **http://127.0.0.1:5000**

---

## 🔑 Default Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@shop.com | admin123 |

Register any new account for a customer account.

---

## 🗃️ Database Schema

```
users         → id, name, email, password, role, address, phone
categories    → id, name, icon
products      → id, name, description, price, original_price,
                category_id, stock, rating, is_featured
cart          → id, user_id, product_id, quantity
orders        → id, user_id, total_amount, status, shipping_address, payment_method
order_items   → id, order_id, product_id, quantity, unit_price
wishlist      → id, user_id, product_id
```

---

## 📸 Pages Overview

- `/` — Home with hero, featured products, categories
- `/products` — Full catalog with search, filter, sort
- `/product/<id>` — Product detail with related items
- `/cart` — Shopping cart
- `/checkout` — Place order
- `/orders` — Order history
- `/wishlist` — Saved items
- `/profile` — Account settings
- `/admin` — Admin dashboard (admin only)

---

## 👩‍💻 Author

**Palleda Sahana**  
ECE Graduate, Class of 2024  
Ballari Institute of Technology and Management  
GitHub: [@palledasahana](https://github.com/palledasahana)

---

## 📄 License

MIT License — Free to use and modify.

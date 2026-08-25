from flask import Flask, render_template, redirect
    

def create_app():
    app = Flask(__name__)
    cart_items = []

    products = [
        {
            "id": 1,
            "name": "iPhone 15",
            "price": 79999,
            "image": "iphone.jpg",
            "description": "Latest Apple iPhone with amazing camera."
        },
        {
            "id": 2,
            "name": "Samsung Galaxy S24",
            "price": 69999,
            "image": "samsung.jpg",
            "description": "Powerful Samsung flagship smartphone."
        },
        {
            "id": 3,
            "name": "HP Laptop",
            "price": 55999,
            "image": "laptop.jpg",
            "description": "High performance laptop."
        },
        {
            "id": 4,
            "name": "Wireless Headphones",
            "price": 4999,
            "image": "headphones.jpg",
            "description": "Premium sound quality headphones."
        }
    ]

    @app.route('/')
    def home():
        return render_template(
            'index.html',
            products=products
        )

    @app.route('/product/<int:id>')
    def product_detail(id):

        product = next(
            (p for p in products if p["id"] == id),
            None
        )

        return render_template(
            'product_details.html',
            product=product
        )
    @app.route('/add-to-cart/<int:id>')
    def add_to_cart(id):
        
        product = next(
            (p for p in products if p["id"] == id),
            None
        )
        
        if product:
            cart_items.append(product)
        
        return redirect('/cart')
    
    @app.get('/cart')
    def cart():
        
        return render_template(
            'cart.html',
            cart_items=cart_items
        ) 
    @app.route('/remove-from-cart/<int:id>')
    def remove_from_cart(id):
        
        for item in cart_items:
            if item["id"] == id:
                cart_items.remove(item)
                break
        return redirect('/cart')

    return app
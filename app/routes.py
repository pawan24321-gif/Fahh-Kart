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
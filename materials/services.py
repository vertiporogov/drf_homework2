import stripe

stripe.api_key = 'sk_test_51P2z6wJ11dzhnQNmfSj1VpCwGvCR5asxu36fmMCxwYQKdyHMCl6lsv2ZxUlYHu2malP33cgAz1I5JJj3LUIOx23Z00Vv8JZAV9'


def get_link(amount):
    product = stripe.Product.create(name="Paid training")

    payment_amount = stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product_data={"name": "Payment"}
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": payment_amount['id'], "quantity": 1}],
        mode="payment",
    )

    return product['name'], session["url"], session["id"]

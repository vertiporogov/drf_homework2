import os

import stripe
from django.conf import settings

stripe.api_key = os.getenv('STRIPE_API_KEY')


def get_link(amount):
    product = stripe.Product.create(name="Paid training", currency="rub")

    payment_amount = stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product_data={"name": "Paid training"}
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": payment_amount['id'], "quantity": 1}],
        mode="payment",
    )

    return product['name'], session["url"], session["id"]

import os

import stripe

stripe.api_key = os.getenv('STRIPE_API_KEY')


def get_link(payment):
    course_name = payment.course.name
    product = stripe.Product.create(
        name=course_name
    )

    payment_amount = stripe.Price.create(
        product=product.id,
        currency="rub",
        unit_amount=int(payment.payment_amount) * 100,
    )

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": payment_amount['id'], "quantity": 1}],
        mode="payment",
    )

    return product.name, session.url, session.id

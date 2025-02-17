# payments.py (Placeholder for payment integration)
def process_payment(order, payment_details):
    # Placeholder logic for payment processing
    if payment_details['amount'] == order.total_price:
        order.order_status = 'paid'
        order.save()
        return True
    return False

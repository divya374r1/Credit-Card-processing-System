def process_payment(amount):
    if amount > 0:
        return "Payment Successful"
    else:
        return "Payment Failed"

print(process_payment(100))

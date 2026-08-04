from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCard(PaymentStrategy):

    def pay(self, amount: float) -> None:
        discount = amount * 0.05
        final_amount = amount - discount
        print(
            f"₹{final_amount:.2f} paid using Credit Card (5% discount applied)."
        )


class PayPal(PaymentStrategy):

    def pay(self, amount: float) -> None:
        fee = 20
        final_amount = amount + fee
        print(f"₹{final_amount:.2f} paid using PayPal (₹20 fee added).")


class UPI(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f"₹{amount:.2f} paid using UPI (No extra charges).")


class CryptoPayment(PaymentStrategy):

    def pay(self, amount: float) -> None:
        print(f"₹{amount:.2f} paid using Cryptocurrency (BTC/ETH).")


class PaymentProcessor:

    def __init__(self, payment_method: PaymentStrategy) -> None:
        self.payment_method = payment_method

    def process_payment(self, amount: float) -> None:
        self.payment_method.pay(amount)


amount = float(input("Enter Amount: ₹"))
print("\nChoose Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")
print("4. Crypto")

choice = input("Enter Choice: ")

payment: PaymentStrategy

if choice == "1":
    payment = CreditCard()
elif choice == "2":
    payment = PayPal()
elif choice == "3":
    payment = UPI()
elif choice == "4":
    payment = CryptoPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)

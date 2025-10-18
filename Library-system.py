class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    def calculateLateFee(self, days_late):
        raise NotImplementedError("This method should be overridden by subclasses")


# Both EBook and PrintedBook inherit from Book
class EBook(Book):
    def calculateLateFee(self, days_late):
        return days_late * 0.5  # 50 cents per day


class PrintedBook(Book):
    def calculateLateFee(self, days_late):
        return days_late * 1  # $1 per day


# Payment interface
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")


class PaypalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount:.2f} payment through PayPal")


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount:.2f} payment through Credit Card")


class Library:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def processBookPayment(self, amount):
        self.payment_processor.process_payment(amount)


# Usage example
if __name__ == "__main__":
    # Create book instances
    ebook = EBook("Real niqqa", "Dumisani Chaitezvi", "1234567890")
    printed_book = PrintedBook("To Kill a Mockingbird", "Harper Lee", "0987654321")

    # Create a library instance with a specific payment processor
    library = Library(PaypalPaymentProcessor())

    # Process payment for a late fee
    late_fee = ebook.calculateLateFee(5)
    library.processBookPayment(late_fee)

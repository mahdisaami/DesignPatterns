from src.observer.decorator import notify_observers
from src.observer.notification import SMSNotification, EmailNotification, PushNotification


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def create(cls, name, price):
        return cls(name, price)


class Payment:
    pass


class Purchase:
    observers = [SMSNotification, EmailNotification, PushNotification]

    def __init__(self, product_list):
        self.product_list = product_list
        self.payment = Payment()
        self._is_paid = False

    @classmethod
    def create(cls, product_list):
        return cls(product_list)

    @notify_observers('purchase paid')
    def check_out(self):
        self._is_paid = True
        return "Your payment has been successfully completed"

    @notify_observers('purchase canceled')
    def cancel(self):
        self._is_paid = False
        return 'Your payment has been canceled!'

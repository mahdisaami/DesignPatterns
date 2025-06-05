class SMSNotification:
    @staticmethod
    def send(msg):
        return f'Sms notif has been sent to {msg}'


class EmailNotification:
    @staticmethod
    def send(msg):
        return f'Email notif has been sent to {msg}'


class PushNotification:
    @staticmethod
    def send(msg):
        return f'Push notif has been sent to {msg}'

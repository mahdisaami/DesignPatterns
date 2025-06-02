from time import sleep


class LazyLoader:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)



class MySQLHandler:
    def __init__(self):
        sleep(1)

    @staticmethod
    def connect():
        return "successfully connected to MySQL"

class MongoHandler:
    def __init__(self):
        sleep(1)

    @staticmethod
    def connect():
        return "Hello from Mongo"


class NotificationHandler:
    def __init__(self):
        sleep(1)

    @staticmethod
    def show():
        return "Hello from notif center"

if __name__ == '__main__':

    mysql = LazyLoader(MySQLHandler)
    mongo = LazyLoader(MongoHandler)
    notification = LazyLoader(NotificationHandler)

    print(mysql.connect())
    print(mongo.connect())
    print(notification.show())
    print(mysql.connect())
    print(mongo.connect())
    print(notification.show())
    print(mysql.connect())
    print(mongo.connect())
    print(notification.show())
    print(mysql.connect())
    print(mongo.connect())
    print(notification.show())


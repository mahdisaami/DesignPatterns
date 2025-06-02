import datetime
from time import sleep

class LogProxy:
    def __init__(self, user, url):
        self._user = user
        self._url = url

    def receive(self):
        self.logging()
        self._url.receive(self._url.url)

    def logging(self):
        with open('log.log', 'a') as log:
            log.write(
                f'Request has been sent by {self._user.name} to {self._url.url} '
                f'at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
            )

    @classmethod
    def create(cls, user, url):
        return cls(user, url)

class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)


class Website:
    def __init__(self, url):
        self.url = url


    @classmethod
    def create(cls, name):
        return cls(name)

    @staticmethod
    def receive(name):
        print(f'Processing your request to {name} ...')
        sleep(1)
        print('Done...')


if __name__ == "__main__":

    ali = User.create("Ali")
    mahdi = User.create("Mahdi")

    digikala = Website.create("Digikala.com")
    amazon = Website.create("Amazon.com")

    log = LogProxy.create(ali, digikala)
    log2 = LogProxy.create(mahdi, digikala)
    log3 = LogProxy.create(ali, amazon)
    log4 = LogProxy.create(mahdi, amazon)

    for log in [log, log2, log4, log3]:
        log.receive()

import abc


class Page(abc.ABC):
    @abc.abstractmethod
    def show(self):
        pass


class AuthPage(Page):
    def show(self):
        print('Welcome to authenticated page')


class AnonPage(Page):
    def show(self):
        print('Welcome to anonymous page')


class PageDecorator(Page, abc.ABC):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def show(self):
        pass


class PageAuthDecorator(PageDecorator):
    def show(self):
        username = input('Enter your username... ')
        password = input('Enter your password... ')
        if username == 'admin' and password == 'secret':
            self._component.show()
        else:
            print('You are not authenticated')


def client_decorator():
    page = AuthPage()
    authenticated = PageAuthDecorator(page)
    authenticated.show()

if __name__ == "__main__":
    client_decorator()

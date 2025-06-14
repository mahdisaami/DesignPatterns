import abc
from random import randrange


class Publisher(abc.ABC):

    @abc.abstractmethod
    def subscribe(self, observer):
        pass

    @abc.abstractmethod
    def unsubscribe(self, observer):
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class ConcretePublisher(Publisher):
    _observers = []
    _state = None

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print('Notifying observers...')

        for observer in self._observers:
            observer.update(self)

    def operation(self):
        self._state = randrange(0, 10)
        print(f'state changed to {self._state}')
        self.notify()


class Observer(abc.ABC):

    @abc.abstractmethod
    def update(self, publisher):
        pass


class ObserverA(Observer):
    def update(self, publisher):
        if publisher._state <= 5:
            print('ObserverA reacted to the event')


class ObserverB(Observer):
    def update(self, publisher):
        if publisher._state > 5:
            print('ObserverB reacted to the event')



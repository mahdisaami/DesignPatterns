from src.observer1.system import ConcretePublisher, ObserverA, ObserverB

if __name__ == "__main__":
    publisher = ConcretePublisher()

    observer_a = ObserverA()
    observer_b = ObserverB()

    publisher.subscribe(observer_a)
    publisher.subscribe(observer_b)

    publisher.operation()
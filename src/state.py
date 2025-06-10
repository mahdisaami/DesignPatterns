from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_user):
        if to_user.__class__  not in self.current.allowed:
            print(f'{self.current.__class__} is not allowed to send email to {to_user.__class__}')
        else:
            self.flow.append(to_user)
            print(f'message sent to {to_user.__class__}')


class AbstractUser(ABC):
    @property
    @abstractmethod
    def allowed(self):
        pass

class ManagerDirector(AbstractUser):
    allowed = []

class InternalManager(AbstractUser):
    allowed = [ManagerDirector]

class Supervisor(AbstractUser):
    allowed = [InternalManager]

class Operator(AbstractUser):
    allowed = [Supervisor]

class Client(AbstractUser):
    allowed = [Operator]


if __name__ == "__main__":
    manager_director = ManagerDirector()
    internal_manager = InternalManager()
    supervisor = Supervisor()
    operator = Operator()
    client = Client()

    first_message = Message('Issue #1313', 'Issue description', client)

    first_message.send(operator)
    first_message.send(supervisor)
    first_message.send(internal_manager)
    first_message.send(manager_director)

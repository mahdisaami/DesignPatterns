def notify_observers(msg=''):
    def decorator_method(func):
        def wrapped(obj, *args, **kwargs):
            result = func(obj, *args, **kwargs)
            for observer in obj.observers:
                print(observer.send(msg))
            return result

        return wrapped
    return decorator_method

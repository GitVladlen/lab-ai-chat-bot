class Trace(object):
    @staticmethod
    def log(type, msg):
        print("[{type}] {msg}".format(
            type=type,
            msg=msg
        ))
        pass

    pass


class Events(object):
    @staticmethod
    def addEvent(event):
        setattr(Events, event, event)

class Notification(object):
    observers = {}

    @staticmethod
    def addObserver(observer, event):
        if event is None:
            Trace.log("Notification", "event is None")
            return False
            pass

        if observer is None:
            Trace.log("Notification", "observer is None")
            return False
            pass

        if event not in Notification.observers.keys():
            Notification.observers[event] = []
            pass

        Notification.observers[event].append(observer)

        return True
        pass

    @staticmethod
    def notify(event, *args, **kwargs):
        if event not in Notification.observers.keys():
            Trace.log(
                "Notification",
                "event {event} not in observers {observers}".format(
                    event=event,
                    observers=Notification.observers
                )
            )
            return False
            pass

        for observer in Notification.observers[event]:
            observer(*args, **kwargs)
            pass

        return True
        pass

    pass

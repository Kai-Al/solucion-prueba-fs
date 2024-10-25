def add_event_listener(self, event_name, callback, scope=None):
    listeners = self.__event_listeners__.setdefault(event_name, [])
    listeners.append((callback, scope))

def remove_event_listener(self, event_name, callback):
    listeners = self.__event_listeners__.get(event_name)
    if listeners:
        self.__event_listeners__[event_name] = [
            (registered_callback, registered_scope)
            for registered_callback, registered_scope in listeners
            if registered_callback != callback
        ]
        if not self.__event_listeners__[event_name]:
            del self.__event_listeners__[event_name]

def dispatch_event(self, event_name):
    listeners = self.__event_listeners__.get(event_name, [])
    for registered_callback, registered_scope in listeners:
        if registered_scope is not None:
            registered_callback(registered_scope)
        else:
            registered_callback()

def has_listener_for(self, event_name):
    return event_name in self.__event_listeners__ and bool(self.__event_listeners__[event_name])

def has_callback_for(self, event_name, callback):
    listeners = self.__event_listeners__.get(event_name, [])
    return any(
        registered_callback == callback for registered_callback, _ in listeners
    )

class EventDispatcher:
    @staticmethod
    def mixin(obj):
        obj.__event_listeners__ = {}
        obj.add_event_listener = add_event_listener.__get__(obj)
        obj.remove_event_listener = remove_event_listener.__get__(obj)
        obj.dispatch_event = dispatch_event.__get__(obj)
        obj.has_listener_for = has_listener_for.__get__(obj)
        obj.has_callback_for = has_callback_for.__get__(obj)
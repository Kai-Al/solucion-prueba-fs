def add_event_listener(self, event_name, callback, scope=None):
    """
    Agrega un listener (callback) para un evento específico.

    Args:
        event_name (str): El nombre del evento.
        callback (callable): La función a llamar cuando se despacha el evento.
        scope (any, opcional): Un objeto o valor que se pasará al callback cuando se invoque. Por defecto es None.
    """
    # Inicializa la lista de listeners para el evento si no existe
    listeners = self.__event_listeners__.setdefault(event_name, [])
    # Agrega el callback y el scope a la lista de listeners
    listeners.append((callback, scope))

def remove_event_listener(self, event_name, callback):
    """
    Elimina un listener específico de un evento.

    Args:
        event_name (str): El nombre del evento.
        callback (callable): La función que se desea eliminar de los listeners del evento.
    """
    listeners = self.__event_listeners__.get(event_name)
    if listeners:
        # Filtra los listeners para eliminar el callback especificado
        self.__event_listeners__[event_name] = [
            (registered_callback, registered_scope)
            for registered_callback, registered_scope in listeners
            if registered_callback != callback
        ]
        # Si no quedan listeners para el evento, se elimina la entrada del diccionario
        if not self.__event_listeners__[event_name]:
            del self.__event_listeners__[event_name]

def dispatch_event(self, event_name):
    """
    Despacha un evento, llamando a todos los listeners registrados para ese evento.

    Args:
        event_name (str): El nombre del evento a despachar.
    """
    # Obtiene la lista de listeners para el evento, o una lista vacía si no hay
    listeners = self.__event_listeners__.get(event_name, [])
    for registered_callback, registered_scope in listeners:
        # Llama al callback con el scope si se proporcionó, o sin argumentos si no
        if registered_scope is not None:
            registered_callback(registered_scope)
        else:
            registered_callback()

def has_listener_for(self, event_name):
    """
    Verifica si hay algún listener registrado para un evento específico.

    Args:
        event_name (str): El nombre del evento.

    Returns:
        bool: True si hay al menos un listener registrado para el evento, False en caso contrario.
    """
    return event_name in self.__event_listeners__ and bool(self.__event_listeners__[event_name])

def has_callback_for(self, event_name, callback):
    """
    Verifica si un callback específico está registrado para un evento.

    Args:
        event_name (str): El nombre del evento.
        callback (callable): La función callback a verificar.

    Returns:
        bool: True si el callback está registrado para el evento, False en caso contrario.
    """
    listeners = self.__event_listeners__.get(event_name, [])
    return any(
        registered_callback == callback for registered_callback, _ in listeners
    )

class EventDispatcher:
    @staticmethod
    def mixin(obj):
        """
        Agrega funcionalidad de manejo de eventos al objeto proporcionado.
        En particular, agrega los métodos add_event_listener, remove_event_listener, dispatch_event, has_listener_for y has_callback_for.
        
        Args:
            obj: El objeto al que se le agregará la funcionalidad de EventDispatcher.
        """
        # Inicializa el diccionario de listeners en el objeto
        obj.__event_listeners__ = {}
        # Asigna los métodos al objeto.
        obj.add_event_listener = add_event_listener.__get__(obj)
        obj.remove_event_listener = remove_event_listener.__get__(obj)
        obj.dispatch_event = dispatch_event.__get__(obj)
        obj.has_listener_for = has_listener_for.__get__(obj)
        obj.has_callback_for = has_callback_for.__get__(obj)
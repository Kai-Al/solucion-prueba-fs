import unittest
from unittest.mock import MagicMock
from event_dispatcher import EventDispatcher

class EventObject:
    pass

class TestEventDispatcher(unittest.TestCase):

    def test_mixin(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)

        self.assertTrue(callable(test_obj.add_event_listener))
        self.assertTrue(callable(test_obj.dispatch_event))
        self.assertTrue(callable(test_obj.remove_event_listener))
        self.assertTrue(callable(test_obj.has_listener_for))
        self.assertTrue(callable(test_obj.has_callback_for))

    def test_add_event_listener(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")

        test_obj.add_event_listener(test_event, test_func)
        self.assertTrue(test_obj.has_listener_for(test_event))

    def test_add_event_with_callback(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")

        test_obj.add_event_listener(test_event, test_func)
        self.assertTrue(test_obj.has_callback_for(test_event, test_func))

    def test_multiple_callbacks_for_event(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")
        test_func2 = lambda: print("Test function 2")

        test_obj.add_event_listener(test_event, test_func)
        test_obj.add_event_listener(test_event, test_func2)

        self.assertTrue(test_obj.has_listener_for(test_event))
        self.assertTrue(test_obj.has_callback_for(test_event, test_func))
        self.assertTrue(test_obj.has_callback_for(test_event, test_func2))

    def test_no_shared_store_between_instances(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_obj2 = EventObject()
        EventDispatcher.mixin(test_obj2)
        test_event = "testEvent"
        test_func = lambda: print("Test function")

        test_obj.add_event_listener(test_event, test_func)
        self.assertTrue(test_obj.has_callback_for(test_event, test_func))
        self.assertFalse(test_obj2.has_callback_for(test_event, test_func))

    def test_has_listener_for(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")

        test_obj.add_event_listener(test_event, test_func)
        self.assertFalse(test_obj.has_listener_for("xxx"))

    def test_has_callback_for(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")
        test_func2 = lambda: print("Test function 2")

        test_obj.add_event_listener(test_event, test_func)
        self.assertTrue(test_obj.has_callback_for(test_event, test_func))
        self.assertFalse(test_obj.has_callback_for(test_event, test_func2))

    def test_remove_event_listener(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")
        test_func2 = lambda: print("Test function 2")

        test_obj.add_event_listener(test_event, test_func)
        test_obj.add_event_listener(test_event, test_func2)
        test_obj.remove_event_listener(test_event, test_func)

        self.assertTrue(test_obj.has_callback_for(test_event, test_func2))
        self.assertFalse(test_obj.has_callback_for(test_event, test_func))

    def test_remove_all_callbacks_removes_event_name(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = lambda: print("Test function")

        test_obj.add_event_listener(test_event, test_func)
        test_obj.remove_event_listener(test_event, test_func)

        self.assertFalse(test_obj.has_listener_for(test_event))

    def test_dispatch_event(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = MagicMock()
        test_func2 = MagicMock()

        test_obj.add_event_listener(test_event, test_func)
        test_obj.add_event_listener(test_event, test_func2)
        test_obj.dispatch_event(test_event)

        test_func.assert_called()
        test_func2.assert_called()

    def test_remove_listener_prevents_dispatch(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        test_func = MagicMock()
        test_func2 = MagicMock()

        test_obj.add_event_listener(test_event, test_func)
        test_obj.add_event_listener(test_event, test_func2)
        test_obj.remove_event_listener(test_event, test_func2)
        test_obj.dispatch_event(test_event)

        test_func.assert_called()
        test_func2.assert_not_called()

    def test_dispatch_event_with_scope(self):
        test_obj = EventObject()
        EventDispatcher.mixin(test_obj)
        test_event = "testEvent"
        scope = {"executeSuccess": True}
        success = {"value": False}

        def test_scoped_function(scope):
            if scope["executeSuccess"]:
                success["value"] = True

        test_obj.add_event_listener(test_event, test_scoped_function, scope)
        test_obj.dispatch_event(test_event)

        self.assertTrue(success["value"])


if __name__ == "__main__":
    unittest.main()

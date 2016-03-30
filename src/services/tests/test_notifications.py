import unittest
from services import notifications


def test_get_notifications():
    assert notifications.get_notifications() == []


class TestNotifications(unittest.TestCase):
    def test_get_notifications(self):
        assert notifications.get_notifications() == []

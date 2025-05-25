from unittest.mock import Mock, call

from discounts import DiscountManager
from model_objects import DiscountData, Product, User


class SpyNotifier:
    def __init__(self):
        self.notified_users = []

    def notify(self, user, message):
        # don't send any messages from the unit test, record which users are notified
        self.notified_users.append(user)


def test_discount_for_users_with_spy():
    notifier = SpyNotifier()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]
    assert users[0] in notifier.notified_users
    assert users[1] in notifier.notified_users


def test_discount_for_users_with_mocking_framework_spy():
    notifier = Mock()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]
    expected_calls = [
        call(users[0], f"You may be interested in a discount on this product! {product.name}"),
        call(users[1], f"You may be interested in a discount on this product! {product.name}"),
    ]
    notifier.notify.assert_has_calls(expected_calls)


class MockNotifier:
    def __init__(self):
        self.expected_user_notifications = []

    def notify(self, user, message):
        # don't send any messages from the unit test, check all notifications are expected
        expected_user = self.expected_user_notifications.pop(0)
        if user != expected_user:
            raise RuntimeError(f"got notification message for unexpected user {user.name}, was expecting {expected_user.name} instead")

    def expect_notification_to(self, user):
        self.expected_user_notifications.append(user)


def test_discount_for_users_with_mock():
    notifier = MockNotifier()
    discount_manager = DiscountManager(notifier)
    product = Product("headphones")
    product.discounts = []
    discount_details = DiscountData("10% off")
    users = [User("user1", [product]), User("user2", [product])]
    notifier.expect_notification_to(users[0])
    notifier.expect_notification_to(users[1])

    discount_manager.create_discount(product, discount_details, users)

    assert product.discounts == [discount_details]

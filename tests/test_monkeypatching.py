from hexlet_testing.implementations import get_class
from hexlet_testing.implementations import User, NotificationError
import pytest

# сервис уведомлений, который нужно протестировать
NotificationService = get_class()




# BEGIN (write your solution here)
@pytest.fixture
def email_service():
    def send(self, email, message):
        if message == '':
            return False
        return True


@pytest.fixture
def sms_service():
    def send(self, phone, message):
        if message == '':
            return False
        return True

@pytest.fixture
def push_service():
    def send(self, device_id, message):
        if message == '':
            return False
        return True



def test_notification_service(user, email_service, sms_service, push_service):
    noty = NotificationService(email_service, sms_service, push_service)
    result = noty.send_notification(user, "yyyyyy", ['email', 'sms', 'push'])
    assert result == True
# END

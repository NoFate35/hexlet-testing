import os


class NotificationError(Exception):
    pass


class User:
    def __init__(self, email=None, phone=None, device_id=None):
        self.email = email
        self.phone = phone
        self.device_id = device_id


class NotificationService:
    def __init__(self, email_service, sms_service, push_service):
        self.email_service = email_service
        self.sms_service = sms_service
        self.push_service = push_service

    def send_notification(self, user, message, channels):
        if not channels:
            raise NotificationError("No channels specified")
        results = []
        if 'email' in channels and user.email:
            results.append(self.email_service.send(user.email, message))
        if 'sms' in channels and user.phone:
            results.append(self.sms_service.send(user.phone, message))
        if 'push' in channels and user.device_id:
            results.append(self.push_service.send(user.device_id, message))
        return all(results)


class IncorrectNotificationSystem1:
    def __init__(self, email_service, sms_service, push_service):
        self.email_service = email_service
        self.sms_service = sms_service
        self.push_service = push_service

    def send_notification(self, user, message, channels):
        results = []
        # Неправильная логика: игнорируем параметр channels и всегда пытаемся отправить по всем каналам
        if user.email:
            results.append(self.email_service.send(user.email, message))
        if user.phone:
            results.append(self.sms_service.send(user.phone, message))
        if user.device_id:
            results.append(self.push_service.send(user.device_id, message))
        return all(results)


class IncorrectNotificationSystem2:
    def __init__(self, email_service, sms_service, push_service):
        self.email_service = email_service
        self.sms_service = sms_service
        self.push_service = push_service

    def send_notification(self, user, message, channels):
        if not channels:
            raise NotificationError("No channels specified")
        results = []
        if 'email' in channels and user.email:
            results.append(self.email_service.send(user.email, message))
        if 'sms' in channels and user.phone:
            results.append(self.sms_service.send(user.phone, message))
        if 'push' in channels and user.device_id:
            results.append(self.push_service.send(user.device_id, message))
        # Неправильная логика: возвращаем True, только если все каналы использовались
        return len(results) == len(channels)


class IncorrectNotificationSystem3:
    def __init__(self, email_service, sms_service, push_service):
        self.email_service = email_service
        self.sms_service = sms_service
        self.push_service = push_service

    def send_notification(self, user, message, channels):
        results = []
        if not channels:
            return False
        if 'email' in channels and user.email:
            results.append(self.email_service.send(user.email, message))
        if 'sms' in channels and user.phone:
            results.append(self.sms_service.send(user.phone, message))
        if 'push' in channels and user.device_id:
            results.append(self.push_service.send(user.device_id, message))
        # Неправильная логика: возвращаем True, если хотя бы один канал вернул True
        return any(results)


classes = {
    "right": NotificationService,
    "fail1": IncorrectNotificationSystem1,
    "fail2": IncorrectNotificationSystem2,
    "fail3": IncorrectNotificationSystem3,
}


def get_class():
    name = os.environ['CLASS_VERSION']
    return classes[name]

from unittest.mock import Mock


class MyObject:
    def __init__(self, dependency):
        self.dependency = dependency

    def my_method(self, arg):
        # какой-то метод, который зависит от зависимости
        return self.dependency.some_method(arg)

class Dependency():
    def __init__(self, arg):
        self.arg = arg
    def rrr():
        return self.arg
        
# Создаем мок-объект для зависимости
mock_dependency = Mock()

# Создаем объект, который мы будем тестировать
my_object = MyObject(mock_dependency)

# Имитируем поведение зависимости в мок-объекте
mock_dependency.some_method.return_value = 42

# Тестируем метод объекта
result = my_object.my_method("some argument")
print("resultttt", result)

# Проверяем, что метод объекта вызвал метод зависимости с правильным аргументом
print("yyyyyy", mock_dependency.some_method.assert_called_once_with("some argument"))


# Проверяем, что метод объекта вернул правильный результат
assert result == 42
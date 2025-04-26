import os
from datetime import datetime, timedelta

from freezegun import freeze_time
from functions import get_function

delete_old_files = get_function()


def create_file(directory, filename, days_old):
    """Вспомогательная функция для создания файла с заданной датой изменения."""
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as f:
        f.write("test content")
    old_time = datetime.now() - timedelta(days=days_old)
    os.utime(file_path, (old_time.timestamp(), old_time.timestamp()))


# BEGIN (write your solution here)
@freeze_time("2012-01-14")
def test_norm_func(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    create_file(d, 'yyyy.txt', 5)
    create_file(d, 'iiii.txt', 3)
    create_file(d, 'jjjj.txt', 3)
    delete_old_files(d, 4)
    assert len(os.listdir(d)) == 2

# END

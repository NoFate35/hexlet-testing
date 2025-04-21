from github import Github
from hexlet_testing.monkeypatching import get_private_fork_names

def test_get_private_fork_names(monkeypatch):
    # определим функцию-подмену сразу в тесте
    def fake_get_repos(self):
        return [
            type("Repo", (), {"name": "repo1", "fork": True})(),
            type("Repo", (), {"name": "repo2", "fork": False})(),
            type("Repo", (), {"name": "repo3", "fork": True})(),
        ]

    # Подменяем методы с помощью monkeypatch
    monkeypatch.setattr(Github, "get_user", lambda self, username: self)
    monkeypatch.setattr(Github, "get_repos", fake_get_repos)

    # Проверяем результат
    result = get_private_fork_names("hexlet")
    assert result == ["repo1", "repo3"]
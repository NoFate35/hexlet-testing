from github import Github


def get_private_fork_names(username):
    client = Github("access_token")
    repos = client.get_user(username).get_repos(type="private")
    return [repo.name for repo in repos if repo.fork]
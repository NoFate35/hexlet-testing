test:
	PYTHONPATH=src CLASS_VERSION=right suppressor pass pytest tests
	PYTHONPATH=src CLASS_VERSION=fail1 suppressor fail pytest tests
	PYTHONPATH=src CLASS_VERSION=fail2 suppressor fail pytest tests
	PYTHONPATH=src CLASS_VERSION=fail3 suppressor fail pytest tests
.PHONY: test

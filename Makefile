release:
	python setup.py sdist upload -r pypi

register:
	python setup.py sdist register -r pypi

# Test it via `pip install -i https://testpypi.python.org/pypi <project_name>`
test-release:
	python setup.py sdist upload -r test

test-register:
	python setup.py sdist register -r test

.PHONY: register test-register release test-release

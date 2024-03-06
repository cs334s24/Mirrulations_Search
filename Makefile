# NOTE: This file MUST use tabs for indentation rather than spaces
#       If you get an error "*** missing separator. Stop" then you
#       probably have spaces for indentation.
export PATH:=${PWD}/.venv/bin:${PATH};

all: test lint

test:
	pytest;
	cd frontend && npm test -- --watchAll=false;

lint:
	pylint --rcfile=api/.pylintrc api/;

clean:
	# Find and remove all files and  folders that match
    # -E for extended grep to match the pattern
	-find . | grep -E "(__pycache__|\.pyc)" | xargs rm -rf
    # -w for whole word match
	-find . | grep -w ".pytest_cache" | xargs rm -rf

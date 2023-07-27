from setuptools import find_packages,setup
from typing import List

NAME = "sensor"
VERSION = "0.0.1"
AUTHOR = "vikram jha"
AUTHOR_EMAIL_ID = "jhav7662@gmail.com"
REQUIREMENTS_FILE_NAME = 'requirements.txt'


def get_requirements(file_path:str = REQUIREMENTS_FILE_NAME)->list(str):
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    return requirements

setup(name=NAME,
version=VERSION,
author=AUTHOR,
author_email=AUTHOR_EMAIL_ID,
packages=find_packages(),
install_requires= get_requirements()

)



# setup.py

from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt', 'r') as req_file:
        requirements = req_file.readlines()
    # Remove any whitespace and comments
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements

setup(
    name='tdd-data-engineering',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
)

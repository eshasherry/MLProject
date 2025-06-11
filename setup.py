from typing import List

from setuptools import setup, find_packages

HYPHEN_DOT_E = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readline()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements


setup(name='MLProject',
      version='1.0',
      description='Machine Learning',
      author='Esha Sherry',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt'))

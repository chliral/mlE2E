from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path : str) -> List[str] :
    '''
    this function will return the requirements from the requirements.txt file
    '''

    HYPEN_E_DOT = "-e ."
    requirements = []
    with open("requirements.txt") as fid:
        requirements = [l.strip() for l in fid.readlines()]
        
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

    return requirements


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlE2E",                        # Replace with your package name
    version="0.0.1",
    author="Aayush",
    author_email="chloral24@gmail.com",
    description="Machine learning end-to-end project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chliral/mlE2E",
    install_requires=get_requirements('requirements.txt')
)

                                                                                                                                        
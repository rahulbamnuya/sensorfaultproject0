from setuptools import setup, find_packages
from typing import List
HYPEN_PACKAGE = "-e ."
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_PACKAGE in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="Faulty-Detection",
    version="0.0.1",
    author="Rahul Bamaniya",
    author_email="rahul@gmail.com",
    install_requires=get_requirements("requirements.txt"),  # <- fix here
    packages=find_packages()
)

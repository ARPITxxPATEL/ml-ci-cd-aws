from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    this function wil return a list of requiremnets
    '''
    requirements=[]
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="ml-ci-cd-aws",
    version="0.0.1",
    author="Arpit",
    author_email="arpitkumar2105@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
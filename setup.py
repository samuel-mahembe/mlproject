from typing import List
from setuptools import setup, find_packages

def get_requirements(file_path:str) -> List[str]:
    """
    This function reads the requirements from a given file and returns a list of dependencies.
    """
    HYPHEN_E_DOT = "-e ."
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
    return requirments

setup(
    name='ml_project',
    version='0.0.1',
    author='Samuel Mahembe',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
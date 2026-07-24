from setuptools import find_packages,setup
from typing import List

minus_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of packages 
    """
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if minus_e_dot in requirements:
            requirements.remove(minus_e_dot)

    return requirements
setup(
    name='machine_learning_project',
    version="0.0.1",
    author= "Gireesh Tallur",
    author_email="girishtallur07@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
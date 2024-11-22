from setuptools import find_packages,setup
from typing import List


# -e . in the requirments.txt file is to call the file using the setup.py file. 
HYPEN_E_DOT = '-e .'

def get_requirments(file_path:str) -> List[str]:
    """ This is a function that will retrun the list of requirments 
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =  [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = 'mlproject',
    version = '0.01',
    author = 'Adam',
    author_email = 'adamkadwory@gmail.com',
    packages = find_packages(),
    install_requires =  get_requirments('requirements.txt')

)
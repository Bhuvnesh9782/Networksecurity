from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            Lines=file.readlines()
            ## Process each line
            for line in Lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version="0.0.1",
    author="Bhuvnesh Agrawal",
    author_email="bhuvnesh1074167@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
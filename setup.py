#This file package the whole directory
from setuptools import setup, find_packages #for finding all the __init__.py in all the folders

setup(
    name = "src", 
    version = "0.0.1",
    description="It is ML deployment package",
    author="Mansit",
    packages=find_packages(),
    license='MIT'    

)
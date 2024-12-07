from setuptools import find_packages
from setuptools import setup

setup(
    name='advent-of-code',
    version='0.1.0',
    install_requires=['requests'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
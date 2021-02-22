from setuptools import setup, find_packages
from distutils.command.sdist import sdist as _sdist

class sdist(_sdist):
    """Custom script run during setup.py sdist"""


setup(
    name='my-package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.7.3',
    ],
    cmdclass={
        'sdist': sdist
    })

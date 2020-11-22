import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

print (find_packages())

setup(name='Bob Chroller',
      version='0.1',
      description='DC Inside Chroller',
      url='https://github.com/bakpark/dc-bob-chroller',
      author='bakpark',
      author_email='bakparkbj@gmail.com',
      packages=find_packages(),
      install_requires=[
        "selenium",
        "bs4",
        "PyQt5"
      ],
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ],
      zip_safe=False)
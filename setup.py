""" Setup tool module for projecty SaSSy
See:
https://github.com/krazybean/SaSSy
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SaSSy',
    version='0.0.1',
    description='Web Software as a Service',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/krazybean/SaSSy',
    author='krazybean',
    author_email='krazybean@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Website Hosting Development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # Requirements
    install_requires=['flask', 'tox'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/krazybean/SaSSy/issues',
        'Source': 'https://github.com/krazybean/SaSSy',
    },
)
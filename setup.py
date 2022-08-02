#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Alex Hayes",
    author_email='alex@alution.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Django modelling for `geopostcodes.com",
    entry_points={
        'console_scripts': [
            'django_geopostcodes=django_geopostcodes.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django_geopostcodes',
    name='django_geopostcodes',
    packages=find_packages(include=['django_geopostcodes', 'django_geopostcodes.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/alexhayes/django_geopostcodes',
    version='0.2.2',
    zip_safe=False,
)

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='ParkingLotManagementSystem',
    version='1.4.0-release',
    py_modules=['tdirdlotmg'],
    author='Madhu.',
    packages=find_packages(exclude=['tdirdlotmg.tests']),
    install_requires=[
        'numpy',
        'pandas',
        'nose'
        ],
    entry_points={
        'console_scripts': [
            'plmpsapi=tdirdlotmg',
        ]
    },
    include_package_data=True,
    # test_suite='nose.collector',
    # tests_require=['nose'],
)

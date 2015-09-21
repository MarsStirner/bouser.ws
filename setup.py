# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'viruzzz-kun'
__version__ = '0.1'


if __name__ == '__main__':
    setup(
        name="bouser_ws",
        version=__version__,
        description="WebSocket service for Bouser",
        long_description='',
        author=__author__,
        author_email="viruzzz.soft@gmail.com",
        license='ISC',
        url="http://github.com/hitsl/bouser_ws",
        packages=[
            "bouser_ws",
        ],
        zip_safe=False,
        package_data={},
        install_requires=[
            'bouser',
            'autobahn',
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Plugins",
            "Programming Language :: Python",
        ])

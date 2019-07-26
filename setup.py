from setuptools import setup, find_packages


setup(
    name='aztokens',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': 'aztokens=aztokens.main:main',
    },
)

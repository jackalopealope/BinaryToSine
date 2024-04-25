from setuptools import setup

setup(
    name='binarytosine',
    version='1.0.0',
    description='Plays sine waves based on binary input',
    author='Jack Hanni',
    packages=['binarytosine'],
    install_requires=[
        'numpy',
        'sounddevice'
    ],
    entry_points={
        'console_scripts': [
            'sineplayer = sineplayer.main:main'
        ]
    }
)

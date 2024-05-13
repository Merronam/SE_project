from setuptools import setup

setup(
    name='US_VIS'

    version='0.1',

    description='Visualisation tools for umbrella sampling calculations',

    license='None',

    packages=['US_VIS'],

    install_requires=[
    ],

    extras_require={
        'docs': [
            'sphinx'
        ],
        'dev': [
            'pytest',
            'pytest-cov',
        ],
    },

    zip_safe=False
)

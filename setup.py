from setuptools import setup

setup(
    name='us_vis'

    version='0.1',

    description='Visualisation tools for umbrella sampling calculations',

    license='None',

    packages=['us_vis'],

    install_requires=[
    ],

    extras_require={
        'docs': [
            'sphinx'
        ],
        'dev': [
            'flake8',
            'pytest',
            'pytest-cov',
        ],
    },

    zip_safe=False
)

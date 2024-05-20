from setuptools import setup

setup(
    name='us_vis',

    version='0.1',

    description='Visualisation tools for umbrella sampling calculations',

    packages=['us_vis'],

    install_requires=["pandas", "matplotlib"],

    extras_require={
        'docs': [
            'sphinx'
        ],
        'dev': [
            'pytest',
        ],
    },

    zip_safe=False
)

from setuptools import setup, find_packages

setup(
    name="scripts",
    version="1.0",
    author="Nikita Shuldov",
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas', 
        'scikit-learn', 
    ]
	)
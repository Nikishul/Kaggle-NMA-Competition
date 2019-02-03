rom setuptools import setup, find_packages

setup(
    name="python",
    version="1.0",
    author="Nikita Shuldov",
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas', 
        'scikit-learn', 
        'joblib', 
        'jupyter', 
    ]
	)
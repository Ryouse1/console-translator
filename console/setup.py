from setuptools import setup, find_packages

setup(
    name="console_translator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "googletrans==4.0.0-rc1"
    ]
)

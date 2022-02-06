from setuptools import setup, find_packages

setup(
    name='webcheck',
    version='0.1.0',
    packages=find_packages(include=['webcheck', 'webcheck.*']),
    install_requires=[
        'certifi==2021.10.8',
        'charset-normalizer==2.0.11',
        'idna==3.3',
        'pyaml==21.10.1',
        'pydantic==1.9.0',
        'PyYAML==6.0',
        'requests==2.27.1',
        'typing-extensions==4.0.1',
        'urllib3==1.26.8',
        'wrapt==1.13.3'
    ],
    description='A Python package that allows network metrics collection easily.'
)

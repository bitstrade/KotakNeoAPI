from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.1"
# To install the library, run the following
#
# python setup.py install

REQUIRES = ["bidict==0.23.1","certifi==2024.8.30","idna==3.10","numpy","pyjsparser==2.7.1","PyJWT==2.9.0",
            "python-dateutil==2.9.0","python-dotenv==1.0.1","requests==2.32.3","six==1.16.0","urllib3==2.2.3",
            "websocket-client==1.8.0","websockets==13.1","pandas","asyncio==3.4.3"]

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author="ne API",
    author_email="",
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)

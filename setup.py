import setuptools
from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "Readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'A password security software'
LONG_DESCRIPTION = 'A password security software use in generating unique password for each of each service i.e you can generate special password for each of your social media or services with just one master password'

# Setting up
setup(
    name="peupasswd",
    version=VERSION,
    author="blackstackhub (Black Stack Hub)",
    author_email="<blackstackhub@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['peupasswd', 'security', 'password security', 'neupasswd', 'encryption'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
from setuptools import setup
import codecs
import os



with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "Readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


# Setting up
setup(
    name="peupasswd",
    version='1.0.1.2',
    author="blackstackhub (Black Stack Hub)",
    author_email="<blackstackhub@gmail.com>",
    description='A password security software',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["peupasswd"],
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
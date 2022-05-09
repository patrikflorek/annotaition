import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="annotation",
    version="0.1.0",
    description="Provide a data structure for labeling ML dataset",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/patrikflorek/annotaition",
    author="Patrik Florek",
    author_email="patrikflorek@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["annotaition"],
    include_package_data=True,
    entry_points={},
)

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Sales Tax Calculator",
    version="0.0.1",
    description="A calculator for sales tax.",
    long_description=long_description,
    url="https://github.com/Bella288/SalesTax",
    author="Bella Lawrence",
    author_email="linwood.lawrence@students.sacs.k12.in.us",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

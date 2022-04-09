from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "A Python library to make handling dates easier"
LONG_DESCRIPTION = (
    "PyEasyDates allows using intuitively named functions "
    "to quickly parse dates without specifying the precise date format"
)

setup(
    name="py_easy_dates",
    version=VERSION,
    author="Gourav Kumar",
    author_email="gourav@gvkr.in",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
)

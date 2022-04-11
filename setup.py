"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
Modified by Madoshakalaka@Github (dependency links added)
"""
from os import path

from setuptools import glob
from setuptools import setup

# Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="changeme-types-package-name",
    description="Type Stubs for changeme-package-name",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cex-solutions/changeme-package-name",
    author="Binovate Labs",
    author_email="cex-dev@binovate.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Typing :: Stubs Only",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="GPLv3",
    keywords="stubs",
    package_data={
        "changeme-package-name-stubs": [
            item.split("changeme-package-name-stubs/")[-1] for item in glob.glob("**/*.pyi", recursive=True)
        ]
        + ["METADATA.toml"]
    },
    packages=["changeme-package-name-stubs"],
    python_requires=">=3.7, <4",
    install_requires=[],
    extras_require={"dev": ["mypy==0.942", "pipenv-setup==3.2.0", "twine==4.0.0"]},
    dependency_links=[],
    project_urls={
        "Bug Reports": "https://github.com/cex-solutions/changeme-types-package-name/issues",
        "Source": "https://github.com/cex-solutions/changeme-types-package-name",
    },
)

from os import path

from setuptools import glob
from setuptools import setup

# Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="types-sqlalchemy-utils",
    description="Type Stubs for sqlalchemy-utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cex-solutions/sqlalchemy-utils",
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
    keywords="stubs sqlalchemy sqlalchemy-utils",
    package_data={
        "sqlalchemy_utils-stubs": [
            item.split("sqlalchemy_utils-stubs/")[-1] for item in glob.glob("**/*.pyi", recursive=True)
        ]
        + ["METADATA.toml"]
    },
    packages=["sqlalchemy_utils-stubs"],
    python_requires=">=3.7, <4",
    install_requires=[],
    extras_require={
        "dev": [
            "sqlalchemy-utils==0.41.2",
            "sqlalchemy2-stubs==0.0.2a38",
            "mypy==1.10.0",
            "pipenv-setup==3.2.0",
            "twine==5.0.0",
        ]
    },
    dependency_links=[],
    project_urls={
        "Bug Reports": "https://github.com/cex-solutions/types-sqlalchemy-utils/issues",
        "Source": "https://github.com/cex-solutions/types-sqlalchemy-utils",
    },
)

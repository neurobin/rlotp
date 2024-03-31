#!/usr/bin/env python

from setuptools import setup

setup(
    name="rlotp",
    version="2.9.0",
    url="https://github.com/rlotp/rlotp",
    project_urls={
        "Documentation": "https://neurobin.github.io/rlotp",
        "Source Code": "https://github.com/neurobin/rlotp",
        "Issue Tracker": "https://github.com/neurobin/rlotp/issues",
        "Change Log": "https://github.com/neurobin/rlotp/blob/master/Changes.rst",
    },
    license="MIT License",
    author="RLOTP contributors",
    author_email="kislyuk@gmail.com",
    description="Python One Time Password Library",
    long_description=open("README.rst").read(),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "test": ["coverage", "wheel", "ruff", "mypy"],
    },
    packages=["rlotp", "rlotp.contrib"],
    package_dir={"": "src"},
    package_data={"rlotp": ["py.typed"]},
    platforms=["MacOS X", "Posix"],
    zip_safe=False,
    test_suite="test",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

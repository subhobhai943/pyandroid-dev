"""Setup configuration for PyAndroid library."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyandroid-dev",
    version="1.0.0",
    author="Subhobhai",
    author_email="subhobhai943@example.com",
    description="A Python library for Android application development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subhobhai943/pyandroid-dev",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Mobile Development",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add any dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="android, mobile, development, python, cross-platform",
    project_urls={
        "Bug Reports": "https://github.com/subhobhai943/pyandroid-dev/issues",
        "Source": "https://github.com/subhobhai943/pyandroid-dev",
        "Documentation": "https://github.com/subhobhai943/pyandroid-dev/wiki",
    },
)

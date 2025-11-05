from setuptools import find_packages, setup

setup(
    name="pysnowfall",
    version="1.0.0",
    author="AshKetshup",
    author_email="dsimoes2000@gmail.com",
    description="A Python Implementation of a Snowflake ID Generator (based on PedroCavaleiro/Avalanche)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AshKetshup/Snowfall",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[],
)

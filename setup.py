import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="s3-utils",
    version="0.0.1",
    author="Falak Sher Marri",
    author_email="marribaloch128@gmail.com",
    description="Utilities for AWS S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/citibeats-labs/s3-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
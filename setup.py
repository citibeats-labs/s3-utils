import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="s3-wrapper",
    version="0.0.6",
    author="Citibeats Labs",
    author_email="labs@citibeats.net",
    description="Utilities for AWS S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/citibeats-labs/s3-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
      'boto3',
    ],
    python_requires='>=3.7',
)
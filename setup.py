from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # the name must match the folder name 'verysimplemodule'
    name="versionmanagerpy",
    version='1.0.2',
    author="Kamron Cole",
    author_email="kjc8084@rit.edu",
    description='A GitHub Project Version Manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeonixRIT/versionmanager.py",
    project_urls={
        "Bug Tracker": "https://github.com/NeonixRIT/versionmanager.py/issues",
    },
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'github', 'version', 'manager', 'version manager'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)

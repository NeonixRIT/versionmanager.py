from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A GitHub Project Version Manager.'
LONG_DESCRIPTION = 'A GitHub Project Version Manager that polls latest version data from GitHub repo release tag.'

setup(
    # the name must match the folder name 'verysimplemodule'
    name="versionmanager",
    version=VERSION,
    author="Kamron Cole",
    author_email="kjc8084@rit.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'github', 'version', 'manager', 'version manager'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

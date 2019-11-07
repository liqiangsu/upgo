import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='upgo',  
    version='0.1',
    scripts=['upgo.py', "bin/upgo.cmd"], #TODO inlclude other OS
    author="Jake Zhang & Danny Su",
    author_email="jakezhang1989@hotmail.com",
    description="AWS utility that help manaing multi-services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liqiangsu/upgo",
    packages=setuptools.find_packages(),
    license = "Apache License Version 2.0",
    classifiers=[
        "Development Status :: 1 - Planning"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],

 )
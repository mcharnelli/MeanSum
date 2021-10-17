from setuptools import find_packages, setup
from setuptools import setup, Extension
import shutil
import os 
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.install import install as InstallCommandBase
from setuptools.command.develop import develop as DevelopCommmandBase
from setuptools.command.build_ext import build_ext as build_ext_orig
BASEPATH = Path(__file__).resolve().parent


setup(
    name="MeanSum",
    packages=find_packages(),
    version="0.2.1",
    description="MeanSum",
    author="",
    install_requires=[
	"nltk",
	"tensorboardX",
    ],
    license="MIT",

)

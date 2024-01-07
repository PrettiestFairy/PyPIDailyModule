# coding: utf8
""" 
@File: setup.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-07
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="austin_module_daily",
    version="0.0.1",
    author="Austin D",
    author_email="fairylandhost@outlook.com",
    description="Austin personally developed Python library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com.AustinFairyland/AustinModulesDaily",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AGPL-3.0 License"
    ],
    python_requires=">=3.7",
    
)

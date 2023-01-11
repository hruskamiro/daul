# -*- coding: utf-8 -*-
# Copyright (c) 2023 Miroslav Hruska
"""
The setup script for the daul package. 
"""

#%% Modules
from setuptools import setup, find_packages

#%% Actual setup
setup(
  name="daul",
  version='0.1.0',
  description="Data analysis and other utilities for python.", 
  #   
  author="Miroslav Hruska",
  author_email="hruska.miro@gmail.com", 
  #   
  url='https://github.com/hruskamiro/daul', 
  keywords="data analysis utilities",
  classifiers=[
    "License :: OSI Approved :: MIT License",
  ],
  # 
  packages=find_packages(),
  #   
  python_requires='>=2.7,<3', 
  #   
  install_requires=['numpy>=1.16.5', 
                    'pandas>=0.24.2', 
                    'fplib>=0.1.1',
                    'pathlib>=1.0.1']
)

#!/bin/bash

export JUPYTER_CONFIG_DIR=config jupyter notebook notebooks
jupyter nbextension install RISE/livereveal --symlink --nbextensions config/nbextensions
jupyter nbextension enable livereveal/main
jupyter notebook notebooks

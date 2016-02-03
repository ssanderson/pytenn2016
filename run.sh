#!/bin/bash

jupyter nbextension install RISE/livereveal --symlink --nbextensions config/nbextensions
jupyter notebook notebooks --config config/jupyter_notebook_config.py

#!/bin/bash

venv_name="pytenn2016"

if [[ -z "$(type -t workon)" ]];
then
    echo "No function named 'workon' found. Did you execute ./run.sh instead of 'source'-ing?"
    echo "See https://virtualenvwrapper.readthedocs.org/en/latest/install.html"
elif [[ -z "$(lsvirtualenv -b | grep $venv_name)" ]];
then
    echo "No virtualenv named $venv_name found."
else
    workon pytenn2016

    # Install module and dependencies editably.
    pip install -e . ./pyxl3

    export JUPYTER_CONFIG_DIR=config jupyter notebook notebooks
    jupyter nbextension install RISE/livereveal --symlink --nbextensions config/nbextensions
    jupyter nbextension enable livereveal/main
    jupyter notebook notebooks/Main.ipynb
fi

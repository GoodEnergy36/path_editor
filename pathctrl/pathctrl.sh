#!/bin/bash

if [ -n "$PYTHON_EXECUTED" ]; then
    my_path=$(cat ./path.txt)

    echo "export PATH="$my_path > ~/.zshrc

    source ~/.zshrc

    echo -e "\nplease restart your terminal to see changes\n"
else
    echo "Wrong script buddy."
fi
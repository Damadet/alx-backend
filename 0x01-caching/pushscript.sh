#!/usr/bin/env bash

read -p "Enter your commit file: " FILE

git add $FILE

read -p "Enter your commit message: " COMMIT

git commit -m '$COMMIT'

git push
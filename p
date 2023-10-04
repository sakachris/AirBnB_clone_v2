#!/usr/bin/env bash
#add, commit, push to github

git add .
echo "commit message: "
read -r message

git commit -m "$message"
git push

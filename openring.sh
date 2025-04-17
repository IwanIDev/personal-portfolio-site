#!/bin/bash

cd openring

go run openring.go \
  -s https://drewdevault.com/blog/index.xml \
  -s https://emersion.fr/blog/rss.xml \
  -s https://danluu.com/atom.xml \
  < ../openring-in.html \
  > ../openring.html

cd ../

mv openring.html themes/PelicanTheme/templates/

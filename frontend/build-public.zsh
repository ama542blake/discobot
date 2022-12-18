#!/bin/zsh

# copies all HTML and CSS source files into the public directory
# doesn't handle ts files because tsc does that already

GREEN="\033[1;32m"
NOCOLOR="\033[0m"

# copy all non-compiled files to the base directory for hosting
echo "${GREEN}COPY PUBLIC:${NOCOLOR} copying HTML files..."
cp -R ./src/index.html ./public/index.html
echo "${GREEN}COPY PUBLIC:${NOCOLOR} finished copying HTML files"

echo "${GREEN}COPY PUBLIC:${NOCOLOR} compiling SASS..."
sass src/styles/
cp -R src/styles/ public/css/   # move to the public directory
rm public/css/index.scss
rm src/styles/index.css
rm src/styles/index.css.map
echo "${GREEN}COPY PUBLIC:${NOCOLOR} done compiling SASS"

echo "${GREEN}COPY PUBLIC:${NOCOLOR} copying CSS files..."
cp -R ./src/css ./public/css
echo "${GREEN}COPY PUBLIC:${NOCOLOR}: finished copying CSS files"
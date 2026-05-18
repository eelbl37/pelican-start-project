Title: Initial setup
Date: 2026-05-01
Author: Einte Elsinga
Modified: 2026-05-01
Category: theme maken
Tags: start, setup, democontent
Summary: Starten met pelican. Installeren en quickstart maken.
Status: Published

# Initial setup

Let's create a blog called The Analog Fox, following Pelican's quickstart guide.

I created a virtual environment and installed Pelican as suggested, then run

mkdir theanalogfox
cd theanalogfox
pelican-quickstart

For this project I will only run the blog locally, so I didn't configure any specific way to publish it, neither properly set up a URL prefix. If you are about to create a real website please read Pelican's documentation about those settings.

> Where do you want to create your new web site? [.] 
> What will be the title of this web site? The Analog Fox
> Who will be the author of this web site? Leonardo Giordani
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) 
> How many articles per page do you want? [10] 3
> What is your time zone? [Europe/Paris] 
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) 
> Do you want to upload your website using FTP? (y/N) 
> Do you want to upload your website using SSH? (y/N) 
> Do you want to upload your website using Dropbox? (y/N) 
> Do you want to upload your website using S3? (y/N) 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
> Do you want to upload your website using GitHub Pages? (y/N) 
Done. Your new project is available at /home/leo/devel/theanalogfox

If you run pelican -lr now and visit http://localhost:8000 with your browser you will see the first page of the blog rendered with the default theme.


# Demo content

Demo content¶

Before we venture into the jungle of Jinja templates it's worth creating some content. As this is a very boring activity I prepared a little script that you can run in the terminal.

#!/bin/bash

NUM_POSTS=20
CONTENT_DIR=content
LOREM_API=https://jaspervdj.be/lorem-markdownum/markdown.txt
IMAGES_API=https://placeimg.com/1000/341/animals

rm -fR content
mkdir -p content/images

for i in $(seq -w 1 ${NUM_POSTS})
do
    post_file=${CONTENT_DIR}/post${i}.markdown

    echo "Creating post ${i}"
    echo "Title: A sample article ${i}" >> ${post_file}
    echo "Date: 2021-03-${i}" >> ${post_file}
    echo "Category: News" >> ${post_file}
    echo "Tags: $(seq 1 20 | shuf | head -n3 | sed -r s,"^","tag", | paste -sd "," -)" >> ${post_file}
    echo "Image: post${i}.jpg" >> ${post_file}
    echo "Summary: Summary of post ${i}" >> ${post_file}
    echo >> ${post_file}

    curl -s ${LOREM_API} | sed -r s,"^#","##", >> ${post_file}

    curl -s ${IMAGES_API} > ${CONTENT_DIR}/images/post${i}.jpg
done

Save it as create_content.sh and give it execution permissions with chmod 775 create_content.sh. At this point you can run it with ./create_content.sh and it will create the directory content with 20 posts and an image for each of them. You can safely run it multiple times, it will automatically delete the previous output.

If you know bash feel free to hack the script to do something more complicated, but this very simple program does everything we need to work on Pelican themes.

Running pelican -lr and visiting http://localhost:8000 will now show a richer website.

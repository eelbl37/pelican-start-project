Title: Templates
Date: 2026-05-01
Author: Einte Elsinga
Modified: 2026-05-01
Category: template
Tags: start, setup, democontent
Summary: Starten met het leren templates te maken.
Status: Published

# The template

From now on I will make extensive use of the documentation at https://docs.getpelican.com/en/latest/themes.html#creating-themes, so please be sure to have that page open in your browser.

For this tutorial I will use the template "Future Imperfect" by HTML5 UP. The template can be seen in action at this page, and you can download it using the button in the top right corner of the page itself.

Please consider supporting HTML UP even only with a Tweet. Being a content creator myself I know how important it can be to receive any type of feedback from readers/users.

Let's have a quick look at the template before we dive into the core of the post. We have a navbar at the top of the screen, with a link to the homepage, several links to specific pages, a search button, and a menu. In the body of the page there is a sidebar on the left and a preview of the articles on the right.

The sidebar contains the title and the subtitle of the blog, two lists of posts, the about section, and some social buttons. The first list of posts features image, title, date, and the avatar of the author, while the second list has just a small thumbnail, title, and date. Each post in the main list shows the full image, title, subtitle, name and avatar of the author, publication date, a preview of the content of the article, and a button that links the full version of the article. Last, tags are listed at the bottom right, just next to the number of likes and comments.

Just to be clear from the start, I won't implement everything we see here in my Pelican theme. I won't touch the navbar, and I won't discuss likes and comments, which require external systems when it comes to static sites. I will also simplify the sidebar, using only one list of posts. Moreover, I will not preview the articles in the main page, but print the full content.

Unzip the template archive in a subdirectory of the blog directory called future-imperfect. The archive doesn't contains a root folder, so you need to create it explicitly.

Enter the theme directory and change the layout of the files to follow Pelican's requirements:

```
    mv assets/ static
    mv images/ static/
    mkdir templates
    mv *.html templates/
```


At this point edit the file pelicanconf.py in the main directory of the blog, adding the variable THEME



# pelicanconf.py

```
PATH = 'content'

THEME = "future-imperfect"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
```

If you refresh the blog page now you will see that the output doesn't even have a working style sheet, but don't worry, Pelican is still working correctly. We are overriding Pelican's output with the file future-imperfect/templates/index.html, which is supposed to be a Jinja template, but being part of the HTML5 template is just injecting static content. In particular, the CSS/JS assets are not loaded correctly, as you can see.

Let's learn the first piece of syntax adjusting the CSS and JS links, then, so that we can at least have a good output to look at. We need to change the path assets/ with {{ SITEURL }}/theme/




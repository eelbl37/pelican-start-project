Title: Variabels on pelican
Date: 2026-05-01
Author: Einte Elsinga
Modified: 2026-05-01
Category: template
Tags: start, setup, Variabels
Summary: Begin van een index.html. Variabels in pelican
Status: Published


## Variabels

Deep dive

How does {{ SITEURL }}/theme work?

Pelican's documentation on themes says

THEME_STATIC_DIR = 'theme'

Destination directory in the output path where Pelican will place the files collected from THEMESTATICPATHS. Default is het leeg.

the variable THEME_STATIC_PATHS is by default static, which is why we created that directory inside the theme.

As you can see all these paths are configurable, should you prefer different names.



## Pelican variabels

As I mentioned, we are currently overriding Pelican's output with a static template. What we want to do is to inject values known to Pelican into the template itself, be those static variables or more dynamic items like articles, tags, and images.

To do this, Pelican uses Jinja, a widely adopted template engine written in Python. If you want to fully understand how to create Pelican themes, then, you need to learn Jinja. Don't worry, it's not complicated, and since Jinja uses Python you will catch up very quickly. I won't get into details about the Jinja syntax that I will use, please check out the Jinja documentation if you have any doubts.

We actually already used Pelican's variables and Jinja templates when we prefixed links with {{ SITEURL }}. Aside from that, however, the first and simplest variable injection for our template are title and subtitle.


## Title

The Pelican variable we are interested in is SITENAME, which has been initialised by the quickstart script as you can see in the configuration file

```
    pelicanconf.py

    SITENAME = "The Analog Fox"
```


We need to replace the static text with this variable three times: in the tag title, in the navigation bar and in the header at the top of the sidebar.

## index.html title

<html>
  <head>
    <title>{{ SITENAME }}</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/main.css" />
  </head>
  <body class="is-preload">

    <!-- Wrapper -->
    <div id="wrapper">

      <!-- Header -->
      <header id="header">
        <h1><a href="index.html">{{ SITENAME }}</a></h1>
        <nav class="links">
          <ul>
            <li><a href="#">Lorem</a></li>

[...]

      <!-- Sidebar -->
      <section id="sidebar">

        <!-- Intro -->
        <section id="intro">
          <a href="#" class="logo"><img src="{{ SITEURL }}/theme/images/logo.jpg" alt="" /></a>
          <header>
            <h2>{{ SITENAME }}</h2>
            <p>Another fine responsive site template by <a href="http://html5up.net">HTML5 UP</a></p>
          </header>
        </section>

## subtitle

Pelican provides support even for the subtitle, but that wasn't filled in by the setup script for us, so we need to create the variable in the configuration file

    
    pelicanconf.py

    SITENAME = "The Analog Fox"
    SITESUBTITLE = "A great blog about old stuff"
  


## index.html

        <section id="intro">
          <a href="#" class="logo"><img src="{{ SITEURL }}/theme/images/logo.jpg" alt="" /></a>
          <header>
            <h2>{{ SITENAME }}</h2>
            <p>{{ SITESUBTITLE }}</p>
          </header>
        </section>



Marvellous! Now the page should show the title of the blog in the window header, announcing to the world the The Analog Fox is ready to take over the world of vintage!

OK, I might be a bit overexcited, but I love when plans come together ;)

## Gebruik pelicanconf.py

Pelican passes the whole configuration file to the template, together with the parsed content of the site itself, so you are free to use any variable, should you need them, or to introduce new ones (which we will do in the next section).

For now, just to familiarise with the concept, you might try to add TIMEZONE under the subtitle

      
      future-imperfect/templates/index.html

                <header>
                  <h2>{{ SITENAME }}</h2>
                  <p>{{ SITESUBTITLE }}</p>
                  <p>{{ TIMEZONE }}</p>
                </header>
      

I don't think this specific change is really useful, but it's good to remember that all those variables are available.

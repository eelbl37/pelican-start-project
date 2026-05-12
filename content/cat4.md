Title: index.html template
Date: 2026-05-01
Author: Einte Elsinga
Modified: 2026-05-01
Category: template
Tags: start, setup
Summary: Begin van een index.html. Deze template maakt de homepage
Status: Published


# Template index.html

```
    <!DOCTYPE HTML>
    <!--
        Future Imperfect by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
      -->
    <html>
      <head>
        <title>Future Imperfect by HTML5 UP</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="{{ SITEURL }}/theme/css/main.css" />
      </head>

    [...]

        <script src="{{ SITEURL }}/theme/js/jquery.min.js"></script>
        <script src="{{ SITEURL }}/theme/js/browser.min.js"></script>
        <script src="{{ SITEURL }}/theme/js/breakpoints.min.js"></script>
        <script src="{{ SITEURL }}/theme/js/util.js"></script>
        <script src="{{ SITEURL }}/theme/js/main.js"></script>

      </body>
    </html>    
    ```


We also need to correctly link images. Change any occurrence of images/ into {{ SITEURL}}/theme/images/, e.g.
```
    <div class="meta">
      <time class="published" datetime="2015-11-01">November 1, 2015</time>
      <a href="#" class="author"><span class="name">Jane Doe</span><img src="{{ SITEURL }}/theme/images/avatar.jpg" alt="" /></a>
    </div>
  </header>
  <a href="single.html" class="image featured"><img src="{{ SITEURL }}/theme/images/pic01.jpg" alt="" /></a>
  ```


If you refresh the page after these changes you will see the template fully rendered (minus the images you saw in the demo, those are replaced by placeholders in the downloaded version).

A little trick: if you remove the comments at lines 177 and 487 you will get a nice recap of the graphical components of the template. I will not use them, so I removed lines 176-487, but remember that those cheat sheets can be very useful when trying to understand how a template works.

As I mentioned earlier, I also removed the third list of posts, as it doesn't add anything to what we will learn. You are clearly free to keep it and experiment with it.


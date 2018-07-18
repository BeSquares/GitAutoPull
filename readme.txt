=== GitAutoPull ===
Requires at least: Python installed
License: MIT
License URI: http://www.gnu.org/licenses/gpl-2.0.html

== Installation ==

- Modify gitPull.conf.json with your git url and the pull location on your server
- Upload the files to your server
- Set 777 chmod for gitPull.py file
- Create new webhook on your git with gitPull.py location example.com/autos/gitPull.py

== Notic ==

If you have a private git you need to include the password inside the config file see gitPull.conf.json for example, For this reason make sure to upload .htaccess file in the same directory to block any direct access for the config file

== Debug ==

To enable debug mode you can use cgitb add the following line after line 6 cgitb.enable()
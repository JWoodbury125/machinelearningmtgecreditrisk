

Added the embedded html code in app.py and javascripts and Css  and as static is parent folder for referencing files in flask.

Problems faced: External javascripts files are not added when runs on flask
.Was not able to access the javascripts images and css referenced in html file from the parent folder


Solution worked on:
https://stackoverflow.com/questions/14711552/external-javascript-file-is-not-getting-added-when-runs-on-flask



Problem solution
For referencing css and javascripts, I found that the flask has inbuilt static folder and everything should be referred from static folder in the available in the subtree .



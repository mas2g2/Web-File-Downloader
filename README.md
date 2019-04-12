Filename: "readlink.py"
This script, given a website link, checks the <a> elements for their href attribute
and downloads the documents that are in their href document, as the script is
currently written it downloads documents from the urls specified in line 4, to get
this script to download files from another web site, you must go to line 4 in file "readlink.py" and add the website from which you would like to download files.

This script was made with the purpose of downloading a massive amount of pictures 
from a web page where each picture was presented with an <a> tag that when clicked
directed the user to the image. Originally the only way to download the images was
to click the links that would direct the user to a webpage where only the image 
would be displayed, but this script "scrapes" or looks for <a> tags which reference
downloadable documents and downloads all of those documents

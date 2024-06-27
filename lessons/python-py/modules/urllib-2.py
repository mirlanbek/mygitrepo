from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()

with open ("index.html", "w+") as w:
    w.write(str(html.decode()))


# Now on VSC  install Live Server, rghit click on index.html file, open with Live Server



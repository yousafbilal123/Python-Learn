import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Match found!")
else:
    print("No match found.")

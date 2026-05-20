import os

html_path = r"c:\Users\NHNcommerce\Desktop\folder\me\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Toss Blue Hex Codes with Emerald Green Hex Codes
html = html.replace("#3182f6", "#059669")
html = html.replace("#e8f3ff", "#ecfdf5")
html = html.replace("#2272eb", "#047857")
html = html.replace("#1c64f2", "#047857")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Themed HTML to Emerald successfully")

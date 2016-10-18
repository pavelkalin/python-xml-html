from xml.etree import ElementTree

path = 'xml-in/templates.xml'
root = ElementTree.parse(path).getroot()
pathto = 'html-out/'

for child in root:
    path = pathto + child[0].text + '.html'
    with open(path, 'w') as f:
        print(child[1].text, file=f)

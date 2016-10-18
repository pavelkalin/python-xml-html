# python-xml-html
Parse specific xml file and create html files from it


It expects a xml in xml-in folder to be like this 
```xml
<resultset>
<row>
    <element1>Subject</element1>
    <element2>html</element2>
</row>
<row>...</row>
<row>...</row>
</resultset>
```
Output will create html files in html-out folder with Subject as name of the file and html as content

##How to use it:

Clone repository into any folder via 
1. git clone git@github.com:pavelkalin/python-xml-html.git
2. put your xml into xml-in folder
3. run ```python main``` 
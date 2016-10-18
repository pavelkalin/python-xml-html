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
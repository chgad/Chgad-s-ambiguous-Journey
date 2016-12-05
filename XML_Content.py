import re
import xml



c_file = open("Content.txt","r+")
content=c_file.read()
c_file.close()
print(type(content))
#print(content)

pattern = re.compile(r"E\w+E")
x= re.findall(pattern,content)

titles_e=[title.replace("E","")for title in x]
cont=[]
for t in x :
        pos = content.find(t)
        start = content.find("{",pos)
        stop = content.find("}",pos)
        cont.append(content[start : stop+1].replace("\n",""))
        content = content[stop+1:]

text = [strings.replace("{","").replace("}","") for strings in cont]
print(len(titles_e))
print(len(text))
titles_text=[]
for title in titles_e:
    pos = titles_e.index(title)
    print(pos)
    txt = text[pos]
    titles_text.append((title,txt))

print(titles_text)


new = open("glossary_cont.txt","a")
for (k,v) in titles_text :
    if titles_e.index(k) == 0:
        xml="""<list>
  <glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>%s</p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>"""% (k,v)
        new.write(xml)
    elif titles_e.index(k)== -1:
        xml="""<glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>  <span>%s</span></p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>
</list>"""%(k,v)
        new.write(xml)
    else:
        xml="""<glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>  <span>%s</span></p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>"""%(k,v)
        new.write(xml)
new.close()




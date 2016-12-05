import re
import xml



c_file = open("Content.txt","r")
content=c_file.read()
c_file.close()

pattern = re.compile(r"E\w+E")                                  #find all titles; titles need to be encapsulated with E's
x= re.findall(pattern,content)

titles_e=[title.replace("E","")for title in x]


cont=[]
for t in x :                                                    # find the text blocks used for definition later on; text needs to be encapsulated
        pos = content.find(t)
        start = content.find("{",pos)
        stop = content.find("}",pos)
        cont.append(content[start : stop+1].replace("\n",""))
        content = content[stop+1:]
text = [strings.replace("{","").replace("}","") for strings in cont]

titles_text=[]                                                  # concatinate titles, with the corresponding text in a list of tuples

for title in titles_e:
    pos = titles_e.index(title)
    print(pos)
    txt = text[pos]
    titles_text.append((title,txt))


new = open("glossary_cont.txt","a")
for (k,v) in titles_text :                                              # now write the xml with title,text in the new file
    if titles_e.index(k) == 0:                                          # first title needs a leading <list> tag
        xml="""<list>
  <glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>%s</p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>"""% (k,v)
        new.write(xml)
    elif titles_e.index(k)== -1:                                        #last title needs a ending </list> tag
        xml="""<glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>  <span>%s</span></p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>
</list>"""%(k,v)
        new.write(xml)
    else:                                                               #all other titles , texts
        xml="""<glossentry>
    <glossTerm>%s</glossTerm>
    <glossDef><![CDATA[<p>  <span>%s</span></p>]]></glossDef>
    <glossSynonyms/>
  </glossentry>"""%(k,v)
        new.write(xml)

new.close()




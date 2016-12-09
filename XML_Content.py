import re

def work_file(content_file):                           #content has to be the files name with the info in it
    c_file = open(content_file,"r")
    content=c_file.read()
    c_file.close()
    return content                                      # return content in a string

def process_cont_string(content):
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
        txt = text[pos]
        titles_text.append((title,txt))
    return titles_text                                              # return list of title,text values


""" Here an Update mode is created"""
def work_update_file(wish_file):                # the file to be updated
    new = open(wish_file,"r")
    f = new.read()
    new.close()
    f.replace("</list>","")                     # remove the last xml operator </list>
    return f

def add_stuff(wish_file,titles_text):

    new = open(wish_file, "a")
    for (k, v) in titles_text:
        if titles_text.index((k, v)) == 0:                      # here the leading <list> is missing due to fact that we update the file
            xml = """
      <glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA<p>[%s</p>]]></glossDef>
        <glossSynonyms/>
      </glossentry>""" % (k, v)
            new.write(xml)
        elif titles_text.index((k, v)) == len(titles_text) - 1:  # last title needs a ending </list> tag
            xml = """<glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA[<p>  %s</p>]]></glossDef>
        <glossSynonyms/>
        </glossentry>
            </list>""" % (k, v)
            new.write(xml)
        else:  # all other titles , texts
            xml = """<glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA[<p>  %s</p>]]></glossDef>
        <glossSynonyms/>
      </glossentry>""" % (k, v)
            new.write(xml)







def create_xml_glossary(titles_text):                #creats a xml-cont file named glossary_cont.txt
    new = open("glossary_cont.txt","a")
    for (k,v) in titles_text :
        if titles_text.index((k,v)) == 0:
            xml="""<list>
      <glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA[<p>%s</p>]]></glossDef>
        <glossSynonyms/>
      </glossentry>""" % (k,v)
            new.write(xml)
        elif titles_text.index((k,v)) == len(titles_text)-1:                                        #last title needs a ending </list> tag
            xml="""<glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA[<p>  %s</p>]]></glossDef>
        <glossSynonyms/>
        </glossentry>
            </list>""" %(k,v)
            new.write(xml)
        else:                                                               #all other titles , texts
            xml="""<glossentry>
        <glossTerm>%s</glossTerm>
        <glossDef><![CDATA[<p>  %s</p>]]></glossDef>
        <glossSynonyms/>
      </glossentry>"""%(k,v)
            new.write(xml)
    new.close()
""" For creation of a new .xml glossary file decomment"""
#string = work_file("Content.txt")# replace Content.txt with the file that contains YOUR content !! .txt files only !!
#titles_text = process_cont_string(string)
#create_xml_glossary(titles_text)# creates an .txt file named glossary_cont.txt , change .txt to .xml afterwards
"""For updating a existent .xml gloyyary file"""
#string = work_update_file("test")# replace test with the name of your glossary !! Channge the .xml to txt for processing undo afterwards !!
#titles_text = process_cont_string("content")#replace content witht the files name containing the glossary's contentn !! .txt files only!!
#add_stuff(titles_text)



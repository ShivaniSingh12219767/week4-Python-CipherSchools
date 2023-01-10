with open("week4-Python-CipherSchools/index.html","r") as webpage:
    with open("week4-Python-CipherSchools/output2.txt","a") as wf:
        page = webpage.read()
        link_exists = True
        while link_exists:
            pos = page.find("<a href=")
            if pos == -1:
                link_exists = False
            else:
                first_quote = page.find("\'",pos)
                second_quote = page.find("\'",first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url + '\n')
                page = page[second_quote:]
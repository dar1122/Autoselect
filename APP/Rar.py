from unrar import rarfile
import re




def rarto(url1,url2):

    file = rarfile.RarFile(url1+url2)

    x=file.namelist()

    for name in x:
        dll = re.match('.+.dll',name)
        so  = re.match('.+.so',name)
        ini = re.match('.+.ini', name)
        sql = re.match('.+.sql', name)

        if (dll!=None) |(so != None) |(ini!=None) |(sql!=None):
            file.extract(name,'F:/desktest')
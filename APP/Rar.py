from unrar import rarfile
import re




def rarto(url1,url2,getname,to_url):

    file = rarfile.RarFile(url1+url2)

    x=file.namelist()

    for name in x:
        for num in getname:
            if num==name :
                if re.match('.+.so', num) != None:
                    file.extract(num,to_url+'so')
                elif re.match('.+.ini', num) != None:
                    file.extract(num, to_url+'ini')
                elif re.match('.+.dll', num) != None:
                    file.extract(num, to_url+'dll')
                elif re.match('.+.sql', num) != None:
                    file.extract(num, to_url+'sql')
                else:
                    file.extract(num, to_url)
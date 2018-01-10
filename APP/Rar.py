from unrar import rarfile
import re




def rarto(url1,url2,getname):

    file = rarfile.RarFile(url1+url2)

    x=file.namelist()

    for name in x:
        for num in getname:
            if num==name :
                if re.match('.+.so', num) != None:
                    file.extract(num,'F:/desktest/so')
                elif re.match('.+.ini', num) != None:
                    file.extract(num, 'F:/desktest/ini')
                elif re.match('.+.dll', num) != None:
                    file.extract(num, 'F:/desktest/dll')
                elif re.match('.+.sql', num) != None:
                    file.extract(num, 'F:/desktest/sql')
                else:
                    file.extract(num, 'F:/desktest')
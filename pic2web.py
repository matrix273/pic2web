import os

def toweb():
    path=os.getcwd()
    extension = '.html'
    name= os.path.basename(path)+extension
    f = open( name,'w+')
    f.write('''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='UTF-8'>
    <body bgcolor='#FFD700'>
    <title>'''+os.path.basename(path)+'''</title>
    </head>
    <body>
    <p style='text-align:center'>
    ''')
    f.close()
    f = open(name,'a+')
    filelist = os.listdir(path)
    for i in filelist:
        port = os.path.splitext(i)
        if port[1] ==".jpg":    
            print('<img src="'+path+'\\'+i+"\""+'width="1330"'+' />',file=f)
        
    f.close()
    f = open(name,'a+')
    f.write('</p>\n</body>\n</html>\n</html>')
    f.close()

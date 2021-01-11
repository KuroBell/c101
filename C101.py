import dropbox
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadFile(self,source,destination):
        db = dropbox.Dropbox(self.accesstoken)
        for r,d,f in os.walk(source):
            for i in f:
                path= os.path.join(r,f)
                relativepath = os.path.relpath(path,source)
                dropboxpath = os.path.join(destination,relativepath)
                with open(path,'rb') as p:
                    db.files_upload(p.read(),dropbox,mode = WriteMode('overwrite'))
                    
def main():
     AT = 'sl.Ao9ljxg4StzWZDgcrl_KhKzYayxd91DR3FjPKQl8qOM86mwTZvqTIMCo0qCqBOuBK0IjKq1lL_Sut-5Q2uZ5o1oBAeljPWh2NUhQ1kspGKi8KP3tq-sTUicy4FnaBsMuP7aalnE'
     t = TransferData(AT)
     source = str(input('Enter the folder path to transfer'))
     destination = input('Enter full path to upload to dropbox')
     t.uploadFile(source,destination)
     print('operation successful')

main()
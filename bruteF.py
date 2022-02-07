import PyPDF2 as pd
import time

starttime = time.time() 
##filename = input('Path to the file: ')
file = open("/Users/vanshbafna/Desktop/module5/C223/Brute_Encrypted.pdf",'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile = open("/Users/vanshbafna/Desktop/module5/C223/wordlist.txt")
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print("Trying To Decode Password By:{}".format(word))
        result = pdfReader.decrypt(word)
        endtime = time.time() 
        if result == 1:
            duration = endtime - starttime
            print('Your password decoded in'+str(duration)+' seconds')
            print("sucess the password is: " + word)
            break

        elif result == 0:
            tried += 1
            print("password tried: " + str(tried))
            continue

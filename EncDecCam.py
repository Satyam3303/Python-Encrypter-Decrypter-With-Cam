import string
import cv2
import time

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

def enc(all,key,pazz):
    f = open('D:\Important Stuffs\Projects\Python Encryptor Decryptor With Camera\Python-Encrypter-Decrypter-With-Cam\hello.txt','r')
    pl_text = f.read()
    f.close()
    cip_text=""
    for letter in pl_text:
        index = all.index(letter)
        cip_text += key[index]
    f = open('D:\Important Stuffs\Projects\Python Encryptor Decryptor With Camera\Python-Encrypter-Decrypter-With-Cam\hello.txt','w')
    f.write(cip_text)
    f.write(pazz)
    f.close()
    print(cip_text)
    Main()

def dec(all,key,pazz):
    f = open('D:\Important Stuffs\Projects\Python Encryptor Decryptor With Camera\Python-Encrypter-Decrypter-With-Cam\hello.txt','r')
    cip_text = f.read()
    f.close()
    if pazz in cip_text:
        cip_text = cip_text.replace(pazz,'')
        pl_text=""
        for letter in cip_text:
            index = key.index(letter)
            pl_text += all[index]
        f = open('D:\Important Stuffs\Projects\Python Encryptor Decryptor With Camera\Python-Encrypter-Decrypter-With-Cam\hello.txt','w')
        f.write(pl_text)
        f.close()
        print(pl_text)
        Main()
    
    else:
        print("Wrong Password")
        
        start_time = time.time()
        while (time.time() - start_time) < 5:
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame from camera")
                Main()

    
            out.write(frame)

            cv2.imshow("Camera", frame)
            


        cap.release()
        out.release()
        cv2.destroyAllWindows()



def Main():
    allchar = " " + string.punctuation + string.digits + string.ascii_letters
    keychar = string.punctuation + string.ascii_letters  + string.digits + " "

    allchar = list(allchar)
    keychar = list(keychar)
    x = input("Enter the operation\n 1 Encryption\n 2 Decryption")
    a = input("Enter the key")

    if(x=='1'):
        enc(allchar,keychar,a) 

    elif(x=='2'):
        dec(allchar,keychar,a)
    
    
if __name__=='__main__':
    Main()

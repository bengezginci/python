#Local ağ bilgisayardan söküldüğünde ekranı kilitleyen python uygulaması
#When Lan Offline Lock Screen

import time, os, ctypes, subprocess#, keyboard
  
def internet_on():
    try:
        result = subprocess.run(
                ['ping', '192.168.16.1', '-n', '3', '-l', '32', '-w', '3'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW  # Hide the shell window
            )
        return result.returncode == 0  # If ping is successful, return True
    except Exception as e:
        return False  # If there’s any exception, return False
    #return (lambda a: True if 0 == a.system('ping 192.168.16.1 -n 3 -l 32 -w 3 >nul') else False)(os)


def Kop():
    #print("Sistem kopuk")
    Kitle()
    
def Kitle():
    ctypes.windll.user32.LockWorkStation()
    
def KontrolEt():
    #Kopma=0
    while True:
        #print('countdown started', flush=True)
        
        if(internet_on() is False):
            '''Kopma+=1
            if Kopma >1:
                Kop()
                Kopma=0'''
            Kop()
            
                
            #print(internet_on(), Kopma)
            #print(i, end=', ', flush=True)
        time.sleep(1)


KontrolEt()

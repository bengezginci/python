#Lan kablosu çıkarılırsa ve netschool kapatılırsa ekranı kilitle
#Uzantısını .pyw yaparsanız arkaplanda sessizce çalışır
#Ctrl+Alt+Z ile program çalışmayı durdurur
#When Lan disconnect and netschool shotdown lock the screen
#If you run with .pyw extension, it will work in background

import ctypes, os, subprocess, time, keyboard

def internet_on():
    try:
        result = subprocess.run(
                ['ping', '192.168.3.1', '-n', '3', '-l', '32', '-w', '3'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW  # Hide the shell window
            )
        return result.returncode == 0  # If ping is successful, return True
    except Exception as e:
        return False  # If there’s any exception, return False
    #return (lambda a: True if 0 == a.system('ping 192.168.16.1 -n 3 -l 32 -w 3 >nul') else False)(os)

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    #output = subprocess.check_output(call).decode()
    output = subprocess.check_output(call, creationflags=subprocess.CREATE_NO_WINDOW).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

def Calisiyormu(Liste):
    for L in Liste:
        if(process_exists(L) is False):
            Kop()
    '''for L in Liste:
        if(process_exists(L)):
            print(L + " calisiyor")
        else:
            print(L +" Calismiyor")'''


def Kop():
    #print("Sistem kopuk")
    Kitle()
   
def Kitle():
    ctypes.windll.user32.LockWorkStation()
   
def KontrolEt():
    #Kopma=0
    while True:
        #print('countdown started', flush=True)
       
        if keyboard.is_pressed('ctrl+alt+z'):
            #print("Uygulama durduruldu.")
            break
        if(internet_on() is False):
            '''Kopma+=1
            if Kopma >1:
                Kop()
                Kopma=0'''
            Kop()
            #print(internet_on(), Kopma)
            #print(i, end=', ', flush=True)

        Calisiyormu(['runplugin.exe', 'StudentUI.exe', 'Runplugin64.exe']) #netsupport uygulamaları
        
        time.sleep(8)


KontrolEt()


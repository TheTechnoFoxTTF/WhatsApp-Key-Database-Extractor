from helpers.CustomCI import CustomInput, CustomPrint
import os
import subprocess
import platform
import re


# Detect OS
isWindows = False
isLinux = False
if platform.system() == 'Windows' : isWindows = True 
if platform.system() == 'Linux' : isLinux = True

# Global variables
isJAVAInstalled = False

# Global command line helpers
adb = 'bin\\adb.exe'
delete = 'del'
tmp = 'tmp\\'
confirmDelete = '/q'
grep = 'bin\\grep.exe'
curl = 'bin\\curl.exe'
helpers = 'helpers\\'
bin = 'bin\\'
extracted = 'extracted'
tar = 'tar.exe'
if(isLinux) : 
    adb = 'adb'
    delete = 'rm -rf'
    tmp = 'tmp/'
    confirmDelete = ''
    grep = 'grep'
    curl = 'curl'
    helpers = 'helpers/'
    bin = 'bin/'
    tar = 'tar'


def main() : 
    ShowBanner()
    global isJAVAInstalled
    isJAVAInstalled = CheckJAVA()
    ExtractAB(isJAVAInstalled)

def CheckJAVA() : 
    JAVAVersion = re.search('(?<=version ")(.*)(?=")', str(subprocess.check_output('java -version'.split(), stderr=subprocess.STDOUT))).group(1)
    isJAVAInstalled = True if(JAVAVersion) else False
    if (isJAVAInstalled) : 
        CustomPrint('Found Java installed on system. Continuing...')
        return isJAVAInstalled
    else : 
        noJAVAContinue = CustomInput('It looks like you don\'t have JAVA installed on your system. Would you like to (C)ontinue with the process and \'view extract\' later? or (S)top? : ', 'green') or 'c'
        if(noJAVAContinue=='c') : 
            CustomPrint('Continuing without JAVA, once JAVA is installed on system run \'view_extract.py\'', 'green')
            return isJAVAInstalled
        else : 
            Exit()

def CleanTmp() :
        if(os.path.isdir(tmp)) : 
            CustomPrint('Cleaning up tmp folder...')
            os.remove('tmp/whatsapp.tar')
            os.remove('tmp/whatsapp.ab')

def Exit():
    CustomPrint('\nExiting...', 'green')
    os.system('bin\\adb.exe kill-server')
    quit()

def ExtractAB(isJAVAInstalled) :
    if not (isJAVAInstalled) : 
        CustomPrint('Can not detect JAVA on system.')
        Exit()
    if(os.path.isfile(tmp + 'whatsapp.ab')) :
        abPass = CustomInput('Please enter password for backup (leave empty for none) : ')
        try : 
            os.system('java -jar ' + bin + 'abe.jar unpack ' + tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ' + str(abPass))
            CustomPrint('Successfully \'fluffed\' '+ tmp + 'whatsapp.ab ' + tmp + 'whatsapp.tar ')
            TakingOutMainFiles()
        except Exception as e : 
            CustomPrint(e)

def ShowBanner() : 
    banner_path = 'non_essentials/banner.txt'
    try : 
        banner = open(banner_path,'r')
        banner_content = banner.read()
        CustomPrint(banner_content, 'green', ['bold'])
        banner.close()
    except Exception as e : 
        CustomPrint(e)
    CustomPrint('============ WhatsApp Key / Database Extrator on non-rooted Android ============\n', 'green', ['bold'])
    
def TakingOutMainFiles() : 
    targetName = CustomInput('Enter a reference name for this target. : ') or 'target'
    os.mkdir(extracted + '/' + targetName) if not (os.path.isdir(extracted + '/' + targetName)) else CustomPrint('Folder already exists.')
    CustomPrint('Taking out main files in ' + tmp + ' folder temporaily.')
    try : 
        os.system('' if (isLinux) else bin  + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/f/key') ; os.replace('tmp/apps/com.whatsapp/f/key', extracted + '/' + targetName + '/key')
        os.system('' if (isLinux) else bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/msgstore.db') ; os.replace('tmp/apps/com.whatsapp/db/msgstore.db', extracted + '/' + targetName + '/msgstore.db')
        os.system('' if (isLinux) else bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/wa.db') ; os.replace('tmp/apps/com.whatsapp/db/wa.db', extracted + '/' + targetName + '/wa.db')
        os.system('' if (isLinux) else bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/axolotl.db') ; os.replace('tmp/apps/com.whatsapp/db/axolotl.db' , extracted + '/' + targetName + '/axolotl.db')
        os.system('' if (isLinux) else bin + tar + ' xvf ' + tmp + 'whatsapp.tar -C ' + tmp + ' apps/com.whatsapp/db/chatsettings.db') ; os.replace('tmp/apps/com.whatsapp/db/chatsettings.db', extracted + '/' + targetName + '/chatsettings.db')
        # Reset bin here...
        CleanTmp()
    except Exception as e : 
        CustomPrint(e)
        CleanTmp()

if __name__ == "__main__":
    main()
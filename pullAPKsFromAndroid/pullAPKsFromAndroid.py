#/bin/bash

import os

apkli = "adb shell pm list packages -f> apklist_path/apklist.txt"
#pullsdc = "adb pull /sdcard/ all/"
#bur= "adb bugreport all/bureport.zip"
#port = "adb shell netstat -anp >all/netstat.txt"

os.system(apkli)
#os.system(pullsdc)
#os.system(bur)
#os.system(port)

f=open("apklist_path/apklist.txt")

for line in f.readlines():
    if line == '\n':
        continue
    else:
        line = line.replace("package:","")
        apkaddr=line.rsplit("=", 1)[0]
        print("apkaddr:"+apkaddr)
        apk=line.rsplit("=", 1)[1].replace('\n','')
        print("apk:"+apk)

        try:
            print('-'*60)
            adb = 'adb pull '+ apkaddr + ' apklist_path'+apk+'.apk'
            print(adb)
            os.system(adb)

        except:
            continue
        
#pull odex

# for line in f.readlines():
#     if line == '\n':
#         continue
#     else:
#         line = line.replace("package:","")
#         odexaddr=line.split("=")[0].replace('apk','odex')
#         print("apkaddr:"+odexaddr)
#         apk=line.split("=")[1].replace('\n','')
#         print("apk:"+apk)

#         try:
#             print('-'*60)
#             adb = 'adb pull '+ odexaddr + ' apklist_path'+apk+'.odex'
#             print(adb)
#             os.system(adb)

#             o2samil = 'java -jar baksmali-2.5.2.jar x odex/'+ apk +'.odex' + ' -o '+ 'odex/'+apk+'/ '+ '-a 16 -d framework/'
#             print(o2samil)
#             os.system(o2samil)

#             s2dex = 'java -jar smali-2.5.2.jar a odex/'+apk+'/ '+'-o all/apklist/'+apk+'/'+apk+'.dex'
#             print(s2dex)
#             os.system(s2dex)
#         except:
#             continue 
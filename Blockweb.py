
import os

'''Clears the host file '''
def clear():
    os.chdir('C:\Windows\System32\drivers\etc')
    confirmation = input("Type \"confirm\" to clear host file  ")
    confirmation = confirmation.strip()
    if confirmation == 'confirm':
        with open('hosts', 'w+') as file:
            file.truncate(0)

'''Clears file that contains websites we want to block '''
def clearblocweb():
    os.chdir('C:\DEV\Block\WebsiteLimitandBlock')
    with open('blocweb.txt','r+') as  BlockWebsitesEntered:
        print(BlockWebsitesEntered.read())
        confirmation = input("Type \"confirm\" to clear list of blocked websites   ")
        confirmation = confirmation.strip()
        if confirmation == 'confirm':
            BlockWebsitesEntered.truncate(0)

def block(): #stands for simple block
    bloclist = []
    continu = 'y'
    while continu == 'y':
        os.chdir('C:\Windows\System32\drivers\etc')
        with open('hosts', 'r+') as file:
            print(file.read())
            print(bloclist)
            z = input("Please enter file in format: \"www.domainname.com\"")
            bloclist.append(f"127.0.0.1 {z}")
            print('Would you like to add anything else?    ')
            continu = input("y or n ")
            continu = continu.strip()

    if continu == 'n':
        #remove dups in blocklist
        blocset = {dup for dup in bloclist}
        bloclist = list(blocset)
        with open('hosts', 'a+') as file:
            for i in bloclist:
                file.write("\n"+i)

        os.chdir('C:\DEV\Block\WebsiteLimitandBlock')
        with open("blocweb.txt", "a+") as BlockWebsitesEntered:
            print(BlockWebsitesEntered.read())

        # read blocweb.txt and look for duplicates
            for i in bloclist:
                BlockWebsitesEntered.write('\n'+ i)

'''Displays contents of host file'''
def display():
    os.chdir('C:\Windows\System32\drivers\etc')
    with open('hosts', 'r+') as file:
        print(file.read())
    
def displaylist():
    '''list of websites that are on the block text file'''
    os.chdir('C:\DEV\Block\WebsiteLimitandBlock')
    with open("blocweb.txt", "r+") as BlockWebsitesEntered:
        print(BlockWebsitesEntered.read())

def timerblock(): # add param start_time,end_time
    '''clears file and then reads stuff from readlist whenever needed'''
    os.chdir('C:\Windows\System32\drivers\etc')
    with open('hosts', 'w+') as file:
        file.truncate(0)
        file.close()
    os.chdir('C:\DEV\Block\WebsiteLimitandBlock')#make blank text file that is apart of setup and populate the file with website
    with open('blocweb.txt','r+') as blocweb:
        putback = blocweb.readlines()
    os.chdir('C:\Windows\System32\drivers\etc')
    with open('hosts', 'r+') as file:
        x = file.readlines()
        for j in putback:
            if j not in x:
                file.writelines(j)

'''removes from host file'''
def removeblock():
    site = input('What website do you want to unblock(www."".""): ')
    to_remove = f"127.0.0.1 {site}"
    os.chdir('C:\Windows\System32\drivers\etc')
    file = open('hosts','r+')
    lines = file.readlines()
    to_add = []
    for line in lines:
        if to_remove not in line:
            to_add.append(line)
    file.truncate(0)
    file = open('hosts','a+')
    for line in to_add:
        file.writelines('\n' + line)


'''removes from host and blocweb '''
def permremoveblock():
    site = input('What website do you want to unblock: ')
    to_remove = f"127.0.0.1 {site}"
    os.chdir('C:\Windows\System32\drivers\etc')
    file = open('hosts', 'r+')
    lines = file.readlines()
    to_add = []
    for line in lines:
        if to_remove not in line:
            to_add.append(line)
    file.truncate(0)
    file = open('hosts', 'a+')
    for line in to_add:
        file.writelines('\n' + line)

    os.chdir('C:\DEV\Block\WebsiteLimitandBlock')#text file
    BlockWebsitesEntered = open('blocweb.txt','r+')
    lines = BlockWebsitesEntered.readlines()
    to_add = []
    for line in lines:
        if to_remove not in line:
            to_add.append(line)
    BlockWebsitesEntered.truncate(0)
    BlockWebsitesEntered = open('blocweb.txt','a+')
    for line in to_add:
        BlockWebsitesEntered.writelines('\n' + line)

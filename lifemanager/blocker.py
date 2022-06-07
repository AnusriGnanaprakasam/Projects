import os

'''Clears the host file '''
def clear():
    os.chdir('C:\Windows\System32\drivers\etc')
    with open('hosts', 'w+') as file:
        file.truncate(0)


def block(bloclist): #stands for simple block
    os.chdir('C:\Windows\System32\drivers\etc')
    appendhost = []
    for website in bloclist:
        appendhost.append("127.0.0.1 "+website)
    
    with open('hosts', 'a+') as file:
        for i in appendhost:
            file.write("\n"+i)
            
'''Displays contents of host file'''
def display():
    os.chdir('C:\Windows\System32\drivers\etc')
    with open('hosts', 'r+') as file:
        print(file.read())
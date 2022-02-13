#make delete function that deletes takes the type of thing to be deleted(task,topic,etc.) and 
f = open("StoreTopic.json",'r+')
lines = f.readlines()
length = len(lines)
nameofTopic = 'miska'
for i in lines:
   if nameofTopic in i:
      print(i)
      nameofTopic = i
lines.remove(nameofTopic)
f.truncate(0)
for i in lines:
   f.write(i)
f.close()




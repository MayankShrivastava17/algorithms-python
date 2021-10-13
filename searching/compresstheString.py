print("Enter string:")
string = input()
current = string[0]
count = 0
for i in range(len(string)):
 if string[i] == current: 
   count += 1
 else:
   
   print("(" + str(count)+","+str(current)+")",end="")
   current = string[i]
   count = 1

print("("+str(count)+","+str(current)+")",end="")
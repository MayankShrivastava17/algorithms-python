upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
upper_new=[]
lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lower_new=[]
number=["0","1","2","3","4","5","6","7","8","9"]
number_new=[]
character=["$","#","@"]
character_new=[]
while True:
    password=list(input("Enter Password: "))
    if len(password)<6:
        print("Password is too short")
        continue
    elif len(password)>16:
        print("Password is too long")
        continue
    else:
        for i in password:
            if i in upper:
                upper_new.append(i)
            elif i in lower:
                lower_new.append(i)
            elif i in number:
                number_new.append(i)
            elif i in character:
                character_new.append(i)
    if len(upper_new)==0:
        print("Password Must Contain At Least 1 Uppercase Alphabet")
        continue
    elif len(lower_new)==0:
        print("Password Must Contain At Least 1 Lowercase Alphabet")
        continue
    elif len(character_new)==0:
        print("Password Must Contain At Least 1 Special Character")
        continue
    elif len(number_new)==0:
        print("Password Must Contain At Least 1 Number Between 0-9")
        continue
    else:
        print("Congratulations !  You Entered A Valid Password")
        break
    
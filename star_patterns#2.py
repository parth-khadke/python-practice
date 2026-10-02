'''
for i in range(1,6):
    if i==1:
        for j in range(0,5):
            if j==0:
                print("$ ", end="")
                print(4 * "* ")
            elif j==1:
                print("* ", end = "")
                print("$ ", end ="")
                print(3 * "* ")
            elif j==2:
                print(2 * "* ", end = "")
                print("$ ", end ="")
                print(2 * "* ")
            elif j==3:
                print(3 * "* ", end = "")
                print("$ ", end ="")
                print( "* ")
            elif j==4:
                print(4 * "* ", end = "")
                print("$ ", end ="")


                
'''
i=0
for k in range(0,5):
    if k==0 or k==4:
        print(k * "* ", end="")
        print("$ ", end="")
        print((4-k) * "* ")
    if i>=0 and i<3:  
        print("* "+ i*"  "+ "$ "+ (2-i)*"  "+ "*")
    i+=1

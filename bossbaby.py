#Time Complexity of BigO(n) and Memory Complexity of BigO(1)
#define the function name
def bossbaby_revenge(shots_record): 

    #Incase we have weird input
    if len(shots_record) <= 0: 
        raise ValueError("Error: Invalid Input")

    #First case: if the boss baby shot first they are immediately a Bad Boy
    if shots_record[0] == "R": 
        return "Bad Boy"
    s_count = 0 
  

    for i in range(len(shots_record)): 

        #Second case: if the boss baby did not return fire there are also a Bad Boy

        #Implementation: We can easily check whether "the boss baby has not returned fire" by counting S and deleting S when we find R 
        #If we find R but S = 0 we can ignore it since the example shows that you can return as much as you want "as long as you don't start first"
       
        if shots_record[i] == "S": 
            s_count += 1
        elif shots_record[i] == "R": 
            if s_count > 0:
                s_count -= 1
        else: 
            #Also just in case there's anything aside S and R in the string
            raise ValueError("Error: Invalid Input")

    return "Good boy" if s_count == 0 else "Bad boy"


print(bossbaby_revenge("SSRSRR"))

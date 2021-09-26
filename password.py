# taking input and storing it on password

password=input("\033[1;32;47m  Enter the password you want for your system \n")

# enter data and store it on data 
data=input("Enter your data")
print("system locked")
# taking chance and giving it a value of 0
chance=0

# using while loop and defining a condition if chance is less then or equal to 2 then start
while(chance<=2):

    # taking input from user and storing it in user
    user=input("Enter your password")

    # if user equal to password then pritn system unlocked and chance become 3 and while loop stops
    if(user==password):
        print('System unlocked')
        chance=3

        # asking if user want to see his data and storing it into ans
        ans=input("If you want to see your data (y/n)")
        a='y'
        b="n"

        # if ans equal to y start condition 1 if ans equal to n start condition 2 else start condition 3
        if(ans==a): #codition 1
            print("you data is \n",data)
        
        elif(ans==b):#codition 2
            print('enjoy your data is safe')    
        
        else:#codition 3
            print("can not understand your answer")    
    
    # else print try again and chance added by 1 and cary on
    else:
        print("Try again")
        chance=chance+1
        print("Chances left =",3-chance)

# when chance become 3 print system locked
print("Your system is locked. ")
    
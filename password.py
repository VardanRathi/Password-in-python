# taking input and storing it on password

password=input("\033[1;33;40m  Enter the password you want for your system \n")

# enter data and store it on data 
data=input(" Enter your data\n")
print("\033[1;31;40m system locked")
# taking chance and giving it a value of 0
chance=0

# using while loop and defining a condition if chance is less then or equal to 2 then start
while(chance<=2):

    # taking input from user and storing it in user
    user=input("\033[1;34;40m Enter your password")

    # if user equal to password then pritn system unlocked and chance become 3 and while loop stops
    if(user==password):
        print('\033[1;32;40m System unlocked')
        chance=3

        # asking if user want to see his data and storing it into ans
        ans=input(" If you want to see your data (y/n)")
        a='y'
        b="n"

        # if ans equal to y start condition 1 if ans equal to n start condition 2 else start condition 3
        if(ans==a): #codition 1
            print(" you data is \n"'\033[1;37;40m',data)
        
        elif(ans==b):#codition 2
            print('\033[1;32;40m enjoy your data is safe')    
        
        else:#codition 3
            print("\033[1;31;40m can not understand your answer")    
    
    # else print try again and chance added by 1 and cary on
    else:
        print("\033[1;31;40m Wrong Password \n \033[1;33;40m Try again")
        chance=chance+1
        # print("\033[1;35;40m Chances left =",3-chance)

# when chance become 3 print system locked
print("\033[1;31;40m Your system is locked. ")
    
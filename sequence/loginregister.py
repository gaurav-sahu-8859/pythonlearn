users=[
    {
        "name":"mohit",
        "email":"mohit@gmail.com",
        "password":"1234"
    },
    {
        "name":"gagan",
        "email":"rohit@gmail.com",
        "password":"1234"
    },
]

q=""
while(q!="0"):
    print("press 0 for exit")
    print("press 1 for login")
    print("press 2 for register")
    print("press 3 for delete")
    print("press 4 for update")
    print("press 5 for print details")
    q=input("enter mode:")
    if(q=="0"):
        break
    elif(q=="1"):
        email=input("enter email:")
        password=input("enter password:")
        userfound=""
        for user in users:
            if(email==user["email"] and password==user["password"]):
                userfound=user
                break
        if(userfound):
            print("login succesfull!\n welcome user:",userfound["name"])
        else:
            print("login failed!")
    elif(q=="2"):
        pass
        # user={
        #     name:
        #     email:
        #     passwod:
        # }
        # users.append(user)
        # note duplicate will be not register
    elif(q=="3"):
        # delete
        pass
    elif(q=="4"):
        # update
        pass
    elif(q=="5"):
        print(users)
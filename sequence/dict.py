# data={
#     "name":"gaurav",
#     "email":"g@gmail.com",
#     "password":"1234"
# }

# for i in data:
#     print(i,":",data[i])

# print("name:",data["name"])
# print("email:",data["email"])
# print("password:",data["password"])

# ----------------------------------------------------------------------------

# task
# chatbot-project

dataset={
    "hi":"helo",
    "hello":"hi",
    "how are you":"fine how can i help you",
    "whats my name":"dont know your name if you tell me then then next time i'll recognize"
}

q=None
name=""
while q!="exit":
    q=input("enter your query:")#hi

    if(q in dataset):

        if(q=="whats my name" and name==""):
            print("bot:",dataset[q])
            name=input("enter your name:")
        elif(name):
            print("your name is:",name)
        else:
            print("bot:",dataset[q])
        
        # print(dataset[q])
    else:
        print("no data found")
data={
    "name":"gaurav",
    "email":"g@gmail.com",
    "password":"1234"
}

for i in data:
    print(i,":",data[i])

# print("name:",data["name"])
# print("email:",data["email"])
# print("password:",data["password"])

# task
# chatbot-project

datset={
    "hi":"helo",
    "hello":"hi",
    "how are you":"fine how can i help you",
}

q=1
while(q!=0):
    q=input("enter your query")
    print(datset[q])
import instaloader,datetime
from time import sleep

L = instaloader.Instaloader()
date = datetime.datetime.now()


# Login or load session
username = "###YOUR USERNAME###"
password = "###YOUR PASSWORD###"
L.login(username, password)  # (login)

target_user = str(input("enter name of the user : ")) # target user


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, target_user)


### followings
followings_list = []
count = 0

print("Getting followings ...")


for following in profile.get_followees():
    followings_list.append(following.username)
    file = open(target_user+"_followings_"+date.strftime("%Y%m%d_%H_%M")+".txt", "a+")
    file.write(followings_list[count])
    file.write("\n")
    file.close()
    if (count % 300) == 0 and (count != 0) :
        print(count," stopping to evade checkpoint [followings]")
        sleep(1)
    count = count + 1

print("done.")

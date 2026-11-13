anime = []

isContinue = True

while isContinue == True:
    ans = input("Do you know anime ??? (yes/no) ").lower()

    if ans == "yes":
        title = input("What is the title of Anime : ")
        anime.append(title)
        ans = input("Do you wish to continue ??? (yes/no) ").lower()
        if ans == "yes":
            print("Continue")
            continue
        else:
            print(anime)
            break



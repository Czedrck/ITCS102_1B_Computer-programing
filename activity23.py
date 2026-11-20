#LEVEL 4:
#------------------------------------------------------------

Ippo = ["Strength", "National"]
Takamura = ["Overall", "International"]
Miyata = ["Speed", "National"]

Hinata = ["Middle Blocker", "#10"]
Kageyama = ["Setter", "#9"]
Tsukishima = ["Middle Blocker", "#11"]

Sakuragi = ["Rebound"]
Rukawa = ["Scorer"]
Akagi = ["Leader"]

#LEVEL 3:
#------------------------------------------------------------

Hajime_Ippo = {"ippo":Ippo, "takamura":Takamura, "miyata":Miyata}
Haikyu = {"hinata":Hinata, "kageyama":Kageyama, "tsukishima":Tsukishima}
Slamdunk = {"sakuragi":Sakuragi, "rukawa":Rukawa, "akagi":Akagi}

#LEVEL 2:
#------------------------------------------------------------

sports = {"hajie_ippo":Hajime_Ippo, "haikyu":Haikyu, "slamdunk":Slamdunk}

#LEVEL 1:
#------------------------------------------------------------

anime = {"Old anime": sports}

print("=== 1. Going down one level at a time ===")
print(anime["Old anime"]["Hajime_Ippo"]["Ippo"][1])

print()
print("=== 2. Loop level 1: categories ===")
for category in anime:
    print(category)
    
print()
print("=== 3. Loop levels 1-2: categories and titles ===")
for category, titles in anime.items():
    print(category)
    for title in titles:
        print(" -", title)

print()
print("=== 4. Loop all levels ===")
for category, titles in anime.items():
    print(category)
    for title in titles




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

Rudeus = ["Water magic"]
Orsted = [""]
Ruijerd = [""]

Naofumi = [""]
Raphtalia = [""]
Filo = [""]

#LEVEL 3:
#------------------------------------------------------------

Hajime_Ippo = {"ippo":Ippo, "takamura":Takamura, "miyata":Miyata}
Haikyu = {"hinata":Hinata, "kageyama":Kageyama, "tsukishima":Tsukishima}
Slamdunk = {"sakuragi":Sakuragi, "rukawa":Rukawa, "akagi":Akagi}
Mushoku = {"rudeus":Rudeus, "orsted":Orsted, "ruijerd":Ruijerd}
Shield_Hero = {"naofumi":Naofumi, "raphtalia":Raphtalia, "filo":Filo}

#LEVEL 2:
#------------------------------------------------------------

sports = {"hajime_ippo":Hajime_Ippo, "haikyu":Haikyu, "slamdunk":Slamdunk}
isekai = {"mushoku":Mushoku, "shield_hero":Shield_Hero}

#LEVEL 1:
#------------------------------------------------------------

anime = {"Old anime":sports, "New anime":isekai}

print("=== 1. Going down one level at a time ===")
print(anime["Old anime"]["hajime_Ippo"]["ippo"][1])

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
    for title, characters in titles.items():
        print(" " + title)
        for name, info in characters.items():
            print("   " + name)
            print("   Description:", info[0])
            print("   Power:", info[1])
            
print()
print("=== 5. Count every character ===")
count = 10
for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1
print("Total characters:", count)

print()
print("=== 6. Search for a character ===")
search = "Rem"
found = False
for category, titles in anime.items():
    for titles, characters in titles.items():
        if search in characters:
            print(search, "is from", title, "(" + category + ")")
            print("Power!", characters[search][1])
            found = True
print(search, "not found..")
        
















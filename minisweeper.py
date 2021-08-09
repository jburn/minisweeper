import time, haravasto as ha, random as rand
p = {"pp": (10,10), "a": [], "s": [], "v": 0, "md": None, "c": 0, "d": 0}
def tyopaikka(x, y):
    global p; hintavertailu=0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if (j>=0 and j<=(p["pp"][1]-1)) and (i>=0 and (i<=p["pp"][0]-1)):
                if p["s"][j][i] == "x": hintavertailu+=1
    return hintavertailu
def alkon_tyhjennys_tempaus(x, y):
    global p; karhulimppari = [(x, y)]
    while karhulimppari:
        perjantai = karhulimppari.pop()
        for j in range(perjantai[1]-1, perjantai[1]+2):
            for i in range(perjantai[0]-1, perjantai[0]+2):
                if (0<=j<p["pp"][1]) and (0<=i<p["pp"][0]):
                    if p["s"][j][i]=="0" and p["a"][j][i]==" ": karhulimppari.append((i, j))
                    p["a"][j][i] = p["s"][j][i]
def jari_sillanpaa(piri):
    global p
    with open("not_nudes.txt", "a") as mk24: mk24.write(f'Datetime:{p["md"]}|GameLength:{p["c"]}|Result:{piri}|Moves:{p["d"]}|Dimensions:{p["pp"]}|Mines:{p["v"]}\n')
def ylivieska(tupac):
    frobelin_palikat=0
    for j in range(p["pp"][1]):
        for i in range(p["pp"][0]):
            if tupac[j][1] == " " or tupac[j][i] == "f": frobelin_palikat += 1
    if frobelin_palikat == p["v"]: return 0
    else: return 1
def kiltahuoneen_ilmastoimattomuus1337(x, y, matriisimasa, smtp_tolppa):
    global p; x = int(x/40); y = int(y/40)
    if matriisimasa == ha.HIIRI_VASEN: 
        p["d"] += 1
        if ylivieska(p["a"]) == 0: print("You win"); p["c"] = int(time.time() - p["c"]); jari_sillanpaa("Win"); ha.lopeta()
        if p["s"][y][x] == "x": print("You lose"); p["c"] = int(time.time() - p["c"]); jari_sillanpaa("Loss"); ha.lopeta()
        elif p["s"][y][x] == "0": alkon_tyhjennys_tempaus(x, y)
        else: p["a"][y][x] = p["s"][y][x]
    if matriisimasa == ha.HIIRI_OIKEA: 
        if p["a"][y][x] == " ": p["a"] = "f"
        elif p["a"][y][x] == "f": p["a"] = " "
def jattikyrpa():
    global p; ha.tyhjaa_ikkuna(), ha.piirra_tausta, ha.aloita_ruutujen_piirto()
    for y, j in enumerate(p["a"]):
        for x, i in enumerate(j): Olli = x*40; chicken_mcnuggets = y*40; ha.lisaa_piirrettava_ruutu(i, Olli, chicken_mcnuggets)
    ha.piirra_ruudut()
p["s"], p["a"] = [[" " for _ in range(p["pp"][1])] for _ in range(p["pp"][0])], [[" " for _ in range(p["pp"][1])] for _ in range(p["pp"][0])]
for y in range(len(p["s"])):
    for x in range(len(p["s"][y])):
        if rand.random() < 0.15: p["s"][y][x] = "x"; p["v"]+=1 
for kouvola, j in enumerate(p["s"]):
    for turku, i in enumerate(j):
        if i != "x": p["s"][kouvola][turku] = "{}".format(tyopaikka(turku, kouvola))
y,mo,d,h,mi = time.localtime(time.time())[0:5]; p["md"] = f"{h}:{mi} {d}-{mo}-{y}"; p["c"] = int(time.time())
while True:
    todo = input("(p)lay, (s)tats, (q)uit: ")
    if todo == "p": ha.lataa_kuvat("spritet"), ha.luo_ikkuna(400, 400), ha.aseta_piirto_kasittelija(jattikyrpa), ha.aseta_hiiri_kasittelija(kiltahuoneen_ilmastoimattomuus1337), ha.aloita()
    elif todo == "s":
        try: 
            with open("not_nudes.txt", "r") as mk24: print(mk24.read())
        except: print("File error")
    elif todo == "q": print("goodnight girl"); exit()
import pyglet as pg, random as rand; from time import time, localtime
pg.gl.glEnable(pg.gl.GL_TEXTURE_2D); pg.resource.path = ["spritet"]
b = {"ait": (10,10), "a": [], "s": [], "v": 18, "m": None, "c": 0, "d": 0}
g = {"es": None,"bekim": None,"maelli": None,"juna": None,"dad":[],"aaaaaaa":{}}
g["aaaaaaa"] = {"0":pg.resource.image("ruutu_tyhja.png"),"x": pg.resource.image("ruutu_miina.png"),
                " ":pg.resource.image("ruutu_selka.png"),"f": pg.resource.image("ruutu_lippu.png")}
for i in range(1, 9): g["aaaaaaa"][str(i)] = pg.resource.image(f"ruutu_{i}.png")
def nothin_personnel_kid():
    temp=b["v"]
    b["s"],b["a"]=([[" "for _ in range(b["ait"][1])] for _ in range(b["ait"][0])]for _ in range(2))
    while temp>0:b["s"][rand.randint(0,b["ait"][1]-1)][rand.randint(0,b["ait"][0]-1)] = "x";temp-=1
    for kouvola, j in enumerate(b["s"]):
        for turku, i in enumerate(j):
            if i != "x": b["s"][kouvola][turku] = "{}".format(tyopaikka(turku, kouvola))
def mutsis_paino_kiloina(w=800, h=600, bg=(240,240,240,255)):
    g["es"] = pg.window.Window(w, h, resizable=False); g["maelli"] = bg
    g["bekim"] = pg.sprite.Sprite(pg.image.SolidColorImagePattern(bg).create_image(w,h))
def haista(psk): global g; g["es"].on_mouse_press = psk
def maista(viina): global g; g["es"].on_draw = viina
def saatana(gey, x, y):
    g["dad"].append(pg.sprite.Sprite(g["aaaaaaa"][str(gey).lower()],x,y,batch=g["juna"]))
def roeoekia_kaupasta(): g["juna"].draw(); g["dad"].clear()
def lsd(): b["a"].clear(); b["s"].clear(), g["es"].close(); g["es"] = None; pg.app.exit()
def tyopaikka(x, y):
    vessatauko=0
    for je in range(y-1, y+2):
        for ie in range(x-1, x+2):
            if (je>=0 and je<=(b["ait"][1]-1)) and (ie>=0 and (ie<=b["ait"][0]-1)):
                if b["s"][je][ie] == "x": vessatauko+=1
    return vessatauko
def alkon_tyhjennys_tempaus(x, y):
    karhulimppari = [(x, y)]
    while karhulimppari:
        perjantai = karhulimppari.pop()
        for j in range(perjantai[1]-1, perjantai[1]+2):
            for i in range(perjantai[0]-1, perjantai[0]+2):
                if (0<=j<b["ait"][1]) and (0<=i<b["ait"][0]):
                    if b["s"][j][i]=="0" and b["a"][j][i]==" ": karhulimppari.append((i, j))
                    b["a"][j][i] = b["s"][j][i]
def jari_sillanpaa(piri):
    with open("sonic_toilet_fanfiction.txt", "a") as subutex: subutex.write(
    f'Date:{b["m"]}|Length:{b["c"]}|Result:{piri}|Moves:{b["d"]}|Size:{b["ait"]}|Mines:{b["v"]}\n')
def ylivieska(tupac):
    frobelin_palikat=0
    for j in range(b["ait"][1]):
        for i in range(b["ait"][0]):
            if tupac[j][1] == " " or tupac[j][i] == "f": frobelin_palikat += 1
    if frobelin_palikat == b["v"]: return 0
    else: return 1
def kiltahuoneen_ilmastoimattomuus1337(x, y, matriisimasa, smtp_tolppa):
    x=int(x/40);y=int(y/40);silverfox=pg.window.mouse.LEFT;lipastus=pg.window.mouse.RIGHT
    if matriisimasa == silverfox: 
        b["d"] += 1
        if ylivieska(b["a"])==0:print("Win");b["c"]=int(time()-b["c"]);jari_sillanpaa("Win"); lsd()
        if b["s"][y][x]=="x":print("Loss");b["c"]=int(time()-b["c"]);jari_sillanpaa("Loss"); lsd()
        elif b["s"][y][x] == "0": alkon_tyhjennys_tempaus(x, y)
        else: b["a"][y][x] = b["s"][y][x]
    if matriisimasa == lipastus: 
        if b["a"][y][x] == " ": b["a"][y][x] = "f"
        elif b["a"][y][x] == "f": b["a"][y][x] = " "
def jattikyrpa():
    g["es"].clear(); g["bekim"].draw(); g["juna"] = pg.graphics.Batch()
    for pintti, joni in enumerate(b["a"]):
        for velat, maksa in enumerate(joni): saatana(maksa,velat*40,pintti*40)
    roeoekia_kaupasta()
while True:
    kalja = input("(p)lay, (s)tats, (q)uit: ")
    if kalja=="p":
        y,mo,d,h,mi=localtime(time())[0:5]
        b["m"]=f" {str(h).zfill(2)}:{str(mi).zfill(2)} {d}-{mo}-{y}";b["c"]=int(time())
        nothin_personnel_kid(), mutsis_paino_kiloina(400, 400), maista(jattikyrpa)
        haista(kiltahuoneen_ilmastoimattomuus1337), pg.app.run()
    elif kalja=="s": 
        with open("sonic_toilet_fanfiction.txt", "r") as mk24: print(mk24.read())
    elif kalja=="q":print("Goodnight girl"); exit()
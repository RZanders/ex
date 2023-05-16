with open("tekst.txt") as f:
    text = f.read()
    nevajadzigi = ".,?!;:()"
    for suimbolnins in nevajadzigi:
        text = text.replace(suimbolnins,"")    
    text = text.split(" ")

    vardu_skaits = {}
    for vards in text:
        if len(vards) > 3:
            vardu_skaits[vards] = text.count(vards)

    print(vardu_skaits)



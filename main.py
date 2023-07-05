if __name__ == "__main__":

    # temp = int(input("Vvedit temperaturu na dvori: "))

    # if 10 < temp < 20:           # promischok
    #     print("TEST")
    #
    #     print("Proholodno")
    # elif temp > 20:
    #     print("Hariache")
    # else:
    #     print("Cholodno")

    # if -10 < temp < 10:
    #     print("Proholodno")
    #
    # elif temp > 10:
    #     print("Gariache")
    #
    # else:
    #     print("Holodno")

    # temp = int(input("Vvedit temperaturu na dvori: "))
    # riven_kisn = int(input("Vvedit riven kisn na dvori: "))
    #
    # if 25 < temp < 35 and riven_kisn > 18:
    #     print("Vikno vidkryte")
    # else:
    #     print("Vikno zakryte")

    # age = int(input("Vvedit vik klienta: "))
    # dohid = int(input("Vvedit richnyi dohid klienta: "))
    # employed_answ = input("Vvedit vidomosti prazi klienta (y/n): ")
    # blacklisted_answ = (input("Vvedit spysok klientiv (y/n: ")
    #
    # if employed_answ.lower() == 'y':
    #     employed = True
    # else:
    #     employed = False
    #
    # if blacklisted_answ.lower() == 'y' :
    #     blacklisted = False
    # else:
    #     blacklisted = True
    #
    # if 18 < age <= 65 and dohid >= 25000 and employed == True and blacklisted == False:
    #     print("DOZVOLENO")
    # else:
    #     print("VIDHYLENO")


    age = int(input("Vvedit vik klienta: "))
    dohid = int(input("Vvedit richnyi dohid klienta: "))

    if 18 < age < 65 and dohid < 20000 or 26 < age < 40 and 20000 < dohid < 40000:
        print("STUDENTSKYI KREDYT")
    elif 41 < age < 60 and dohid > 40000:
        print("POTOCHNYI KREDYT")
    else:
        print("OSOBYSTYI KREDYT")

    if dohid*age/4:
        

        print("STUDENTSKYI KREDYT"  "POTOCHNYI KREDYT"  "OSOBYSTYI KREDYT")



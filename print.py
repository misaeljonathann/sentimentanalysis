lexicon = {}

# Ambil leksikon yang udah ada
try :
    with open('lexicon.txt', 'r') as file:
        for line in file:
            kata, nilai = line.split(" ")
            lexicon[kata] = int(nilai)
except FileNotFoundError :
    print("File ngga ada")

# Tambahin kata pada leksikon (unique)
kata = "start"
while kata != "stop":

    line = input("Masukin Kata Lagi : ")
    kata, nilai = line.split(" ")

    if kata in lexicon:
        lexicon[str(kata)] += int(nilai)
    else:
        lexicon[str(kata)] = int(nilai)

with open('lexicon.txt', 'w') as outfile:
    for key in lexicon :
        outfile.write(key + " " + str(lexicon[key]) + "\n")

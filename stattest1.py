import matplotlib.pyplot as plt

chal_test_1 = {'Thresh': 177, 'Lulu': 1382, 'Corki': 359, 'Sona': 513, 'DragonGold': 286, 'Zoe': 770, 'Bard': 1001, 'Soraka': 690, 'Heimerdinger': 630, 'Nami': 508, 'Tristana': 458, 'Sylas': 972, 'DragonPurple': 482, 'TrainerDragon': 772, 'Vladimir': 108, 'Ryze': 171, 'Illaoi': 265, 'Gnar': 395, 'Anivia': 389, 'Neeko': 600, 'DragonGreen': 350, 'Karma': 169, 'Ashe': 307, 'Yasuo': 906, 'Ornn': 641, 'Sejuani': 464, 'Lillia': 203, 'Nunu': 443, 'Volibear': 192, 'Hecarim': 578, 'AoShin': 273, 'Elise': 64, 'Talon': 330, 'Pyke': 280, 'DragonBlue': 395, 'Shen': 295, 'LeeSin': 116, 'Swain': 177, 'Shyvana': 267, 'Braum': 131, 'Jinx': 83, 'AurelionSol': 130, 'Leona': 135, 'TahmKench': 30, 'Qiyana': 122, 'Twitch': 297, 'Xayah': 211, 'Yone': 210, 'Taric': 66, 'Olaf': 96, 'Diana': 88, 'Aatrox': 66, 'Kayn': 140, 'Sett': 130, 'Skarner': 20, 'Ezreal': 18, 'Nidalee': 18, 'Varus': 137, 'Senna': 21}
x = []
y = []
for champ in chal_test_1:
    x.append(champ)
    y.append(chal_test_1[champ])
    
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
plt.show()
    

ytot = 0
for a in y:
    ytot+=a

print(ytot)
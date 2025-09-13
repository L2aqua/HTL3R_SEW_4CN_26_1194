#Frage 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#Wenn Schleifenrumpf nicht eingerückt wird eine Exception geworfen

#Frage 2
i = 1
while i < 6:
    print(i)
    i += 1
#Wenn i nicht erhöht wird entschteht eine infite loop

#frage 3
preis= 59.99
if preis <= 20:
     preis = preis - 0.4 * preis # 40% Rabatt
elif preis > 60:
     preis = preis - 0.1 * preis # 10% Rabatt
else:
     preis = preis - 0.25 * preis # 25% Rabatt
print(preis)

#Frage 4
var_x = 5
var_i = 0
while var_i < 7:
    var_x = var_x + 1
    var_i = var_i + 2
print(var_x)
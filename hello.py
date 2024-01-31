
Nom=int(input("Saisit un nombre : "))
print("tu as saisit le numero "+str(Nom))

for e in range(1,11):
    mul=Nom*e
    print(mul)

B=input("Si tu veux t'arreter, tape 'stop' ou si tu veux continuer tape ce que tu veux: ")
if B =='stop':
    print("Fin")
else:
    for e in range(1,11):
        mul=Nom*e
        print(mul)

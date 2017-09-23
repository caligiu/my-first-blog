print('Ciao, Django Girls!')
if 3>2:
	    print('Funziona!')
else:
		print('Non funziona :(')
nome= 'Giulia'
if nome=='Giulia':
	print('Ciao Giulia!')
elif nome =='Barbara':
	print('Ciao Barabara!')
else:
	print('Ciao anonimo!')
volume = 57
if volume<21:
	print("un po' basso!")
elif 21 <= volume < 34:
	print("Adatto per una serata in relax!")
elif 21 <= volume > 44:
	print("Perfetto per ascoltare ogni dettaglio!")
elif 21 <= volume >57:
	print("I vicini potrebbero lamentarsi!")
else:
	print("Oddio troppo alto!")

def ciao():
	print('Ciao!')
	print('Come stai?')
ciao()

def ciao(nome):
    if nome =='Ola':
    	print("Ciao Ola!")
    elif nome =='Giulia':
    	print("Ciao Giulia!")
    elif nome == 'Barbara':
    	print("Ciao Barbara!")
    else:
    	print("Ciao Anonimo!")
ciao(nome)
ciao('Barbara')
ciao('Luca')
def ciao(nome):
    print('Ciao '+ nome + '!')
ciao('Marta')

ragazze=['Maria','Marianna','MariaLisa','Maria Maddalena', 'Marina']
for nome in ragazze:
    ciao(nome)
    print('Prossima ragazza')

for i in range(1,9):
	print(i)

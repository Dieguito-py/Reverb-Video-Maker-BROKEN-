print('Artista: ')
art = input()
print('Música: ')
msc = input()
musica = art + ' '+ msc + (' (Official Audio)')
ly =  msc.lower()
characters = " -"
for x in range(len(characters)):
    ly = ly.replace(characters[x],"")


print('  ')
print('Música:', musica)
print('Obtendo link...')
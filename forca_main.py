import forca_command

lst = []
life = 6
cont = 0
command = forca_command.Hangman()
wr = command.hide_word(0)
wo = command.hide_word(1)
for i in wo:
    lst.append(i)

while life != 0 and '_' in wo:
    command.status(cont, wo)
    letter = str(input('Digite uma letra: ')).lower()
    print()

    if not(letter in wr):
        forca_command.wrong_w.append(letter)
        cont += 1
        life -= 1
    else:
        wo = ''
        forca_command.right_w.append(letter)

        for i in command.right_word(letter, wr):
            lst.pop(i)
            lst.insert(i, letter)

        for i in lst:
            wo += i

command.status(cont, wo)
forca_command.victory_defeat(life)


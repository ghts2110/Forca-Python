import random
import forca_v1
wrong_w = []
right_w = []


class Hangman:
    def status(self, cont, wo):
        print(forca_v1.board[cont] + '\n')
        print('palavra: ' + wo)
        self.print_game_status()

    def right_word(self, letter, word):
        lst = []
        for pos, char in enumerate(word):
            if char == letter:
                lst.append(pos)

        return lst

    def hide_word(self, n):
        if n == 0:
            return wr
        elif n == 1:
            return len(wr) * '_'

    def print_game_status(self):
        print('\nletras erradas:')
        for i in wrong_w:
            print(i)

        print('\nletras certas:')
        for i in right_w:
            print(i)


def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip()


wr = rand_word()


def victory_defeat(life):
    if life > 0:
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + wr)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

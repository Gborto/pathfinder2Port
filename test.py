from players import Player


def main():
    p1 = Player('Jary','dwarf', 'fighter')
    p2 = Player('Abu', charClass='wizard', race='human')

    print(p1, p2)


if __name__ == '__main__':
    main()

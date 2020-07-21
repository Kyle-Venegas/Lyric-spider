import os
def menu():
    while True:
        os.system('clear')
        print('1. Album')
        print('2. Song')
        print('0. Exit')
        choice = input('Choice?: ')
        os.system('clear')
        if choice == '1':
            import album
            album.lyric()
            break
        elif choice == '2':
            import song
            song.lyric()
            break
        elif choice == '0':
            break
        else:
            continue
            
if __name__ == '__main__':
    menu()

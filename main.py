import sys, os
sys.path.append(os.path.dirname(__file__))  # ensures current file's folder is on sys.path
import game


is_running = True

def main():
    global is_running
    while is_running:
        print("---------------------")
        print("     GUESS GAME      ")
        print("---------------------")
        print("SELECT DIFFICULT LEVEL")
        print("1. EASY   (5 chance)")
        print("2. MEDIUM (3 chance)")
        print("3. HARD   (1 chance)")
        print("0. EXIT")
        try:
            choice = int(input("CHOICE LEVEL 1/2/3 (0 to exit): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if choice == 1:
            game.easy()
        elif choice == 2:
            game.medium()
        elif choice == 3:
            game.hard()
        elif choice == 0:
            print("Goodbye!")
            is_running = False
        else:
            print("PLEASE! ENTER A VALID LEVEL.")
            







# Panggil fungsi game dari game.py

# Terima hasil permainan (menang / kalah / score)

# Tanyakan apakah user ingin bermain lagi

# Jika tidak, tampilkan pesan penutup dan keluar program

if __name__ == "__main__":
    main()

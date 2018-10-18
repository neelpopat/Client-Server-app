# work is done by ravjot
def menu():
        try:
                print("\nThe menu")
                print("................")
                print("(1)Get domain name and IP")
                print("(2)Get Statistics")
                print("(3)Sort Data")
                print("(4)Add Organisation")
                print("(5)Remove Organisation")
                print("(6)Quit")
                print("..................")
                option = int(input("Enter your choice(1,2,3,4,5,6): "))
                if option in range(1,7):
                        return option

                else:
                        print("Invalid input")
                        print("\nTry again")
                        menu()

        except ValueError:
                print("It must be a number")
                print("\nTry again")
                menu()

                           
        
        

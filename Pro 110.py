import random

response = "n"

while not response == "y":
    response = input("Roll dice?")

while not response == "q":
    response = input("Press r to roll. Press q to quit.")
    if response == "r":
        num1 = random.randint(1,7)
        if num1 == 1:
            print("""
                    [   ]
                    [ 0 ]
                    [   ]
            """)

        if num1 == 2:
            print("""
                    [  0]
                    [   ]
                    [0  ]
            """)

        if num1 == 3:
            print("""
                    [  0]
                    [ 0 ]
                    [0  ]
            """)

        if num1 == 4:
            print("""
                    [0 0]
                    [   ]
                    [0 0]
            """)

        if num1 == 5:
            print("""
                    [0 0]
                    [ 0 ]
                    [0 0]
            """)

        if num1 == 6:
            print("""
                    [0 0]
                    [0 0]
                    [0 0]
            """)
    

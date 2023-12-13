command = ""
while True: #command != "quit":
    command = input("> ").lower() #Added .lower() to avoid duplicates - DRY principle
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")

#o/p
#> start
#Car started...
#> stop
#Car stopped.
#> asd
#> 2
#> quit

#> help
        #start - to start the car
        #stop - to stop the car
        #quit - to quit

#> a
#Sorry, I don't understand that!
#> 1
#Sorry, I don't understand that!

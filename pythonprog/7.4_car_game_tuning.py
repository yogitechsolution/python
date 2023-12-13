command = ""
started = False # Added condition if car already started 
#stopped = False # Added condition if car already stopped 
while True: 
    command = input("> ").lower() 
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started: #Using 1 variable NOT 2
            print("Car is already stopped")
        else:
            started = False #Using 1 variable NOT 2
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
#> stop
#Car is already stopped
#> start
#Car started...
#> start
#Car is already started
#> stop
#Car stopped.
#> stop
#Car is already stopped
#> quit

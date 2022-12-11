import random
# This Function is just for number readablity 
def grams(ln):
    ln=str(ln)
    gram=""
    if ln[-1] == str(1):
        gram="st"
    elif ln[-1]==str(2):
        gram="nd"
    elif ln[-1]==str(3):
        gram="rd"
    elif ln[-1] >=str(4) or ln==0:
        gram="th"
    return ln+gram

# Elevator class
class Elevator:
    
    def __init__(self, starting_floor,destination_floor):
        self.current_floor = starting_floor
        self.destination_floor=destination_floor
        # self.door_open = False

    # Method for moving the elevator up
    def move_up(self):
        self.current_floor = self.destination_floor
        # self.door_open = False
        print("Elevator moving up to floor {}".format(grams(self.current_floor)))

    # Method for moving the elevator down
    def move_down(self):
        self.current_floor -= 1
        # self.door_open = False
        print("Elevator moving down to floor {}".format(grams(self.current_floor)))

    # Method for stopping the elevator
    def stop(self):
        print("Elevator stopping at floor {}".format(grams(self.current_floor)))

    # Method for opening the elevator doors
    def open_doors(self):
        # self.door_open = True
        print("Elevator doors opening at floor {}".format(grams(self.current_floor)))

    # Method for closing the elevator doors
    def close_doors(self):
        # self.door_open = False
        print("Elevator doors closing at floor {}".format(grams(self.current_floor)))

class floor_caller:
    def __init__(self,direction):
        self.direction=direction
    # method to call the elevator
    def moving(self):
        if self.direction == "UP":
            print("Elevator moving up to your floor")
        elif self.direction == "Down":
            print("Elevator moving down to your floor")

class oprating:
    
    def __init__(self):
        self.fn=random.randint(0,18)
        self.ln=random.randint(0,21)
        self.up_down=random.randint(1, 2)

    # Method to run the Elevator 
    def running(self):             
        print(f"You are on {grams(self.fn)} Floor")
        print(f"Lift is on {grams(self.ln)} Floor")
        if self.fn == self.ln :
            lift=floor_caller("UP")
        elif self.fn > self.ln:
            lift=floor_caller("UP")
            lift.moving()
        elif self.fn < self.ln :
            lift = floor_caller("Down")
            lift.moving()
        print(f"Elevator doors opening at floor {grams(self.fn)}")
        print(f"Elevator doors closing at floor {grams(self.fn)}")
        print("Welcome to Wild Elevator!")  
        print("Enter 000 to Stop the Elevator")
        Destination_fn=input("Enter Destination Floor... :")
        elevator = Elevator(self.fn,Destination_fn)
        if Destination_fn == "000":
            elevator.stop()
        elif int(Destination_fn) == self.fn:
            try :
                elevator.open_doors()
            except:
                print(f"You are on the {grams(Destination_fn)} floor only.")
        elif int(Destination_fn) > self.fn :
            elevator.move_up()
            elevator.open_doors()
            elevator.close_doors()

        elif int(Destination_fn) < self.fn :
            elevator.move_down()
            elevator.open_doors()
            elevator.close_doors()

        
if __name__ == "__main__":
    run_elevator=oprating()
    run_elevator.running()
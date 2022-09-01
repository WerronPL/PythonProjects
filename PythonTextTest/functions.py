
import os
import Variables

class StartClass(object):

    def __init__(self, ):
        self.var_delta = Variables.delta
        self.var_speed = Variables.speed
        self.var_started = Variables.started
        self.var_trunk_open = Variables.trunk_open
        self.var_name = Variables.name
        

    def start(self):
        if Variables.vars[2] == False:
            Variables.vars[2] = True
            return Variables.vars[2]
        else:
            print("ur gae")

            

    def start_car(self:Variables.vars[0:3]):
        StartClass.start(self)
        if  Variables.vars[2] == True:
            speeds = Variables.vars[1] 
            acceleration = Variables.vars[0]
            speeds = speeds + acceleration
            print("Vrooooom!")
        elif Variables.vars[2] == False:
            print("You need to start me first")
        else:
            print("OMG fkning ERROR! Solve IT NOW!")

class VehicleClass(object):

    def __init__(self):
        self.trunk_open = False

    def stop(self):
        self.speed = 0
        return "stopped vehicle"

    def open_trunk(self):
        self.trunk_open = True
        return self.trunk_open

    def close_trunk(self):
        self.trunk_open = False
        return self.trunk_open

class AmogusClass:

    import sys
    name = "Wiktor"

    def who_is_sus(self, name = os.getlogin()):
        import sys
        if len(sys.argv) == 2:
            self.name = name
            return self.name
        else:
            self.name = 'Wiktor'
        print(f'You are sus {name}')



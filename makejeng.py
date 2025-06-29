import novapi
from mbuild.encoder_motor import encoder_motor_class
from mbuild import gamepad
from mbuild import power_expand_board
from mbuild import power_manage_module
from mbuild.smartservo import smartservo_class
import time

class Ikazuchibot:
    
    def logo():
        print("""
        
         ______     __  __     ______     __  __     __        __     ______     ______  
        /\  ___\   /\ \/\ \   /\  ___\   /\ \_\ \   /\ \      /\ \   /\  __ \   /\__  _\ 
        \ \___  \  \ \ \_\ \  \ \___  \  \ \  __ \  \ \ \     \ \ \  \ \ \/\ \  \/_/\ \/ 
         \/\_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\     \ \_\  \ \_____\    \ \_\ 
          \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/      \/_/   \/_____/     \/_/ 
                                                                        [ROYAL PALADIN]
        """)
        print(";-; This code made by SUSHI_IOT || DEV by Ikazuchi || ROYAL PALADIN! Team [WIP]")
    
    def __init__(self):
        self.upper_left_motor_wheel = encoder_motor_class("M1", "INDEX1")
        self.upper_right_motor_wheel = encoder_motor_class("M2", "INDEX1")
        self.lower_left_motor_wheel = encoder_motor_class("M3", "INDEX1")
        self.lower_right_motor_wheel = encoder_motor_class("M4", "INDEX1")
        self.upper_convey = "DC1"
        self.midway_convey = "DC2"
        self.lower_convey = "DC3"
        self.folklift = "DC4"
        self.gripper_left = "DC5"
        self.gripper_right = "DC6"
        #self.intaker_left = "DC7"
        self.intaker_right = "DC8"
        self.servo_level_adjustment = smartservo_class("M5", "INDEX1")
        self.brushless_motor = "BL1"
        self.set_toggle_brushless = 0
        self.set_toggle_dc = 0
        self.set_toggle_servo = 0
        self.set_intake_toggle = 0
        self.set_upper_convey_only = 0

    def set_motor_speed(self, ul, ur, ll, lr):
        self.upper_left_motor_wheel.set_power(ul)
        self.upper_right_motor_wheel.set_power(ur)
        self.lower_left_motor_wheel.set_power(ll)
        self.lower_right_motor_wheel.set_power(lr)

    def move_forward(self):
        self.set_motor_speed(70, -70, 70, -70)

    def move_backward(self):
        self.set_motor_speed(-70, 70, -70, 70)

    def move_right_sideway(self):
        self.set_motor_speed(70, 70, -70, -70)

    def move_left_sideway(self):
        self.set_motor_speed(-70, -70, 70, 70)

    def spin_right(self):
        self.set_motor_speed(-70, -70, -70, -70)

    def spin_left(self):
        self.set_motor_speed(70, 70, 70, 70)

    def stop_motor(self):
        self.set_motor_speed(0, 0, 0, 0)

    def brushless_speed(self, bl_speed):
        power_expand_board.set_power(self.brushless_motor, bl_speed)

    def shooter(self):
        if self.set_toggle_brushless == 0:
            self.brushless_speed(80)
            self.set_toggle_brushless = 1
        else:
            self.brushless_speed(0)
            self.set_toggle_brushless = 0

    def convey_system(self, reverse=False, toggle=False, upper_only=False):
        dcspeed = -80 if reverse else 80

        if toggle and not upper_only:
            if self.set_toggle_dc == 0:
                power_expand_board.set_power(self.upper_convey, dcspeed)
                power_expand_board.set_power(self.midway_convey, dcspeed)
                power_expand_board.set_power(self.lower_convey, dcspeed)
                self.set_toggle_dc = 1
            else:
                power_expand_board.set_power(self.upper_convey, 0)
                power_expand_board.set_power(self.midway_convey,0)
                power_expand_board.set_power(self.lower_convey, 0)
                self.set_toggle_dc = 0
        elif upper_only:
            if self.set_upper_convey_only == 0:
                power_expand_board.set_power(self.upper_convey, dcspeed)
                power_expand_board.set_power(self.midway_convey, dcspeed)
                power_expand_board.set_power(self.lower_convey, 0)
                self.set_upper_convey_only = 1
            else:
                power_expand_board.set_power(self.upper_convey, 0)
                power_expand_board.set_power(self.midway_convey, 0)
                power_expand_board.set_power(self.lower_convey, 0)
                self.set_upper_convey_only = 0
        else:
            power_expand_board.set_power(self.upper_convey, dcspeed)
            power_expand_board.set_power(self.midway_convey, dcspeed)
            power_expand_board.set_power(self.lower_convey, dcspeed)

    def servo_control(self):
        if self.set_toggle_servo == 0:
            self.servo_level_adjustment.move_to(50, 70)
            self.set_toggle_servo = 1
        elif self.set_toggle_servo == 1:
            self.servo_level_adjustment.move_to(70, 70)
            self.set_toggle_servo = 2
        elif self.set_toggle_servo == 2:
            self.servo_level_adjustment.move_to(90, 70)
            self.set_toggle_servo = 3
        elif self.set_toggle_servo == 3:
            self.servo_level_adjustment.move_to(110, 70)
            self.set_toggle_servo = 4
        elif self.set_toggle_servo == 4:
            self.servo_level_adjustment.move_to(120, 70)
            self.set_toggle_servo = 5
            
        else:
            self.servo_level_adjustment.move_to(130, 70)
            self.set_toggle_servo = 0

    def forklift_system(self):
        ly = gamepad.get_joystick("Ly")
        if ly <= -20:
            power_expand_board.set_power(self.folklift, ly)
        elif ly >= 20:
            power_expand_board.set_power(self.folklift, ly)
        else:
            power_expand_board.set_power(self.folklift, 0)

    def gripper_system_open(self):
        power_expand_board.set_power(self.gripper_left, 80)
        power_expand_board.set_power(self.gripper_right, -80)

    def gripper_system_close(self):
        power_expand_board.set_power(self.gripper_left, -80)
        power_expand_board.set_power(self.gripper_right, 80)
        
    def gripper_system_disable(self):
        power_expand_board.set_power(self.gripper_left, 0)
        power_expand_board.set_power(self.gripper_right, 0)    

    def intake_system(self):
        if self.set_intake_toggle == 0:
            #power_expand_board.set_power(self.intaker_left, 100)
            power_expand_board.set_power(self.intaker_right, 100)
            self.set_intake_toggle = 1
        else:
            #power_expand_board.set_power(self.intaker_left, 0)
            power_expand_board.set_power(self.intaker_right, 0)
            self.set_intake_toggle = 0
           
    
    def control_system(self):
        
        ly = gamepad.get_joystick("Ly")
        rx = gamepad.get_joystick("Rx")
        if rx > 20:
            self.spin_right()
            time.sleep(0.1)
        elif rx < -20:
            self.spin_left()
            time.sleep(0.1)
        if gamepad.is_key_pressed("Up"):
            self.move_forward()
        elif gamepad.is_key_pressed("Down"):
            self.move_backward()
        elif gamepad.is_key_pressed("Left"):
            self.move_left_sideway()
        elif gamepad.is_key_pressed("Right"):
            self.move_right_sideway()
        
        else:
            self.stop_motor()
    
        if gamepad.is_key_pressed("+"):
            self.shooter()
            time.sleep(0.2)
            
        elif gamepad.is_key_pressed("≡"):
            self.intake_system()
            time.sleep(0.2)    

        elif gamepad.is_key_pressed("R1"):
            self.convey_system(reverse=True, toggle=True, upper_only=False)
            time.sleep(0.2)

        elif gamepad.is_key_pressed("R2"):
            self.convey_system(reverse=False, toggle=True, upper_only=False)
            time.sleep(0.2)
        
        elif gamepad.is_key_pressed("L1"):
            self.convey_system(reverse=True, toggle=True, upper_only=True)
            time.sleep(0.2)
        
        elif gamepad.is_key_pressed("L2"):
            self.convey_system(reverse=False, toggle=True, upper_only=True)
            time.sleep(0.2)
            
        elif gamepad.is_key_pressed("N2"):
            self.servo_control()
            time.sleep(0.2)

        elif gamepad.is_key_pressed("N1") and not gamepad.is_key_pressed("N4"):
            self.gripper_system_close()
        
        elif gamepad.is_key_pressed("N4") and not gamepad.is_key_pressed("N1"):
            self.gripper_system_open()
        
        elif not gamepad.is_key_pressed("N4") and not gamepad.is_key_pressed("N1"):
            self.gripper_system_disable()
        self.forklift_system()
            
logo()

robot = Ikazuchibot()
while True:
    robot.control_system()
    
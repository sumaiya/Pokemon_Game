
# Sumaiya Hashmi & Cooper Galvin
# CS 5 final project
# vPython game!

# Type play() to begin!!!

import random
from random import *
from visual import *
import math
from math import *
import sys
import webbrowser
from webbrowser import *


def menu():
    """the menu"""

    print "(1) Bulbasaur vs. Pikachu"
    print "(2) Diglett vs.Charmander"
    print "(3) Jigglypuff vs Psyduck"
    print "(4) Quit"

def play():
    """the user-interaction loop"""
    print "Welcome, Pokemon trainers!"
    url = 'http://www.youtube.com/watch?v=B_ecwRtVmSY'
    webbrowser.open_new_tab(url)
    
    while True:
        menu()
        uc = str(input("Select your battle:"))
        if uc == '1':
            
            print "\n \n Defeat your opponent by getting their health points down to zero \n or knocking them off the stage. \
                   \n Ultimate moves may only be used twice per round.\n"
            print "Controls:"
            print "Player 1, Bulbasaur: \n Turn right: d \n Turn left: a \n Forward: w \
                    \n Back: s \n Jump: j \n Strafe right: q \
                    \n Strafe left: e \n Tackle: 1 \n Vinewhip: 2 \n SolarBeam (Ultimate): 3 \n"
            print "Player 2, Pikachu: \n Turn right: right arrow \n Turn left: left arrow \n Forward: up arrow \
                    \n Back: down arrow \n Jump: l \n Strafe right: ; \n Strafe left: ' \
                    \n ThunderShock: , \n Slam: . \n Thunder (Ultimate): / \n"
            c = str(input("Type 9 to begin game:"))
            if c == '9':
                return battle1()
                
            else:
                print "Try again"
                    
                
            


            #open file
        elif uc == '2':
            
            print "\n \n Defeat your opponent by getting their health points down to zero \n or knocking them off the stage. \
                    \n Ultimate moves may only be used twice per round.\n"
            print "Controls:"
            print "Player 1, Diglett: \n Turn right: d \n Turn left: a \n Forward: w \
                    \n Back: s \n Jump: j \n Strafe right: q \
                    \n Strafe left: e \n Rock throw: 1 \n Tackle: 2 \n Dig: 3 \n"
            print "Player 2, Charmander: \n Turn right: right arrow \n Turn left: left arrow \n Forward: up arrow \
                    \n Back: down arrow \n Jump: l \n Strafe right: ; \n Strafe left: ' \
                    \n Ember: ; \n Bodyslam: . \n Fire spin (Ultimate): / \n"
            c = str(input("Type 9 to begin game:"))
            if c == '9':
                return battle2()
            
            else:
                print "Try again"            
        elif uc == '3':
            print "\n \n Defeat your opponent by getting their health points down to zero \n or knocking them off the stage. \
                   \n Ultimate moves may only be used twice per round.\n"
            print "Controls:"
            print "Player 1, Jigglyuff: \n Turn right: d \n Turn left: a \n Forward: w \
                    \n Back: s \n Jump: j \n Strafe right: q \
                    \n Strafe left: e \n Hyper voice: 1 \n Round: 2 \n Sing: 3 \n"
            print "Player 2, Psyduck: \n Turn right: right arrow \n Turn left: left arrow \n Forward: up arrow \
                    \n Back: down arrow \n Jump: l \n Strafe right: ; \n Strafe left: ' \
                    \n Psychic: ; \n Headbutt: . \n Water pulse (Ultimate): / \n"
            c = str(input("Type 9 to begin game:"))
            if c == '9':
                return battle3()
                
            else:
                print "Try again"
        elif uc == '4':
            break
        else:
            print "That's not on the menu!"
    print
    print "Come back soon!"
    




###BATTLE 3!
from visual import *
import math


class stage1:

    def __init__(self, pos, heading=vector(0,0,1)):
        """constructs the stage on screen"""
        self.parts = [] #creates the list of all the components of the stage
        self.pos = vector(pos)
        self.heading = norm(heading)
        self.flats = box(pos = self.pos, length=40.0, height=0.25, width=40.0, color=color.green, material = materials.marble)
        self.parts += [self.flats]
     
        """self.parts += [extN] + [extE] + [extS] + [extW]

        rect = shapes.rectangle(pos=(self.pos), width = 42.0, height = 42.0)
        inner = shapes.rectangle(pos=(self.pos), width = 39.5, height = 39.5)
        pth = [(0,-1,0), (0,5,0)]
        ext = extrusion(pos=pth, shape=rect-inner, color=color.green)"""

      
        

        
    def __rpr__(self):
        """creates the 3D representation of the stage for python"""
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s


class Jigglypuff:
    """ a collection of VPython parts that
        will move together == a robot!
    """

    # make x, y, z axes with labels
    
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our robot class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        
        self.body = self.body = sphere( pos=self.pos,
                          radius =.9, color=(1,.75,.9))
        
        self.parts += [self.body] # add it to our "parts" list
        
        # two eyes
        left_eye = sphere(pos=self.pos+vector(.25,.17,.8),
                          radius=0.2, color=color.cyan)
        self.parts += [left_eye]
        right_eye = sphere(pos=self.pos+vector(-.25,.17,.8),
                           radius = 0.2, color=color.cyan)
        self.parts += [right_eye]

        # eye white
        left_weye = ring(pos=self.pos+vector(.25,.17,.85),axis=(.1,.1,.6),radius=0.2,thickness=0.03, color=color.white)
        self.parts += [left_weye]
        right_weye = ring(pos=self.pos+vector(-.25,.17,.85),axis=(-.1,0.1,.6),radius=0.2,thickness=0.03, color=color.white)
        self.parts += [right_weye]


        #pupil
        left_pupil = sphere(pos=self.pos+vector(.27,.19,.95),
                          radius=0.065, color=color.white)
        self.parts += [left_pupil]
        right_pupil = sphere(pos=self.pos+vector(-.23,.19,.95),
                           radius = 0.065, color=color.white)
        self.parts += [right_pupil]

        

        #ears
        left_ear = cone(pos=self.pos+vector(0.35,0.58,0.4), axis = (.25,.5,0.2), radius = 0.3, color = (1,.75,.9))
        self.parts += [left_ear]
        
        right_ear = cone(pos=self.pos + vector(-0.35,.58,.4), axis = (-.25,.5,0.2), radius = 0.3, color = (1,.75,.9))
        self.parts += [right_ear]

        #innerear
        left_inner = cone(pos=self.pos+vector(0.35,0.58,0.5), axis = (.25,.5,0.1), radius = 0.2, color = color.black)
        self.parts += [left_inner]
        
        right_inner = cone(pos=self.pos + vector(-0.35,.58,.5), axis = (-.25,.5,0.1), radius = 0.2, color=color.black)
        self.parts += [right_inner]

        #arms

        self.arml = ellipsoid( pos = self.pos+vector(.47,-.26,.6),axis=(-5,5,5),
                                length =.2,
                                height =.2, width =.57,
                                color = (1,.75,.9))
        self.parts += [self.arml]

        self.armr = ellipsoid( pos = self.pos+vector(-.47,-.26,.6), axis=(5,5,5),
                                 length =.2,
                                height =.2, width =.57,
                                color = (1,.75,.9))
        self.parts += [self.armr]

        

        #mouth
        mouth = ellipsoid( pos = self.pos+vector(0,-.18,.9), axis= (0,0,1), length =.2, height =.2, width =.3, color = color.red)
        self.parts += [mouth]

        #feet

        self.footl = ellipsoid( pos = self.pos+vector(.3,-.8,.5),axis=(-5,5,5),
                                length =.2,
                                height =.2, width =.5,
                                color = (1,.75,.9))
        self.parts += [self.footl]

        self.footr = ellipsoid( pos = self.pos+vector(-.3,-.8,.5), axis=(5,5,5),
                                 length =.2,
                                height =.2, width =.5,
                                color = (1,.75,.9))
        self.parts += [self.footr]
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)

class Psyduck:
    """ a collection of VPython parts that
        will move together == a Pokemon!
    """

    # make x, y, z axes with labels
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our Psyduck class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        self.body = ellipsoid( pos=self.pos, length = 1,
                          height =1.5, width = 1)
        self.body.color = (1,.84,0)
        self.parts += [self.body] # add it to our "parts" list

        #pokemon head length - x width -z, height-y
        self.head = ellipsoid( pos=self.pos + vector (0,.72,0),
                                length = .9,
                                height =1.2, width = 1)
        self.head.color = (1,.84,0)
        self.parts += [self.head]

        #jaw
        self.jaw = ellipsoid( pos=self.pos + vector (0,.60,.5),axis = (0,-1,1),
                                length = 1,
                                height =.3, width = .8, color = (1,.86,0.62))
        self.parts += [self.jaw] 


        #making Psyduck's booty
        self.butt = ellipsoid( pos=self.pos + vector (0,-.3,0),
                                length = 1.35,
                                height =1.15, width = 1)
        self.butt.color = (1,.84,0)
        self.parts += [self.butt] 

        
        # two  eyes
        left_eye = ellipsoid(pos=self.pos+vector(.18,.9,.45),
                          length=0.2, height=0.2, width= 0.2, color=color.white)
        self.parts += [left_eye]
        right_eye = ellipsoid(pos=self.pos+vector(-.18,.9,.45),
                           length = 0.2, height = 0.2, width=0.2, color=color.white)
        self.parts += [right_eye]

        # two  pupils
        left_eye = sphere(pos=self.pos+vector(.18,.9,.55),
                          radius = 0.02, color=color.black)
        self.parts += [left_eye]
        right_eye = sphere(pos=self.pos+vector(-.18,.9,.55),
                           radius = 0.02, color=color.black)
        self.parts += [right_eye]
               


        # arms

        self.arml = ellipsoid( pos = self.pos+vector(-.45,.2,0),
                                length =.8, axis = (-.5, .4, 0),
                                height =.4, width =.4,
                                color = (1,.84,0))
        self.parts += [self.arml]

        self.armr = ellipsoid( pos = self.pos+vector(.45,.2,0),
                                 length =.8,axis = (.5, .4, 0),
                                height =.4, width =.4,
                                color = (1,.84,0))
        self.parts += [self.armr]
        
        #forearms

        self.farml = ellipsoid( pos = self.pos+vector(-.6,.6,0),
                                length =.8, axis = (.2, .5, 0),
                                height =.3, width =.3,
                                color = (1,.84,0))
        self.parts += [self.farml]

        self.farmr = ellipsoid( pos = self.pos+vector(.6,.6,0),
                                 length =.8,axis = (-.2, .5, 0),
                                height =.3, width =.3,
                                color = (1,.84,0))
        self.parts += [self.farmr]


        
        #tail
        self.tail = ellipsoid(pos=self.pos+vector(0,-.27,-.4), axis=(0,.8,-1), length =1,height =.4, width =.5,color=(1,.84,0))
        #self.tail = arrow(pos=self.pos+vector(0,-.2,-.5), axis=(0,1,-1),
                   # shaftwidth=.1, color=color.orange, material = materials.emissive)
        self.parts += [self.tail]
        



        
        #feet

        self.footl = ellipsoid( pos = self.pos+vector(-.3,-.8,.22),
                                length =.5,
                                height =.2, width =1,
                                color = (1,.86,0.62))
        self.parts += [self.footl]

        self.footr = ellipsoid( pos = self.pos+vector(.3,-.8,.22),
                                 length =.5,
                                height =.2, width =1,
                                color = (1,.86,0.62))
        self.parts += [self.footr]
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
   


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)


def battle3():
    """Play the game!"""
    # set up the visual conditions - the window is called "scene"
    scene2 = display(width=1400, height=850,center=(0,9,40), background=(0,1,1))
    # set up the visual conditions - the window is called "scene"
    scene = scene2
    scene.autoscale = False  # should the scene fill the window?
    scene.background = color.black  # the background "space" color

    # create other, non-robot objects
    #create walls
    wallS = shapes.line(start = (-20,20), end=(20,20))
    wallE = shapes.line(start = (20,20), end=(20,-20))
    wallN = shapes.line(start = (-20,-20), end=(20,-20))
    wallW = shapes.line(start = (-20,20), end=(-20,-20))
    wpath = [(0,-1,0), (0,1.25,0)]
    extN = extrusion(pos = wpath, shape = wallN, color = color.red, material = materials.chrome)
    extE = extrusion(pos = wpath, shape = wallE, color = color.green, material= materials.chrome)
    extS = extrusion(pos = wpath, shape = wallS, color = color.blue, material=materials.chrome)
    extW = extrusion(pos = wpath, shape = wallW, color = color.orange, material =materials.chrome)

   #pokeball at center of stage
    outerw = shapes.circle(radius=3)
    cut = shapes.rectangle(pos=(0,1.5),width=6,height=3)
    outerr= outerw-cut

    
    innerb = shapes.circle(radius=0.7,thickness=0.2)

    pthw = [(0,-.75,0),(0,-.74,0)]
    pthb = [(0,-.75,0),(0,-.72,0)]

    outerwe = extrusion(pos=pthw, shape = outerw, color=color.white)
    innerbe = extrusion(pos=pthb,shape=innerb, color=color.black)
    outerre = extrusion(pos=pthw, shape=outerr, color=color.red)      
    


  #lighting
    lampR = local_light(pos=(21,13,-30), color=color.white)
    lampsR = box(pos=(21,13,-30),axis=(-3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standR = box(pos=(21,0,-30), axis=(-3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)

    lampL = local_light(pos=(-21,13,-30), color=color.white)
    lampsL = box(pos=(-21,13,-30),axis=(3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standL = box(pos=(-21,0,-30), axis=(3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)


   

    #establishing original HP
    bulbaHP = 50
    pikaHP = 50
    bulbaHPtext = text(pos = (-9,-3,20),
                       text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                       depth=-0.3, color=color.green)
    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)



    
    # the controlled robot
    player1 = Jigglypuff(pos=(-10,0,0))
    # another robot, this one not controlled
    player2 = Psyduck(pos=(10,0,0))

    thestage = stage1(pos=(0,-1,0))
    HYDROPUMP_PP = 2
    
    # the main loop - handle user events
    while True:

        # It's easier to adjust constants if they
        # have names and are all in one place!
        TURN_AMOUNT = 15 # degrees
        MOVE_AMOUNT = .3 # units
        FLY_AMOUNT = 0.3 #unit of flight
        STRAFE_AMOUNT = 0.3 #strafe units
        KNOCKBACK_AMOUNT = 0.005
        BOUNCE_AMOUNT = 10
        rate(1000000)  # at most 30 loops per second
        
        if scene.mouse.clicked != 0: # mouse click?
            print "mouse click!"
            event = scene.mouse.getclick() # remove event
            scene.mouse.events = 0 # reset mouse events
            
        if scene.kb.keys: # is there a keyevent?
            s = scene.kb.getkey() # get keypress
            keys_seen = [s]
            if scene.kb.keys:
                s2 = scene.kb.getkey()
                keys_seen += [s2]
                print "keys_seen is", keys_seen
            
            # controls for player1
            

            if s == "a":
                player1.turn(TURN_AMOUNT)
            if s == "d":
                player1.turn(-TURN_AMOUNT)
            if s == "s":
                player1.forward(-MOVE_AMOUNT)
            if s == "w":
                player1.forward(MOVE_AMOUNT)
            if s == "j":
                player1.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player1.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.pos += player1.velocity*dt        
                    if player1.pos.y >= 5:
                        player1.velocity.y = -player1.velocity.y
                    elif player1.pos.y <= 0:
                        player1.velocity.y = 0
                        n = 1
                    else:
                        player1.pos += player1.velocity*dt
                player1.pos.y = 0
            

            
            if s == "q":
                player1.strafe(STRAFE_AMOUNT)
            if s == "e":
                player1.strafe(-STRAFE_AMOUNT)
            # controls for player2
            if s == "l": #THIS IS AN L
                player2.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player2.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt        
                    if player2.pos.y >= 5:
                        player2.velocity.y = -player2.velocity.y
                    elif player2.pos.y <= 0:
                        player2.velocity.y = 0
                        n = 1
                    else:
                        player2.pos += player2.velocity*dt
                player2.pos.y = 0
            if s == "left":
                player2.turn(TURN_AMOUNT)
            if s == "right":
                player2.turn(-TURN_AMOUNT)
            if s == "down":
                player2.forward(-MOVE_AMOUNT)
            if s == "up":
                player2.forward(MOVE_AMOUNT)
            
            if s == ";":
                player2.strafe(STRAFE_AMOUNT)
            if s == "'":
                player2.strafe(-STRAFE_AMOUNT)
        #
        # check the state of the "game"
        #
        
            #TIME FOR THE ATTACKS!!!
        
            #Psyduck's Psychic
            
        
            if s == ",":
                print "Psyduck uses Psychic!"
                thunder= ring(pos = player2.pos + player2.heading, axis=player2.heading, radius=8, thickness=0.8, color = (1,0,1))
                
                die_dist = mag (player1.pos - thunder.pos)
                deltat = 0.02
                t = 0
                thunder.velocity = player2.heading * 5
                while t<5:
                    rate(1000)
                    thunder.pos = thunder.pos + thunder.velocity*deltat
                    t = t + deltat
                    die_dist = mag (player1.pos - thunder.pos)
                    if die_dist < 2:
                        player1.body.color = color.red
                        die_dist = mag (player1.pos - thunder.pos)
                        
                    if player1.body.color == color.red:
                        bulbaHP -= 10
                        print "Jigglypuff got blasted by Psyduck's Psychic! He is losing health points!!"
                        print "Jigglypuff's current HP", bulbaHP
                        bulbaHPtext.visible = False
                        bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                        die_dist = mag (player1.pos - thunder.pos)
                        thunder.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * thunder.velocity
                            player1.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player1.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player1.body.color = (1,.75,.9)
                        
                thunder.visible = False
                
            player1.body.color = (1,.75,.9)

            # Psyduck's Hydropump
            if s == "/":
                if HYDROPUMP_PP>0:
                    HYDROPUMP_PP-=1
                    print "Psyduck uses Hydropump!"
                    thunder= ring(pos = player2.pos + player2.heading, axis=player2.heading, radius=8, thickness=2, color = color.blue)
                    thunder.trail = curve(color=thunder.color, radius = 4)
                    die_dist = mag (player1.pos - thunder.pos)
                    deltat = 0.02
                    t = 0
                    thunder.velocity = player2.heading * 5
                    while t<5:
                        rate(1000)
                        thunder.pos = thunder.pos + thunder.velocity*deltat
                        t = t + deltat
                        thunder.trail.append(pos=thunder.pos)
                        die_dist = mag (player1.pos - thunder.pos)
                        if die_dist < 2:
                            player1.body.color = color.red
                            die_dist = mag (player1.pos - thunder.pos)
                            
                        if player1.body.color == color.red:
                            bulbaHP -= 10
                            print "Jigglypuff got hit by Psyduck's Psychic. He is losing health points!!"
                            print "Jigglypuff's current HP", bulbaHP
                            bulbaHPtext.visible = False
                            bulbaHPtext = text(pos = (-9,-3,20),
                               text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                               depth=-0.3, color=color.green)
                            die_dist = mag (player1.pos - thunder.pos)
                            thunder.visible = False
                            thunder.trail.visible = False
                            deltat2 = 0.02
                            t2 = 0
                            while t2<3:
                                rate(1000)
                                motion_vector = KNOCKBACK_AMOUNT * thunder.velocity
                                player1.pos += motion_vector
                                t2 = t2 + deltat2
                                for part in player1.parts:
                                    part.pos += motion_vector
                            break
                            
                        else:
                            player1.body.color = (1,.75,.9)
                            
                    thunder.visible = False
                    thunder.trail.visible = False
                    
                player1.body.color = (1,.75,.9)
                
                
            # Jigglypuff's Hyper voice
            
            if s == "1":
                print "Jigglypuff uses Hyper voice!"
                vinewhip= ring(pos = player1.pos + player1.heading, axis=player1.heading, radius=2, thickness=0.8)
                pdie_dist = mag (player2.pos - vinewhip.pos)
                deltat = 0.02
                t = 0
                vinewhip.velocity = player1.heading * 5
                vinewhip.trail = curve(color=vinewhip.color, radius = 1)
                while t<3:
                    rate(1000)
                    vinewhip.pos = vinewhip.pos + vinewhip.velocity*deltat
                    t = t + deltat
                    vinewhip.trail.append(pos=vinewhip.pos)
                    pdie_dist = mag (player2.pos - vinewhip.pos)
                    if pdie_dist < 2:
                        player2.body.color = color.red
                        pdie_dist = mag (player2.pos - vinewhip.pos)
                        
                    if player2.body.color == color.red:
                        pikaHP -= 6.5
                        print "Psyduck got deafened by Jigglypuff's Hypervoice. He is losing health points!!"
                        print "Psyduck's current HP", pikaHP
                        pikaHPtext.visible = False
                        pikaHPtext = text(pos = (0,-3,20),
                           text='P2 HP:'+'-'*int((pikaHP/5.0)),
                           depth=-0.3, color=color.green)
                        vinewhip.visible = False
                        vinewhip.trail.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * vinewhip.velocity
                            player2.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player2.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player2.body.color = (1,.84,0)
                vinewhip.visible = False
                vinewhip.trail.visible = False
                player2.body.color = (1,.84,0)

            #Jigglypuff's Ultimate: Sing
            if s == "3":
                print "Jigglypuff uses Sing!"
                sing = ring(pos=player1.pos, axis=(0,1,0), radius = 2, thickness = 0.2, color=color.magenta)
                pdie_dist = mag (player2.pos - sing.pos)
                while sing.radius <20:
                    rate(100)
                    sing.radius += 0.25
                sing.visible = False
                print "That wasn't very effective!"
                player2.body.color = (1,.84,0)


                
            #Jigglypuff's Round
            if s == "2":
                print "Jigglypuff uses Round!"
                MOVE_AMOUNT = 3
                player1.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player1.pos - player2.pos)
                if robot_dist < 2:
                    player2.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player1.heading
                        player2.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player2.parts:
                            part.pos += motion_vector
                    pikaHP -= 10
                    print "Psyduck got smacked by Jigglypuff's round. He is losing health points!!"
                    print "Psyduck's current HP", pikaHP
                    pikaHPtext.visible = False
                    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)
                    player2.body.color = (1,.84,0)
                    
                else: 
                    player2.body.color = (1,.84,0)
            #Psyduck's Headbutt
            if s == ".":
                print "Psyduck uses Headbutt!"
                MOVE_AMOUNT = 3
                player2.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player2.pos - player1.pos)
                if robot_dist < 2:
                    player1.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player2.heading
                        player1.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player1.parts:
                            part.pos += motion_vector
                    bulbaHP -= 10
                    print "Jigglypuff got smacked by Psyduck's headbutt. He is losing health points!!"
                    print "Jigglyfuff's current HP", bulbaHP
                    bulbaHPtext.visible = False
                    bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                    player1.body.color = (1,.75,.9)
                    
                else: 
                    player1.body.color = (1,.75,.9)

            #hit wall, wall breaks.
            """wallNdist = mag(extN.pos - player1.pos)
            if wallNdist.any() < 0.5:
                extN.visible = False
                for part in player1.parts:
                    part.pos = (0,0,0)
              """               

            
            # case for fainting.
            if bulbaHP<=0:
               print "Jigglypuff faints. Psyduck has won the battle!"
               player1.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                   rate(1000)
                   t += dt
                   for part in player1.parts:
                       part.pos += player1.velocity*dt
               for part in player1.parts:
                   part.visible = False
                
                
               scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if pikaHP<=0:
               print "Psyduck faints. Jigglypuff has won the battle!"
               player2.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                    rate(1000)
                    t += dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt
               for part in player2.parts:
                    part.visible = False
                    
               scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            #hit walls once, wall disappears, reset. again, fall off stage and die:

            
            if extN.visible == True and player1.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
                
                
                #for part in player1.parts:
                 #   part.visible= False
                #player1 = Jigglypuff(pos=(0,0,0))
                
            
            if extN.visible == False and player1.pos.z < -21:
                    print "Jigglypuff falls off the stage! Psyduck has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player1.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player1.pos.x > 21:
                    print "Jigglypuff falls off the stage! Psyduck has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extS.visible == True and player1.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player1.pos.z > 21:
                    print "Jigglypuff falls off the stage! Psyduck has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extW.visible == True and player1.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player1.pos.x < - 21 :
                    print "Jigglypuff falls off the stage! Psyduck has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extN.visible == True and player2.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extN.visible == False and player2.pos.z < - 21:
                    print "Psyduck falls off the stage! Jigglypuff has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player2.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player2.pos.x > 21:
                    print "Psyduck falls off the stage! Jigglypuff has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extS.visible == True and player2.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player2.pos.z > 21:
                    print "Psyduck falls off the stage! Jigglypuff has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extW.visible == True and player2.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player2.pos.x < -21:
                    p =  "Psyduck falls off the stage! Jigglypuff has won the battle!"
                    print p
                    """tx = text(pos = (0,-3,20),
                           text=p,
                           depth=-0.3, color=color.green)"""
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')


### BATTLE 2!
from visual import *
import math
import random

class stage1:

    def __init__(self, pos, heading=vector(0,0,1)):
        """constructs the stage on screen"""
        self.parts = [] #creates the list of all the components of the stage
        self.pos = vector(pos)
        self.heading = norm(heading)
        self.flats = box(pos = self.pos, length=40.0, height=0.25, width=40.0, color=color.green, material = materials.marble)
        self.parts += [self.flats]
     
        """self.parts += [extN] + [extE] + [extS] + [extW]

        rect = shapes.rectangle(pos=(self.pos), width = 42.0, height = 42.0)
        inner = shapes.rectangle(pos=(self.pos), width = 39.5, height = 39.5)
        pth = [(0,-1,0), (0,5,0)]
        ext = extrusion(pos=pth, shape=rect-inner, color=color.green)"""

      
        

        
    def __rpr__(self):
        """creates the 3D representation of the stage for python"""
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s


class Diglett:
    """ a collection of VPython parts that
        will move together == a robot!
    """

    # make x, y, z axes with labels
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our robot class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        
        self.body = self.body = ellipsoid( pos=self.pos, length = 1,
                          height =1.5, width = 1)
        self.body.color = (0.36,0.21,0)
        
        self.parts += [self.body] # add it to our "parts" list
        
        # two (?) eyes
        left_eye = ellipsoid(pos=self.pos+vector(.2,.4,.4),
                          length = .1, height = .3, width = .1, color=color.black)
        self.parts += [left_eye]
        right_eye = ellipsoid(pos=self.pos+vector(-.2,.4,.4),
                           length = .1, height = .3, width = .1, color=color.black)
        self.parts += [right_eye]

        # creating the nose
        nose = ellipsoid( pos = self.pos+vector(0,.1,.45), axis= (0,0,1), length =.2, height =.2, width =.3, color = color.red)
        self.parts += [nose]
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)

class Charmander:
    """ a collection of VPython parts that
        will move together == a Pokemon!
    """

    # make x, y, z axes with labels
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our Charmander class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        self.body = ellipsoid( pos=self.pos, length = 1,
                          height =1.5, width = 1)
        self.body.color = (1,.4,0)
        self.parts += [self.body] # add it to our "parts" list

        #pokemon head length - x width -z, height-y
        self.head = ellipsoid( pos=self.pos + vector (0,.72,0),
                                length = .9,
                                height =1.2, width = 1)
        self.head.color = (1,.4,0)
        self.parts += [self.head]

        #jaw
        self.jaw = ellipsoid( pos=self.pos + vector (0,.65,.5),
                                length = .55,
                                height =.5, width = .7, color = (1,.4,0))
        self.parts += [self.jaw] 


        #making Charmander's booty
        self.butt = ellipsoid( pos=self.pos + vector (0,-.3,0),
                                length = 1.,
                                height =1.15, width = 1)
        self.butt.color = (1,.4,0)
        self.parts += [self.butt] 

        
        # two (?) eyes
        left_eye = ellipsoid(pos=self.pos+vector(.18,.9,.45),
                          length=0.1, height=0.2, width= 0.15, color=color.black)
        self.parts += [left_eye]
        right_eye = ellipsoid(pos=self.pos+vector(-.18,.9,.45),
                           length = 0.1, height = 0.2, width=0.15, color=color.black)
        self.parts += [right_eye]

        #smile
        #smile = paths.arc(pos=self.pos+radius=2,angle1=-pi,angle2=0)
        #self.parts += [smile]
               


        # arms

        self.arml = ellipsoid( pos = self.pos+vector(-.45,.2,.25),
                                length =.8, 
                                height =.4, width =.4,
                                color = (1,.4,0))
        self.parts += [self.arml]

        self.armr = ellipsoid( pos = self.pos+vector(.45,.2,.25),
                                 length =.8,
                                height =.4, width =.4,
                                color = (1,.4,0))
        self.parts += [self.armr]




        
        #tail
        self.tail = cylinder(pos=self.pos+vector(0,-.27,-.4), axis=(0,.8,-1), radius=.15, color=(1,.4,0))
        #self.tail = arrow(pos=self.pos+vector(0,-.2,-.5), axis=(0,1,-1),
                   # shaftwidth=.1, color=color.orange, material = materials.emissive)
        self.parts += [self.tail]
        #fire
        self.fire1 = cone(pos=self.pos+vector(-.2,1,-1.5), axis=(.2,-.5,.2), radius=.1,color=color.red, material=materials.chrome)
        self.parts += [self.fire1]
        
        self.fire2 = cone(pos=self.pos+vector(.2,1,-1.5), axis=(-.2,-.5,.2), radius=.1,color=color.red,material=materials.chrome)
        self.parts += [self.fire2]

        self.fire3 = cone(pos=self.pos+vector(0,1.1,-1.5), axis=(0,-.5,.2), radius=.1,color=color.yellow,material=materials.shiny)
        self.parts += [self.fire3]



        #mouth
        mouth = ellipsoid( pos = self.pos+vector(0,.58,.8), axis= (0,0,1), length =.2, height =.2, width =.3, color = color.red)
        self.parts += [mouth]

        #feet

        self.footl = ellipsoid( pos = self.pos+vector(-.3,-.8,.22),
                                length =.2,
                                height =.2, width =.4,
                                color = (1,.4,0))
        self.parts += [self.footl]

        self.footr = ellipsoid( pos = self.pos+vector(.3,-.8,.22),
                                 length =.2,
                                height =.2, width =.4,
                                color = (1,.4,0))
        self.parts += [self.footr]

        
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
   


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)


def battle2():
    """Play the game!"""
    # set up the visual conditions - the window is called "scene"
    scene2 = display(width=1400, height=850,center=(0,9,40), background=(0,1,1))
    # set up the visual conditions - the window is called "scene"
    scene = scene2
    scene.autoscale = False  # should the scene fill the window?
    scene.background = color.black  # the background "space" color

    # create other, non-robot objects
    #create walls
    wallS = shapes.line(start = (-20,20), end=(20,20))
    wallE = shapes.line(start = (20,20), end=(20,-20))
    wallN = shapes.line(start = (-20,-20), end=(20,-20))
    wallW = shapes.line(start = (-20,20), end=(-20,-20))
    wpath = [(0,-1,0), (0,1.25,0)]
    extN = extrusion(pos = wpath, shape = wallN, color = color.red, material = materials.chrome)
    extE = extrusion(pos = wpath, shape = wallE, color = color.green, material= materials.chrome)
    extS = extrusion(pos = wpath, shape = wallS, color = color.blue, material=materials.chrome)
    extW = extrusion(pos = wpath, shape = wallW, color = color.orange, material =materials.chrome)

   #pokeball at center of stage
    outerw = shapes.circle(radius=3)
    cut = shapes.rectangle(pos=(0,1.5),width=6,height=3)
    outerr= outerw-cut

    
    innerb = shapes.circle(radius=0.7,thickness=0.2)

    pthw = [(0,-.75,0),(0,-.74,0)]
    pthb = [(0,-.75,0),(0,-.72,0)]

    outerwe = extrusion(pos=pthw, shape = outerw, color=color.white)
    innerbe = extrusion(pos=pthb,shape=innerb, color=color.black)
    outerre = extrusion(pos=pthw, shape=outerr, color=color.red)      
    


  #lighting
    lampR = local_light(pos=(21,13,-30), color=color.white)
    lampsR = box(pos=(21,13,-30),axis=(-3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standR = box(pos=(21,0,-30), axis=(-3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)

    lampL = local_light(pos=(-21,13,-30), color=color.white)
    lampsL = box(pos=(-21,13,-30),axis=(3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standL = box(pos=(-21,0,-30), axis=(3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)




    #establishing original HP
    bulbaHP = 50
    pikaHP = 50
    bulbaHPtext = text(pos = (-9,-3,20),
                       text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                       depth=-0.3, color=color.green)
    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)


    FIRESPIN_PP = 2
    
    # the controlled robot
    player1 = Diglett(pos=(-10,-.5,0))
    # another robot, this one not controlled
    player2 = Charmander(pos=(10,0,0))

    thestage = stage1(pos=(0,-1,0))

    
    # the main loop - handle user events
    while True:

        # It's easier to adjust constants if they
        # have names and are all in one place!
        TURN_AMOUNT = 15 # degrees
        MOVE_AMOUNT = .3 # units
        FLY_AMOUNT = 0.3 #unit of flight
        STRAFE_AMOUNT = 0.3 #strafe units
        KNOCKBACK_AMOUNT = 0.005
        BOUNCE_AMOUNT = 10
        rate(1000000)  # at most 30 loops per second
        
        if scene.mouse.clicked != 0: # mouse click?
            print "mouse click!"
            event = scene.mouse.getclick() # remove event
            scene.mouse.events = 0 # reset mouse events
            
        if scene.kb.keys: # is there a keyevent?
            s = scene.kb.getkey() # get keypress
            keys_seen = [s]
            if scene.kb.keys:
                s2 = scene.kb.getkey()
                keys_seen += [s2]
                print "keys_seen is", keys_seen
            
            # controls for player1
            

            if s == "a":
                player1.turn(TURN_AMOUNT)
            if s == "d":
                player1.turn(-TURN_AMOUNT)
            if s == "s":
                player1.forward(-MOVE_AMOUNT)
            if s == "w":
                player1.forward(MOVE_AMOUNT)
            if s == "j":
                player1.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player1.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.pos += player1.velocity*dt        
                    if player1.pos.y >= 5:
                        player1.velocity.y = -player1.velocity.y
                    elif player1.pos.y <= 0:
                        player1.velocity.y = 0
                        n = 1
                    else:
                        player1.pos += player1.velocity*dt
                player1.pos.y = 0
            

            
            if s == "q":
                player1.strafe(STRAFE_AMOUNT)
            if s == "e":
                player1.strafe(-STRAFE_AMOUNT)
            # controls for player2
            if s == "l": #THIS IS AN L
                player2.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player2.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt        
                    if player2.pos.y >= 5:
                        player2.velocity.y = -player2.velocity.y
                    elif player2.pos.y <= 0:
                        player2.velocity.y = 0
                        n = 1
                    else:
                        player2.pos += player2.velocity*dt
                player2.pos.y = 0
            if s == "left":
                player2.turn(TURN_AMOUNT)
            if s == "right":
                player2.turn(-TURN_AMOUNT)
            if s == "down":
                player2.forward(-MOVE_AMOUNT)
            if s == "up":
                player2.forward(MOVE_AMOUNT)
            
            if s == ";":
                player2.strafe(STRAFE_AMOUNT)
            if s == "'":
                player2.strafe(-STRAFE_AMOUNT)
        #
        # check the state of the "game"
        #
        
            #TIME FOR THE ATTACKS!!!
        
            #Charmander's Ember
            
        
            if s == ",":
                print "Charmander uses Ember!"
                thunder=  cone(pos = player2.pos + player2.heading, radius = 0.5, axis = (0,1,0), color = color.red)
                die_dist = mag (player1.pos - thunder.pos)
                deltat = 0.02
                t = 0
                thunder.velocity = player2.heading * 5
                thunder.trail = curve(color=thunder.color, radius = .2)
                while t<3:
                    rate(1000)
                    thunder.pos = thunder.pos + thunder.velocity*deltat
                    t = t + deltat
                    thunder.trail.append(pos=thunder.pos)
                    die_dist = mag (player1.pos - thunder.pos)
                    if die_dist < 2:
                        player1.body.color = color.red
                        die_dist = mag (player1.pos - thunder.pos)
                        
                    if player1.body.color == color.red:
                        bulbaHP -= 5
                        print "Diglett got burned by Charmander's ember. He is losing health points!!"
                        print "Diglett's current HP", bulbaHP
                        bulbaHPtext.visible = False
                        bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                        die_dist = mag (player1.pos - thunder.pos)
                        thunder.visible = False
                        thunder.trail.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * thunder.velocity
                            player1.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player1.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player1.body.color = (0.36,0.21,0)
                        
                thunder.visible = False
                thunder.trail.visible = False
                
            player1.body.color = (0.36,0.21,0)
            
            # Diglett's Rock Throw
            
            if s == "1":
                for part in player1.parts:
                       part.visible = True
                print "Diglett uses Rock Throw!"
                vinewhip= sphere (pos = player1.pos + player1.heading, radius = 1, color = (0.36,0.21,0))
                pdie_dist = mag (player2.pos - vinewhip.pos)
                deltat = 0.01
                t = 0
                vinewhip.velocity = player1.heading * 5
                
                while t<3:
                    rate(1000)
                    vinewhip.pos = vinewhip.pos + vinewhip.velocity*deltat
                    t = t + deltat
                    pdie_dist = mag (player2.pos - vinewhip.pos)
                    if pdie_dist < 2:
                        player2.body.color = color.red
                        pdie_dist = mag (player2.pos - vinewhip.pos)
                        
                    if player2.body.color == color.red:
                        pikaHP -= 5
                        print "Charmander got hit by Diglett's rock throw. He is losing health points!!"
                        print "Charmander's current HP", pikaHP
                        pikaHPtext.visible = False
                        pikaHPtext = text(pos = (0,-3,20),
                           text='P2 HP:'+'-'*int((pikaHP/5.0)),
                           depth=-0.3, color=color.green)
                        vinewhip.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * vinewhip.velocity
                            player2.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player2.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player2.body.color = (1,.4,0)
                vinewhip.visible = False
                player2.body.color = (1,.4,0)
            #Diglett's Tackle
            if s == "2":
                for part in player1.parts:
                       part.visible = True
                print "Diglett uses Tackle!"
                MOVE_AMOUNT = 3
                player1.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player1.pos - player2.pos)
                if robot_dist < 2:
                    player2.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player1.heading
                        player2.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player2.parts:
                            part.pos += motion_vector
                    pikaHP -= 15
                    print "Charmander got hit by Diglett's tackle. He is losing health points!!"
                    print "Charmander's current HP", pikaHP
                    pikaHPtext.visible = False
                    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)
                    player2.body.color = (1,.4,0)
                    
                else: 
                    player2.body.color = (1,.4,0)

            #Diglett's Dig
            if s == '3':
                print "Diglett uses Dig!"
                
                for part in player1.parts:
                    part.visible = False

           #Charmander's Fire Spin
            if s == "/":
                if FIRESPIN_PP>0:
                    FIRESPIN_PP-=1
                    print "Charmander uses Fire Spin!"
                    sing = ring(pos=player2.pos, axis=(0,1,0), radius = 2, thickness = 0.2, color=color.red, material=materials.chrome)
                    pdie_dist = mag (player1.pos - sing.pos)
                    while sing.radius <20:
                        rate(100)
                        sing.radius += 0.25
                        if pdie_dist <= sing.radius:
                            sing.visible = False
                            player1.body.color = color.red
                            pdie_dist = mag (player1.pos - sing.pos)
                            
                            if player1.body.color == color.red:
                                player1.pos.y=0
                                sing.visible = False
                                bulbaHP -= 10
                                print "Diglett got burned by Charmander's Fire Spin. He is losing health points!!"
                                print "Diglett's current HP", bulbaHP
                                bulbaHPtext.visible = False
                                bulbaHPtext = text(pos = (-9,-3,20),
                                   text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                                   depth=-0.3, color=color.green)
                                sing.visible = False
                                player1.velocity = vector(0,1,0)
                                dt = 0.01
                                n = 0
                                while n == 0:
                                    rate(500)
                                    player1.pos += player1.velocity*dt
                                    player1.body.color =(.36,.21,0)
                                    for part in player1.parts:
                                        part.pos += player1.velocity*dt
                                    if player1.pos.y >= 5:
                                        player1.velocity.y = -player1.velocity.y
                                    elif player1.pos.y <= 0:
                                        player1.velocity.y = 0
                                        n = 1
                                    else:
                                        player1.pos += player1.velocity*dt
                                player1.pos.y = 0
                                break
                    sing.visible = False
                else:
                    print "Charmander is trying to use Firespin, but that move is out of PP."

            #Charmander's Bodyslam
            if s == ".":
                print "Charmander uses Bodyslam!"
                MOVE_AMOUNT = 3
                player2.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player2.pos - player1.pos)
                if robot_dist < 2:
                    player1.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player2.heading
                        player1.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player1.parts:
                            part.pos += motion_vector
                    bulbaHP -= 10
                    print "Diglett got smacked by Charmander's bodyslam. He is losing health points!!"
                    print "Diglett's current HP", bulbaHP
                    bulbaHPtext.visible = False
                    bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                    player1.body.color = (0.36,0.21,0)
                    
                else: 
                    player1.body.color = (0.36,0.21,0)
            #hit wall, wall breaks.
            """wallNdist = mag(extN.pos - player1.pos)
            if wallNdist.any() < 0.5:
                extN.visible = False
                for part in player1.parts:
                    part.pos = (0,0,0)
              """               

            
            # case for fainting.
            if bulbaHP<=0:
               print "Diglett faints. Charmander has won the battle!"
               player1.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                   rate(1000)
                   t += dt
                   for part in player1.parts:
                       part.pos += player1.velocity*dt
               for part in player1.parts:
                   part.visible = False
                
                
               scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if pikaHP<=0:
               print "Charmander faints. Diglett has won the battle!"
               player2.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                    rate(1000)
                    t += dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt
               for part in player2.parts:
                    part.visible = False
                    
               scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            #hit walls once, wall disappears, reset. again, fall off stage and die:

            
            if extN.visible == True and player1.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
                
                
                #for part in player1.parts:
                 #   part.visible= False
                #player1 = Diglett(pos=(0,0,0))
                
            
            if extN.visible == False and player1.pos.z < -21:
                    print "Diglett falls off the stage! Charmander has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player1.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player1.pos.x > 21:
                    print "Diglett falls off the stage! Charmander has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extS.visible == True and player1.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player1.pos.z > 21:
                    print "Diglett falls off the stage! Charmander has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extW.visible == True and player1.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player1.pos.x < - 21 :
                    print "Diglett falls off the stage! Charmander has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extN.visible == True and player2.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extN.visible == False and player2.pos.z < - 21:
                    print "Charmander falls off the stage! Diglett has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player2.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player2.pos.x > 21:
                    print "Charmander falls off the stage! Diglett has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extS.visible == True and player2.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player2.pos.z > 21:
                    print "Charmander falls off the stage! Diglett has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extW.visible == True and player2.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player2.pos.x < -21:
                    p =  "Charmander falls off the stage! Diglett has won the battle!"
                    print p
                    """tx = text(pos = (0,-3,20),
                           text=p,
                           depth=-0.3, color=color.green)"""
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')


###BATTLE 1!

from visual import *
import math
import random

class stage1:

    def __init__(self, pos, heading=vector(0,0,1)):
        """constructs the stage on screen"""
        self.parts = [] #creates the list of all the components of the stage
        self.pos = vector(pos)
        self.heading = norm(heading)
        self.flats = box(pos = self.pos, length=40.0, height=0.25, width=40.0, color=color.green, material = materials.marble)
        self.parts += [self.flats]
     
        """self.parts += [extN] + [extE] + [extS] + [extW]

        rect = shapes.rectangle(pos=(self.pos), width = 42.0, height = 42.0)
        inner = shapes.rectangle(pos=(self.pos), width = 39.5, height = 39.5)
        pth = [(0,-1,0), (0,5,0)]
        ext = extrusion(pos=pth, shape=rect-inner, color=color.green)"""

      
        

        
    def __rpr__(self):
        """creates the 3D representation of the stage for python"""
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s


class Bulbasaur:
    """ a collection of VPython parts that
        will move together == a Pokemon
    """

    # make x, y, z axes with labels
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our Bulbasaur class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        self.head = sphere(pos=(self.pos.x, self.pos.y + .25, self.pos.z +.35) , radius=.60,
                           color=(0.49, 0.82, 0.66),
                           material = materials.marble)
        self.parts += [self.head] # add it to our "parts" list


        # The body: width = z direction, length = x direction, height = y direction 
        self.body = ellipsoid ( pos = self.pos + vector (0, 0, -.25),
                                length = 1.7, height = 1.5,
                                width = 1.9, color = (0.49, 0.82, 0.66),
                                material = materials.marble)
        self.parts += [self.body]
        # two (?) eyes
        left_eye = sphere(pos=self.pos+vector(.25,.5,.65),
                          radius=0.20, color=color.white)
        self.parts += [left_eye]
        right_eye = sphere(pos=self.pos+vector(-.25,.5,.65),
                           radius=0.20, color=color.white)
        self.parts += [right_eye]

        # creating the mouth
        mouth = ellipsoid( pos = self.pos+vector(0,0,0.92), axis= (0,0,1), length =.2, height =.2, width =.3, color = color.red)
        self.parts += [mouth]
        

        #creating bulb
        bulb = cone(pos = self.pos+vector(0,.4,-.45),
                    axis=(0,1,-.25),
                        radius = 0.75, color = color.green, material= materials.wood)
        self.parts += [bulb]
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)

class Pikachu:
    """ a collection of VPython parts that
        will move together == a Pokemon!
    """

    # make x, y, z axes with labels
    
    def __init__(self, pos, heading=vector(0,0,1)):
        """ constructor for our Pikachu class """
        # list of vPython 3D shapes that make up this robot
        self.parts = []
        # Position of the origin of robot; we make sure it's a vector
        # For consistency, we use the same name as VPython's objects
        self.pos = vector(pos)
        # Direction in which robot is moving, normalized to unit length
        self.heading = norm(heading)
        
        # the main body of our robot is a sphere
        self.body = ellipsoid( pos=self.pos, length = 1,
                          height =1.5, width = 1)
        self.body.color = color.yellow
        self.parts += [self.body] # add it to our "parts" list

        #pokemon head length - x width -z, height-y
        self.head = ellipsoid( pos=self.pos + vector (0,.72,0),
                                length = 1,
                                height =.9, width = 1)
        self.head.color = color.yellow
        self.parts += [self.head] 

        #making pikachu's booty
        self.butt = ellipsoid( pos=self.pos + vector (0,-.3,0),
                                length = 1.35,
                                height =1.15, width = 1)
        self.butt.color = color.yellow
        self.parts += [self.butt] 

        
        # two (?) eyes
        left_eye = sphere(pos=self.pos+vector(.20,.9,.4),
                          radius=0.08, color=color.black)
        self.parts += [left_eye]
        right_eye = sphere(pos=self.pos+vector(-.20,.9,.4),
                           radius=0.08, color=color.black)
        self.parts += [right_eye]
        # two ears
        left_ear = cone(pos = self.pos+vector(0.3,.9,.1), axis=(.35,.60,0),
                        radius = 0.2, color = color.yellow)
        self.parts += [left_ear]
        right_ear = cone(pos = self.pos+vector(-0.3,.9,.1), axis=(-.35,.60,0),
                         radius = 0.2, color = color.yellow)
        self.parts += [right_ear]
        


        #pikachu needs arms

        self.arml = ellipsoid( pos = self.pos+vector(-.45,.2,.25),
                                length =.6, 
                                height =.4, width =.4,
                                color = color.yellow)
        self.parts += [self.arml]

        self.armr = ellipsoid( pos = self.pos+vector(.45,.2,.25),
                                 length =.6,axis = (.5, .5, 0),
                                height =.4, width =.4,
                                color = color.yellow)
        self.parts += [self.armr]



        #signature electric cheeks
        cheekL = cone( pos = self.pos+vector(-.28,.75,.45),
                            axis= (0,0,.05), radius = 0.1, color = color.red, material = materials.emissive)
        self.parts += [cheekL]
        
        cheekR = cone( pos = self.pos+vector(.28,.75,.45),
                            axis= (0,0,.05), radius = 0.1, color = color.red, material = materials.emissive)
        self.parts += [cheekR]
        
        #tail
        self.tail = arrow(pos=self.pos+vector(0,0,-.5), axis=(0,1,-1),
                    shaftwidth=.1, color=color.yellow, material = materials.emissive)
        self.parts += [self.tail]
        
        #mouth
        mouth = ellipsoid( pos = self.pos+vector(0,.7,.5), axis= (0,0,1), length =.2, height =.2, width =.3, color = color.magenta)
        self.parts += [mouth]

        #feet

        self.footl = ellipsoid( pos = self.pos+vector(-.3,-.85,.25),
                                length =.2,
                                height =.2, width =.4,
                                color = color.yellow)
        self.parts += [self.footl]

        self.footr = ellipsoid( pos = self.pos+vector(.3,-.85,.25),
                                 length =.2,
                                height =.2, width =.4,
                                color = color.yellow)
        self.parts += [self.footr]

        
    def __repr__(self):
        """ prints the pieces, position, and heading of self """
        s = "  position:" + str(self.pos) + "\n"
        s += "  heading: " + str(self.heading) + "\n"
        return s

    def forward(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''
        motion_vector = amount * self.heading
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
    def fly(self, amount):
        """moves the Pokemon in the positive or negative y direction
        """
        motion_vector = amount * vector(0, 1, 0)
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
   


    def strafe(self, amount):
        ''' Change Pokemon's location by moving in 
            the heading direction by a given amount '''

        strafe_direction = rotate(self.heading, angle=math.pi/2.0, axis=(0,1,0))
        motion_vector = amount * strafe_direction
        self.pos += motion_vector
        for part in self.parts:
            part.pos += motion_vector
           
    def turn(self, angle):
        ''' Turn the Pokemon by the given angle, in degrees '''
        # convert the angle to radians first
        theta = math.radians(angle)
        # rotate the heading vector around the vertical y-axis
        self.heading = rotate(self.heading, angle=theta, axis=(0,1,0))
        # rotate all of the parts around the current position
        for part in self.parts:
            part.rotate(angle=theta, axis=(0,1,0), origin=self.pos)


def battle1():
    """Play the game!"""
    # set up the visual conditions - the window is called "scene"
    scene2 = display(width=1400, height=850,center=(0,9,40), background=(0,1,1))
    # set up the visual conditions - the window is called "scene"
    scene = scene2
    scene.autoscale = False  # should the scene fill the window?
    scene.background = color.black  # the background "space" color

    # create other, non-robot objects
    #create walls
    wallS = shapes.line(start = (-20,20), end=(20,20))
    wallE = shapes.line(start = (20,20), end=(20,-20))
    wallN = shapes.line(start = (-20,-20), end=(20,-20))
    wallW = shapes.line(start = (-20,20), end=(-20,-20))
    wpath = [(0,-1,0), (0,1.25,0)]
    extN = extrusion(pos = wpath, shape = wallN, color = color.red, material = materials.chrome)
    extE = extrusion(pos = wpath, shape = wallE, color = color.green, material= materials.chrome)
    extS = extrusion(pos = wpath, shape = wallS, color = color.blue, material=materials.chrome)
    extW = extrusion(pos = wpath, shape = wallW, color = color.orange, material =materials.chrome)

   
   #pokeball at center of stage
    outerw = shapes.circle(radius=3)
    cut = shapes.rectangle(pos=(0,1.5),width=6,height=3)
    outerr= outerw-cut

    
    innerb = shapes.circle(radius=0.7,thickness=0.2)

    pthw = [(0,-.75,0),(0,-.74,0)]
    pthb = [(0,-.75,0),(0,-.72,0)]

    outerwe = extrusion(pos=pthw, shape = outerw, color=color.white)
    innerbe = extrusion(pos=pthb,shape=innerb, color=color.black)
    outerre = extrusion(pos=pthw, shape=outerr, color=color.red)      
    


  #lighting
    lampR = local_light(pos=(21,13,-30), color=color.white)
    lampsR = box(pos=(21,13,-30),axis=(-3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standR = box(pos=(21,0,-30), axis=(-3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)

    lampL = local_light(pos=(-21,13,-30), color=color.white)
    lampsL = box(pos=(-21,13,-30),axis=(3,-.75,-1.5),length=6,height=3,width=1.5,color=color.white,material=materials.emissive)
    standL = box(pos=(-21,0,-30), axis=(3,0,-1.5),length=1,height=25,width=1,color=color.gray(0.5),material=materials.shiny)



    #establishing original HP
    bulbaHP = 50
    pikaHP = 50
    bulbaHPtext = text(pos = (-9,-3,20),
                       text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                       depth=-0.3, color=color.green)
    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)



    
    # the controlled robot
    player1 = Bulbasaur(pos=(-10,0,0))
    # another robot, this one not controlled
    player2 = Pikachu(pos=(10,0,0))

    thestage = stage1(pos=(0,-1,0))

    SOLARBEAM_PP = 2
    THUNDER_PP = 2
    # the main loop - handle user events
    
    while True:

        # It's easier to adjust constants if they
        # have names and are all in one place!
        TURN_AMOUNT = 15 # degrees
        MOVE_AMOUNT = .3 # units
        FLY_AMOUNT = 0.3 #unit of flight
        STRAFE_AMOUNT = 0.3 #strafe units
        KNOCKBACK_AMOUNT = 0.005
        BOUNCE_AMOUNT = 10
        rate(1000000)  # at most 30 loops per second
        
        
        if scene.mouse.clicked != 0: # mouse click?
            print "mouse click!"
            event = scene.mouse.getclick() # remove event
            scene.mouse.events = 0 # reset mouse events
            
        if scene.kb.keys: # is there a keyevent?
            s = scene.kb.getkey() # get keypress
            keys_seen = [s]
           
            
            # controls for player1
            

            if s == "a":
                player1.turn(TURN_AMOUNT)
            if s == "d":
                player1.turn(-TURN_AMOUNT)
            if s == "s":
                player1.forward(-MOVE_AMOUNT)
            if s == "w":
                player1.forward(MOVE_AMOUNT)
            if s == "j":
                player1.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player1.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.pos += player1.velocity*dt        
                    if player1.pos.y >= 5:
                        player1.velocity.y = -player1.velocity.y
                    elif player1.pos.y <= 0:
                        player1.velocity.y = 0
                        n = 1
                    else:
                        player1.pos += player1.velocity*dt
                player1.pos.y = 0
            

            
            if s == "q":
                player1.strafe(STRAFE_AMOUNT)
            if s == "e":
                player1.strafe(-STRAFE_AMOUNT)
            # controls for player2
            if s == "l": #THIS IS AN L
                player2.velocity = vector(0,1,0)
                dt = 0.01
                n = 0
                while n == 0:
                    rate(500)
                    player2.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt        
                    if player2.pos.y >= 5:
                        player2.velocity.y = -player2.velocity.y
                    elif player2.pos.y <= 0:
                        player2.velocity.y = 0
                        n = 1
                    else:
                        player2.pos += player2.velocity*dt
                player2.pos.y = 0
            if s == "left":
                player2.turn(TURN_AMOUNT)
            if s == "right":
                player2.turn(-TURN_AMOUNT)
            if s == "down":
                player2.forward(-MOVE_AMOUNT)
            if s == "up":
                player2.forward(MOVE_AMOUNT)
            if s == ";":
                player2.strafe(STRAFE_AMOUNT)
            if s == "'":
                player2.strafe(-STRAFE_AMOUNT)
        #
        # check the state of the "game"
        #
        
            #TIME FOR THE ATTACKS!!!
        
            #Pikachu's ThunderShock!!
            
        
            if s == ",":
                print "Pikachu uses ThunderShock!"
                thunder= sphere (pos = player2.pos + player2.heading, radius = 0.5, color = color.yellow)
                die_dist = mag (player1.pos - thunder.pos)
                deltat = 0.02
                t = 0
                thunder.velocity = player2.heading * 5
                thunder.trail = curve(color=thunder.color)
                while t<3:
                    rate(1000)
                    thunder.pos = thunder.pos + thunder.velocity*deltat
                    t = t + deltat
                    thunder.trail.append(pos=thunder.pos)
                    die_dist = mag (player1.pos - thunder.pos)
                    if die_dist < 2:
                        player1.body.color = color.red
                        die_dist = mag (player1.pos - thunder.pos)
                        
                    if player1.body.color == color.red:
                        bulbaHP -= 5
                        print "Bulbasaur got shocked by Pikachu's ThunderShock. He is losing health points!!"
                        print "Bulbasaur's current HP", bulbaHP
                        bulbaHPtext.visible = False
                        bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                        die_dist = mag (player1.pos - thunder.pos)
                        thunder.visible = False
                        thunder.trail.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * thunder.velocity
                            player1.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player1.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player1.body.color = (0.49, 0.82, 0.66)
                        
                thunder.visible = False
                thunder.trail.visible = False
                
            player1.body.color = (0.49, 0.82, 0.66)
            
            # Bulbasaur's Vinewhip!
            
            if s == "2":
                print "Bulbasaur uses Vinewhip!"
                vinewhip= sphere (pos = player1.pos + player1.heading, radius = 0.1, color = color.green)
                pdie_dist = mag (player2.pos - vinewhip.pos)
                deltat = 0.02
                t = 0
                vinewhip.velocity = player1.heading * 5
                vinewhip.trail = curve(color=vinewhip.color)
                while t<3:
                    rate(1000)
                    vinewhip.pos = vinewhip.pos + vinewhip.velocity*deltat
                    t = t + deltat
                    vinewhip.trail.append(pos=vinewhip.pos)
                    pdie_dist = mag (player2.pos - vinewhip.pos)
                    if pdie_dist < 2:
                        player2.body.color = color.red
                        pdie_dist = mag (player2.pos - vinewhip.pos)
                        
                    if player2.body.color == color.red:
                        pikaHP -= 5
                        print "Pikachu got whipped by Bulbasaur's vinewhip. He is losing health points!!"
                        print "Pikachu's current HP", pikaHP
                        pikaHPtext.visible = False
                        pikaHPtext = text(pos = (0,-3,20),
                           text='P2 HP:'+'-'*int((pikaHP/5.0)),
                           depth=-0.3, color=color.green)
                        vinewhip.visible = False
                        vinewhip.trail.visible = False
                        deltat2 = 0.02
                        t2 = 0
                        while t2<3:
                            rate(1000)
                            motion_vector = KNOCKBACK_AMOUNT * vinewhip.velocity
                            player2.pos += motion_vector
                            t2 = t2 + deltat2
                            for part in player2.parts:
                                part.pos += motion_vector
                        break
                        
                    else:
                        player2.body.color = color.yellow
                vinewhip.visible = False
                vinewhip.trail.visible = False
                player2.body.color = color.yellow
            #Bulbasaur's Tackle
            if s == "1":
                print "Bulbasaur uses Tackle!"
                MOVE_AMOUNT = 3
                player1.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player1.pos - player2.pos)
                if robot_dist < 2:
                    player2.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player1.heading
                        player2.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player2.parts:
                            part.pos += motion_vector
                    pikaHP -= 10
                    print "Pikachu got hit by Bulbasaur's tackle. He is losing health points!!"
                    print "Pikachu's current HP", pikaHP
                    pikaHPtext.visible = False
                    pikaHPtext = text(pos = (0,-3,20),
                       text='P2 HP:'+'-'*int((pikaHP/5.0)),
                       depth=-0.3, color=color.green)
                    player2.body.color = color.yellow
                    
                else: 
                    player2.body.color = color.yellow 
            #Pikachu's Slam
            if s == ".":
                print "Pikachu uses Slam!"
                MOVE_AMOUNT = 3
                player2.forward(MOVE_AMOUNT)
                MOVE_AMOUNT = 0.3
                robot_dist = mag(player2.pos - player1.pos)
                if robot_dist < 2:
                    player1.body.color = color.red 
                    deltat2 = 0.02
                    t2 = 0
                    while t2<3:
                        rate(1000)
                        motion_vector = KNOCKBACK_AMOUNT*5.0 * player2.heading
                        player1.pos += motion_vector
                        t2 = t2 + deltat2
                        for part in player1.parts:
                            part.pos += motion_vector
                    bulbaHP -= 10
                    print "Bulbasaur got smacked by Pikachu's slam. He is losing health points!!"
                    print "Bulbasaur's current HP", bulbaHP
                    bulbaHPtext.visible = False
                    bulbaHPtext = text(pos = (-9,-3,20),
                           text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                           depth=-0.3, color=color.green)
                    player1.body.color = (0.49, 0.82, 0.66)
                    
                else: 
                    player1.body.color = (0.49, 0.82, 0.66)

            if s == "/":
                if THUNDER_PP>0:
                    
                    print "Pikachu IS USING HIS ULTIMATE MOVIE, Thunder!!!"


                    SB_List = []
                    for i in range(100):
                        x_pos = random.choice( range(-20,20) )
                        z_pos = random.choice( range(-20,20) )
                        sb = sphere(pos=(x_pos,10,z_pos), radius = 1, color = color.yellow)
                        SB_List += [sb]
                    
                    while sb.pos.y >=0:
                        
                        for sb in SB_List:
                            sb.pos += 0.02 * vector(0,-20,0)
                            die_dist = mag (player1.pos - sb.pos)
                            if die_dist < 2:
                                player1.body.color = color.red
                                die_dist = mag (player1.pos - sb.pos)    
                            if player1.body.color == color.red:
                                bulbaHP -= 1.5
                                print "Bulbasaur got shocked by Pikachu's Thunder. He is losing health points!!"
                                print "Bulbasaur's current HP", bulbaHP
                                bulbaHPtext.visible = False
                                bulbaHPtext = text(pos = (-9,-3,20),
                                   text='P1 HP:'+'-'*int((bulbaHP/5.0)),
                                   depth=-0.3, color=color.green)
                                player1.body.color = (0.49, 0.82, 0.66)
                                for sb in SB_List:
                                    sb.visible = False
                                break
                        if die_dist>=2:
                            while True:
                                
                                
                                # It's easier to adjust constants if they
                                # have names and are all in one place!
                                TURN_AMOUNT = 15 # degrees
                                MOVE_AMOUNT = .3 # units
                                FLY_AMOUNT = 0.3 #unit of flight
                                STRAFE_AMOUNT = 0.3 #strafe units
                                KNOCKBACK_AMOUNT = 0.005
                                BOUNCE_AMOUNT = 10
                                rate(100)  # at most 30 loops per second
                                
                                if scene.mouse.clicked != 0: # mouse click?
                                    print "mouse click!"
                                    event = scene.mouse.getclick() # remove event
                                    scene.mouse.events = 0 # reset mouse events
                                
                                if scene.kb.keys: # is there a keyevent?
                                    s = scene.kb.getkey() # get keypress
                                    keys_seen = [s]
                                    if scene.kb.keys:
                                        s2 = scene.kb.getkey()
                                        keys_seen += [s2]
                                        print "keys_seen is", keys_seen
                                    
                                    # controls for player1
                                    

                                    if s == "a":
                                        player1.turn(TURN_AMOUNT)
                                        break
                                    if s == "d":
                                        player1.turn(-TURN_AMOUNT)
                                        break
                                    if s == "s":
                                        player1.forward(-MOVE_AMOUNT)
                                        break
                                    if s == "w":
                                        player1.forward(MOVE_AMOUNT)
                                        break
                                    
                                    if s == "q":
                                        player1.strafe(STRAFE_AMOUNT)
                                        break
                                    if s == "e":
                                        player1.strafe(-STRAFE_AMOUNT)
                                        break
                                    # controls for player2
                                    
                                    if s == "left":
                                        player2.turn(TURN_AMOUNT)
                                        break
                                    if s == "right":
                                        player2.turn(-TURN_AMOUNT)
                                        break
                                    if s == "down":
                                        player2.forward(-MOVE_AMOUNT)
                                        break
                                    if s == "up":
                                        player2.forward(MOVE_AMOUNT)
                                        break
                                    
                                    if s == ";":
                                        player2.strafe(STRAFE_AMOUNT)
                                        break
                                    if s == "'":
                                        player2.strafe(-STRAFE_AMOUNT)
                                        break
                            
                    for sb in SB_List:
                        sb.visible = False
                    THUNDER_PP -= 1
                    print "THUNDER PP IS", THUNDER_PP
                else:
                    print "Pikachu tried to use Thunder, but there is no PP left for that move."

            #Bulbasaur's Hyperbeam
            if s == "3":
                if SOLARBEAM_PP>0:
                    SOLARBEAM_PP-=1
                    print "Bulbasaur uses Hyperbeam!"
                    vinewhip= sphere (pos = player1.pos + player1.heading, radius = 8, color = (0.71,1,1))
                    pdie_dist = mag (player2.pos - vinewhip.pos)
                    deltat = 0.02
                    t = 0
                    vinewhip.velocity = player1.heading * 5
                    vinewhip.trail = curve(color=vinewhip.color, radius = 8)
                    while t<5:
                        rate(1000)
                        vinewhip.pos = vinewhip.pos + vinewhip.velocity*deltat
                        t = t + deltat
                        vinewhip.trail.append(pos=vinewhip.pos)
                        pdie_dist = mag (player2.pos - vinewhip.pos)
                        if pdie_dist < 2:
                            player2.body.color = color.red
                            pdie_dist = mag (player2.pos - vinewhip.pos)
                            
                        if player2.body.color == color.red:
                            pikaHP -= 10
                            print "Pikachu got hit by Bulbasaur's Hyperbeam. He is losing health points!!"
                            print "Pikachu's current HP", pikaHP
                            pikaHPtext.visible = False
                            pikaHPtext = text(pos = (0,-3,20),
                               text='P2 HP:'+'-'*int((pikaHP/5.0)),
                               depth=-0.3, color=color.green)
                            vinewhip.visible = False
                            vinewhip.trail.visible = False
                            deltat2 = 0.02
                            t2 = 0
                            while t2<3:
                                rate(1000)
                                motion_vector = KNOCKBACK_AMOUNT * vinewhip.velocity
                                player2.pos += motion_vector
                                t2 = t2 + deltat2
                                for part in player2.parts:
                                    part.pos += motion_vector
                            break
                            
                        else:
                            player2.body.color = color.yellow
                    vinewhip.visible = False
                    vinewhip.trail.visible = False
                    player2.body.color = color.yellow
                else:
                    print "Bulbasaur is trying to use Solarbeam, but that move is out of PP."
            #hit wall, wall breaks.
            """wallNdist = mag(extN.pos - player1.pos)
            if wallNdist.any() < 0.5:
                extN.visible = False
                for part in player1.parts:
                    part.pos = (0,0,0)
              """               

            
            # case for fainting.
            if bulbaHP<=0:
               print "Bulbasaur faints. Pikachu has won the battle!"
               player1.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                   rate(1000)
                   t += dt
                   for part in player1.parts:
                       part.pos += player1.velocity*dt
               for part in player1.parts:
                   part.visible = False
                
                
               scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if pikaHP<=0:
               print "Pikachu faints. Bulbasaur has won the battle!"
               player2.velocity = vector(0,-1,0)
               dt = 0.01
               t = 0
               while t<5:
                    rate(1000)
                    t += dt
                    for part in player2.parts:
                        part.pos += player2.velocity*dt
               for part in player2.parts:
                    part.visible = False
                    
               scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            #hit walls once, wall disappears, reset. again, fall off stage and die:

            
            if extN.visible == True and player1.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
                
                
                #for part in player1.parts:
                 #   part.visible= False
                #player1 = Bulbasaur(pos=(0,0,0))
                
            
            if extN.visible == False and player1.pos.z < -21:
                    print "Bulbasaur falls off the stage! Pikachu has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player1.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player1.pos.x > 21:
                    print "Bulbasaur falls off the stage! Pikachu has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extS.visible == True and player1.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player1.pos.z > 21:
                    print "Bulbasaur falls off the stage! Pikachu has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
                
            if extW.visible == True and player1.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player1.heading
                player1.pos -= motion_vector
                for part in player1.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player1.pos.x < - 21 :
                    print "Bulbasaur falls off the stage! Pikachu has won the battle!"
                    player1.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player1.parts:
                            part.pos += player1.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 1 has fainted. Player 2 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extN.visible == True and player2.pos.z < -19:
                extN.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extN.visible == False and player2.pos.z < - 21:
                    print "Pikachu falls off the stage! Bulbasaur has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player1.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

            if extE.visible == True and player2.pos.x > 19:
                extE.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extE.visible == False and player2.pos.x > 21:
                    print "Pikachu falls off the stage! Bulbasaur has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extS.visible == True and player2.pos.z > 19:
                extS.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extS.visible == False and player2.pos.z > 21:
                    print "Pikachu falls off the stage! Bulbasaur has won the battle!"
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')
            if extW.visible == True and player2.pos.x < -19:
                extW.visible = False
                motion_vector = BOUNCE_AMOUNT * player2.heading
                player2.pos -= motion_vector
                for part in player2.parts:
                    part.pos -= motion_vector
            
            if extW.visible == False and player2.pos.x < -21:
                    p =  "Pikachu falls off the stage! Bulbasaur has won the battle!"
                    print p
                    """tx = text(pos = (0,-3,20),
                           text=p,
                           depth=-0.3, color=color.green)"""
                    player2.velocity = vector(0,-1,0)
                    dt = 0.01
                    t = 0
                    while t<5:
                        rate(1000)
                        t += dt
                        for part in player2.parts:
                            part.pos += player2.velocity*dt
                    for part in player2.parts:
                        part.visible = False
                    
                    scene.text2 = text(text = 'Player 2 has fainted. Player 1 is the Pokemon Master!', depth = 0.3, height = 2, color = color.red, pos = (0,10,-7), align='center')

                    

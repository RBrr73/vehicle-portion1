    chassis.py - Chassis component for the vehicle example problem.
"""

# This oottaDAO component determines the vehicle acceleration based on the
# power output of the engine, modified by the transmission torque ratio.

from math import pi
import time
import RPi.GPIO as GPIO

# pylint: disable-msg=E0611,F0401
import math, time
from oottadao.main.api import Component
from oottadao.main.datatypes.api import Float



class Chassis(Component):
    """ A vehicle dynamics component - calculates acceleration.
    Design parameters:
    mass_vehicle        # Vehicle Mass (kg)
    Cf                  # Friction coef (multiplies W)
    Cd                  # Drag coef (multiplies V**2)
    area                # Frontal area (for drag calc) (sq m)
    
    Simulation inputs:
    mass_engine         # Engine Mass (kg)
    velocity            # Vehicle velocity (m/s)
    engine_torque       # Engine Torque (Nm)
    torque_ratio        # Torque ratio due to Transmission
    tire_circ           # Circumference of tire (m)
    
    Outputs:
    acceleration        # Calculated vehicle acceleration (m/s^2)
    """
    
    # set up interface to the framework  
    # pylint: disable-msg=E1101
    
    mass_vehicle = Float(1200.0, iotype='in', units='kg', 
                              desc='Vehicle Mass')
    Cf = Float(0.035, iotype='in', 
                    desc='Friction Coefficient (multiplies W)')
    Cd = Float(0.3, iotype='in', 
               desc='Drag Coefficient (multiplies V**2)')
    area = Float(2.164, iotype='in', units='m**2', 
                      desc='Frontal area')
    engine_torque = Float(200.0, iotype='in', units='N*m', 
                               desc='Torque at engine output')
    mass_engine = Float(150.0, iotype='in', units='kg',
                             desc='Engine weight estimation')
    velocity = Float(0., iotype='in', units='m/s', 
                          desc='Current Velocity of Vehicle')
    torque_ratio = Float(0., iotype='in', 
                         desc='Ratio of output torque to engine torque')        
    tire_circ = Float(2, iotype='in', units='m', 
                           desc='Circumference of tire')
    acceleration = Float(0., iotype='out', units='m/(s*s)', 
                              desc='Vehicle acceleration ')    

        
        
    def execute(self):
        """ Calculates the instantaneous acceleration for the vehicle. """
        
        torque = self.engine_torque*self.torque_ratio
        tire_radius = self.tire_circ/(2.0*pi)
                
        friction = self.Cf*mass*9.8
        drag = .5*(1.225)*self.Cd*self.area*V*V
        
        mass = self.mass_vehicle + self.mass_engine
        V = self.velocity
       
        self.acceleration = (torque/tire_radius - friction - drag)/mass


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)



while True:
  try:
    # Makes the motor spin one way for 3 seconds
    GPIO.output(17, True)
    GPIO.output(18, False)
    time.sleep(3)
    # Spins the other way for a further 3 seconds
    GPIO.output(17, False)
    GPIO.output(18, True)
    time.sleep(3)
  except(KeyboardInterrupt):
    # If a keyboard interrupt is detected then it exits cleanly!
    print('Finishing up!')
    GPIO.output(17, False)
    GPIO.output(18, False)
    quit()

# End Chassis.py


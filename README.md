quadcopter
==========

DRAFT

Vision:
-----
To build an automous quadcopter from scratch

Plan of attack:
----------------------------
Instead of spending a lot of money and buying a prebuilt quadcopter and autopilot module, I will waste more money in an attempt to build a copter from scratch. Code will be written in Python or C depending on the board chosen.

I will be using online resource such as (To name a few):
http://ghowen.me/build-your-own-quadcopter-autopilot/ 
r/multicopter
http://www.multirotorforums.com/
http://diydrones.com/

Milestones:
-----------
I'm unsure how difficult each task is really is so I've split it out into extra milestones

Quadcopter assembly
- Board+Sensors all soldered up
- Quad frame Assembled (Will be desgined and 3D printed by me)
- Quad parts assembled (ie motors, propellers, board etc. bolted onto frame)

Basic Quadcopter features
- Motor controls (Propeller on off, speed control)
- Quad Stabilization (fly up and stay there, possibly take light bumps)
- Quad turning (staying in place and turning left or right)
- Quad movement (moving forward, etc.)

Autopilot
- Auto land/takeoff (?)
- Single waypoint commands (Takeoff, go to B, Land)
- Multi waypoints/tasking (?)

Stretch goals
- GUI via Android device or web browser (?)
- Camera
- Some Data connection to device

Parts List (STUB)
----------------
- Motor (x4)
- ESC (x4)
- LiPo Battery
- Controller board (Raspberry pi, Arduino, Beaglebone, or some other ARM or AVR based board)
- Gyroscope
- Accelerometer
- Magnetometer (?)
- Altimeter - Barometric pressure sensor (?)
- GPS
- Wifi (and/or connection for data)

Questions/Notes to self
--------------------------
- What board will I be using? Can't start without deciding on a board
- I should impliment manual controls before jumping to autonomous
- How will I send commands over while testing?
- What do use as a data connection? Range is important (or will be)
- Rpi battery usage
- Use two boards instead? One to control quadcopter and stabilize while rpi navigates and uses GPS? 
- In addition to dual boards, possibly prototype with a Pi and move to a dual board setup in the future
- How fast will the Pi be? Too many layers between motor controls and Pythons script (maybe)
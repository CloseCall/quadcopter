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
-[ ]Board+Sensors all soldered up
-[ ]Quad frame Assembled (Will be desgined and 3D printed by me)
-[ ]Quad parts assembled (ie motors, propellers, board etc. bolted onto frame)

Basic Quadcopter features
-[ ]Motor controls (Propeller on off, speed control)
-[ ]Quad Stabilization (fly up and stay there, possibly take light bumps)
-[ ]Quad turning (staying in place and turning left or right)
-[ ]Quad movement (moving forward, etc.)

Autopilot
-[ ]Auto land/takeoff (?)
-[ ]Single waypoint commands (Takeoff, go to B, Land)
-[ ]Multi waypoints/tasking (?)

Stretch goals
-[ ]GUI via Android device or web browser (?)
-[ ]Camera
-[ ]Some Data connection to device

Parts List (STUB)
----------------
+Motor (x4)
+ESC (x4)
+LiPo Battery
+Controller board (Raspberry pi, Arduino, Beaglebone, or some other ARM or AVR based board)
+Gyroscope
+Accelerometer
+GPS
+Wifi (and/or connection for data)
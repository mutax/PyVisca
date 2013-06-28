PyVisca
=======

Reimplementation of libvisca in python to control Cameras via the serial line visca protocol


Why?
----

I found a SONY EVI-D100P in the trash and decided to play around with it.

The camera has analog video output and a serial port for remote control using the Visca protocol.

I found the protocol being publicly documented by Sony in a camera manual and a C implementation
of that protocol at http://sourceforge.net/projects/libvisca/ - but I wanted an easier solution
so I started implementing the commandset my camera offers in python.


Status
------

Currently the basic functions all work but there is no error handling yet as at this stage it was
just a proof of concept. I plan on adding this and make it a full featured implementation, at leat
for my camera.

The error handling might make some changes neccessary due to the fact that some commands are being executed
asynchronously and the camera returns an ACK when the command was accepted and another message when it was
completed (e.g. tilting, panning). This will require some changes so don't expect anything to be stable.

As this is a side project these changes are not highest priority.

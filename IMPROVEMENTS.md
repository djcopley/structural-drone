# Next steps and improvements

This document provides an outline for future improvements and next steps regarding the 
structural inspection drone. In addition, it will also highlight several software quirks that, 
given a little attention, should not be too difficult to iron out.

## Logging

One feature that needs to be fully implemented is package level logging. A detailed record 
of all actions taken by the drone software should be cataloged in a file so that in the event 
of a failure, the source of the problem may be quickly pinpointed. 

## Dynamic content loading

Content in the front end should be automatically loaded from the backend. This will save the hassle of manually coding 
and debugging when (inevitably) someone forgets to add it. 

## Remove hard-coded class names

This improvement goes hand-in-hand with the dynamic content loading feature. Currently, 
detected class names are hardcoded in several areas including the graphical user interface 
and classifier code. This should be reworked so all class names are loaded dynamically from 
the `.names` files.

## Seperate video input and output packages

New packages for video source/sink located in the model package. As stated above, allow dynamic loading of these 
backends.

## More graphical user input tuning parameters

- Different video sources (webcam, gopro, etc.)
- Different or multiple video outputs (file, udp stream, etc.)

## Finish setup.py installation

Our program requires opencv to be compiled with the GStreamer backend. See if there is any way to do manual C 
compilation. If not create an installation script. Also, add the neural network files to package data so they are 
installed with the python files.

## Update README and other documentation

Documentation is super incomplete and out of date. Update it. Also add docstrings to functions and methods.

## Updated testing

Write unit tests for all modules

## Simulator mode

Steal the stream from the Gazebo simulator and run processing.

## Dockerize?

Would be awesome to dockerize and take advantage of hardware acceleration

## Add object permanence

In `action.py` devise some sort of object permanence scheme so that multiple actions are not being taken for the same 
feature in two different frames.

## Fix threading

Threading does not exit gracefully. In addition, edge cases may cause a thread to continue running.

## Try catch common errors and add the ability to reconnect to GoPro

Common errors should be caught and program should continue to gracefully start. Allow the user to reconnect to GoPro.

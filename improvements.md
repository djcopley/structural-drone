# Next steps and improvements

This document provides an outline for future improvements and next steps regarding the 
structural inspection drone. In addition, it will also highlight several software quirks that, 
given a little attention, should not be too difficult to iron out.

## Logging

One feature that needs to be fully implemented is package level logging. A detailed record 
of all actions taken by the drone software should be cataloged in a file so that in the event 
of a failure, the source of the problem may be quickly pinpointed. 

## Dynamic content loading

A soft

## Remove hard-coded class names

This improvement goes hand-in-hand with the dynamic content loading feature. Currently, 
detected class names are hardcoded in several areas including the graphical user interface 
and classifier code. This should be reworked so all class names are loaded dynamically from 
the `.names` files.

## Seperate video input and output packages

## More graphical user input tuning parameters

- Logging
- Update view automatically when new content is added in the model
- 
# Skeyes Structural Inspection Drone

### Table of Contents

[Introduction](#introduction)<br>
[Installation](#installation)<br>
[Setup and Configuration](#setup-and-configruation)<br>

## Introduction

Conventional approaches to building inspection are laborious, costly, and dangerous. As it stands, an inspector has to
personally travel around any building he would like to inspect; furthermore, in the case of a particularly tall
building, he would have to be elevated to thoroughly survey the external surfaces of the structure. This process is
slow, expensive, and potentially dangerous. On the contrary, the use of an automated drone for such a task would be
faster, cheaper, safer, and more convenient for everyone involved. The drone will allow a user to plug a device into
their laptop and give the program some basic instructions, then receive a streamlined output of video data that they can
use in lieu of performing a manual inspection. The user will not have to physically move in order to investigate the
building for flaws, they can stay in one place and observe the process from a comfortable or convenient location. This
drone additionally makes the inspection of taller buildings more feasible, as the operator will not have to elevate
themselves in order to achieve a close investigation of the outer surfaces of the building. Additionally, any data that
is recorded by the drone can be conveniently stored and later accessed by the user. Ultimately, our goal with this
product is to reduce the risk, inconvenience, and potential overhead of having to perform a relatively simple task such
as a building inspection.

Building inspections have always been necessary, in almost any industry – nowadays, however, they are almost always
performed via the use of a drone. Conventional approaches to building inspection are laborious, costly, and dangerous.
Building inspectors may have to traverse obstructive or treacherous terrain, and as a result they may have to use
ladders, construction lifts, or even constructed scaffolding. All of these things have associated risks – they can take
long amounts of time, incur liabilities which companies have to insure, they can be dangerous for inspectors to use or
climb – sometimes there could simply not be enough space to bring in the necessary equipment. Using an inspection drone,
however, inspectors can acquire high-quality videos of buildings without endangering themselves or using any other
overhead. This solution offers the added benefit of being able to save the high-quality footage for later review.

Our project brings this idea to the next level. Often the drones that are used are manually controlled, meaning that the
operator must constantly be within line of sight and appropriate range of the drone. Our drone, however, is autonomous.
Using an integrated flight-controller software, our operator sets the flight path and sends the drone on its way, up and
around the building. A gimbal mounted on our drone stabilizes a camera, which records the nearby building and streams
the video data back to the ground control station. Within the ground control station, this video data is presented to
the operator; meanwhile, our two-stage feature analysis system is run in the background, identifying relevant features,
and highlighting them for the user. Identified objects, such as gutters and windows, are outlined in the video feed for
the operator to see, and a trained deep neural network identifies whether this specific feature is nominal or defective.
If a feature is determined to be nominal, the drone simply continues with its mission. If the feature is defective –
that is to say, a window is cracked or a gutter is clogged – the drone pauses its mission and waits for the user to
allow it to continue, storing its stabilized video footage.

The driving idea behind this drone is to bring an even more convenient and thorough approach to building inspection,
while developing a novel method of machine learning implementation. Our goal is to make an easily-operable, low-risk,
and sophisticated solution to the commonplace issue of building inspection.

## Installation

This following section will describe the installation of the skeyes structural inspection drone application. All
required dependencies will be detailed; however, optional dependencies will not be covered. Please note that the
directions are for and this application has only been tested on *nix systems. Other operating systems may exhibit
unexpected behaviors.

1. Open a terminal window
2. Clone the structural-drone repository from github with the command and change directory

```sh
git clone https://github.com/djcopley/structural-drone && cd structural-drone
```

3. Run the prerequisite installation script (this script will download and compile GStreamer and OpenCV with the
   GStreamer and Qt backend, and then install)

```sh
sh ./prereq-install.sh
```

4. Install the structural drone python package via the setup.py installation script

```sh
python3 setup.py install
```

5. Optionally, Install NVIDIA graphics drivers and the CUDA toolkit for hardware acceleration (outside the scope of this
   document)

## Setup and Configruation

The following section will describe tuning parameters, configuration, and use of the skeyes structural inspection drone
and application.

1. Preflight checklist 
   
   1.1 Propellers are tightly fastened 
   
   1.2 All devices are fastened securely (Especially battery and GPS)
   
   1.3 Make any hazards are clear of drone 
   
   1.4 Ensure that drone has GPS signal and connection to remote 
   
   1.5 Configure failsafes
   
2. Plug in usb telemetry radio to ground control station
3. Ensure ground control station is connected to GoPro wifi network
4. Run the “Skeyes” graphical application and wait for the user interface to appear
5. Launch QGroundControl

### Skeyes Software Configuration

***Main Menu***

The main screen contains a list of building features that the neural networks are trained to recognize. From this menu,
you can control the action taken by the drone when any of these features are detected damaged.

***Settings Menu***

Enable / Disable UDP Stream Checkbox

1. UDP IP Address 
   
    This option allows the user to enter an IP address to stream to. This will be the device where the
    processed video shows up.
   
2. UDP Port
   
    This option allows the user to enter a UDP port to stream to. Make sure this matches with the port setting
    in QGroundControl.

Enable / Disable File Logging

1. File Path 
   
    This option allows the user to specify a file path to save

***Known Issues***
Sometimes QGroundControl can interfere with the GoPro video stream. If the skeyes GUI fails to launch, start by quitting
both QGroundControl and the Skeyes application. Next make sure that the computer is connected to the GoPro wifi network.
Next, launch the skeyes application and wait for the graphical user interface to display. Finally, start QGroundControl.
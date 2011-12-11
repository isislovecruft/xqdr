# What is xqdr?
xqdr is an autonomous quadrocopter powered by Android and Arduino. The Android phone is not the remote controller, as is occasionally seen in other quadrocopter designs -- the Android phone is the brains of the copter, and as such it resides _on the copter itself_. This project is just getting out of the planning stage and into the development stage, but we do know what we want the robot to do, and we have a general idea of how we're getting there.

# How does it work?
An xqdr will be controlled by an Android app, which will control things like balance, where the copter is going or wants to go, and how it plans on getting there. This Android app will talk to Android Scripting Environment (ASE), which will in turn communicate serially though a hardwired cable (not Bluetooth!) to the Arduino, which will then control four Electronic Speed Controls (ESCs), which then throttle the servo motors. Whoo! That's a lot of things connected to thing that do things. 

# Why are you using an Android phone?
Because newer Android phones often have gyroscopes, accelerometers, cameras, light sensors, processors, and a whole bunch of other neat things that would actually cost more if we bought them all separately and connected them to the Arduino. Also, because "bricked" phones can be bought cheaply online, and which often aren't all too complicated to fix.

# What does "xqdr" mean?
xqdr is short for Xaosquopter, which is a portmanteau of a neologism ("xaos") and an ellision ("quadro" + "copter" --> "quopter"). xqdr is _always_ left uncapitalized, in homage to the webcomic xkcd. It is likewise unpronounceable.

# How do I get hold of the developers?
So far, there are two developers actively working on this project, [Isis Lovecruft](http://www.patternsinthevoid.net) and [Robby Kraft](http://polyto.pe). Isis can be contacted at isis(at)patternsinthevoid(dot)net and Robby at robbykraft(at)gmail(dot)com.

# Can I help?
Of course! You're welcome to fork our repo and make changes, but please keep in mind that we're trying to make this software work for the broadest range of hardware (i.e. models of Android phones) and platforms (AOSs) possible. Also, we could _really_ use help with frame design and 3D printing, because most of the quadrocopter frames out there cost bank (~$200) and we're trying to keep costs down.
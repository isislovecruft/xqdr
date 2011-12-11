XQDR Notes
==========

Android Scripting Environment can be used to run various languages
natively on an Android device (Ruby, Python, Java, Rhino (JS -> Java),
Lua (http://www.lua.org/about.html, I don't even know what that's for)).
Code for ASE is here:
<http://code.google.com/p/android-scripting/downloads/list>

MarineCompass is an Android app which gives roll, pitch, yaw, and
direcional heading. It's source code can be found here:
<http://svn.pierrox.net/mcompass/trunk/>

We will need to do Android (MicroUSB) -> USB -> serial. A way to do this
may be using Android Serial Port API.

- Will this work with Samsung Galaxy S running CM 7.1?
- <http://code.google.com/p/android-serialport-api/>

We will need to put Cyanogen on whatever phone we get:
<http://forum.cyanogenmod.com/topic/36540-cyanogenmod-doesnt-work-on-galaxy-sii/>

The other option, rather than using USB to serial, is to use Bluetooth.
Bluetooth shields for Arduinos are expensive, but there is a way to DIY
them:
<http://txapuzas.blogspot.com/2009/12/paperbluetooth-bluetooth-shield-para.html>

The phone will also need to run Amarino, which is an Android to Arduino
environment. Amarino has an API library that is a .jar file that I don't
really understand where it goes or what to do with it yet. Right now it is
at ~/Dev/robots/copter/AmarinoLibrary_v055.jar

- Where do I put this?
    - So far, I think the .jar file need to be included in any
Android Programs which are going to communicate with the Arduino.
    - The API guide for the Amarino Library's functions is online.
- To see the insides of the .jar file, do "mv <file>.jar <file>.zip
and then unzip it.
- Do I need to include this jar in programs that I write for the arduino?
    - I don't think so? I'm pretty sure it gets included in the Android
programs, not in the Arduino .pde files.

Documentation for this API library can be found here:
<http://www.amarino-toolkit.net/tl_files/doc/index.html>

Information about Amarino can be found here:
<http://www.amarino-toolkit.net/index.php/docs.html>

And you've already put the code on your personal phone, it's in the android
dev folder, under platform-tools/, and the install procedure was simply
> ./adb install <blahblahpackagename>

The arduino will need to be programmed to give good IO with processing,
http://www.arduino.cc/playground/interfacing/Processing
so that a python controller on the phone will say "i" with "i" defined in
a java/C library to mean "increase servo power +1", and the processing program
on the arduino will know that this means to increase the power to the servo.

It may also be useful to use the Arduino PID library, which is here:
<http://www.arduino.cc/playground/Code/PIDLibrary>

From Wikipedia:
> "A PID controller calculates an 'error' value as
> the difference between a measured [Input] and a desired setpoint.
> The controller attempts to minimize the error by adjusting [an
> Output]."

So, you tell the PID what to measure (the "Input",) Where you
want that measurement to be (the "Setpoint",) and the variable to
adjust that can make that happen (the "Output".) The PID then
adjusts the output trying to make the input equal the setpoint.

For reference, in a car, the Input, Setpoint, and Output would be
the speed, desired speed, and gas pedal angle respectively.

Here are some resources for pulling datasets from and calibrating
accelerometers: <http://code.google.com/p/quaduino-ng/wiki/TechResources>

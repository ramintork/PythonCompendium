Tire Pressure Kata
===================

You are working on software for a Formula 1 racing car. The car has a sensor that detects tire pressure while it is driving around the track. You are working on the back-end software used by the technicians at the side of the track. The tire pressure sensor class is already working, it has a method 'sample_pressure' which returns a number indicating the current tire pressure in PSI. This method makes an out-of-process call to the actual sensor in the moving racing car, and you can't call it from a unit test.

Unfortunately the racing car driver suspects there is a bug in the alarm class. If the pressure is exactly 17.0 PSI, or exactly 21.0 PSI, that should trigger the alarm, and it doesn't at present.

Write a test that exposes the bug - it should fail. If you fix the bug, the test should pass.

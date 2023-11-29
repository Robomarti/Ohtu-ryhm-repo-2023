Run Robotframework tests in root with run_robot_tests.sh.

Santtu: Weird bug when running robot tests; (Only without --headless, so works fine now) chrome starts running in background and eats up the CPU,
if I run the tests multiple times this becomes more severe and locks up my PC. Fixed by killing the chrome task in task manager,
I don't know if this is only on my PC or if it happens on everyones computers.

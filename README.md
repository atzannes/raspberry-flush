# raspberry-flush
Servo Motor Control with Raspberry Pi

Run `python flush.py` to perform a flush

Run `crontab -e` and add the following lines:

```
# 11:00am every Monday
0 11 * * 1     python /home/pi/src/raspberry-flush/flush.py

# 11:02am every Monday
2 11 * * 1     python /home/pi/src/raspberry-flush/flush.py
```

Run `PYTHONPATH=/home/pi/src/ python3 -m raspberry-flush.button`
to run the button-watching process that flushes when the button
is pressed

Run `crontab -e` and add the following line to run the button-watching
process on boot:

```
@reboot PYTHONPATH=/home/pi/src/ python3 -m raspberry-flush.button
```

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

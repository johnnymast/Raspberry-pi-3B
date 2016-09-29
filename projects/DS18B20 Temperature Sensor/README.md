Add to /boot/config.txt the following line and reboot before starting this sample....

```bash
dtoverlay=w1-gpio,gpiopin=4,pullup=on
```

Add the following lines to /etc/modules and reboot your raspberry

```bash
w1-gpio pullup=1
w1-therm
```

import time, os
import lcd_py
import RPi.GPIO as GPIO
#==========================
#by Muhammad Nabeel
lcd_py.lcd_init()
lcd_py.lcd_byte(lcd_py.LCD_LINE_1,lcd_py.LCD_CMD)
lcd_py.lcd_string("Distance Meas.",1)
time.sleep(1)

btn_sht=22

GPIO_TRIGGER = 31
GPIO_ECHO = 29
GPIO.cleanup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(btn_sht, GPIO.IN)
def distance():

    GPIO.output(GPIO_TRIGGER, True)
 

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
def Ser_data():
  while(1):
     dist = distance()
     lcd_py.lcd_byte(lcd_py.LCD_LINE_2,lcd_py.LCD_CMD)
     lcd_py.lcd_string(str(int(dist)) +" cm",1)
     if (GPIO.input(btn_sht) == False):
          time.sleep(2)
          lcd_py.lcd_init()
          lcd_py.lcd_byte(lcd_py.LCD_LINE_1,lcd_py.LCD_CMD)
          lcd_py.lcd_string("Shutting Down",1)
          time.sleep(2)
          lcd_py.lcd_init()
          os.system("sudo shutdown -h now")
     time.sleep(1)

#------------------------------------------------------
#------------------------------------------------------

def main():
    global k
    Ser_data()
if __name__ == '__main__':
  main()
  print 'm'

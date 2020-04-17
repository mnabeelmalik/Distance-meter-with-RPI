import time
import RPi.GPIO as GPIO
# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND
 
# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 12
LCD_D4 = 13
LCD_D5 = 15
LCD_D6 = 16
LCD_D7 = 18
 
# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
GPIO.cleanup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)       # Use Board GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD)#initialize
  lcd_byte(0x32,LCD_CMD)#initialize
  lcd_byte(0x28,LCD_CMD)#number of lines
  lcd_byte(0x0C,LCD_CMD)#cursor off
  lcd_byte(0x06,LCD_CMD)#cursor direction left
  lcd_byte(0x01,LCD_CMD)#clear disp
 
def lcd_string(message,sty):
  # Send string to display
  if (sty==1):
    message = message.center(LCD_WIDTH," ")
  elif (sty==2):
    message = message.ljust(LCD_WIDTH," ") 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
 
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(LCD_RS, mode) # RS
 
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10: # and with 16
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:  # and with 32
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40: # and with 64
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80: # and with 128
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
  
  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01: # and with 1
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02: # and with 2
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04: # and with 4
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08: # and with 8
    GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

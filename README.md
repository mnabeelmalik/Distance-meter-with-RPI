# Distance-meter-with-RPI

This is the project use to measure the distance by usign sr-04 ultrasonic sensor with SBC raspberrypi.


the pin mapping is Board.

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
 
# Define GPIO to LCD mapping with raspberry.
LCD_RS = 7
LCD_E  = 12
LCD_D4 = 13
LCD_D5 = 15
LCD_D6 = 16
LCD_D7 = 18
 

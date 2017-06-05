import pyupm_i2clcd as lcd

class LcdDisplay():

    color = [255, 0, 0]

    def __init__(self):
        self.myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
        self.myLcd.clear()
        self.myLcd.setColor(255, 0, 0)
    
    # displays text on screen
    def writeText(self, text):
        self.myLcd.write(text)
    
    # changing display color with fade effect
    def changeColor(self, r, g, b):
        changing_direction = [0, 0, 0]
        
        if r < self.color[0]: changing_direction[0] = 1
        elif r == self.color[0]: changing_direction[0] = 0
        else: changing_direction[0] = -1
        
        if g < self.color[1]: changing_direction[1] = 1
        elif g == self.color[1]: changing_direction[1] = 0
        else: changing_direction[1] = -1
        
        if b < self.color[2]: changing_direction[2] = 1
        elif b == self.color[2]: changing_direction[2] = 0
        else: changing_direction[2] = -1
        
        while not (r == self.color[0] and g == self.color[1] and b == self.color[2]):
            self.color[0] = self.color[0] - changing_direction[0]
            self.color[1] = self.color[1] - changing_direction[1]
            self.color[2] = self.color[2] - changing_direction[2]
            
            self.myLcd.setColor(self.color[0], self.color[1], self.color[2])
    
    # darken lcd display color
    def darken(self, value):
        self.changeColor(self.color[0] * value, self.color[1] * value, self.color[2] * value)
    
    # lighten lcd display color
    def lighten(self, value):
        self.darken(1 + value)
        
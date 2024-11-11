#Hunter STandifer
#temperatureconvert.py

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """Converts temperature values between Fahrenheit and Celsius."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title="Temperature Converter")
        
        # Labels for the fields
        self.addLabel(text="Degrees Fahrenheit", row=0, column=0)
        self.addLabel(text="Degrees Celsius", row=0, column=1)
        
        # Entry fields
        self.fahrField = self.addFloatField(value=32.0, row=1, column=0)
        self.celsField = self.addFloatField(value=0.0, row=1, column=1)
        
        # Buttons for conversion
        self.addButton(text=">>>>", row=2, column=0, command=self.fahrToCels)
        self.addButton(text="<<<<", row=2, column=1, command=self.celsToFahr)
        
    # Conversion methods
    def fahrToCels(self):
        """Converts Fahrenheit to Celsius."""
        fahrenheit = self.fahrField.getNumber()
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsField.setNumber(celsius)
        
    def celsToFahr(self):
        """Converts Celsius to Fahrenheit."""
        celsius = self.celsField.getNumber()
        fahrenheit = celsius * 9 / 5 + 32
        self.fahrField.setNumber(fahrenheit)

# Running the application
if __name__ == "__main__":
    TemperatureConverter().mainloop()

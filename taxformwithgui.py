#Hunter Standifer
#Taxformwithgui.py

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Takes the income and outputs the taxes owed"""
    def __init__(self):
        """Sets up window"""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Labels for the fields
        self.addLabel(text="Gross income", row=0, column=0)
        self.addLabel(text="Dependents", row=1, column=0)
        self.addLabel(text="Total Tax", row=2, column=0)

        # Entry Fields
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)
        self.dependentsField = self.addIntegerField(value=0, row=1, column=1)
        self.taxField = self.addTextField(text = "0.0", row=2, column=1, state="readonly")

        # The command button
        self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.computeTax)

    # The event handling method for the button
    def computeTax(self):
        """Inputs the income and number of dependents,
        computes the tax, and outputs the result"""
        TAX_RATE = 0.20
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0
        
        # Get values from input fields
        grossIncome = self.incomeField.getNumber()
        numDependents = self.dependentsField.getNumber()
        
        # Calculate taxable income and tax
        taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)
        incomeTax = taxableIncome * TAX_RATE
        incomeTax = max(incomeTax, 0)  # Ensure tax is not negative
        
        # Set the tax field with the computed tax rounded to 2 decimals
        self.taxField.setText(f"{round(incomeTax, 2):.2f}")

# Running the application
if __name__ == "__main__":
    TaxCalculator().mainloop()





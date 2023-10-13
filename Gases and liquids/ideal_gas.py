class BoyleLaw:
    
    def __init__(self, P1=None, V1=None, P2=None, V2=None):
        self.P1 = P1
        self.V1 = V1
        self.P2 = P2
        self.V2 = V2
    
    def calculate(self):
        # If P1, V1 and P2 are known -> calculate V2
        if self.P1 is not None and self.V1 is not None and self.P2 is not None and self.V2 is None:
            self.V2 = (self.P1 * self.V1) / self.P2
            return self.V2
        
        # If P1, V1 and V2 are known -> calculate P2
        elif self.P1 is not None and self.V1 is not None and self.P2 is None and self.V2 is not None:
            self.P2 = (self.P1 * self.V1) / self.V2
            return self.P2
        
        # If V1, P2 and V2 are known -> calculate P1
        elif self.P1 is None and self.V1 is not None and self.P2 is not None and self.V2 is not None:
            self.P1 = (self.P2 * self.V2) / self.V1
            return self.P1
        
        # If P1, P2 and V2 are known -> calculate V1
        elif self.P1 is not None and self.V1 is None and self.P2 is not None and self.V2 is not None:
            self.V1 = (self.P2 * self.V2) / self.P1
            return self.V1
        
        else:
            raise ValueError("Exactly three values must be provided to calculate the fourth.")


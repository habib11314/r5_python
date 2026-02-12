class PointPlan:
    abscisse: float
    ordonne: float

    def __init__(self, abscisse: float=None, ordonne: float=None):

        if(abscisse is not None and ordonne is  None):
            raise ValueError("Valeur de l'ordonnée manquante")
        if(abscisse is  None and ordonne is not None):
            raise ValueError("Valeur de l'abscisse manquante")
        if(abscisse is None and ordonne is None):
            self._abscisse = None
            self._ordonne = None
        
        self._abscisse = abscisse
        self._ordonne = ordonne

    def __str__ (self)->str:
        if(self.abscisse is None and self.ordonne is None):
            return f"abscisse=None, ordonne=None"
        return f"abscisse={self.abscisse}, ordonne={self.ordonne}"
        
    @classmethod
    def from_point(cls,original:'PointPlan')->'PointPlan':
        return cls(abscisse=original.abscisse, ordonne=original.ordonne)


    @property
    def abscisse(self)-> float| None:
        return self._abscisse
    
    @property
    def ordonne(self)-> float| None:
        return self._ordonne

    @abscisse.setter 
    def abscisse(self, a): 
        self._abscisse = a
    
    @ordonne.setter
    def ordonnee(self, ordonne):
        self._ordonne = ordonne


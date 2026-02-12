from points.point_plan import PointPlan

class Point3D(PointPlan):
    def __init__(self,abscisse:float =None ,ordonne:float=None,azimut:float=None):
        super().__init__(abscisse,ordonne)
        if (azimut is None):
            raise ValueError("Valeur de l'azimut manquante")    
        self.azimut=azimut
    
    @property
    def azimut(self)-> float:
        return self._azimut
    
    @azimut.setter
    def azimut(self,azimut:float):
        self._azimut=azimut
    
    def afficher(self)->None:
        print(f"Point Plan 3D : (abscisse: {self.abscisse}, ordonne: {self.ordonne}, azimut: {self.azimut})")
    
    #1  p.Point_Plan_3d()

    #2  p.afficher()

    #3  Point_Plan_3d.afficher(p)

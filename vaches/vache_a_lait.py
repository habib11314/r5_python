from vaches.vache import Vache


class Vache_a_lait(Vache):
    def __init__(self,lait_disponible:float=None,lait_total_produit:float=None,laitTotalTraite:float=None,petitNom: str=None, poids: float=None, age: int=None):
        self.lait_disponible=lait_disponible
        self.lait_total_produit=lait_total_produit
        self.lait_total_traite=lait_total_traite

        super().__init__(petitNom: str=None, poids: float=None, age: int=None)
        
    



@property
def lait_disponible(self) -> float:
    return self._lait_disponible

@lait_disponible.setter
def lait_disponible(self, value: float) -> None:
    if value is not None and value < 0.0:
        raise InvalidVacheException("La quantité de lait disponible ne peut pas être négative")
    self._lait_disponible = value
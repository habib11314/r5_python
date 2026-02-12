from Stragie.Protocol.RuminationStrategy import RuminationStrategy
from vaches.vache import Vache
from vaches.vache_a_lait import Vache_a_lait

class Pie_Noire_Milk(RuminationStrategy):

    def calculer_lait(self, vache: "Vache", panse_avant_rumination: float) -> float:
        if panse_avant_rumination <= 0.0: 
            raise InvalidVacheException("La panse avant rumination doit être positive")
        return  self.panse_avant_rumination*self._RENDEMENT_LAIT 

    def stocker_lait(self, vache:"Vache", volume_lait:float) -> None:
        if volume_lait < 0.0: raise InvalidVacheException("Le volume de lait produit ne peut pas être négatif")
        vache.lait_disponible += volume_lait
        vache.lait_total_produit += volume_lait


    def post_rumination(self, vache:"Vache") -> None:
        vache.lait_disponible +=vache.lait_total_produit

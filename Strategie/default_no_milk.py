from Stragie.Protocol.RuminationStrategy import RuminationStrategy
from vaches.vache import Vache

class DefaultNoMilk(RuminationStrategy):

    def calculer_lait(self, vache: "Vache", panse_avant_rumination: float) -> float:
        return 0.0

    def stocker_lait(self, vache:"Vache", volume_lait:float) -> None:
        return None

    def post_rumination(self, vache:"Vache") -> None:
        return None
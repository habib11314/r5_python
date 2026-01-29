import pytest
#    dossier.fichier          classe
from points.point_plan import PointPlan

def test_1():
    p=PointPlan()
    # Arrange
    p.abscisse=1
    # Assert
    assert p.abscisse==1

def test_should_raise_value_error_when_only_abscisse_is_provided():
    point = PointPlan()
    point.abscisse=5
    with pytest.raises(ValueError):
        point.__init__(abscisse=5)


def test_should_raise_value_error_when_only_ordonne_is_provided():
    point = PointPlan()
    point.ordonne=10
    with pytest.raises(ValueError):
        point.__init__(ordonne=10)
def test_should_initialize_with_no_arguments():
    point = PointPlan()
    assert point.abscisse is None

def test_should_initialize_with_abscisse_recupé():
    point=PointPlan(abscisse=3, ordonne=4)
    point.abscisse=7
    assert point.abscisse==7

def test_should_initialize_with_ordonne_recupé():
    point=PointPlan(abscisse=3, ordonne=4)
    point.ordonne=9
    assert point.ordonne==9

def test_should_initialize_with_abscisse_and_ordonne_and_check_values():
    point=PointPlan(abscisse=2, ordonne=8)
    assert point.abscisse==2

def test_should_initialize_with_copie_change():
    original=PointPlan(abscisse=5, ordonne=10)
    copie=PointPlan.from_point(original)
    copie.abscisse=15
    assert original.abscisse==5

def test_should_initialize_with_copie_same_values():
    original=PointPlan(abscisse=5, ordonne=10)
    copie=PointPlan.from_point(original)
    copie.ordonne=10
    assert copie.ordonne==10

def test_should_initialize_with_copie_are_none():
    original=PointPlan()
    copie=PointPlan.from_point(original)
    assert copie.abscisse is None


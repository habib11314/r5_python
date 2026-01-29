import pytest
from points.point_plan_3d import Point_Plan_3d
from points.point_plan import PointPlan

def test_point_plan_3d_initialization():
    p = Point_Plan_3d(abscisse=1.0, ordonne=2.0, azimut=3.0)
    assert p.azimut == 3.0

def test_should_raise_value_error_when_azimut_is_not_provided():
    
    p3d=Point_Plan_3d(abscisse=1.0, ordonne=2.0, azimut=3.0)
    p3d.azimut=None

    with pytest.raises(ValueError):
        Point_Plan_3d.__init__(p3d,abscisse=1.0, ordonne=2.0, azimut=None)
    
def test_point_plan_3d_modifier_azimut():
    p = Point_Plan_3d(abscisse=1.0, ordonne=2.0, azimut=3.0)
    p.azimut=30.0
    assert p.azimut == 30.0

def test_should_point_plan_3d_afficher():
    p = Point_Plan_3d(abscisse=1.0, ordonne=2.0, azimut=3.0)
    try:
        p.afficher()
    except Exception as e:
        pytest.fail(f"afficher method raised an exception: {e}")
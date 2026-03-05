from src.cot.models import Target


def test_target_has_lat_lon_description():
    target = Target(lat=34.0522, lon=-118.2437, description="Test target")
    assert target.lat == 34.0522
    assert target.lon == -118.2437
    assert target.description == "Test target"


def test_target_fields_are_typed():
    target = Target(lat=0.0, lon=0.0, description="")
    assert isinstance(target.lat, float)
    assert isinstance(target.lon, float)
    assert isinstance(target.description, str)

import xml.etree.ElementTree as ET

from src.cot.models import Target
from src.cot.builder import build_cot_xml


def test_build_cot_xml_returns_string():
    target = Target(lat=34.0522, lon=-118.2437, description="Enemy position")
    result = build_cot_xml(target)
    assert isinstance(result, str)


def test_build_cot_xml_is_valid_xml():
    target = Target(lat=34.0522, lon=-118.2437, description="Enemy position")
    result = build_cot_xml(target)
    root = ET.fromstring(result)  # raises if invalid XML
    assert root.tag == "event"


def test_build_cot_xml_contains_lat_lon():
    target = Target(lat=34.0522, lon=-118.2437, description="Enemy position")
    result = build_cot_xml(target)
    root = ET.fromstring(result)
    point = root.find("point")
    assert point is not None
    assert float(point.attrib["lat"]) == 34.0522
    assert float(point.attrib["lon"]) == -118.2437


def test_build_cot_xml_contains_description():
    target = Target(lat=34.0522, lon=-118.2437, description="Enemy position")
    result = build_cot_xml(target)
    root = ET.fromstring(result)
    remarks = root.find("detail/remarks")
    assert remarks is not None
    assert remarks.text == "Enemy position"

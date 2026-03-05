import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

from src.cot.models import Target


def build_cot_xml(target: Target) -> str:
    now = datetime.now(timezone.utc)
    stale = now + timedelta(minutes=10)
    fmt = "%Y-%m-%dT%H:%M:%S.%f"

    event = ET.Element("event", {
        "version": "2.0",
        "uid": str(uuid.uuid4()),
        "type": "a-h-G",
        "time": now.strftime(fmt) + "Z",
        "start": now.strftime(fmt) + "Z",
        "stale": stale.strftime(fmt) + "Z",
        "how": "m-g",
    })

    ET.SubElement(event, "point", {
        "lat": str(target.lat),
        "lon": str(target.lon),
        "hae": "0",
        "ce": "9999999",
        "le": "9999999",
    })

    detail = ET.SubElement(event, "detail")
    remarks = ET.SubElement(detail, "remarks")
    remarks.text = target.description

    return ET.tostring(event, encoding="unicode")

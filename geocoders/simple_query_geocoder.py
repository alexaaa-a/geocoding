from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        full_address = ''
        current_id = area_id

        while current_id is not None:
            area = API.get_area(current_id)
            full_address = f"{area.name}, {full_address}"
            current_id = area.parent_id

        return full_address.strip(", ")

OBJECT_TYPE = "teller"
GEO_SERVER_URL = "http://geoserver:8080/geoserver/wfs"
GEOMETRY = "found_at"
ATTRIBUTES = ["text", ]

RETURN = "feature_id"
CONVERSION_URL = "http://converter:5000/gml/"

SERVICER_URL = "http://servicer:5000"

ROUTING = {
    'db_pre_update': ['field_database']
}
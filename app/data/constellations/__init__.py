import os
import json

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

constellations = {}
constellation_data_files = ["constellations.json", "constellations.bounds.json", "constellations.lines.json"]

for constellation_data_file in constellation_data_files:
    with open(os.path.join(os.path.dirname(__file__), constellation_data_file)) as data_file_content:
        file_content_as_json = byteify(json.load(data_file_content))

    if constellation_data_file == "constellations.json":
        items = file_content_as_json["features"]
        for item in items:
            constellations[item["id"]] = {}
            constellations[item["id"]]["properties"] = item["properties"]
            constellations[item["id"]]["location"] = item["geometry"]

    else:
        items = file_content_as_json["features"]
        for item in items:
            if constellation_data_file == "constellations.bounds.json":
                constellations[item["id"]]["bounds"] = item["geometry"]
            else:
                constellations[item["id"]]["lines"] = item["geometry"]

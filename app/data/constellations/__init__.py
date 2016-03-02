import os
import json

''' source:
    http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python
    There's no built-in option to make the json module functions return byte strings instead of unicode strings.
    However, this short and simple recursive function will convert any decoded JSON object from using unicode
    strings to UTF-8-encoded byte strings:
'''


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )


def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )


def _byteify(data, ignore_dicts=False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [_byteify(item, ignore_dicts=True) for item in data]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data


constellations = {}
constellation_data_files = ["constellations.json", "constellations.bounds.json", "constellations.lines.json"]

for constellation_data_file in constellation_data_files:
    with open(os.path.join(os.path.dirname(__file__), constellation_data_file)) as data_file_content:
        # file_content_as_json = json_load_byteified(data_file_content)
        file_content_as_json = json.load(data_file_content)  # decided to go with the unicode

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

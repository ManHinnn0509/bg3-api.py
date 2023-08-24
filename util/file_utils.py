import json

from xml.dom import minidom

def read_xml_file(filepath: str):
    try:
        return minidom.parse(filepath)
    except:
        return None

def read_json_file(p: str, encoding="utf-8"):
    """
        Reads a json file's content from given path

        None will be returned if exception caught
    """
    try:
        with open(p, "r", encoding=encoding) as f:
            return json.load(f)
    except Exception as e:
        # print(e)
        return None

def write_json_file(p: str, d: dict):
    try:
        with open(p, 'w+', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False
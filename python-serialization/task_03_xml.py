#!/usr/bin/python3
'''
In this exercise we'll explore serialization
and deserialization using XML as an alternative format to JSON.
'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''
    This will take a Python dictionary and
    a filename as parameters. It should serialize
    the dictionary into XML and save it to the given filename.
    '''
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    '''
    This will take a filename as its parameter,
    read the XML data from that file,
    and return a deserialized Python dictionary.
    '''
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for child in root:
        result[child.tag] = child.text

    return result

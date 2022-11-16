import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

print(root.find('{http://maven.apache.org/POM/4.0.0}version').text)

import xml.dom.minidom
import argparse

def unescape_xml_string(xml_string):
    # problem chars from xml string 
    unescaped_content = xml_string.replace('\\"', '"').replace('\\n', '\n')
    return unescaped_content

def remove_whitespace_nodes(node, unlink=True):
    remove_list = []
    for child in node.childNodes:
        if child.nodeType == xml.dom.minidom.Node.TEXT_NODE and not child.data.strip():
            remove_list.append(child)
        elif child.hasChildNodes():
            remove_whitespace_nodes(child, unlink)
    for node in remove_list:
        node.parentNode.removeChild(node)
        if unlink:
            node.unlink() #omg i am working with memory now, am I a programmer?

def main(xml_data):
    xml_data = unescape_xml_string(xml_data)
    dom = xml.dom.minidom.parseString(xml_data)

    # Remove empty lines
    remove_whitespace_nodes(dom.documentElement)

    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process and pretty print XML from a string.')
    parser.add_argument('xml_string', type=str, help='XML string to be processed')
    
    args = parser.parse_args()
    
    main(args.xml_string)

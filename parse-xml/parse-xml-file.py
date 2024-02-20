import xml.dom.minidom
import argparse

def read_and_unescape_xml(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
 # problem chars from xml string 
    unescaped_content = content.replace('\\"', '"').replace('\\n', '\n')
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

def main(xml_file_path):
    xml_data = read_and_unescape_xml(xml_file_path)
    dom = xml.dom.minidom.parseString(xml_data)

    remove_whitespace_nodes(dom.documentElement)

    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process and pretty print XML from a file.')
    parser.add_argument('file_path', type=str, help='Path to the XML file to be processed')
    
    args = parser.parse_args()
    
    main(args.file_path)

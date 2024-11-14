import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_voc_annotation(filename, width, height, objects):
    """Creates a VOC annotation XML structure."""
    annotation = ET.Element("annotation")

    # Create and append filename element
    filename_elem = ET.SubElement(annotation, "filename")
    filename_elem.text = filename

    # Create and append size element
    size = ET.SubElement(annotation, "size")
    width_elem = ET.SubElement(size, "width")
    width_elem.text = str(width)
    height_elem = ET.SubElement(size, "height")
    height_elem.text = str(height)
    depth_elem = ET.SubElement(size, "depth")
    depth_elem.text = "3"  # assuming RGB images

    # Create and append object elements
    for obj in objects:
        obj_elem = ET.SubElement(annotation, "object")
        name_elem = ET.SubElement(obj_elem, "name")
        name_elem.text = obj["category"]

        bndbox = ET.SubElement(obj_elem, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(round(obj["bbox"][0]))
        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(round(obj["bbox"][1]))
        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(round(obj["bbox"][2]))
        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(round(obj["bbox"][3]))

    return annotation

def save_xml(annotation, output_path):
    """Saves the XML to file with pretty printing."""
    xml_str = minidom.parseString(ET.tostring(annotation)).toprettyxml(indent="   ")
    with open(output_path, "w") as f:
        f.write(xml_str)

def convert_jsonl_to_voc(jsonl_file, output_dir, text_folder_path, class_name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    all_name = []
    with open(jsonl_file, 'r') as file, open(os.path.join(text_folder_path, 'test.txt'), 'w') as test_file, open(os.path.join(text_folder_path, 'all_queries.txt'), 'w') as query_file:
        for line in file:
            data = json.loads(line)

            # Process primary annotation
            filename = f'TS{int(data["filename"].split(".")[0]):06}.xml'
            voc_filename = f'TS{int(data["filename"].split(".")[0]):06}.jpg'
            objects = [{"bbox": instance["bbox"], "category": class_name} for instance in data["detection"]["instances"]]
            annotation = create_voc_annotation(voc_filename, data["width"], data["height"], objects)
            save_xml(annotation, os.path.join(output_dir, filename))
            if filename not in all_name:
                test_file.write(f'{filename.split(".")[0]}\n')
                all_name.append(filename)

            # Process query_file annotation
            query_filename = f'QS{int(data["query_file"]["filename"].split(".")[0]):06}.xml'
            query_voc_filename = f'QS{int(data["query_file"]["filename"].split(".")[0]):06}.jpg'
            query_objects = [{"bbox": data["query_file"]["exemplar"][0], "category": class_name}]
            query_annotation = create_voc_annotation(query_voc_filename, data["query_file"]["width"], data["query_file"]["height"], query_objects)
            save_xml(query_annotation, os.path.join(output_dir, query_filename))
            if query_filename not in all_name:
                query_file.write(f'{query_filename.split(".")[0]}++{filename.split(".")[0]}++{data["query_file"]["category"]}\n')
                all_name.append(query_filename)

# Paths for input and output
jsonl_file_path = './val_filename.jsonl'
output_directory = './Annotations'
text_folder_path = './ImageSets/Main'

# Convert JSONL to VOC XML
convert_jsonl_to_voc(jsonl_file_path, output_directory, text_folder_path, class_name="V*BNFS")

import xml.etree.ElementTree as et

xml_path = "input.xml"

def _indent(elem, level=0):
	i = "\n" + level*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			_indent(elem, level+1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i

class ConvertXaml:

	def __init__(self, xml_path):
		self.xml_path = xml_path

	def _read_xml_str(self):
		file_xml = open(self.xml_path, "r")
		file_con = file_xml.readlines()
		file_str = "".join(file_con)   \
			.replace("x:Name", "Name") \
			.replace("DynamicResource", "StaticResource")
		# print file_str
		file_xml.close()
		return file_str

	def _convert_model3dgroup(self, root, child):
		# InteractivelModeVisual3D.Model
		inter_3d                      = et.SubElement(root,"InteractivelModeVisual3D")
		if "_04_C_" in child.attrib["Name"]:
			inter_3d.attrib["Tag"]        = child.attrib["Name"][:8].strip("_").replace("_", "-")
		else:
			inter_3d.attrib["Tag"]        = child.attrib["Name"]
		inter_3d.attrib["Name"]       = "Name" + child.attrib["Name"]
		inter_3d.attrib["MouseDown"]  = "OnMouseDownMachineFront"
		inter_3d.attrib["MouseEnter"] = "OnMouseEnterMachineFront"
		inter_3d.attrib["MouseLeave"] = "OnMouseLeaveMachineFront"
		inter_model                   = et.SubElement(inter_3d, "InteractivelModeVisual3D.Model")
		inter_model.append(child)
		# print et.tostring(inter_3d)

	def _convert_geometrymodel3d(self, root, child):
		inter_3d       = et.SubElement(root,"InteractivelModeVisual3D")
		inter_model    = et.SubElement(inter_3d, "InteractivelModeVisual3D.Model")
		model_3d_group = et.SubElement(inter_model, "Model3DGroup")
		model_3d_group.append(child)
		# print et.tostring(inter_3d)

	def _write_xml_str(self, xml_str):
		file_xml = open("output.xml", "w")
		file_con = file_xml.write(xml_str)
		file_xml.close()

	def _convert_all(self):
		tree = et.fromstring(self._read_xml_str())
		root = et.Element("Model3DGroup")

		root.attrib["Name"] = tree.attrib["Name"]
		root.attrib["Transform"] = tree.attrib["Transform"]
		
		for child in tree:
			if "Model3DGroup" == child.tag:
				self._convert_model3dgroup(root, child)
			if "GeometryModel3D" == child.tag:
				self._convert_geometrymodel3d(root, child)
		_indent(root, 0)
		xml_str = et.tostring(root)    \
			.replace("Name=", "x:Name=") \
			.replace("InteractivelModeVisual3D", "local:InteractivelModeVisual3D")
		self._write_xml_str(xml_str) 
		# print xml_str

convert = ConvertXaml(xml_path)
convert._convert_all()
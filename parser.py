import jinja2
import xml.etree.ElementTree as ET

tree = ET.parse('lomax.xml')
root = tree.getroot()

templateLoader = jinja2.FileSystemLoader(searchpath="./tpl/")
templateEnv = jinja2.Environment(loader=templateLoader)
t = templateEnv.get_template("simple_html.tpl")
print(t.render(root=root))

import jinja2
import xml.etree.ElementTree as ET
import yaml

tree = ET.parse('lomax.xml')
root = tree.getroot()

config = yaml.safe_load(open('config.yml', 'r'))

def score_element(xmlEl, conf):
    score = 0
    type = xmlEl.get('type')
    type = "" if type is None else type
    tags = xmlEl.get('tags')
    tags = "" if tags is None else tags.split(",")
    priorities = conf["priorities"]
    for tag in priorities:
        if xmlEl.get('type') == tag or tag in tags:
            score += priorities[tag]
    return score

def prioritize(xmlList, tagType, conf):
    limits = conf["limits"]
    limit = -1
    if tagType in limits:
        limit = limits[tagType] 
    xmlList = [xmlEl for xmlEl in xmlList]
    xmlList = sorted(xmlList, key=lambda el: -score_element(el, conf))
    if limit > 0:
        xmlList = xmlList[0:limit]
    return xmlList

templateLoader = jinja2.FileSystemLoader(searchpath="./tpl/")
templateEnv = jinja2.Environment(loader=templateLoader)
t = templateEnv.get_template("simple_html.tpl")
print(t.render(resume=root, conf=config, prioritize=lambda x, tt: prioritize(x, tt, config)))

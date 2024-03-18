import jinja2
import sys
import xml.etree.ElementTree as ET
import yaml

RESUME_DATA = sys.argv[1]
RESUME_CONFIG = sys.argv[2]
RESUME_TEMPLATE = sys.argv[3]

tree = ET.parse(open(RESUME_DATA, 'r'))
root = tree.getroot()

config = yaml.safe_load(open(RESUME_CONFIG, 'r'))

def score_element(xml_el, conf):
    score = 0
    type = xml_el.get('tag')
    tags = xml_el.get('tags')
    tags = "" if tags is None else tags.split(",")
    priorities = conf["priorities"]
    if priorities is not None:
        for tag in priorities:
            if type == tag or tag in tags:
                score += priorities[tag]
    return score

def prioritize(xml_list, tag_type, conf):
    limits = conf["limits"]
    limit = -1
    if limits is not None and tag_type in limits:
        limit = limits[tag_type] 
    xml_list = [xml_el for xml_el in xml_list]
    xml_list = sorted(xml_list, key=lambda el: -score_element(el, conf))
    if limit > 0:
        xml_list = xml_list[0:limit]
    return xml_list

def date_format(datelike):
    d = datelike.get('day')
    m = datelike.get('month')
    y = datelike.get('year')
    dstring = ""
    if m is not None:
        dstring = m
        if d is not None:
            dstring = f"{m} {d},"
    dstring = dstring + f" {y}"
    return dstring

def daterange_format(dfrom, dto):
    if dto is None:
        return f"{date_format(dfrom)} - present"
    else:
        return f"{date_format(dfrom)} - {date_format(dto)}"

helpers = {
    "prioritize": lambda x, tt: prioritize(x, tt, config),
    "date": date_format,
    "daterange": daterange_format 
}

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
t = templateEnv.get_template(RESUME_TEMPLATE)
print(t.render(resume=root, conf=config, **helpers))

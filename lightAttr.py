import maya.cmds as cmds
import common.yaml as yaml

lights = cmds.ls(type='light')

lig_dict = {}

for lig in lights:
    attr_list = cmds.listAttr(lig)
    attr_dict = {}
    for a in attr_list:
        attr_node = '%s.%s' % (lig, a)

        try:
            attr = cmds.getAttr('%s' % attr_node)
        except RuntimeError:
            attr = None
        except ValueError:
            pass

        attr_dict[a] = attr

    lig_dict[lig] = attr_dict

yamlFile = '/Users/macintosh/Library/Preferences/Autodesk/maya/2017/ligAttrivute.yaml'

stream = file(yamlFile, 'w')
yaml.dump(lig_dict, stream, default_flow_style=False)

stream = file(yamlFile, 'r')
doc = yaml.load(stream)

lights = cmds.ls(type='light')

for lig in lights:
    for a in doc[lig]:
        attr = '%s.%s' % (lig, a)
        print
        attr, doc[lig][a]
        try:
            cmds.setAttr(attr, doc[lig][att])
        except Exception:
            pass




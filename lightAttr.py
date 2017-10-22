import maya.cmds as cmds
import common.yaml as yaml


class LightAttr():
    def __init__(self, parent=None):
        super(LightAttr,self).__init__()

    def getLightAttr(self):
        lights = cmds.ls(type='light')

        self.lig_dict = {}

        for lig in lights:
            attr_list = cmds.listAttr(lig)
            attr_dict = {}
            for a in attr_list:
                attr_node = '%s.%s' % (lig, a)

                try:
                    attr = cmds.getAttr('%s' % attr_node)
                except RuntimeError or ValueError:
                    attr = None

                attr_dict[a] = attr

            self.lig_dict[lig] = attr_dict

    def dump_attr(self):
        yamlFile = '/Users/macintosh/Library/Preferences/Autodesk/maya/2017/ligAttribute.yaml'

        stream = file(yamlFile, 'w')
        yaml.dump(self.lig_dict, stream, default_flow_style=False)

    def load_attr(self):
        stream = file(yamlFile, 'r')
        self.doc = yaml.load(stream)

    def setLightAttr(self):
        lights = cmds.ls(type='light')

        for lig in lights:
            for a in self.doc[lig]:
                attr = '%s.%s' % (lig, a)
                try:
                    cmds.setAttr(attr, self.doc[lig][att])
                except Exception:
                    pass




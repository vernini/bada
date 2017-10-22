import maya.cmds as cmds
import common.yaml as yaml

yamlFile = '/Users/macintosh/Library/Preferences/Autodesk/maya/2017/ligAttribute.yaml'

class LightAttr():
    def __init__(self):
        if cmds.window('lightTransfer', exists=True):
            cmds.deleteUI('lightTransfer')
        myWindow=cmds.window('lightTransfer',t='Light Transfer',h=400,w=200)

        cmds.columnLayout(adj=True)
        cmds.button(label='Get Light Attribute',command=self.getLightAttr)
        cmds.button(label='Dump Light Attribute',command=self.dump_attr)
        cmds.button(label='Load Light Attribute',command=self.load_attr)
        cmds.button(label='Set Light Attribute',command=self.setLightAttr)
        cmds.showWindow(myWindow)

    def getLightAttr(self,*args):
        lights = cmds.ls(type='light')

        self.lig_dict = {}

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
                    attr = None

                attr_dict[a] = attr

            self.lig_dict[lig] = attr_dict



    def dump_attr(self,*args):

        stream = file(yamlFile, 'w')
        yaml.dump(self.lig_dict, stream, default_flow_style=False)

    def load_attr(self, *args):
        stream = file(yamlFile, 'r')
        self.doc = yaml.load(stream)

    def setLightAttr(self, *args):
        lights = cmds.ls(type='light')

        for lig in lights:
            for a in self.doc[lig]:
                attr = '%s.%s' % (lig, a)
                try:
                    cmds.setAttr(attr, self.doc[lig][a])
                except Exception:
                    pass




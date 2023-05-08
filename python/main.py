import maya.cmds as cmds

def drawingOverrides():
    models = cmds.ls('*:*:model_GRP') #subject to rig structure, to be substitued for needed node
    for m in models:
        cmds.select(m)
        cmds.setAttr((m + '.overrideEnabled'), 0) #if set to 1, turns on drawing overrides

drawingOverrides()
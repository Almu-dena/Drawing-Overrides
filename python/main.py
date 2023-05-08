import maya.cmds as cmds


asset = '*:*:model_GRP' #subject to studio convention rig structure, to be substituted for needed asset
def drawingOverrides():
    models = cmds.ls(asset)
    for m in models:
        cmds.select(m)
        cmds.setAttr((m + '.overrideEnabled'), 0) #if set to 1, turns on drawing overrides

drawingOverrides()
import maya.cmds as cmds

'''
Script is subject to studio convention, substitute value of asset variable for the
corresponding rig structure needed
'''

asset = '*:*:model_GRP'
def drawingOverrides():
    """
    Function that selects all assets with the convention of the variable and unchecks
    drawingOverrides inside the display attribute for each
    """

    models = cmds.ls(asset)
    for m in models:
        cmds.select(m)
        cmds.setAttr((m + '.overrideEnabled'), 0) #if set to 1, turns on drawing overrides

drawingOverrides()
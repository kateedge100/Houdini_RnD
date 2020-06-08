import re
import hou

def scene_name_check():
    sceneName = hou.hipFile.basename()
   
    # Naming convention - a_b_c_v1.hipnc
    pattern = re.compile("([a-zA-Z]+_)+v[0-9]+.(hipnc|hip)")
    match = pattern.match(sceneName)
   
    if not match:
        raise ValueError('Scene name does not match naming convention')
       

def version_scene():
   
    # Check scene name fits the naming convention
    scene_name_check()
   
    sceneName = hou.hipFile.basename().split('.')[0]
   
    # Save scene
    hou.hipFile.save()
   
    version = sceneName.split('_')[-1].replace('v','')
    updatedVersion = int(version) + 1
   
    versionedSceneName = sceneName.replace(version, str(updatedVersion))
   
    updatedPath = hou.hipFile.path().replace(sceneName, versionedSceneName)
       
    # Version scene
    hou.hipFile.save(file_name=updatedPath)
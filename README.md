# Houdini_RnD
A collection of personal Houdini tools and scripts

## Setup
To setup add the following lines to your houdini.env file

```
HOUDINI_RND = "/path/to/Houdini_RnD"
HOUDINI_PATH = "$HOUDINI_PATH:$HOUDINI_RND"
PYTHONPATH = "$PATH:$HOUDINI_RND/scripts"
```

## Houdini Tips and Tricks
Documentation on various aspects of Houdini can be found under [docs](/docs). 

## Shelf Tools

### Version Scene
Versions a scene following the naming conventions *scene_name_v1.hip*

## OTLS

### TOP Cache
Setup to cache SOP geo using TOPS and read the files back in through a file node.
# SPDX-License-Identifier: GPL-2.0-or-later

# <pep8-80 compliant>

__author__ = "Nutti <nutti.metro@gmail.com>"
__status__ = "production"
__version__ = "6.6"
__date__ = "22 Apr 2022"


bl_info = {
    "name": "Magic UV",
    "author": "Nutti, Mifth, Jace Priester, kgeogeo, mem, imdjs, "
              "Keith (Wahooney) Boshoff, McBuff, MaxRobinot, "
              "Alexander Milovsky, Dusan Stevanovic, MatthiasThDs, "
              "theCryingMan, PratikBorhade302",
    "version": (6, 6, 0),
    "blender": (2, 80, 0),
    "location": "See Add-ons Preferences",
    "description": "UV Toolset. See Add-ons Preferences for details",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "{BLENDER_MANUAL_URL}/addons/uv/magic_uv.html",
    "tracker_url": "https://github.com/nutti/Magic-UV",
    "category": "UV",
}


if "bpy" in locals():
    import importlib
    importlib.reload(common)
    importlib.reload(utils)
    utils.bl_class_registry.BlClassRegistry.cleanup()
    importlib.reload(op)
    importlib.reload(ui)
    importlib.reload(properties)
    importlib.reload(preferences)
else:
    import bpy
    from . import common
    from . import utils
    from . import op
    from . import ui
    from . import properties
    from . import preferences

import bpy


def register():
    utils.bl_class_registry.BlClassRegistry.register()
    properties.init_props(bpy.types.Scene)
    user_prefs = utils.compatibility.get_user_preferences(bpy.context)
    if user_prefs.addons['magic_uv'].preferences.enable_builtin_menu:
        preferences.add_builtin_menu()


def unregister():
    preferences.remove_builtin_menu()
    properties.clear_props(bpy.types.Scene)
    utils.bl_class_registry.BlClassRegistry.unregister()


if __name__ == "__main__":
    register()

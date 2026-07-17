from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

# FIXME Add option_presets
from .options import option_groups#, option_presets


class BATIMWebWorld(WebWorld):
    game = "Bendy and the Ink Machine"

    # You can choose between dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "grassFlowers" #FIXME Choose a theme

    setup_en = Tutorial(
        "Multiworld Setup Guide", # Title
        "A guide to setting up Bendy and the Ink Machine for MultiWorld.", # Description
        "English", # Language
        "setup_en.md", # File Path
        "setup/en", # Link
        ["Lorecrafter703"], # Authors
    )

    tutorials = [setup_en]

    # FIXME ADD option presets
    option_groups = option_groups
    #options_presets = option_presets

from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

# FIXME Add Options
# # The first type of Option we'll discuss is the Toggle.
# # A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# # The default for a toggle is "off".
# # If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.
# class HardMode(Toggle):
#     """
#     In hard mode, the basic enemy and the final boss will have more health.
#     The Health Upgrades become progression, as they are now required to beat the final boss.
#     """
#
#     # The docstring of an option is used as the description on the website and in the template yaml.
#
#     # You'll also want to set a display name, which will determine what the option is called on the website.
#     display_name = "Hard Mode"
#
#
# # A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
# class ConfettiExplosiveness(Range):
#     """
#     How much confetti each use of a confetti cannon will fire.
#     """
#
#     display_name = "Confetti Explosiveness"
#
#     range_start = 0
#     range_end = 10
#
#     # Range options must define an explicit default value.
#     default = 3
#
#
# # A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
# class PlayerSprite(Choice):
#     """
#     The sprite that the player will have.
#     """
#
#     display_name = "Player Sprite"
#
#     option_human = 0
#     option_duck = 1
#     option_horse = 2
#     option_cat = 3
#
#     # Choice options must define an explicit default value.
#     default = option_human
#
#     # For choices, you can also define aliases.
#     # For example, we could make it so "player_sprite: kitty" resolves to "player_sprite: cat" like this:
#     alias_kitty = option_cat

class StartingChapter(Choice):
    """
    The first chapter you will have unlocked.
    """
    display_name = "Starting Chapter"
    option_one = 0
    option_two = 1
    option_three = 2
    option_four = 3
    default_option = option_one


class TotalBaconSoups(Range):
    """
    The total number of Bacon Soups included in the world
    """
    display_name = "Total Bacon Soups"
    range_start = 0
    range_end = 117
    default_option = 40


class BaconSoupsRequired(Range):
    """
    What percentage of the total Bacon Soups will be required to begin Chapter 5
    """
    display_name = "Bacon Soups Required"
    range_start = 0
    range_end = 100
    default_option = 75


class MinigameSanity(Toggle):
    """
    Getting perfect scores on the three minigames in the Storage 9 warehouse sends checks
    """
    display_name = "Minigame Sanity"


class TheMeatlySanity(Toggle):
    """
    Finding hidden theMeatly cutouts sends checks
    """
    display_name = "theMeatly Sanity"


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class BATIMOptions(PerGameCommonOptions):
    starting_chapter: StartingChapter
    total_bacon_soups: TotalBaconSoups
    bacon_soups_required: BaconSoupsRequired
    minigame_sanity: MinigameSanity
    the_meatly_sanity: TheMeatlySanity


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Basic Configurations",
        [StartingChapter, TotalBaconSoups, BaconSoupsRequired],
    ),
    OptionGroup(
        "Sanity Options",
        [MinigameSanity, TheMeatlySanity],
    ),
]

# FIXME Presets
# # Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
# option_presets = {
#     "boring": {
#         "hard_mode": False,
#         "hammer": False,
#         "extra_starting_chest": False,
#         "start_with_one_confetti_cannon": False,
#         "trap_chance": 0,
#         "confetti_explosiveness": ConfettiExplosiveness.range_start,
#         "player_sprite": PlayerSprite.option_human,
#     },
#     "the true way to play": {
#         "hard_mode": True,
#         "hammer": True,
#         "extra_starting_chest": True,
#         "start_with_one_confetti_cannon": True,
#         "trap_chance": 50,
#         "confetti_explosiveness": ConfettiExplosiveness.range_end,
#         "player_sprite": PlayerSprite.option_duck,
#     },
# }

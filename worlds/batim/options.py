from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md

class StartingChapter(Choice):
    """
    The first chapter you will have unlocked.
    """
    display_name = "Starting Chapter"
    option_one = 0
    option_two = 1
    option_three = 2
    option_four = 3
    option_five = 4
    default = option_one


class TotalBaconSoups(Range):
    """
    The total number of Bacon Soups included in the world.
    """
    display_name = "Total Bacon Soups"
    range_start = 0
    range_end = 117
    default = 40


class BaconSoupsRequired(Range):
    """
    What percentage of the total Bacon Soups will be required to begin Chapter 5.
    """
    display_name = "Bacon Soups Required"
    range_start = 0
    range_end = 100
    default = 75


class MinigameSanity(Toggle):
    """
    Getting perfect scores on the three minigames in the Storage 9 warehouse sends checks.
    """
    display_name = "Minigame Sanity"


class TheMeatlySanity(Toggle):
    """
    Finding hidden theMeatly cutouts sends checks.
    """
    display_name = "theMeatly Sanity"


class CheckpointSanity(Toggle):
    """
    Randomizes Checkpoints into the item pool. Reaching the areas that would typically unlock checkpoints instead will send a check.
    """
    display_name = "Checkpoint Sanity"


@dataclass
class BATIMOptions(PerGameCommonOptions):
    starting_chapter: StartingChapter
    total_bacon_soups: TotalBaconSoups
    bacon_soups_required: BaconSoupsRequired
    minigame_sanity: MinigameSanity
    the_meatly_sanity: TheMeatlySanity
    checkpoint_sanity: CheckpointSanity


option_groups = [
    OptionGroup(
        "Basic Configurations",
        [StartingChapter, TotalBaconSoups, BaconSoupsRequired],
    ),
    OptionGroup(
        "Sanity Options",
        [MinigameSanity, TheMeatlySanity, CheckpointSanity],
    ),
]

option_presets = {
    "default": {
        "starting_chapter": StartingChapter.option_one,
        "total_bacon_soups": 40,
        "bacon_soups_required": 75,
        "minigame_sanity": False,
        "the_meatly_sanity": False,
        "checkpoint_sanity": False,
    },
    "insanity": {
        "starting_chapter": "random",
        "total_bacon_soups": 40,
        "bacon_soups_required": 75,
        "minigame_sanity": True,
        "the_meatly_sanity": True,
        "checkpoint_sanity": True,
    },
    "bk simulator": {
        "starting_chapter": StartingChapter.option_four,
        "total_bacon_soups": 117,
        "bacon_soups_required": 100,
        "minigame_sanity": True,
        "the_meatly_sanity": True,
        "checkpoint_sanity": True,
    },
    "all random": {
        "starting_chapter": "random",
        "total_bacon_soups": "random",
        "bacon_soups_required": "random",
        "minigame_sanity": "random",
        "the_meatly_sanity": "random",
        "checkpoint_sanity": "random",
    },
}

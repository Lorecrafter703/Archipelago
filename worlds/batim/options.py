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


class GoalChapter(Choice):
    """
    The chapter to be used as a goal.
    """
    display_name = "Goal Chapter"
    option_one = 0
    option_two = 1
    option_three = 2
    option_four = 3
    option_five = 4
    default = option_five


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


class IncludeLaterChapters(Toggle):
    """
    If this option is disabled, chapters after the goal chapter
    will not be included in the randomization.
    """
    display_name = "Include Later Chapters"


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


class IncludeTommyGun(Toggle):
    """
    When this option is enabled, completing the steps to obtain the Tommy Gun will send a check. The tommy gun will not
    be obtainable however, unless the CH3 Tommy Gun item has been received, at which point the Tommy Gun will become
    permanently obtainable, regardless of other factors.
    """
    display_name = "IncludeTommyGun"


class IncludeLeverChallenges(Toggle):
    """
    Completing each of the three Lever challenges will send a check. Lever challenges are accessed as usual, by choosing
    the Angel Path, setting the ink to Boris, and completing Angel's tasks up until defeating the Butcher gang without
    dying. These conditions are initially satisfied upon loading into any checkpoint after the path decision point.
    """
    display_name = "IncludeLeverChallenges"


@dataclass
class BATIMOptions(PerGameCommonOptions):
    starting_chapter: StartingChapter
    goal_chapter: GoalChapter
    include_later_chapters: IncludeLaterChapters
    total_bacon_soups: TotalBaconSoups
    bacon_soups_required: BaconSoupsRequired
    minigame_sanity: MinigameSanity
    the_meatly_sanity: TheMeatlySanity
    checkpoint_sanity: CheckpointSanity
    include_tommy_gun: IncludeTommyGun
    include_lever_challenges: IncludeLeverChallenges


option_groups = [
    OptionGroup(
        "Basic Configurations",
        [StartingChapter, GoalChapter, IncludeLaterChapters, TotalBaconSoups, BaconSoupsRequired],
    ),
    OptionGroup(
        "Sanity Options",
        [MinigameSanity, TheMeatlySanity, CheckpointSanity, IncludeTommyGun, IncludeLeverChallenges],
    ),
]

option_presets = {
    "default": {
        "starting_chapter": StartingChapter.default,
        "goal_chapter": GoalChapter.default,
        "include_later_chapters": False,
        "total_bacon_soups": 40,
        "bacon_soups_required": 75,
        "minigame_sanity": False,
        "the_meatly_sanity": False,
        "checkpoint_sanity": False,
        "include_tommy_gun": False,
        "include_lever_challenges": False,
    },
    "insanity": {
        "starting_chapter": "random",
        "goal_chapter": "random",
        "include_later_chapters": True,
        "total_bacon_soups": 117,
        "bacon_soups_required": 100,
        "minigame_sanity": True,
        "the_meatly_sanity": True,
        "checkpoint_sanity": True,
        "include_tommy_gun": False,
        "include_lever_challenges": True,
    },
    "bk simulator": {
        "starting_chapter": StartingChapter.option_four,
        "goal_chapter": GoalChapter.default,
        "include_later_chapters": True,
        "total_bacon_soups": 117,
        "bacon_soups_required": 100,
        "minigame_sanity": True,
        "the_meatly_sanity": True,
        "checkpoint_sanity": True,
        "include_tommy_gun": True,
        "include_lever_challenges": True,
    },
    "all random": {
        "starting_chapter": "random",
        "goal_chapter": "random",
        "include_later_chapters": "random",
        "total_bacon_soups": "random",
        "bacon_soups_required": "random",
        "minigame_sanity": "random",
        "the_meatly_sanity": "random",
        "checkpoint_sanity": "random",
        "include_tommy_gun": "random",
        "include_lever_challenges": "random",
    },
    "speedrun": {
        "starting_chapter": StartingChapter.option_one,
        "goal_chapter": GoalChapter.option_one,
        "include_later_chapters": False,
        "total_bacon_soups": 117,
        "bacon_soups_required": 1,
        "minigame_sanity": False,
        "the_meatly_sanity": False,
        "checkpoint_sanity": True,
        "include_tommy_gun": False,
        "include_lever_challenges": False,
    }
}


def resolve_option_conflicts(world) -> None:
    # Correct Yaml Options
    starting_chapter = int(world.options.starting_chapter)
    bacon_soups_total = int(world.options.total_bacon_soups)
    cumulative_bacon_soups = [21, 52, 91, 110, 117]
    if not world.options.include_later_chapters:
        last_chapter = int(world.options.goal_chapter)
        starting_chapter = 0 if starting_chapter > last_chapter else starting_chapter
        world.options.starting_chapter = StartingChapter(starting_chapter)
        bacon_soups_total = min(bacon_soups_total, cumulative_bacon_soups[last_chapter])
        world.options.total_bacon_soups = TotalBaconSoups(bacon_soups_total)

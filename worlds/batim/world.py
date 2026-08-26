import settings

from settings import FilePath
from collections.abc import Mapping
from typing import Any, Union, ClassVar, Dict
from rule_builder.cached_world import CachedRuleBuilderWorld
# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as batim_options  # rename due to a name conflict with World.options

# Universal Tracker credit to notrainbowsteve on discord
class UTPackPath(FilePath):
    required = False

class BATIMSettings(settings.Group):
    ut_pack_path: Union[UTPackPath, str] = UTPackPath()

class BATIMWorld(World):
    """
    Bendy and the Ink Machine is a first-person puzzle horror game where Henry returns to Joey Drew Studios to find
    it overrun by monstrous cartoon characters brought to life by the Ink Machine. As he navigates the haunted studio,
    Henry must solve puzzles and uncover dark secrets through audio recordings and clues. The game combines horror with
    nostalgia for classic cartoons, creating a unique and eerie experience.
    """

    game = "Bendy and the Ink Machine"
    web = web_world.BATIMWebWorld()
    options_dataclass = batim_options.BATIMOptions
    options: batim_options.BATIMOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.

    # Universal Tracker credit to notrainbowsteve on discord
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    ut_can_gen_without_yaml = True

    settings_key = "batim_settings"
    settings: ClassVar[BATIMSettings]

    tracker_world: ClassVar = {
        "external_pack_key": "ut_pack_path",
        "map_page_maps": ["maps/maps.json"],
        "map_page_locations": ["locations/ch1_audio.json", "locations/ch1_bacon.json", "locations/ch1_items.json", "locations/ch2_audio.json", "locations/ch2_bacon.json", "locations/ch2_items.json", "locations/ch3_audio.json", "locations/ch3_bacon.json", "locations/ch3_items.json", "locations/ch4_audio.json", "locations/ch4_bacon.json", "locations/ch4_items.json", "locations/ch5_audio.json", "locations/ch5_bacon.json", "locations/ch5_items.json", "locations/misc.json"],
        "map_page_layouts": ["layouts/tabs.json"],
    }

    def generate_early(self) -> None:
        batim_options.resolve_option_conflicts(self)


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)


    def set_rules(self) -> None:
        rules.set_all_rules(self)


    def create_items(self) -> None:
        items.create_all_items(self)


    def create_item(self, name: str) -> items.BATIMItem:
        return items.create_item_with_correct_classification(self, name)


    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "starting_chapter",
            "goal_chapter",
            "include_later_chapters",
            "require_previous_chapters",
            "total_bacon_soups",
            "bacon_soups_required",
            "death_link",
            "minigame_sanity",
            "the_meatly_sanity",
            "checkpoint_sanity",
            "include_tommy_gun",
            "include_lever_challenges",
            "boris_bone",
        )

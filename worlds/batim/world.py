from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as batim_options  # rename due to a name conflict with World.options


class BATIMWorld(World):
    """
    Bendy and the Ink Machine is a first-person puzzle horror game where Henry returns to Joey Drew Studios to find
    it overrun by monstrous cartoon characters brought to life by the Ink Machine. As he navigates the haunted studio,
    Henry must solve puzzles and uncover dark secrets through audio recordings and clues. The game combines horror with
    nostalgia for classic cartoons, creating a unique and eerie experience.
    """

    game = "Bendy and the Ink Machine"
    web = web_world.BATIMWebWorld() #FIXME
    options_dataclass = batim_options.BATIMOptions
    options: batim_options.BATIMOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Archives Hub"


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
            "total_bacon_soups",
            "bacon_soups_required",
            "minigame_sanity",
            "the_meatly_sanity",
        )

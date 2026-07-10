from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BATIMWorld

ITEM_NAME_TO_ID = {
    "Bacon Soup": 1,
    "CH1 Book": 2,
    "CH1 Doll": 3,
    "CH1 Gear": 4,
    "CH1 Inkwell": 5,
    "CH1 Record": 6,
    "CH1 Wrench": 7,
    "Unlock CH2": 8
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "CH1 Doll": ItemClassification.progression,
    "CH1 Gear": ItemClassification.progression,
    "CH1 Wrench": ItemClassification.progression,
    "CH1 Record": ItemClassification.progression,
    "CH1 Inkwell": ItemClassification.progression,
    "CH1 Book": ItemClassification.progression,
    "Bacon Soup": ItemClassification.filler,
    "Unlock CH2": ItemClassification.progression,
}


class BATIMItem(Item):
    game = "Bendy and the Ink Machine"


def get_random_filler_item_name(world: BATIMWorld) -> str:
    return "Bacon Soup"
    # FIXME Multiple Filler Items if needed
    # # APQuest has an option called "trap_chance".
    # # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # # For this purpose, we need to use a random generator.
    #
    # # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # # This ensures that generating with the same generator seed twice yields the same output.
    # # DO NOT use a bare random object from Python's built-in random module.
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Math Trap"
    # return "Confetti Cannon"


def create_item_with_correct_classification(world: BATIMWorld, name: str) -> BATIMItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # FIXME Special options
    # # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    # if name == "Health Upgrade" and world.options.hard_mode:
    #     classification = ItemClassification.progression

    return BATIMItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: BATIMWorld) -> None:
    itempool: list[Item] = [
        world.create_item("CH1 Doll"),
        world.create_item("CH1 Gear"),
        world.create_item("CH1 Wrench"),
        world.create_item("CH1 Record"),
        world.create_item("CH1 Inkwell"),
        world.create_item("CH1 Book"),
        world.create_item("Unlock CH2"),
    ]

    # FIXME Special Options
    # # Some items may only exist if the player enables certain options.
    # # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # # Otherwise, we add a filler Confetti Cannon.
    # if world.options.hammer:
    #     # Once again, it is important to stress that even though the Hammer doesn't always exist,
    #     # it must be present in the worlds item_name_to_id.
    #     # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
    #     itempool.append(world.create_item("Hammer"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    # FIXME Precollected Items
    # # Sometimes, you might want the player to start with certain items already in their inventory.
    # # These items are called "precollected items".
    # # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # # Players can add precollected items themselves via the generic "start_inventory" option.
    # # If you want to add your own precollected items, you can do so via world.push_precollected().
    # if world.options.start_with_one_confetti_cannon:
    #     # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
    #     starting_confetti_cannon = world.create_item("Confetti Cannon")
    #     world.push_precollected(starting_confetti_cannon)

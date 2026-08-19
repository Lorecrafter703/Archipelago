from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .options import StartingChapter, TotalBaconSoups, BaconSoupsRequired

if TYPE_CHECKING:
    from .world import BATIMWorld

ITEM_NAME_TO_ID = {
    "Bacon Soup": 1,
    "Trap": 2,
    "Empty Soup Can": 3,
    "Empty Ink Well": 4,
    "Broken Banjo String": 5,
    "Unlock CH1": 100,
    "CH1 Book": 101,
    "CH1 Doll": 102,
    "CH1 Gear": 103,
    "CH1 Inkwell": 104,
    "CH1 Record": 105,
    "CH1 Wrench": 106,
    "CH1 Checkpoint Basement": 107,
    "Unlock CH2": 200,
    "CH2 Keys": 201,
    "CH2 Valve": 202,
    "CH2 Checkpoint Lost Keys": 203,
    "CH2 Checkpoint Sammy's Office": 204,
    "Unlock CH3": 300,
    "CH3 Toys": 301,
    "CH3 Checkpoint Decisions": 302,
    "CH3 Checkpoint Angel's Bidding": 303,
    "CH3 Checkpoint Butcher Gang": 304,
    "CH3 Tommy Gun": 305,
    "CH3 Boris Bone": 306,
    "Unlock CH4": 400,
    "CH4 Books": 401,
    "CH4 Bossfight Bertrum": 402,
    "CH4 Checkpoint Warehouse": 403,
    "CH4 Checkpoint Haunted House": 404,
    "Unlock CH5": 500,
    "CH5 Checkpoint Administration": 501,
    "CH5 Checkpoint The Ink Machine": 502,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "CH1 Doll": ItemClassification.progression,
    "CH1 Gear": ItemClassification.progression,
    "CH1 Wrench": ItemClassification.progression,
    "CH1 Record": ItemClassification.progression,
    "CH1 Inkwell": ItemClassification.progression,
    "CH1 Book": ItemClassification.progression,
    "CH2 Keys": ItemClassification.progression,
    "CH2 Valve": ItemClassification.progression,
    "CH3 Toys": ItemClassification.progression,
    "CH4 Books": ItemClassification.progression,
    "CH4 Bossfight Bertrum": ItemClassification.progression,
    "Unlock CH1": ItemClassification.progression,
    "Unlock CH2": ItemClassification.progression,
    "Unlock CH3": ItemClassification.progression,
    "Unlock CH4": ItemClassification.progression,
    "Unlock CH5": ItemClassification.progression,
    "Bacon Soup": ItemClassification.progression,
    "CH1 Checkpoint Basement": ItemClassification.useful,
    "CH2 Checkpoint Lost Keys": ItemClassification.useful,
    "CH2 Checkpoint Sammy's Office": ItemClassification.useful,
    "CH3 Checkpoint Decisions": ItemClassification.useful,
    "CH3 Checkpoint Angel's Bidding": ItemClassification.useful,
    "CH3 Checkpoint Butcher Gang": ItemClassification.useful,
    "CH4 Checkpoint Warehouse": ItemClassification.useful,
    "CH4 Checkpoint Haunted House": ItemClassification.useful,
    "CH5 Checkpoint Administration": ItemClassification.useful,
    "CH5 Checkpoint The Ink Machine": ItemClassification.useful,
    "CH3 Tommy Gun": ItemClassification.useful,
    "CH3 Boris Bone": ItemClassification.filler,
    "Empty Soup Can": ItemClassification.filler,
    "Empty Ink Well": ItemClassification.filler,
    "Broken Banjo String": ItemClassification.filler,
    "Trap": ItemClassification.trap,
}


class BATIMItem(Item):
    game = "Bendy and the Ink Machine"


def get_random_filler_item_name(world: BATIMWorld) -> str:
    filler_items: list[str] = [
        "Empty Soup Can",
        "Empty Ink Well",
        "Broken Banjo String",
    ]
    num = world.random.randint(0, 2)
    return filler_items[num]


def create_item_with_correct_classification(world: BATIMWorld, name: str) -> BATIMItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return BATIMItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: BATIMWorld) -> None:
    # Correct Yaml Options
    starting_chapter = int(world.options.starting_chapter)
    last_chapter = 4 if world.options.include_later_chapters else int(world.options.goal_chapter)
    bacon_soups_total = int(world.options.total_bacon_soups)

    itempool: list[Item] = []

    # Bacon Soups
    itempool += [world.create_item("Bacon Soup") for _ in range(bacon_soups_total)]

    # Chapter Unlocks
    for i in range (0, last_chapter + 1):
        if i != starting_chapter:
            itempool += [world.create_item("Unlock CH" + str(i + 1))]
    world.push_precollected(world.create_item("Unlock CH" + str(starting_chapter + 1)))

    # Chapter 1 Items
    itempool += [
        world.create_item("CH1 Doll"),
        world.create_item("CH1 Gear"),
        world.create_item("CH1 Wrench"),
        world.create_item("CH1 Record"),
        world.create_item("CH1 Inkwell"),
        world.create_item("CH1 Book"),
    ]
    if world.options.checkpoint_sanity:
        itempool += [world.create_item("CH1 Checkpoint Basement")]

    # Chapter 2 Items
    if last_chapter >= 1:
        itempool += [world.create_item("CH2 Keys"), world.create_item("CH2 Valve")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH2 Checkpoint Lost Keys"), world.create_item("CH2 Checkpoint Sammy's Office")]

    # Chapter 3 Items
    if last_chapter >= 2:
        itempool += [world.create_item("CH3 Toys")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH3 Checkpoint Decisions"), world.create_item("CH3 Checkpoint Angel's Bidding"), world.create_item("CH3 Checkpoint Butcher Gang")]
        if world.options.include_tommy_gun:
            itempool += [world.create_item("CH3 Tommy Gun")]
        if world.options.boris_bone:
            itempool += [world.create_item("CH3 Boris Bone")]

    # Chapter 4 Items
    if last_chapter >= 3:
        itempool += [world.create_item("CH4 Books"), world.create_item("CH4 Bossfight Bertrum")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH4 Checkpoint Warehouse"), world.create_item("CH4 Checkpoint Haunted House")]

    # Chapter 5 Items
    if last_chapter >= 4:
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH5 Checkpoint Administration"), world.create_item("CH5 Checkpoint The Ink Machine")]

    # Filler Items
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool




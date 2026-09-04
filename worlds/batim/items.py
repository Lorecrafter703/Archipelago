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
    "The Illusion of Living": 101,
    "Bendy Squeaky Toy": 102,
    "Spare Gear": 103,
    "Animators' Inkwell": 104,
    "Vinyl Record": 105,
    "'Pocket' Wrench": 106,
    "CH1 Checkpoint - Bendy Chase": 107,
    "Unlock CH2": 200,
    "Wally's Keys": 201,
    "Sewer Valve": 202,
    "CH2 Checkpoint - Lost Keys": 203,
    "CH2 Checkpoint - Sammy's Office": 204,
    "Unlock CH3": 300,
    "Toy Machine": 301,
    "CH3 Checkpoint - Toy Machine": 302,
    "CH3 Checkpoint - Angel's Bidding": 303,
    "CH3 Checkpoint - Butcher Gang": 304,
    "Tommy Gun": 305,
    "Poor Dog's Bone": 306,
    "Unlock CH4": 400,
    "Book Puzzle": 401,
    "Bertrum Bossfight": 402,
    "CH4 Checkpoint - Warehouse": 403,
    "CH4 Checkpoint - Brute Boris": 404,
    "Unlock CH5": 500,
    "CH5 Checkpoint - Administration": 501,
    "CH5 Checkpoint - The Ink Machine": 502,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Bendy Squeaky Toy": ItemClassification.progression,
    "Spare Gear": ItemClassification.progression,
    "'Pocket' Wrench": ItemClassification.progression,
    "Vinyl Record": ItemClassification.progression,
    "Animators' Inkwell": ItemClassification.progression,
    "The Illusion of Living": ItemClassification.progression,
    "Wally's Keys": ItemClassification.progression,
    "Sewer Valve": ItemClassification.progression,
    "Toy Machine": ItemClassification.progression,
    "Book Puzzle": ItemClassification.progression,
    "Bertrum Bossfight": ItemClassification.progression,
    "Unlock CH1": ItemClassification.progression,
    "Unlock CH2": ItemClassification.progression,
    "Unlock CH3": ItemClassification.progression,
    "Unlock CH4": ItemClassification.progression,
    "Unlock CH5": ItemClassification.progression,
    "Bacon Soup": ItemClassification.progression,
    "CH1 Checkpoint - Bendy Chase": ItemClassification.useful,
    "CH2 Checkpoint - Lost Keys": ItemClassification.useful,
    "CH2 Checkpoint - Sammy's Office": ItemClassification.useful,
    "CH3 Checkpoint - Toy Machine": ItemClassification.useful,
    "CH3 Checkpoint - Angel's Bidding": ItemClassification.useful,
    "CH3 Checkpoint - Butcher Gang": ItemClassification.useful,
    "CH4 Checkpoint - Warehouse": ItemClassification.useful,
    "CH4 Checkpoint - Brute Boris": ItemClassification.useful,
    "CH5 Checkpoint - Administration": ItemClassification.useful,
    "CH5 Checkpoint - The Ink Machine": ItemClassification.useful,
    "Tommy Gun": ItemClassification.useful,
    "Poor Dog's Bone": ItemClassification.filler,
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
        world.create_item("Bendy Squeaky Toy"),
        world.create_item("Spare Gear"),
        world.create_item("'Pocket' Wrench"),
        world.create_item("Vinyl Record"),
        world.create_item("Animators' Inkwell"),
        world.create_item("The Illusion of Living"),
    ]
    if world.options.checkpoint_sanity:
        itempool += [world.create_item("CH1 Checkpoint - Bendy Chase")]

    # Chapter 2 Items
    if last_chapter >= 1:
        itempool += [world.create_item("Wally's Keys"), world.create_item("Sewer Valve")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH2 Checkpoint - Lost Keys"), world.create_item("CH2 Checkpoint - Sammy's Office")]

    # Chapter 3 Items
    if last_chapter >= 2:
        itempool += [world.create_item("Toy Machine")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH3 Checkpoint - Toy Machine"), world.create_item("CH3 Checkpoint - Angel's Bidding"), world.create_item("CH3 Checkpoint - Butcher Gang")]
        if world.options.include_tommy_gun:
            itempool += [world.create_item("Tommy Gun")]
        if world.options.boris_bone:
            itempool += [world.create_item("Poor Dog's Bone")]

    # Chapter 4 Items
    if last_chapter >= 3:
        itempool += [world.create_item("Book Puzzle"), world.create_item("Bertrum Bossfight")]
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH4 Checkpoint - Warehouse"), world.create_item("CH4 Checkpoint - Brute Boris")]

    # Chapter 5 Items
    if last_chapter >= 4:
        if world.options.checkpoint_sanity:
            itempool += [world.create_item("CH5 Checkpoint - Administration"), world.create_item("CH5 Checkpoint - The Ink Machine")]

    # Filler Items
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool




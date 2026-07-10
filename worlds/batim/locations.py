from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BATIMWorld


LOCATION_NAME_TO_ID = {
    "CH1 Bacon Soup 1": 1,
    "CH1 Bacon Soup 2": 2,
    "CH1 Bacon Soup 3": 3,
    "CH1 Bacon Soup 4": 4,
    "CH1 Bacon Soup 5": 5,
    "CH1 Bacon Soup 6": 6,
    "CH1 Bacon Soup 7": 7,
    "CH1 Bacon Soup 8": 8,
    "CH1 Bacon Soup 9": 9,
    "CH1 Bacon Soup 10": 10,
    "CH1 Bacon Soup 11": 11,
    "CH1 Bacon Soup 12": 12,
    "CH1 Bacon Soup 13": 13,
    "CH1 Bacon Soup 14": 14,
    "CH1 Bacon Soup 15": 15,
    "CH1 Bacon Soup 16": 16,
    "CH1 Bacon Soup 17": 17,
    "CH1 Bacon Soup 18": 18,
    "CH1 Bacon Soup 19": 19,
    "CH1 Bacon Soup 20": 20,
    "CH1 Bacon Soup 0": 21,
    "CH1 Book": 22,
    "CH1 Doll": 23,
    "CH1 Gear": 24,
    "CH1 Inkwell": 25,
    "CH1 Record": 26,
    "CH1 Wrench": 27,
    "CH1 Audio Log Thomas 1": 28,
    "CH1 Audio Log Wally 1": 29,
    "CH1 Complete": 30,
    "CH2 Bacon Soup 0": 31,
    "CH2 Bacon Soup 1": 32,
    "CH2 Bacon Soup 2": 33,
    "CH2 Bacon Soup 3": 34,
    "CH2 Bacon Soup 4": 35,
    "CH2 Bacon Soup 5": 36,
    "CH2 Bacon Soup 6": 37,
    "CH2 Bacon Soup 7": 38,
    "CH2 Bacon Soup 8": 39,
    "CH2 Bacon Soup 9": 40,
    "CH2 Bacon Soup 10": 41,
    "CH2 Bacon Soup 11": 42,
    "CH2 Bacon Soup 12": 43,
    "CH2 Bacon Soup 13": 44,
    "CH2 Bacon Soup 14": 45,
    "CH2 Bacon Soup 15": 46,
    "CH2 Bacon Soup 16": 47,
    "CH2 Bacon Soup 17": 48,
    "CH2 Bacon Soup 18": 49,
    "CH2 Bacon Soup 19": 50,
    "CH2 Bacon Soup 20": 51,
    "CH2 Bacon Soup 21": 52,
    "CH2 Bacon Soup 22": 53,
    "CH2 Bacon Soup 23": 54,
    "CH2 Bacon Soup 24": 55,
    "CH2 Bacon Soup 25": 56,
    "CH2 Bacon Soup 26": 57,
    "CH2 Bacon Soup 27": 58,
    "CH2 Bacon Soup 28": 59,
    "CH2 Bacon Soup 29": 60,
    "CH2 Bacon Soup 30": 61,
    "CH2 Keys": 62,
    "CH2 Valve": 63,
    "CH2 Audio Log The Prayer": 64,
    "CH2 Audio Log Distractions": 65,
    "CH2 Audio Log The New Voice Actress": 66,
    "CH2 Audio Log The Projectionist": 67,
    "CH2 Audio Log Lost Key": 68,
    "CH2 Audio Log Favorite Song": 69,
    "CH2 Audio Log Jack Fain": 70,
    "CH2 Complete": 71,
}


class BATIMLocation(Location):
    game = "Bendy and the Ink Machine"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BATIMWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BATIMWorld) -> None:
    ch1_intro = world.get_region("CH1 Intro")
    ch1_basement = world.get_region("CH1 Basement")
    ch2_intro = world.get_region("CH2 Intro")
    ch2_after_keys = world.get_region("CH2 After Keys")
    ch2_after_valve = world.get_region("CH2 After Valve")

    ch1_intro_locations = get_location_names_with_ids([
        "CH1 Doll",
        "CH1 Gear",
        "CH1 Wrench",
        "CH1 Record",
        "CH1 Inkwell",
        "CH1 Book",
        "CH1 Bacon Soup 1",
        "CH1 Bacon Soup 2",
        "CH1 Bacon Soup 3",
        "CH1 Bacon Soup 4",
        "CH1 Bacon Soup 5",
        "CH1 Bacon Soup 6",
        "CH1 Bacon Soup 7",
        "CH1 Bacon Soup 8",
        "CH1 Bacon Soup 9",
        "CH1 Bacon Soup 10",
        "CH1 Bacon Soup 11",
        "CH1 Bacon Soup 12",
        "CH1 Bacon Soup 13",
        "CH1 Bacon Soup 14",
        "CH1 Bacon Soup 15",
        "CH1 Bacon Soup 16",
        "CH1 Bacon Soup 17",
        "CH1 Bacon Soup 18",
        "CH1 Bacon Soup 19",
        "CH1 Audio Log Wally 1"
    ])
    ch1_intro.add_locations(ch1_intro_locations, BATIMLocation)

    ch1_basement_locations = get_location_names_with_ids(["CH1 Bacon Soup 20", "CH1 Bacon Soup 0", "CH1 Audio Log Thomas 1", "CH1 Complete"])
    ch1_basement.add_locations(ch1_basement_locations, BATIMLocation)

    ch2_intro_locations = get_location_names_with_ids([
        "CH2 Bacon Soup 0",
        "CH2 Bacon Soup 3",
        "CH2 Bacon Soup 4",
        "CH2 Bacon Soup 5",
        "CH2 Bacon Soup 6",
        "CH2 Bacon Soup 7",
        "CH2 Bacon Soup 8",
        "CH2 Bacon Soup 9",
        "CH2 Bacon Soup 10",
        "CH2 Bacon Soup 11",
        "CH2 Bacon Soup 12",
        "CH2 Bacon Soup 13",
        "CH2 Bacon Soup 14",
        "CH2 Bacon Soup 15",
        "CH2 Bacon Soup 16",
        "CH2 Bacon Soup 17",
        "CH2 Bacon Soup 18",
        "CH2 Bacon Soup 19",
        "CH2 Bacon Soup 20",
        "CH2 Bacon Soup 25",
        "CH2 Bacon Soup 26",
        "CH2 Bacon Soup 27",
        "CH2 Bacon Soup 28",
        "CH2 Bacon Soup 29",
        "CH2 Audio Log The Prayer",
        "CH2 Audio Log Distractions",
        "CH2 Audio Log The New Voice Actress",
        "CH2 Audio Log The Projectionist",
        "CH2 Audio Log Lost Key",
        "CH2 Keys"
    ])
    ch2_intro.add_locations(ch2_intro_locations, BATIMLocation)

    ch2_after_keys_locations = get_location_names_with_ids([
        "CH2 Bacon Soup 1",
        "CH2 Bacon Soup 2",
        "CH2 Bacon Soup 23",
        "CH2 Bacon Soup 24",
        "CH2 Bacon Soup 30",
        "CH2 Audio Log Favorite Song",
        "CH2 Audio Log Jack Fain",
        "CH2 Valve",
    ])
    ch2_after_keys.add_locations(ch2_after_keys_locations, BATIMLocation)

    ch2_after_valve_locations = get_location_names_with_ids([
        "CH2 Bacon Soup 21",
        "CH2 Bacon Soup 22",
        "CH2 Complete",
    ])
    ch2_after_valve.add_locations(ch2_after_valve_locations, BATIMLocation)

    # FIXME Special Options
    # # Locations may be in different regions depending on the player's options.
    # # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    # top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     top_middle_room.add_locations(top_middle_room_locations, APQuestLocation)
    # else:
    #     overworld.add_locations(top_middle_room_locations, APQuestLocation)
    #
    # # Locations may exist only if the player enables certain options.
    # # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    # if world.options.extra_starting_chest:
    #     # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
    #     # exist, it must still always be present in the world's location_name_to_id.
    #     # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
    #     bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
    #     overworld.add_locations(bottom_left_extra_chest, APQuestLocation)


def create_events(world: BATIMWorld) -> None:
    pass # FIXME Events if needed
    # # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # # In our case, the player must press a button in the top left room to open the final boss door.
    # # AP has something for this purpose: "Event locations" and "Event items".
    # # An event location is no different than a regular location, except it has the address "None".
    # # It is treated during generation like any other location, but then it is discarded.
    # # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    # top_left_room = world.get_region("Top Left Room")
    # final_boss_room = world.get_region("Final Boss Room")
    #
    # # One way to create an event is simply to use one of the normal methods of creating a location.
    # button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    # top_left_room.locations.append(button_in_top_left_room)
    #
    # # We then need to put an event item onto the location.
    # # An event item is an item whose code is "None" (same as the event location's address),
    # # and whose classification is "progression". Item creation will be discussed more in items.py.
    # # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # # it is common practice to create the item when creating the location.
    # # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # # we'll create both the event location and the event item in our locations.py code.
    # button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    # button_in_top_left_room.place_locked_item(button_item)
    #
    # # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # # Luckily, we have another event we want to create: The Victory event.
    # # We will use this event to track whether the player can win the game.
    # # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    # final_boss_room.add_event(
    #     "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    # )

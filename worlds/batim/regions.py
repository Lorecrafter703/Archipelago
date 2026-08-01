from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BATIMWorld


def create_and_connect_regions(world: BATIMWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BATIMWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    # CH1 Locations
    ch1_intro = Region("CH1 Intro", world.player, world.multiworld)
    ch1_basement = Region("CH1 Basement", world.player, world.multiworld)
    # CH2 Locations
    ch2_intro = Region("CH2 Intro", world.player, world.multiworld)
    ch2_after_keys = Region("CH2 After Keys", world.player, world.multiworld)
    ch2_after_valve = Region("CH2 After Valve", world.player, world.multiworld)
    # CH3 Locations
    ch3_intro = Region("CH3 Intro", world.player, world.multiworld)
    ch3_after_toys = Region("CH3 After Toys", world.player, world.multiworld)
    ch3_alice_objectives = Region("CH3 Alice Objectives", world.player, world.multiworld)
    ch3_after_cutouts = Region("CH3 After Cutouts", world.player, world.multiworld)
    # CH4 Locations
    ch4_intro = Region("CH4 Intro", world.player, world.multiworld)
    ch4_after_book_puzzle = Region("CH4 After Book Puzzle", world.player, world.multiworld)
    ch4_warehouse = Region("CH4 Warehouse", world.player, world.multiworld)
    ch4_after_bertrum = Region("CH4 After Bertrum", world.player, world.multiworld)
    ch4_haunted_house = Region("CH4 Haunted House", world.player, world.multiworld)
    # CH5 Locations
    ch5_intro = Region("CH5 Intro", world.player, world.multiworld)
    ch5_administration = Region("CH5 Administration", world.player, world.multiworld)
    ch5_boss = Region("CH5 Boss", world.player, world.multiworld)

    regions = [menu, ch1_intro, ch1_basement, ch2_intro, ch2_after_keys, ch2_after_valve, ch3_intro, ch3_after_toys, ch3_alice_objectives, ch3_after_cutouts, ch4_intro, ch4_after_book_puzzle, ch4_warehouse, ch4_after_bertrum, ch4_haunted_house, ch5_intro, ch5_administration, ch5_boss]

    # FIXME Special Options
    # # Some regions may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: BATIMWorld) -> None:
    menu = world.get_region("Menu")
    ch1_intro = world.get_region("CH1 Intro")
    ch1_basement = world.get_region("CH1 Basement")
    ch2_intro = world.get_region("CH2 Intro")
    ch2_after_keys = world.get_region("CH2 After Keys")
    ch2_after_valve = world.get_region("CH2 After Valve")
    ch3_intro = world.get_region("CH3 Intro")
    ch3_after_toys = world.get_region("CH3 After Toys")
    ch3_alice_objectives = world.get_region("CH3 Alice Objectives")
    ch3_after_cutouts = world.get_region("CH3 After Cutouts")
    ch4_intro = world.get_region("CH4 Intro")
    ch4_after_book_puzzle = world.get_region("CH4 After Book Puzzle")
    ch4_warehouse = world.get_region("CH4 Warehouse")
    ch4_after_bertrum = world.get_region("CH4 After Bertrum")
    ch4_haunted_house = world.get_region("CH4 Haunted House")
    ch5_intro = world.get_region("CH5 Intro")
    ch5_administration = world.get_region("CH5 Administration")
    ch5_boss = world.get_region("CH5 Boss")

    # Chapter 1
    menu.connect(ch1_intro, "Menu to CH1 Intro")
    menu.connect(ch1_basement, "Menu to CH1 Basement")
    ch1_intro.connect(ch1_basement, "CH1 Intro to Basement")
    # Chapter 2
    menu.connect(ch2_intro, "Menu to CH2 Intro")
    menu.connect(ch2_after_valve, "Menu to CH2 After Valve")
    ch2_intro.connect(ch2_after_keys, "CH2 Intro to After Keys")
    ch2_after_keys.connect(ch2_intro, "CH2 After Keys to Intro")
    ch2_after_keys.connect(ch2_after_valve, "CH2 After Keys to After Valve")
    ch2_after_valve.connect(ch2_after_keys, "CH2 After Valve to After Keys")
    # Chapter 3
    menu.connect(ch3_intro, "Menu to CH3 Intro")
    menu.connect(ch3_after_toys, "Menu to CH3 After Toys")
    menu.connect(ch3_after_cutouts, "Menu to CH3 After Cutouts")
    ch3_intro.connect(ch3_after_toys, "CH3 Intro to After Toys")
    ch3_after_toys.connect(ch3_alice_objectives, "CH3 After Toys to Alice Objectives")
    ch3_alice_objectives.connect(ch3_after_cutouts, "CH3 Alice Objectives to After Cutouts")
    # Chapter 4
    menu.connect(ch4_intro, "Menu to CH4 Intro")
    menu.connect(ch4_warehouse, "Menu to CH4 Warehouse")
    menu.connect(ch4_haunted_house, "Menu to CH4 Haunted House")
    ch4_intro.connect(ch4_after_book_puzzle, "CH4 Intro to After Book Puzzle")
    ch4_after_book_puzzle.connect(ch4_warehouse, "CH4 After Book Puzzle to Warehouse")
    ch4_warehouse.connect(ch4_after_bertrum, "CH4 Warehouse to After Bertrum")
    ch4_after_bertrum.connect(ch4_haunted_house, "CH4 After Bertrum to Haunted House")
    # Chapter 5
    menu.connect(ch5_intro, "Menu to CH5 Intro")
    menu.connect(ch5_administration, "Menu to CH5 Administration")
    ch5_intro.connect(ch5_administration, "CH5 Intro to Administration")
    ch5_administration.connect(ch5_boss, "CH5 Administration to Boss")


    # FIXME Special Options
    # # Some Entrances may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")

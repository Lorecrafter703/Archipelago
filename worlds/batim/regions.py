from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BATIMWorld


def create_and_connect_regions(world: BATIMWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BATIMWorld) -> None:
    archives_hub = Region("Archives Hub", world.player, world.multiworld)
    ch1_intro = Region("CH1 Intro", world.player, world.multiworld)
    ch1_basement = Region("CH1 Basement", world.player, world.multiworld)
    ch2_intro = Region("CH2 Intro", world.player, world.multiworld)
    ch2_after_keys = Region("CH2 After Keys", world.player, world.multiworld)
    ch2_after_valve = Region("CH2 After Valve", world.player, world.multiworld)

    regions = [archives_hub, ch1_intro, ch1_basement, ch2_intro, ch2_after_keys, ch2_after_valve]

    # FIXME Special Options
    # # Some regions may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # if world.options.hammer:
    #     top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #     regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: BATIMWorld) -> None:
    archives_hub = world.get_region("Archives Hub")
    ch1_intro = world.get_region("CH1 Intro")
    ch1_basement = world.get_region("CH1 Basement")
    ch2_intro = world.get_region("CH2 Intro")
    ch2_after_keys = world.get_region("CH2 After Keys")
    ch2_after_valve = world.get_region("CH2 After Valve")

    archives_hub.connect(ch1_intro, "Archives Hub to CH1 Intro")
    ch1_intro.connect(ch1_basement, "CH1 Intro to Basement")
    archives_hub.connect(ch2_intro, "Archives Hub to CH2 Intro")
    ch2_intro.connect(ch2_after_keys, "CH2 Intro to After Keys")
    ch2_after_keys.connect(ch2_after_valve, "CH2 After Keys to After Valve")

    # FIXME Special Options
    # # Some Entrances may only exist if the player enables certain options.
    # # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    # if world.options.hammer:
    #     top_middle_room = world.get_region("Top Middle Room")
    #     overworld.connect(top_middle_room, "Overworld to Top Middle Room")

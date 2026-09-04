from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BATIMWorld


LOCATION_NAME_TO_ID = {
    "CH1 Bacon Soup - Ritual Room": 100,
    "CH1 Bacon Soup - Projector Closet": 101,
    "CH1 Bacon Soup - Music Room Top Shelf": 102,
    "CH1 Bacon Soup - Music Room Bottom Shelf": 103,
    "CH1 Bacon Soup - Theater Top Shelf #1": 104,
    "CH1 Bacon Soup - Theater Top Shelf #2": 105,
    "CH1 Bacon Soup - Under the Theater’s Projector": 106,
    "CH1 Bacon Soup - Under the Foyer Projector": 107,
    "CH1 Bacon Soup - Dresser by Workshop Entrance": 108,
    "CH1 Bacon Soup - Hallway Shelf": 109,
    "CH1 Bacon Soup - Break Room Closet #1": 110,
    "CH1 Bacon Soup - Break Room Closet #2": 111,
    "CH1 Bacon Soup - Break Room Closet #3": 112,
    "CH1 Bacon Soup - Break Room Closet #4": 113,
    "CH1 Bacon Soup - Break Room Closet #5": 114,
    "CH1 Bacon Soup - Theater Top Shelf #3": 115,
    "CH1 Bacon Soup - Hallway Closet #1": 116,
    "CH1 Bacon Soup - Hallway Closet #2": 117,
    "CH1 Bacon Soup - Hallway Closet #3": 118,
    "CH1 Bacon Soup - Hallway Closet #4": 119,
    "CH1 Bacon Soup - Flooded Basement": 120,
    "CH1 Ritual Item - Book": 121,
    "CH1 Ritual Item - Doll": 122,
    "CH1 Ritual Item - Gear": 123,
    "CH1 Ritual Item - Inkwell": 124,
    "CH1 Ritual Item - Record": 125,
    "CH1 Ritual Item - Wrench": 126,
    "CH1 Audio Log - Thomas Connor (Flooded Basement)": 127,
    "CH1 Audio Log - Wally Franks (Hallway Table)": 128,
    "CH1 Radio": 129,
    "CH1 theMeatly": 130,
    "CH1 Checkpoint - Bendy Chase": 131,
    "CH1 Complete": 199,
    "CH2 Bacon Soup - Writer’s Desk": 200,
    "CH2 Bacon Soup - Wally’s Closet #1": 201,
    "CH2 Bacon Soup - Wally’s Closet #2": 202,
    "CH2 Bacon Soup - Set Us Free #1": 203,
    "CH2 Bacon Soup - Shelf Before Department Entrance #1": 204,
    "CH2 Bacon Soup - Shelf Before Department Entrance #2": 205,
    "CH2 Bacon Soup - Shelf Before Department Entrance #3": 206,
    "CH2 Bacon Soup - Shelf Before Department Entrance #4": 207,
    "CH2 Bacon Soup - Shelf Before Department Entrance #5": 208,
    "CH2 Bacon Soup - Shelf Before Department Entrance #6": 209,
    "CH2 Bacon Soup - Shelf Before Department Entrance #7": 210,
    "CH2 Bacon Soup - Shelf Before Department Entrance #8": 211,
    "CH2 Bacon Soup - Set Us Free #2": 212,
    "CH2 Bacon Soup - Set Us Free #3": 213,
    "CH2 Bacon Soup - Shelf Before Department Entrance #9": 214,
    "CH2 Bacon Soup - Shelf Before Department Entrance #10": 215,
    "CH2 Bacon Soup - Shelf Before Department Entrance #11": 216,
    "CH2 Bacon Soup - Shelf Before Department Entrance #12": 217,
    "CH2 Bacon Soup - Shelf Before Department Entrance #13": 218,
    "CH2 Bacon Soup - Shelf Before Department Entrance #14": 219,
    "CH2 Bacon Soup - Shelf Before Department Entrance #15": 220,
    "CH2 Bacon Soup - Sammy’s Sacrifice Room": 221,
    "CH2 Bacon Soup - After Bendy Chase": 222,
    "CH2 Bacon Soup - Wally’s Closet #3": 223,
    "CH2 Bacon Soup - Wally’s Closet #4": 224,
    "CH2 Bacon Soup - Shelf Before Department Entrance #16": 225,
    "CH2 Bacon Soup - Shelf Before Department Entrance #17": 226,
    "CH2 Bacon Soup - Shelf Before Department Entrance #18": 227,
    "CH2 Bacon Soup - Shelf Before Department Entrance #19": 228,
    "CH2 Bacon Soup - Shelf Before Department Entrance #20": 229,
    "CH2 Bacon Soup - Jack Fain’s Desk": 230,
    "CH2 Lost Keys": 231,
    "CH2 Sewer Valve": 232,
    "CH2 Audio Log - Sammy Lawrence (Can I Get An Amen?)": 233,
    "CH2 Audio Log - Sammy Lawrence (Music Department Lobby)": 234,
    "CH2 Audio Log - Susie Campbell (Recording Studio)": 235,
    "CH2 Audio Log - Norman Polk (Projector)": 236,
    "CH2 Audio Log - Wally Franks (Sammy’s Office)": 237,
    "CH2 Audio Log - Sammy Lawrence (Wally’s Closet)": 238,
    "CH2 Audio Log - Jack Fain (Desk in Sewers)": 239,
    "CH2 Radio": 240,
    "CH2 theMeatly": 241,
    "CH2 Checkpoint - Lost Keys": 242,
    "CH2 Checkpoint - Sammy's Office": 243,
    "CH2 Complete": 299,
    "CH3 Bacon Soup - Empty Inkwell Shelf in the Dark Hallway": 300,
    "CH3 Bacon Soup - Start of the Dark Hallway": 301,
    "CH3 Bacon Soup - On the Ground in the Dark Hallway #1": 302,
    "CH3 Bacon Soup - On the Ground in the Dark Hallway #2": 303,
    "CH3 Bacon Soup - Outside Boris’ Safehouse #4": 304,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #1": 305,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #2": 306,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #3": 307,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #4": 308,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #5": 309,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #6": 310,
    "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Desk on Stairs": 311,
    "CH3 Bacon Soup - Desk in the Large Office (Level P)": 312,
    "CH3 Bacon Soup - Spiral Staircase: Below Level K, On a Dresser": 313,
    "CH3 Bacon Soup - Shelf by Elevator (Level P)": 314,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #1": 315,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #2": 316,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #3": 317,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #4": 318,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #1": 319,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #2": 320,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #3": 321,
    "CH3 Bacon Soup - Alice’s Torture Room": 322,
    "CH3 Bacon Soup - By the Door to the Lunchroom (Level 11)": 323,
    "CH3 Bacon Soup - By Alice’s Door in the Flooded Morgue": 324,
    "CH3 Bacon Soup - Outside Boris’ Safehouse #3": 325,
    "CH3 Bacon Soup - Back of the Large Office #1 (Level P)": 326,
    "CH3 Bacon Soup - Back of the Large Office #2 (Level P)": 327,
    "CH3 Bacon Soup - Back of the Large Office #3 (Level P)": 328,
    "CH3 Bacon Soup - Outside Boris’ Safehouse #2": 329,
    "CH3 Bacon Soup - Outside Boris’ Safehouse #1": 330,
    "CH3 Bacon Soup - Lunchroom Table (Level 11)": 331,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #4": 332,
    "CH3 Bacon Soup - On the Desk in the Power Hallway #1 (Level K)": 333,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #5": 334,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #6": 335,
    "CH3 Bacon Soup - On the Desk in the Power Hallway #2 (Level K)": 336,
    "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #7": 337,
    "CH3 Bacon Soup - Boris’ Bathroom Secret Soup": 338,
    "CH3 Audio Log - Shawn Flynn (Toy Machine Room)": 339,
    "CH3 Audio Log - Joey Drew (Path of the Demon)": 340,
    "CH3 Audio Log - Susie Campbell (Path of the Angel)": 341,
    "CH3 Audio Log - Wally Franks and Thomas Connor (Level K Power Hallway)": 342,
    "CH3 Audio Log - Thomas Connor (Level 9)": 343,
    "CH3 Audio Log - Susie Campbell (Flooded Morgue)": 344,
    "CH3 Audio Log - Wally Franks (Level 11)": 345,
    "CH3 Audio Log - Grant Cohen (Accounting Office on Level 9)": 346,
    "CH3 Audio Log - Norman Polk (Projectionist’s Maze)": 347,
    "CH3 Audio Log - Henry (Sunken Room)": 348,
    "CH3 Radio": 349,
    "CH3 theMeatly": 350,
    "CH3 Checkpoint - Toy Machine": 351,
    "CH3 Checkpoint - Angel's Bidding": 352,
    "CH3 Checkpoint - Butcher Gang": 353,
    "CH3 Tommy Gun Challenge": 354,
    "CH3 Lever Challenge 1": 355,
    "CH3 Lever Challenge 2": 356,
    "CH3 Lever Challenge 3": 357,
    "CH3 Boris's Bone": 358,
    "CH3 Complete": 399,
    "CH4 Bacon Soup - Unmarked Booth Counter": 400,
    "CH4 Bacon Soup - theMeatly’s Storage Room": 401,
    "CH4 Bacon Soup - Striker’s Corpse (Attraction Storage)": 402,
    "CH4 Bacon Soup - On the Lone Crate (Attraction Storage)": 403,
    "CH4 Bacon Soup - By the Clown Bench (Attraction Storage)": 404,
    "CH4 Bacon Soup - Brute Boris’s Ballroom Battle": 405,
    "CH4 Bacon Soup - By the Broken Elevator": 406,
    "CH4 Bacon Soup - Entrance Railing (Research & Design)": 407,
    "CH4 Bacon Soup - Surrounded by Empty Cans (Research & Design)": 408,
    "CH4 Bacon Soup - Shelf in Lacie’s Workshop (Research & Design)": 409,
    "CH4 Bacon Soup - Near Bertrum’s Audio Log (Attraction Storage)": 410,
    "CH4 Bacon Soup - On the Barrel Upstairs (Maintenance Room)": 411,
    "CH4 Bacon Soup - By the Little Miracle Station (Maintenance Room)": 412,
    "CH4 Bacon Soup - Haunted House Roller Coaster Cart": 413,
    "CH4 Bacon Soup - Library Table": 414,
    "CH4 Bacon Soup - Swollen Searcher Spawner": 415,
    "CH4 Bacon Soup - Spiral Staircase": 416,
    "CH4 Bacon Soup - Lost Ones’ Hideout": 417,
    "CH4 Bacon Soup - Planning Room": 418,
    "CH4 Bulls Eye": 419,
    "CH4 Call the Milk Man": 420,
    "CH4 Wasting Time": 421,
    "CH4 Boss - Bertrum": 422,
    "CH4 Boss - Brute Boris": 423,
    "CH4 Audio Log - ??? (Management Office)": 424,
    "CH4 Audio Log - Susie Campbell (Library)": 425,
    "CH4 Audio Log - Bertrum Piedmont (Planning Room)": 426,
    "CH4 Audio Log - Wally Franks (Minigame Station)": 427,
    "CH4 Audio Log - Lacie Benton (Research & Design)": 428,
    "CH4 Audio Log - Bertrum Piedmont (Attraction Storage)": 429,
    "CH4 Audio Log - Joey Drew (Maintenance Room)": 430,
    "CH4 Radio": 431,
    "CH4 theMeatly": 432,
    "CH4 Checkpoint - Warehouse": 433,
    "CH4 Checkpoint - Brute Boris": 434,
    "CH4 Complete": 499,
    "CH5 Bacon Soup - Alice’s Bed": 500,
    "CH5 Bacon Soup - Safehouse Shelf #1": 501,
    "CH5 Bacon Soup - Safehouse Shelf #2": 502,
    "CH5 Bacon Soup - Safehouse Shelf #3": 503,
    "CH5 Bacon Soup - Closet by Joey’s Office #1": 504,
    "CH5 Bacon Soup - Closet by Joey’s Office #2": 505,
    "CH5 Bacon Soup - Bench by Joey’s Office": 506,
    "CH5 Boss - Sammy Lawrence": 507,
    "CH5 Audio Log - Thomas Connor (Film Vault)": 508,
    "CH5 Audio Log - Wally Franks (Administration Maze)": 509,
    "CH5 Audio Log - Joey Drew (Administration Maze Entrance)": 510,
    "CH5 Audio Log - Joey Drew (Administration Maze Side Room)": 511,
    "CH5 Audio Log - Joey Drew (Joey’s Office)": 512,
    "CH5 Audio Log - Joey Drew (Bendy’s Throne)": 513,
    "CH5 Radio": 514,
    "CH5 theMeatly": 515,
    "CH5 Checkpoint - Administration": 516,
    "CH5 Checkpoint - The Ink Machine": 517,
    "CH5 Complete": 599,
}


class BATIMLocation(Location):
    game = "Bendy and the Ink Machine"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BATIMWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BATIMWorld) -> None:
    last_chapter = 4 if world.options.include_later_chapters else int(world.options.goal_chapter)

    ch1_intro = world.get_region("CH1 Intro")
    ch1_intro_locations = get_location_names_with_ids([
        "CH1 Doll",
        "CH1 Gear",
        "CH1 Wrench",
        "CH1 Record",
        "CH1 Inkwell",
        "CH1 Book",
        "CH1 Bacon Soup - Projector Closet",
        "CH1 Bacon Soup - Music Room Top Shelf",
        "CH1 Bacon Soup - Music Room Bottom Shelf",
        "CH1 Bacon Soup - Theater Top Shelf #1",
        "CH1 Bacon Soup - Theater Top Shelf #2",
        "CH1 Bacon Soup - Under the Theater’s Projector",
        "CH1 Bacon Soup - Under the Foyer Projector",
        "CH1 Bacon Soup - Dresser by Workshop Entrance",
        "CH1 Bacon Soup - Hallway Shelf",
        "CH1 Bacon Soup - Break Room Closet #1",
        "CH1 Bacon Soup - Break Room Closet #2",
        "CH1 Bacon Soup - Break Room Closet #3",
        "CH1 Bacon Soup - Break Room Closet #4",
        "CH1 Bacon Soup - Break Room Closet #5",
        "CH1 Bacon Soup - Theater Top Shelf #3",
        "CH1 Bacon Soup - Hallway Closet #1",
        "CH1 Bacon Soup - Hallway Closet #2",
        "CH1 Bacon Soup - Hallway Closet #3",
        "CH1 Bacon Soup - Hallway Closet #4",
        "CH1 Audio Log - Wally Franks (Hallway Table)",
        "CH1 Radio",
    ])
    ch1_intro.add_locations(ch1_intro_locations, BATIMLocation)

    ch1_basement = world.get_region("CH1 Basement")
    ch1_basement_locations = get_location_names_with_ids([
        "CH1 Bacon Soup - Flooded Basement",
        "CH1 Bacon Soup - Ritual Room",
        "CH1 Audio Log - Thomas Connor (Flooded Basement)",
        "CH1 Complete"
    ])
    ch1_basement.add_locations(ch1_basement_locations, BATIMLocation)

    if world.options.the_meatly_sanity:
        ch1_basement.add_locations(
            get_location_names_with_ids(["CH1 theMeatly"]),
            BATIMLocation
        )
    if world.options.checkpoint_sanity:
        ch1_checkpoint = world.get_region("CH1 Checkpoint")
        ch1_checkpoint.add_locations(
            get_location_names_with_ids(["CH1 Checkpoint - Bendy Chase"]),
            BATIMLocation
        )

    if last_chapter >= 1:
        ch2_intro = world.get_region("CH2 Intro")
        ch2_intro_locations = get_location_names_with_ids([
            "CH2 Bacon Soup - Writer’s Desk",
            "CH2 Bacon Soup - Set Us Free #1",
            "CH2 Bacon Soup - Shelf Before Department Entrance #1",
            "CH2 Bacon Soup - Shelf Before Department Entrance #2",
            "CH2 Bacon Soup - Shelf Before Department Entrance #3",
            "CH2 Bacon Soup - Shelf Before Department Entrance #4",
            "CH2 Bacon Soup - Shelf Before Department Entrance #5",
            "CH2 Bacon Soup - Shelf Before Department Entrance #6",
            "CH2 Bacon Soup - Shelf Before Department Entrance #7",
            "CH2 Bacon Soup - Shelf Before Department Entrance #8",
            "CH2 Bacon Soup - Set Us Free #2",
            "CH2 Bacon Soup - Set Us Free #3",
            "CH2 Bacon Soup - Shelf Before Department Entrance #9",
            "CH2 Bacon Soup - Shelf Before Department Entrance #10",
            "CH2 Bacon Soup - Shelf Before Department Entrance #11",
            "CH2 Bacon Soup - Shelf Before Department Entrance #12",
            "CH2 Bacon Soup - Shelf Before Department Entrance #13",
            "CH2 Bacon Soup - Shelf Before Department Entrance #14",
            "CH2 Bacon Soup - Shelf Before Department Entrance #15",
            "CH2 Bacon Soup - Shelf Before Department Entrance #16",
            "CH2 Bacon Soup - Shelf Before Department Entrance #17",
            "CH2 Bacon Soup - Shelf Before Department Entrance #18",
            "CH2 Bacon Soup - Shelf Before Department Entrance #19",
            "CH2 Bacon Soup - Shelf Before Department Entrance #20",
            "CH2 Audio Log - Sammy Lawrence (Can I Get An Amen?)",
            "CH2 Audio Log - Sammy Lawrence (Music Department Lobby)",
            "CH2 Audio Log - Susie Campbell (Recording Studio)",
            "CH2 Audio Log - Norman Polk (Projector)",
            "CH2 Audio Log - Wally Franks (Sammy’s Office)",
            "CH2 Lost Keys",
        ])
        ch2_intro.add_locations(ch2_intro_locations, BATIMLocation)

        ch2_after_keys = world.get_region("CH2 After Keys")
        ch2_after_keys_locations = get_location_names_with_ids([
            "CH2 Bacon Soup - Wally’s Closet #1",
            "CH2 Bacon Soup - Wally’s Closet #2",
            "CH2 Bacon Soup - Wally’s Closet #3",
            "CH2 Bacon Soup - Wally’s Closet #4",
            "CH2 Bacon Soup - Jack Fain’s Desk",
            "CH2 Audio Log - Sammy Lawrence (Wally’s Closet)",
            "CH2 Audio Log - Jack Fain (Desk in Sewers)",
            "CH2 Sewer Valve",
        ])
        ch2_after_keys.add_locations(ch2_after_keys_locations, BATIMLocation)

        ch2_after_valve = world.get_region("CH2 After Valve")
        ch2_after_valve_locations = get_location_names_with_ids([
            "CH2 Bacon Soup - Sammy’s Sacrifice Room",
            "CH2 Bacon Soup - After Bendy Chase",
            "CH2 Radio",
            "CH2 Complete",
        ])
        ch2_after_valve.add_locations(ch2_after_valve_locations, BATIMLocation)

        if world.options.the_meatly_sanity:
            ch2_after_valve.add_locations(
                get_location_names_with_ids(["CH2 theMeatly"]),
                BATIMLocation
            )
        if world.options.checkpoint_sanity:
            ch2_intro.add_locations(
                get_location_names_with_ids(["CH2 Checkpoint - Lost Keys"]),
                BATIMLocation
            )
            ch2_after_valve.add_locations(
                get_location_names_with_ids(["CH2 Checkpoint - Sammy's Office"]),
                BATIMLocation
            )

    if last_chapter >= 2:
        ch3_intro = world.get_region("CH3 Intro")
        ch3_intro_locations = get_location_names_with_ids([
            "CH3 Bacon Soup - Empty Inkwell Shelf in the Dark Hallway",
            "CH3 Bacon Soup - Start of the Dark Hallway",
            "CH3 Bacon Soup - On the Ground in the Dark Hallway #1",
            "CH3 Bacon Soup - On the Ground in the Dark Hallway #2",
            "CH3 Bacon Soup - Outside Boris’ Safehouse #4",
            "CH3 Bacon Soup - Outside Boris’ Safehouse #3",
            "CH3 Bacon Soup - Outside Boris’ Safehouse #2",
            "CH3 Bacon Soup - Outside Boris’ Safehouse #1",
            "CH3 Bacon Soup - Boris’ Bathroom Secret Soup",
        ])
        ch3_intro.add_locations(ch3_intro_locations, BATIMLocation)

        ch3_after_toys = world.get_region("CH3 After Toys")
        ch3_after_toys_locations = get_location_names_with_ids([
            "CH3 Bacon Soup - Alice’s Torture Room",
            "CH3 Bacon Soup - By Alice’s Door in the Flooded Morgue",
            "CH3 Bacon Soup - On the Desk in the Power Hallway #1 (Level K)",
            "CH3 Bacon Soup - On the Desk in the Power Hallway #2 (Level K)",
            "CH3 Audio Log - Shawn Flynn (Toy Machine Room)",
            "CH3 Audio Log - Susie Campbell (Path of the Angel)",
            "CH3 Audio Log - Joey Drew (Path of the Demon)",
            "CH3 Audio Log - Wally Franks and Thomas Connor (Level K Power Hallway)",
            "CH3 Audio Log - Thomas Connor (Level 9)",
            "CH3 Audio Log - Susie Campbell (Flooded Morgue)",
        ])
        ch3_after_toys.add_locations(ch3_after_toys_locations, BATIMLocation)

        ch3_alice_objectives = world.get_region("CH3 Alice Objectives")
        ch3_alice_objectives_locations = get_location_names_with_ids([
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #1",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #2",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #3",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #4",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #5",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Surrounded by Crates #6",
            "CH3 Bacon Soup - Spiral Staircase: Above Level 11, Desk on Stairs",
            "CH3 Bacon Soup - Desk in the Large Office (Level P)",
            "CH3 Bacon Soup - Spiral Staircase: Below Level K, On a Dresser",
            "CH3 Bacon Soup - Shelf by Elevator (Level P)",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #1",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #2",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #3",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, On the Table #4",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #1",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #2",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #3",
            "CH3 Bacon Soup - By the Door to the Lunchroom (Level 11)",
            "CH3 Bacon Soup - Back of the Large Office #1 (Level P)",
            "CH3 Bacon Soup - Back of the Large Office #2 (Level P)",
            "CH3 Bacon Soup - Back of the Large Office #3 (Level P)",
            "CH3 Bacon Soup - Lunchroom Table (Level 11)",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #4",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #5",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #6",
            "CH3 Bacon Soup - Spiral Staircase: Above Level P, Soup Shelf #7",
            "CH3 Audio Log - Wally Franks (Level 11)",
            "CH3 Audio Log - Grant Cohen (Accounting Office on Level 9)",
            "CH3 Radio",
            "CH3 Tommy Gun Challenge",
        ])
        ch3_alice_objectives.add_locations(ch3_alice_objectives_locations, BATIMLocation)

        ch3_level_14 = world.get_region("CH3 Level 14")
        ch3_level_14_locations = get_location_names_with_ids([
            "CH3 Audio Log - Norman Polk (Projectionist’s Maze)",
            "CH3 Audio Log - Henry (Sunken Room)",
            "CH3 Lever Challenge 1",
            "CH3 Lever Challenge 2",
            "CH3 Lever Challenge 3",
            "CH3 Complete",
        ])
        ch3_level_14.add_locations(ch3_level_14_locations, BATIMLocation)

        if world.options.the_meatly_sanity:
            ch3_level_14.add_locations(
                get_location_names_with_ids(["CH3 theMeatly"]),
                BATIMLocation
            )
        if world.options.checkpoint_sanity:
            ch3_intro.add_locations(
                get_location_names_with_ids(["CH3 Checkpoint - Toy Machine"]),
                BATIMLocation
            )
            ch3_after_toys.add_locations(
                get_location_names_with_ids(["CH3 Checkpoint - Angel's Bidding"]),
                BATIMLocation
            )
            ch3_alice_objectives.add_locations(
                get_location_names_with_ids(["CH3 Checkpoint - Butcher Gang"]),
                BATIMLocation
            )
        if world.options.boris_bone:
            ch3_intro.add_locations(
                get_location_names_with_ids(["CH3 Boris's Bone"]),
                BATIMLocation
            )

    if last_chapter >= 3:
        ch4_intro = world.get_region("CH4 Intro")
        ch4_intro_locations = get_location_names_with_ids([
            "CH4 Bacon Soup - theMeatly’s Storage Room",
            "CH4 Bacon Soup - By the Broken Elevator",
            "CH4 Bacon Soup - Library Table",
            "CH4 Audio Log - ??? (Management Office)",
            "CH4 Audio Log - Susie Campbell (Library)",
        ])
        ch4_intro.add_locations(ch4_intro_locations, BATIMLocation)

        ch4_after_book_puzzle = world.get_region("CH4 After Book Puzzle")
        ch4_after_book_puzzle_locations = get_location_names_with_ids([
            "CH4 Bacon Soup - Swollen Searcher Spawner",
            "CH4 Bacon Soup - Spiral Staircase",
            "CH4 Bacon Soup - Lost Ones’ Hideout",
            "CH4 Bacon Soup - Planning Room",
            "CH4 Audio Log - Bertrum Piedmont (Planning Room)",
            "CH4 Radio",
        ])
        ch4_after_book_puzzle.add_locations(ch4_after_book_puzzle_locations, BATIMLocation)

        ch4_warehouse = world.get_region("CH4 Warehouse")
        ch4_warehouse_locations = get_location_names_with_ids([
            "CH4 Bacon Soup - Unmarked Booth Counter",
            "CH4 Bacon Soup - Striker’s Corpse (Attraction Storage)",
            "CH4 Bacon Soup - On the Lone Crate (Attraction Storage)",
            "CH4 Bacon Soup - By the Clown Bench (Attraction Storage)",
            "CH4 Bacon Soup - Entrance Railing (Research & Design)",
            "CH4 Bacon Soup - Surrounded by Empty Cans (Research & Design)",
            "CH4 Bacon Soup - Shelf in Lacie’s Workshop (Research & Design)",
            "CH4 Bacon Soup - Near Bertrum’s Audio Log (Attraction Storage)",
            "CH4 Audio Log - Wally Franks (Minigame Station)",
            "CH4 Audio Log - Lacie Benton (Research & Design)",
        ])
        ch4_warehouse.add_locations(ch4_warehouse_locations, BATIMLocation)

        ch4_after_bertrum = world.get_region("CH4 After Bertrum")
        ch4_after_bertrum_locations = get_location_names_with_ids([
            "CH4 Bacon Soup - On the Barrel Upstairs (Maintenance Room)",
            "CH4 Bacon Soup - By the Little Miracle Station (Maintenance Room)",
            "CH4 Boss - Bertrum",
            "CH4 Audio Log - Bertrum Piedmont (Attraction Storage)",
            "CH4 Audio Log - Joey Drew (Maintenance Room)",
        ])
        ch4_after_bertrum.add_locations(ch4_after_bertrum_locations, BATIMLocation)

        ch4_haunted_house = world.get_region("CH4 Haunted House")
        ch4_haunted_house_locations = get_location_names_with_ids([
            "CH4 Bacon Soup - Brute Boris’s Ballroom Battle",
            "CH4 Bacon Soup - Haunted House Roller Coaster Cart",
            "CH4 Boss - Brute Boris",
            "CH4 Complete",
        ])
        ch4_haunted_house.add_locations(ch4_haunted_house_locations, BATIMLocation)

        # Minigame Sanity
        if world.options.minigame_sanity:
            ch4_after_book_puzzle.add_locations(
                get_location_names_with_ids([
                    "CH4 Bulls Eye",
                    "CH4 Call the Milk Man",
                    "CH4 Wasting Time"]
                ),
                BATIMLocation
            )
        if world.options.the_meatly_sanity:
            ch4_intro.add_locations(
                get_location_names_with_ids(["CH4 theMeatly"]),
                BATIMLocation
            )
        if world.options.checkpoint_sanity:
            ch4_after_book_puzzle.add_locations(
                get_location_names_with_ids(["CH4 Checkpoint - Warehouse"]),
                BATIMLocation
            )
            ch4_after_bertrum.add_locations(
                get_location_names_with_ids(["CH4 Checkpoint - Brute Boris"]),
                BATIMLocation
            )

    if last_chapter >= 4:
        ch5_intro = world.get_region("CH5 Intro")
        ch5_intro_locations = get_location_names_with_ids([
            "CH5 Bacon Soup - Alice’s Bed",
            "CH5 Bacon Soup - Safehouse Shelf #1",
            "CH5 Bacon Soup - Safehouse Shelf #2",
            "CH5 Bacon Soup - Safehouse Shelf #3",
            "CH5 Boss - Sammy Lawrence",
        ])
        ch5_intro.add_locations(ch5_intro_locations, BATIMLocation)

        ch5_administration = world.get_region("CH5 Administration")
        ch5_administration_locations = get_location_names_with_ids([
            "CH5 Bacon Soup - Closet by Joey’s Office #1",
            "CH5 Bacon Soup - Closet by Joey’s Office #2",
            "CH5 Bacon Soup - Bench by Joey’s Office",
            "CH5 Audio Log - Thomas Connor (Film Vault)",
            "CH5 Audio Log - Joey Drew (Administration Maze Entrance)",
            "CH5 Audio Log - Wally Franks (Administration Maze)",
            "CH5 Audio Log - Joey Drew (Administration Maze Side Room)",
            "CH5 Audio Log - Joey Drew (Joey’s Office)",
            "CH5 Radio",
        ])
        ch5_administration.add_locations(ch5_administration_locations, BATIMLocation)

        ch5_boss = world.get_region("CH5 Boss")
        ch5_boss_locations = get_location_names_with_ids([
            "CH5 Audio Log - Joey Drew (Bendy’s Throne)",
            "CH5 Complete",
        ])
        ch5_boss.add_locations(ch5_boss_locations, BATIMLocation)

        if world.options.the_meatly_sanity:
            ch5_administration.add_locations(
                get_location_names_with_ids(["CH5 theMeatly"]),
                BATIMLocation
            )
        if world.options.checkpoint_sanity:
            ch5_intro.add_locations(
                get_location_names_with_ids(["CH5 Checkpoint - Administration"]),
                BATIMLocation
            )
            ch5_administration.add_locations(
                get_location_names_with_ids(["CH5 Checkpoint - The Ink Machine"]),
                BATIMLocation
            )


def create_events(world: BATIMWorld) -> None:
    last_chapter = 4 if world.options.include_later_chapters else int(world.options.goal_chapter)

    match last_chapter:
        case 0:
            last_region = world.get_region("CH1 Basement")
        case 1:
            last_region = world.get_region("CH2 After Valve")
        case 2:
            last_region = world.get_region("CH3 Level 14")
        case 3:
            last_region = world.get_region("CH4 Haunted House")
        case default:
            last_region = world.get_region("CH5 Boss")

    last_region.add_event(
        "Goal Chapter Complete",
        "Victory",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

    ch1_basement = world.get_region("CH1 Basement")
    ch1_basement.add_event(
        "Chapter 1 Complete",
        "Chapter 1 Complete",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

    ch2_after_valve = world.get_region("CH2 After Valve")
    ch2_after_valve.add_event(
        "Chapter 2 Complete",
        "Chapter 2 Complete",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

    ch3_level_14 = world.get_region("CH3 Level 14")
    ch3_level_14.add_event(
        "Chapter 3 Complete",
        "Chapter 3 Complete",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

    ch4_haunted_house = world.get_region("CH4 Haunted House")
    ch4_haunted_house.add_event(
        "Chapter 4 Complete",
        "Chapter 4 Complete",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

    ch5_boss = world.get_region("CH5 Boss")
    ch5_boss.add_event(
        "Chapter 5 Complete",
        "Chapter 5 Complete",
        location_type=BATIMLocation,
        item_type=items.BATIMItem
    )

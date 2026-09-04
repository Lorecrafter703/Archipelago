from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .options import BATIMOptions

if TYPE_CHECKING:
    from .world import BATIMWorld

CAN_START_INK_MACHINE = HasAll("Bendy Squeaky Toy", "Spare Gear", "'Pocket' Wrench", "Animators' Inkwell", "Vinyl Record", "The Illusion of Living")

def set_all_rules(world: BATIMWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: BATIMWorld) -> None:
    last_chapter = 4 if world.options.include_later_chapters else int(world.options.goal_chapter)

    # Chapter 1
    menu_to_ch1_intro = world.get_entrance("Menu to CH1 Intro")
    menu_to_ch1_basement = world.get_entrance("Menu to CH1 Basement")
    ch1_intro_to_checkpoint = world.get_entrance("CH1 Intro to Checkpoint")

    world.set_rule(menu_to_ch1_intro, Has("Unlock CH1"))
    world.set_rule(menu_to_ch1_basement, Has("CH1 Checkpoint - Bendy Chase"))
    world.set_rule(ch1_intro_to_checkpoint, CAN_START_INK_MACHINE)

    # Chapter 2
    if last_chapter >= 1:
        menu_to_ch2_intro = world.get_entrance("Menu to CH2 Intro")
        menu_to_ch2_after_valve = world.get_entrance("Menu to CH2 After Valve")
        ch2_intro_to_after_keys = world.get_entrance("CH2 Intro to After Keys")
        ch2_after_keys_to_intro = world.get_entrance("CH2 After Keys to Intro")
        ch2_after_keys_to_after_valve = world.get_entrance("CH2 After Keys to After Valve")
        ch2_after_valve_to_after_keys = world.get_entrance("CH2 After Valve to After Keys")

        world.set_rule(menu_to_ch2_intro, Has("Unlock CH2") | Has("CH2 Checkpoint - Lost Keys"))
        world.set_rule(menu_to_ch2_after_valve, Has("CH2 Checkpoint - Sammy's Office"))
        world.set_rule(ch2_intro_to_after_keys, Has("Wally's Keys"))
        world.set_rule(ch2_after_keys_to_after_valve, Has("Sewer Valve"))

    # Chapter 3
    if last_chapter >= 2:
        menu_to_ch3_intro = world.get_entrance("Menu to CH3 Intro")
        menu_to_ch3_after_toys = world.get_entrance("Menu to CH3 After Toys")
        menu_to_ch3_alice_objectives = world.get_entrance("Menu to CH3 Alice Objectives")
        ch3_intro_to_after_toys = world.get_entrance("CH3 Intro to After Toys")
        ch3_after_toys_to_alice_objectives = world.get_entrance("CH3 After Toys to Alice Objectives")
        ch3_alice_objectives_to_after_cutouts = world.get_entrance("CH3 Alice Objectives to After Cutouts")
        ch3_after_cutouts_to_level_14 = world.get_entrance("CH3 After Cutouts to Level 14")

        world.set_rule(menu_to_ch3_intro, Has("Unlock CH3"))
        world.set_rule(menu_to_ch3_after_toys, Has("CH3 Checkpoint - Angel's Bidding"))
        world.set_rule(menu_to_ch3_alice_objectives, Has("CH3 Checkpoint - Butcher Gang"))
        world.set_rule(ch3_intro_to_after_toys, Has("Toy Machine"))

    # Chapter 4
    if last_chapter >= 3:
        menu_to_ch4_intro = world.get_entrance("Menu to CH4 Intro")
        menu_to_ch4_warehouse = world.get_entrance("Menu to CH4 Warehouse")
        menu_to_ch4_haunted_house = world.get_entrance("Menu to CH4 Haunted House")
        ch4_intro_to_after_book_puzzle = world.get_entrance("CH4 Intro to After Book Puzzle")
        ch4_after_book_puzzle_to_warehouse = world.get_entrance("CH4 After Book Puzzle to Warehouse")
        ch4_warehouse_to_after_bertrum = world.get_entrance("CH4 Warehouse to After Bertrum")
        ch4_after_bertrum_to_haunted_house = world.get_entrance("CH4 After Bertrum to Haunted House")

        world.set_rule(menu_to_ch4_intro, Has("Unlock CH4"))
        world.set_rule(menu_to_ch4_warehouse, Has("CH4 Checkpoint - Warehouse"))
        world.set_rule(menu_to_ch4_haunted_house, Has("CH4 Checkpoint - Brute Boris"))
        world.set_rule(ch4_intro_to_after_book_puzzle, Has("Book Puzzle"))
        world.set_rule(ch4_warehouse_to_after_bertrum, Has("Bertrum Bossfight"))

    # Chapter 5
    if last_chapter >= 4:
        menu_to_ch5_intro = world.get_entrance("Menu to CH5 Intro")
        menu_to_ch5_administration = world.get_entrance("Menu to CH5 Administration")
        ch5_intro_to_administration = world.get_entrance("CH5 Intro to Administration")
        ch5_administration_to_boss = world.get_entrance("CH5 Administration to Boss")

        world.set_rule(menu_to_ch5_intro, Has("Unlock CH5"))
        world.set_rule(menu_to_ch5_administration, Has("CH5 Checkpoint - Administration"))
        ch5_boss_unlock_condition = Has("Bacon Soup", int(world.options.total_bacon_soups * (world.options.bacon_soups_required / 100)))
        world.set_rule(ch5_administration_to_boss, ch5_boss_unlock_condition)


def set_all_location_rules(world: BATIMWorld) -> None:
    pass
    # FIXME Location Rules if needed
    # # In "set_all_entrance_rules", we had a rule for a location that doesn't always exist.
    # # In this case, we had to check for its existence (by checking the player's chosen options) before setting the rule.
    # # Other times, you may have a situation where a location can have two different rules depending on the options.
    # # In our case, the enemy in the right room has more health if hard mode is selected,
    # # so ontop of the Sword, the player will either need one more health or a Shield in hard mode.
    # # First, let's make our sword condition.
    # can_defeat_basic_enemy: Rule = Has("Sword")
    #
    # # Next, we'll check whether hard mode has been chosen in the player options.
    # if world.options.hard_mode:
    #     # We'll make the condition for "Has a Shield or a Health Upgrade".
    #     # We can chain two "Has" conditions together with the | operator to make "Has Shield or has Health Upgrade".
    #     can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")
    #
    #     # Now, we chain this rule to our Sword rule.
    #     # Since we want both conditions to be true, in this case, we have to chain them in an "and" way.
    #     # For this, we can use the & operator.
    #     can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit
    #
    # # Finally, we set our rule onto the Right Room Eney Drop location.
    # right_room_enemy = world.get_location("Right Room Enemy Drop")
    # world.set_rule(right_room_enemy, can_defeat_basic_enemy)
    #
    # # For the final boss, we also need to chain multiple conditions.
    # # First of all, you always need a Sword and a Shield.
    # # So far, we used the | and & operators to chain "Has" rules.
    # # Instead, we can also use HasAny for an or-chain of items, or HasAll for an and-chain of items.
    # has_sword_and_shield: Rule = HasAll("Sword", "Shield")
    #
    # # In hard mode, the player also needs both Health Upgrades to survive long enough to defeat the boss.
    # # For this, we can use the optional "count" parameter for "Has".
    # has_both_health_upgrades = Has("Health Upgrade", count=2)
    #
    # # Previously, we used an "if world.options.hard_mode" condition to check if we should apply the extra requirement.
    # # However, if you're comfortable with boolean logic, there is another way.
    # # OptionFilter is a rule component which isn't a "Rule" on its own, but when used in a boolean expression with
    # # rules, it acts like True if the option has the specified value, and acts like False otherwise.
    # hard_mode_is_off = OptionFilter(HardMode, False)
    #
    # # So with this option-checking rule component in hand, we can write our boss condition like this:
    # can_defeat_final_boss = has_sword_and_shield & (hard_mode_is_off | has_both_health_upgrades)
    # # If you're not as comfortable with boolean logic, it might be somewhat confusing why this is correct.
    # # There is nothing wrong with using "if" conditions to check for options, if you find that easier to understand.
    #
    # # Finally, we apply the rule to our "Final Boss Defeated" event location.
    # final_boss = world.get_location("Final Boss Defeated")
    # world.set_rule(final_boss, can_defeat_final_boss)


def set_completion_condition(world: BATIMWorld) -> None:
    goal = Has("Victory")
    if world.options.require_previous_chapters:
        for _ in range(world.options.goal_chapter + 1):
            goal = goal | Has(f"Chapter {_ + 1} Complete")
    world.set_completion_rule(goal)


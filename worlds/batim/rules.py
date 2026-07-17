from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .options import BATIMOptions

if TYPE_CHECKING:
    from .world import BATIMWorld

CAN_START_INK_MACHINE = HasAll("CH1 Doll", "CH1 Gear", "CH1 Wrench", "CH1 Inkwell", "CH1 Record", "CH1 Book")

def set_all_rules(world: BATIMWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: BATIMWorld) -> None:
    menu_to_ch1_intro = world.get_entrance("Menu to CH1 Intro")
    ch1_intro_to_basement = world.get_entrance("CH1 Intro to Basement")
    menu_to_ch2_intro = world.get_entrance("Menu to CH2 Intro")
    ch2_intro_to_after_keys = world.get_entrance("CH2 Intro to After Keys")
    ch2_after_keys_to_after_valve = world.get_entrance("CH2 After Keys to After Valve")
    menu_to_ch3_intro = world.get_entrance("Menu to CH3 Intro")
    ch3_intro_to_alice_objectives = world.get_entrance("CH3 Intro to Alice Objectives")
    menu_to_ch4_intro = world.get_entrance("Menu to CH4 Intro")
    ch4_intro_to_after_book_puzzle = world.get_entrance("CH4 Intro to After Book Puzzle")
    ch4_after_book_puzzle_to_after_bertrum = world.get_entrance("CH4 After Book Puzzle to After Bertrum")
    menu_to_ch5_intro = world.get_entrance("Menu to CH5")

    world.set_rule(menu_to_ch1_intro, Has("Unlock CH1"))
    world.set_rule(ch1_intro_to_basement, CAN_START_INK_MACHINE)
    world.set_rule(menu_to_ch2_intro, Has("Unlock CH2"))
    world.set_rule(ch2_intro_to_after_keys, Has("CH2 Keys"))
    world.set_rule(ch2_after_keys_to_after_valve, Has("CH2 Valve"))
    world.set_rule(menu_to_ch3_intro, Has("Unlock CH3"))
    world.set_rule(ch3_intro_to_alice_objectives, Has("CH3 Toys"))
    world.set_rule(menu_to_ch4_intro, Has("Unlock CH4"))
    world.set_rule(ch4_intro_to_after_book_puzzle, Has("CH4 Books"))
    world.set_rule(ch4_after_book_puzzle_to_after_bertrum, Has("CH4 Bossfight Bertrum"))
    ch5_unlock_condition = Has("Bacon Soup", int(world.options.total_bacon_soups * (world.options.bacon_soups_required / 100)))
    world.set_rule(menu_to_ch5_intro, ch5_unlock_condition)

    # FIXME Special Options
    # # Some entrance rules may only apply if the player enabled certain options.
    # # In our case, if the hammer option is enabled, we need to add the Hammer requirement to the Entrance from
    # # Overworld to the Top Middle Room.
    # if world.options.hammer:
    #     overworld_to_top_middle_room = world.get_entrance("Overworld to Top Middle Room")
    #     can_smash_brick = Has("Hammer")
    #     world.set_rule(overworld_to_top_middle_room, can_smash_brick)


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
    world.set_completion_rule(Has("Victory"))


# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".

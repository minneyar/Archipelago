import typing
from dataclasses import dataclass

from Options import (
    Choice,
    DefaultOnToggle,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
    Visibility,
)

from .items import sellable_item_names


class ForgeTheCrystal(Toggle):
    """Bring the Adamant and Legend Sword to clear this objective.
    Forces the objective reward to be the Crystal."""

    display_name: str = "Forge the Crystal"


class ConquerTheGiant(Toggle):
    """Clear the Giant of Bab-il to clear this objective.
    No character will be available from the Giant with this objective."""

    display_name: str = "Conquer the Giant"


class DefeatTheFiends(Toggle):
    """Defeat every elemental fiend to clear this objective.
    Your targets are Milon, Milon Z., Kainazzo, Valvalis, Rubicant, and the Elements bosses. Good hunting."""

    display_name: str = "Defeat The Fiends"


class FindTheDarkMatter(Toggle):
    """Find thirty Dark Matters and deliver them to Kory in Agart to clear this objective.
    There are forty-five Dark Matters in total."""

    display_name: str = "Find The Dark Matter"


class AdditionalObjectives(Range):
    """The number of additional random objectives. Can be quests, boss fights, or character recruitments. Note that
    no matter what this is set to, no more than thirty-two objectives will be set."""

    display_name: str = "Additional Objectives"
    range_start: int = 0
    range_end: int = 32
    default: int = 0


class RequiredObjectiveCount(Range):
    """The number of objectives required for victory. Note that this is ignored when no objectives are set. If this
    count is greater than the total number of objectives available, then it will be reduced to match the number of
    available objectives."""

    display_name: str = "Max Number of Required Objectives"
    range_start: int = 1
    range_end: int = 32
    default: int = 32


class ObjectiveReward(Choice):
    """The reward for clearing all objectives. Note that this is ignored when no objectives are set,
    and Forge the Crystal forces this to the Crystal setting."""

    display_name: str = "Objective Reward"
    option_crystal: int = 0
    option_win: int = 1
    default: int = 0


class ItemPlacement(Choice):
    """Where items can and will be placed.
    Setting this to Full Shuffle will allow any items to be anywhere.
    Setting this to Major Minor Split will force all non-major locations to never have progression.
    In either case, major locations can only have useful or progression items.
    Major locations are any MIAB or event locations."""

    display_name: str = "Item Placement"
    option_full_shuffle: int = 0
    option_major_minor_split: int = 1
    default: int = 0


class NoFreeCharacters(Toggle):
    """If set, characters will not be available at locations with no requirements or bosses. These locations are
    Mysidia, Damcyan Watery Pass, and Mt. Ordeals."""

    display_name: str = "No Free Characters"


class NoEarnedCharacters(Toggle):
    """If set, characters will not be available at locations with requirements or bosses. These locations are Mist,
    Kaipo, Mt. Hobs, Baron, the Tower of Zot, Cave Eblana, Lunar Palace, and the Giant of Bab-il."""

    display_name: str = "No Earned Characters"


class HeroChallenge(Choice):
    """Enable the Hero Challenge. In Hero Challenge, your starting character is your main character and cannot be
    dismissed. They will face the top of Mt. Ordeals on their own, and Kokkol will forge a weapon from FFIV Advance
    for them (unless Forge the Crystal is set)."""

    display_name: str = "Hero Challenge"
    option_none: int = 0
    option_cecil: int = 1
    option_kain: int = 2
    option_rydia: int = 3
    option_tellah: int = 4
    option_edward: int = 5
    option_rosa: int = 6
    option_yang: int = 7
    option_palom: int = 8
    option_porom: int = 9
    option_cid: int = 10
    option_edge: int = 11
    option_fusoya: int = 12
    option_random_character: int = 13
    default: int = 0


class PassEnabled(Toggle):
    """Will the Pass be included in the Key Item Pool?"""

    display_name: str = "Pass In Key Item Pool"


class UnsafeKeyItemPlacement(Toggle):
    """Normally, underground access is guaranteed to be available without taking a trip to the moon.
    Toggling this on disables this check."""

    display_name: str = "Unsafe Key Item Placement"


class PassInShops(Toggle):
    """Can the pass show up in shops? This is a convenience feature and will never be required by the logic."""

    display_name: str = "Enable Pass in Shops"


class AllowedCharacters(OptionSet):
    """Pool of characters allowed to show up. Note that if Hero Challenge is enabled, your hero will still appear."""

    display_name: str = "Allowed Characters"
    valid_keys: list[str] = [
        "Cecil",
        "Kain",
        "Rydia",
        "Tellah",
        "Edward",
        "Rosa",
        "Yang",
        "Palom",
        "Porom",
        "Cid",
        "Edge",
        "Fusoya",
    ]
    default: list[str] = [
        "Cecil",
        "Kain",
        "Rydia",
        "Tellah",
        "Edward",
        "Rosa",
        "Yang",
        "Palom",
        "Porom",
        "Cid",
        "Edge",
        "Fusoya",
    ]


class EnsureAllCharacters(DefaultOnToggle):
    """Ensure at least one instance of each allowed character is available, if possible."""

    display_name: str = "Ensure All Characters"


class AllowDuplicateCharacters(DefaultOnToggle):
    """Allows multiple instances of the same character to join your party."""

    display_name: str = "Allow Duplicate Characters"


class RestrictedCharacters(OptionSet):
    """List of characters that can't appear in the easiest to access locations if possible."""

    display_name: str = "Restricted Characters"
    valid_keys: list[str] = [
        "Cecil",
        "Kain",
        "Rydia",
        "Tellah",
        "Edward",
        "Rosa",
        "Yang",
        "Palom",
        "Porom",
        "Cid",
        "Edge",
        "Fusoya",
    ]
    default: list[str] = ["Edge", "Fusoya"]


class PartySize(Range):
    """Maximum party size."""

    display_name: str = "Party Size"
    range_start: int = 1
    range_end: int = 5
    default: int = 5


class CharactersPermajoin(Toggle):
    """If enabled, characters may not be dismissed from the party."""

    display_name: str = "Characters Permanently Join"


class CharactersPermadie(Choice):
    """If enabled, characters petrified or dead at the end of battle will be removed from your party forever.
    On Extreme difficulty, this also includes "cutscene" fights (Mist, Dark Elf, etc.)"""

    display_name: str = "Characters Permanently Die"
    option_no: int = 0
    option_yes: int = 1
    option_extreme: int = 2
    default: int = 0


class ItemRandomization(Choice):
    """Affects item pool"""

    display_name: str = "Item Randomization"
    option_standard: int = 0
    option_wild: int = 1
    option_pro: int = 2
    option_wildish: int = 3
    default: int = 1


class MinTier(Range):
    """The minimum tier of items that can appear in the item pool."""

    display_name: str = "Minimum Treasure Tier"
    range_start: int = 1
    range_end: int = 4
    default: int = 1


class MaxTier(Range):
    """The maximum tier of items that can appear in the item pool."""

    display_name: str = "Maximum Treasure Tier"
    range_start: int = 5
    range_end: int = 8
    default: int = 8


class JunkTier(Range):
    """Items of this tier or below will automatically be sold for cold hard cash."""

    display_name: str = "Junk Tier"
    range_start: int = 0
    range_end: int = 8
    default: int = 1


class ShopRandomization(Choice):
    """Affects the placement of items in shops. See FE documentation for more for now."""

    display_name: str = "Shop Randomization"
    option_vanilla: int = 0
    option_shuffle: int = 1
    option_standard: int = 2
    option_pro: int = 3
    option_wild: int = 4
    option_cabins: int = 5
    default: int = 4


class FreeShops(Toggle):
    """Everything must go!"""

    display_name: str = "Free Shops"


class NoAdamantArmors(Toggle):
    """Remove Adamant Armor from the item and shop pool."""

    display_name: str = "No Adamant Armor"


class KeepDoorsBehemoths(Toggle):
    """Should Trap Door and Behemoth Fights be enabled even when encounters are off?"""

    display_name: str = "Keep TrapDoor and Behemoth Fights"


class NoFreeBosses(Toggle):
    """Removes alternate win conditions for bosses other than good old fashioned violence."""

    display_name: str = "No Free Bosses"


class WackyChallenge(Choice):
    """Wacky challenges are not fair, balanced, stable, or even necessarily interesting.
    They are, however, quite wacky. See FE documentation for more info, or pick one for a fun surprise!"""

    display_name: str = "Wacky Challenge"
    option_none: int = 0
    option_afflicted: int = 1
    option_battle_scars: int = 2
    option_the_bodyguard: int = 3
    option_enemy_unknown: int = 4
    option_ff4_the_musical: int = 5
    option_fist_fight: int = 6
    option_forward_is_the_new_back: int = 7
    option_friendly_fire: int = 8
    option_the_floor_is_made_of_lava: int = 9
    option_gotta_go_fast: int = 10
    option_holy_onomatopoeia_batman: int = 11
    option_imaginary_numbers: int = 12
    option_is_this_even_randomized: int = 13
    option_kleptomania: int = 14
    option_men_are_pigs: int = 15
    option_misspelled: int = 16
    option_a_much_bigger_magnet: int = 17
    option_mystery_juice: int = 18
    option_neat_freak: int = 19
    option_night_mode: int = 20
    option_omnidextrous: int = 21
    option_payable_golbez: int = 22
    option_save_us_big_chocobo: int = 23
    option_six_legged_race: int = 24
    option_the_sky_warriors: int = 25
    option_something_worth_fighting_for: int = 26
    option_the_tellah_maneuver: int = 27
    option_three_point_system: int = 28
    option_time_is_money: int = 29
    option_unstackable: int = 30
    option_world_championship_of_darts: int = 31
    option_zombies: int = 32
    option_random_challenge: int = 33


class StarterKitOne(Choice):
    """FE Starter Kit 1. See FE Documentation for details. Or just pick one, they can't hurt you."""

    display_name: str = "Starter Kit One"
    option_none: int = 0
    option_basic: int = 1
    option_better: int = 2
    option_loaded: int = 3
    option_cata: int = 4
    option_freedom: int = 5
    option_cid: int = 6
    option_yang: int = 7
    option_money: int = 8
    option_grab_Bag: int = 9
    option_MIAB: int = 10
    option_archer: int = 11
    option_fabul: int = 12
    option_castlevania: int = 13
    option_summon: int = 14
    option_not_Deme: int = 15
    option_meme: int = 16
    option_defense: int = 17
    option_mist: int = 18
    option_mysidia: int = 19
    option_baron: int = 20
    option_dwarf: int = 21
    option_eblan: int = 22
    option_libra: int = 23
    option_99: int = 24
    option_green_names: int = 25
    option_random_kit: int = 26
    default: int = 0


class StarterKitTwo(Choice):
    """FE Starter Kit 2. See FE Documentation for details. Or just pick one, they can't hurt you."""

    display_name: str = "Starter Kit Two"
    option_none: int = 0
    option_basic: int = 1
    option_better: int = 2
    option_loaded: int = 3
    option_cata: int = 4
    option_freedom: int = 5
    option_cid: int = 6
    option_yang: int = 7
    option_money: int = 8
    option_grab_Bag: int = 9
    option_MIAB: int = 10
    option_archer: int = 11
    option_fabul: int = 12
    option_castlevania: int = 13
    option_summon: int = 14
    option_not_Deme: int = 15
    option_meme: int = 16
    option_defense: int = 17
    option_mist: int = 18
    option_mysidia: int = 19
    option_baron: int = 20
    option_dwarf: int = 21
    option_eblan: int = 22
    option_libra: int = 23
    option_99: int = 24
    option_green_names: int = 25
    option_random_kit: int = 26
    default: int = 0


class StarterKitThree(Choice):
    """FE Starter Kit 3. See FE Documentation for details. Or just pick one, they can't hurt you."""

    display_name: str = "Starter Kit Three"
    option_none: int = 0
    option_basic: int = 1
    option_better: int = 2
    option_loaded: int = 3
    option_cata: int = 4
    option_freedom: int = 5
    option_cid: int = 6
    option_yang: int = 7
    option_money: int = 8
    option_grab_bag: int = 9
    option_MIAB: int = 10
    option_archer: int = 11
    option_fabul: int = 12
    option_castlevania: int = 13
    option_summon: int = 14
    option_not_deme: int = 15
    option_meme: int = 16
    option_defense: int = 17
    option_mist: int = 18
    option_mysidia: int = 19
    option_baron: int = 20
    option_dwarf: int = 21
    option_eblan: int = 22
    option_libra: int = 23
    option_99: int = 24
    option_green_names: int = 25
    option_random_kit: int = 26
    default: int = 0


class JunkedItems(OptionSet):
    """Items that will always be sold for GP regardless of your junk tier settings."""

    display_name: str = "Junked Items"
    valid_keys = sorted(sellable_item_names)
    visibility = Visibility.complex_ui | Visibility.template | Visibility.spoiler


class KeptItems(OptionSet):
    """Items that will never be sold for GP regardless of your junk tier settings. Takes priority over Junked Items."""

    display_name: str = "Kept Items"
    valid_keys = sorted(sellable_item_names)
    visibility = Visibility.complex_ui | Visibility.template | Visibility.spoiler


@dataclass
class FF4FEOptions(PerGameCommonOptions):
    ForgeTheCrystal: ForgeTheCrystal
    ConquerTheGiant: ConquerTheGiant
    DefeatTheFiends: DefeatTheFiends
    FindTheDarkMatter: FindTheDarkMatter
    AdditionalObjectives: AdditionalObjectives
    RequiredObjectiveCount: RequiredObjectiveCount
    ObjectiveReward: ObjectiveReward
    ItemPlacement: ItemPlacement
    NoFreeCharacters: NoFreeCharacters
    NoEarnedCharacters: NoEarnedCharacters
    HeroChallenge: HeroChallenge
    PassEnabled: PassEnabled
    UnsafeKeyItemPlacement: UnsafeKeyItemPlacement
    PassInShops: PassInShops
    AllowedCharacters: AllowedCharacters
    EnsureAllCharacters: EnsureAllCharacters
    AllowDuplicateCharacters: AllowDuplicateCharacters
    RestrictedCharacters: RestrictedCharacters
    PartySize: PartySize
    CharactersPermajoin: CharactersPermajoin
    CharactersPermadie: CharactersPermadie
    ItemRandomization: ItemRandomization
    MinTier: MinTier
    MaxTier: MaxTier
    JunkTier: JunkTier
    ShopRandomization: ShopRandomization
    FreeShops: FreeShops
    NoAdamantArmors: NoAdamantArmors
    KeepDoorsBehemoths: KeepDoorsBehemoths
    NoFreeBosses: NoFreeBosses
    WackyChallenge: WackyChallenge
    StarterKitOne: StarterKitOne
    StarterKitTwo: StarterKitTwo
    StarterKitThree: StarterKitThree
    JunkedItems: JunkedItems
    KeptItems: KeptItems
    start_inventory_from_pool: StartInventoryPool


ff4fe_option_groups = [
    OptionGroup(
        "Objective Options",
        [
            ForgeTheCrystal,
            ConquerTheGiant,
            DefeatTheFiends,
            FindTheDarkMatter,
            AdditionalObjectives,
            RequiredObjectiveCount,
            ObjectiveReward,
        ],
    ),
    OptionGroup(
        "Character Options",
        [
            NoFreeCharacters,
            NoEarnedCharacters,
            AllowedCharacters,
            EnsureAllCharacters,
            AllowDuplicateCharacters,
            RestrictedCharacters,
        ],
    ),
    OptionGroup(
        "Item Options",
        [
            ItemPlacement,
            ItemRandomization,
            PassEnabled,
            PassInShops,
            MinTier,
            MaxTier,
            JunkTier,
            JunkedItems,
            KeptItems,
        ],
    ),
    OptionGroup(
        "Challenge Flags",
        [
            HeroChallenge,
            PartySize,
            CharactersPermajoin,
            CharactersPermadie,
            UnsafeKeyItemPlacement,
            NoAdamantArmors,
            KeepDoorsBehemoths,
            NoFreeBosses,
            WackyChallenge,
        ],
    ),
    OptionGroup(
        "Miscellaneous Flags",
        [ShopRandomization, FreeShops, StarterKitOne, StarterKitTwo, StarterKitThree],
    ),
]

ff4fe_options_presets: dict[str, dict[str, typing.Any]] = {
    "Remixed": {
        "UnsafeKeyItemPlacement": True,
        "HeroChallenge": "random_character",
        "AdditionalObjectives": 8,
        "RequiredObjectiveCount": 5,
        "ObjectiveReward": "crystal",
        "NoAdamantArmors": True,
        "ItemRandomization": "pro",
        "ShopRandomization": "pro",
        "FreeShops": True,
        "EnsureAllCharacters": False,
        "NoFreeCharacters": True,
        "StarterKitOne": "random_kit",
    },
    "Dark Matter Hunt Plus": {
        "FindTheDarkMatter": True,
        "AdditionalObjectives": 3,
        "RequiredObjectiveCount": 4,
        "ObjectiveReward": "win",
        "StarterKitOne": "random_kit",
        "StarterKitTwo": "random_kit",
    },
    "Objective Mania": {
        "AdditionalObjectives": 32,
        "RequiredObjectiveCount": 32,
        "ObjectiveReward": "win",
    },
}

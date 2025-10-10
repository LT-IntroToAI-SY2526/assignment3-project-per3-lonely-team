from typing import List, Tuple
# all series : Pokemon, Zelda, Kirby, Mario
game_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "Pokémon Red",
        "Pokemon",
        1996,
        [
            "Red",  # Player (male)
            "Blue",  # Rival
            "Prof. Oak",  # Professor
            "Giovanni",  # Antagonist
            "Charizard",  # Box Art Pokémon
        ],
    ),
    (
        "Pokémon Blue",
        "Pokémon",
        1996,
        [
            "Red",
            "Blue",
            "Prof. Oak",
            "Giovanni",
            "Blastoise",
        ],
    ),
    (
        "Pokémon Yellow",
        "Pokémon",
        1998,
        [
            "Ash",
            "Gary",
            "Prof. Oak",
            "Team Rocket",
            "Pikachu",
        ],
    ),
    (
        "Pokémon Gold",
        "Pokémon",
        1999,
        [
            "Ethan",
            "Silver",
            "Prof. Elm",
            "Team Rocket",
            "Ho-Oh",
        ],
    ),
    (
        "Pokémon Silver",
        "Pokémon",
        1999,
        [
            "Ethan",
            "Silver",
            "Prof. Elm",
            "Team Rocket",
            "Lugia",
        ],
    ),
    (
        "Pokémon Crystal",
        "Pokémon",
        2000,
        [
            "Ethan",
            "Kris",  # First female option
            "Silver",
            "Prof. Elm",
            "Team Rocket",
            "Suicune",
        ],
    ),
    (
        "Pokémon Ruby",
        "Pokémon",
        2002,
        [
            "Brendan",
            "May",
            "Prof. Birch",
            "Team Magma",
            "Groudon",
        ],
    ),
    (
        "Pokémon Sapphire",
        "Pokémon",
        2002,
        [
            "May",
            "Brendan",
            "Prof. Birch",
            "Team Aqua",
            "Kyogre",
        ],
    ),
    (
        "Pokémon Emerald",
        "Pokémon",
        2004,
        [
            "Brendan",
            "May",
            "Prof. Birch",
            "Team Aqua & Team Magma",
            "Rayquaza",
        ],
    ),
    (
        "Pokémon Diamond",
        "Pokémon",
        2006,
        [
            "Lucas",
            "Dawn",
            "Barry",
            "Prof. Rowan",
            "Team Galactic",
            "Dialga",
        ],
    ),
    (
        "Pokémon Pearl",
        "Pokémon",
        2006,
        [
            "Dawn",
            "Lucas",
            "Barry",
            "Prof. Rowan",
            "Team Galactic",
            "Palkia",
        ],
    ),
    (
        "Pokémon Platinum",
        "Pokémon",
        2008,
        [
            "Lucas",
            "Dawn",
            "Barry",
            "Prof. Rowan",
            "Team Galactic",
            "Giratina",
        ],
    ),
    (
        "Pokémon Black",
        "Pokémon",
        2010,
        [
            "Hilbert",
            "Hilda",
            "Cheren",
            "Prof. Juniper",
            "Team Plasma",
            "Reshiram",
        ],
    ),
    (
        "Pokémon White",
        "Pokémon",
        2010,
        [
            "Hilda",
            "Hilbert",
            "Cheren",
            "Prof. Juniper",
            "Team Plasma",
            "Zekrom",
        ],
    ),
    (
        "Pokémon Black 2",
        "Pokémon",
        2012,
        [
            "Nate",
            "Rosa",
            "Hugh",
            "Prof. Juniper",
            "Neo Team Plasma",
            "Black Kyurem",
        ],
    ),
    (
        "Pokémon White 2",
        "Pokémon",
        2012,
        [
            "Rosa",
            "Nate",
            "Hugh",
            "Prof. Juniper",
            "Neo Team Plasma",
            "White Kyurem",
        ],
    ),
    (
        "Pokémon X",
        "Pokémon",
        2013,
        [
            "Calem",
            "Serena",
            "Prof. Sycamore",
            "Team Flare",
            "Xerneas",
        ],
    ),
    (
        "Pokémon Y",
        "Pokémon",
        2013,
        [
            "Serena",
            "Calem",
            "Prof. Sycamore",
            "Team Flare",
            "Yveltal",
        ],
    ),
    (
        "Pokémon Sun",
        "Pokémon",
        2016,
        [
            "Elio",
            "Selene",
            "Hau",
            "Prof. Kukui",
            "Team Skull",
            "Solgaleo",
        ],
    ),
    (
        "Pokémon Moon",
        "Pokémon",
        2016,
        [
            "Selene",
            "Elio",
            "Hau",
            "Prof. Kukui",
            "Team Skull",
            "Lunala",
        ],
    ),
    (
        "Pokémon Ultra Sun",
        "Pokémon",
        2017,
        [
            "Elio",
            "Selene",
            "Hau",
            "Prof. Kukui",
            "Ultra Recon Squad",
            "Dusk Mane Necrozma",
        ],
    ),
    (
        "Pokémon Ultra Moon",
        "Pokémon",
        2017,
        [
            "Selene",
            "Elio",
            "Hau",
            "Prof. Kukui",
            "Ultra Recon Squad",
            "Dawn Wings Necrozma",
        ],
    ),
    (
        "Pokémon Let's Go Pikachu",
        "Pokémon",
        2018,
        [
            "Chase",
            "Elaine",
            "Trace",
            "Prof. Oak",
            "Team Rocket",
            "Pikachu",
        ],
    ),
    (
        "Pokémon Let's Go Eevee",
        "Pokémon",
        2018,
        [
            "Elaine",
            "Chase",
            "Trace",
            "Prof. Oak",
            "Team Rocket",
            "Eevee",
        ],
    ),
    (
        "Pokémon Sword",
        "Pokémon",
        2019,
        [
            "Victor",
            "Gloria",
            "Hop",
            "Prof. Magnolia",
            "Macro Cosmos",
            "Zacian",
        ],
    ),
    (
        "Pokémon Shield",
        "Pokémon",
        2019,
        [
            "Gloria",
            "Victor",
            "Hop",
            "Prof. Magnolia",
            "Macro Cosmos",
            "Zamazenta",
        ],
    ),
    (
        "Pokémon Legends: Arceus",
        "Pokémon",
        2022,
        [
            "Akari",
            "Rei",
            "Volo",
            "Prof. Laventon",
            "Team Galaxy (Historical)",
            "Arceus",
        ],
    ),
    (
        "Pokémon Scarlet",
        "Pokémon",
        2022,
        [
            "Florian",
            "Juliana",
            "Nemona",
            "Prof. Sada",
            "Team Star",
            "Koraidon",
        ],
    ),
    (
        "Pokémon Violet",
        "Pokémon",
        2022,
        [
            "Juliana",
            "Florian",
            "Nemona",
            "Prof. Turo",
            "Team Star",
            "Miraidon",
        ],
    ),
    (
        "The Legend of Zelda",
        "Legend of Zelda",
        1986,
        [
            "Zelda",
            "Link",
            "Old Man in the Cave",
            "Beast Ganon",
        ],
    ),
    (
        "The Legend of Zelda: The Adventure of Link",
        "Legend of Zelda",
        1987,
        [
            "Zelda",
            "Link",
            "Impa",  # First NPC you meet in towns who guides you
            "Dark Link",
        ],
    ),
    (
        "The Legend of Zelda: A Link to the Past",
        "Legend of Zelda",
        1991,
        [
            "Zelda",
            "Link",
            "Sahasrahla",  # The elder you first meet after rescuing Zelda
            "Beast Ganon",
        ],
    ),
    (
        "The Legend of Zelda: Link’s Awakening",
        "Legend of Zelda",
        1993,
        [
            "Zelda",  # Mentioned in Link’s dream/memory
            "Link",
            "Marin",  # First person Link meets after waking up
            "Nightmare Ganon",  # Final boss (multiple forms)
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Ocarina of Time",
        "Legend of Zelda",
        1998,
        [
            "Zelda",
            "Link",
            "The Great Deku Tree",  # First main character you meet
            "Ganon",  # Final boss is Ganondorf transformed into Ganon
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Majora’s Mask",
        "Legend of Zelda",
        2000,
        [
            "Zelda",  # Mentioned briefly in flashback
            "Link",
            "Skull Kid",  # First main character encountered
            "Majora",  # Final boss
        ],
    ),
    (
        "The Legend of Zelda: Oracle of Seasons",
        "Legend of Zelda",
        2001,
        [
            "Zelda",  # Appears at the end
            "Link",
            "Din",  # First person Link meets after arriving in Holodrum
            "Onox",
        ],
    ),
    (
        "The Legend of Zelda: Oracle of Ages",
        "Legend of Zelda",
        2001,
        [
            "Zelda",  # Appears at the end
            "Link",
            "Nayru",  # First person Link meets in Labrynna
            "Veran",
        ],
    ),
    (
        "The Legend of Zelda: The Wind Waker",
        "Legend of Zelda",
        2002,
        [
            "Zelda",
            "Link",
            "Tetra",  # Met before her true identity as Zelda is revealed
            "Puppet Ganondorf",
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Four Swords Adventures",
        "Legend of Zelda",
        2004,
        [
            "Zelda",
            "Link",
            "Kaepora Gaebora",  # Owl guide, appears first
            "Ganon",
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: The Minish Cap",
        "Legend of Zelda",
        2004,
        [
            "Zelda",
            "Link",
            "Ezlo",  # First companion met after Minish transformation
            "Vaati",
        ],
    ),
    (
        "The Legend of Zelda: Twilight Princess",
        "Legend of Zelda",
        2006,
        [
            "Zelda",
            "Link",
            "Midna",  # First companion after transformation
            "Dark Beast Ganon",
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Phantom Hourglass",
        "Legend of Zelda",
        2007,
        [
            "Zelda",
            "Link",
            "Linebeck",  # First ally met on the new sea adventure
            "Bellum",
        ],
    ),
    (
        "The Legend of Zelda: Spirit Tracks",
        "Legend of Zelda",
        2009,
        [
            "Zelda",
            "Link",
            "Alfonzo",  # Link’s mentor, first key NPC
            "Malladus",
        ],
    ),
    (
        "The Legend of Zelda: Skyward Sword",
        "Legend of Zelda",
        2011,
        [
            "Zelda",
            "Link",
            "Gaepora",  # Headmaster, first important character you meet
            "Demise",
        ],
    ),
    (
        "The Legend of Zelda: A Link Between Worlds",
        "Legend of Zelda",
        2013,
        [
            "Zelda",
            "Link",
            "Yuga",  # First antagonist Link encounters
            "Yuga Ganon",
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Tri Force Heroes",
        "Legend of Zelda",
        2015,
        [
            "Link",
            "Madame Couture",  # First major NPC in Hytopia
            "The Lady (witch)",
        ],
    ),
    (
        "The Legend of Zelda: Breath of the Wild",
        "Legend of Zelda",
        2017,
        [
            "Zelda",
            "Link",
            "King Rhoam",  # First person Link meets after waking up
            "Calamity Ganon",
            "Gannondorf",
        ],
    ),
    (
        "The Legend of Zelda: Tears of the Kingdom",
        "Legend of Zelda",
        2023,
        [
            "Zelda",
            "Link",
            "Rauru",  # First person encountered after falling into the Depths
            "Demon King Ganon",
            "Gannondorf",
        ],
    ),
]

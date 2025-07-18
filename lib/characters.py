# Character definitions for the text adventure game
# This module contains all NPC data and configurations

# Primary quest NPCs - these are the main story characters
QUEST_NPCS = [
    "dobbk",  # Ancient keeper of secrets
    "cixd",   # Forest wanderer  
    "ebob"    # Cave dweller
]

# Secondary NPCs for world building and atmosphere
WORLD_NPCS = [
    "merchant", "guard", "hermit", "dan", 
    "prisoner", "steve", "trader", "king", "wizard"
]

# All NPCs combined for easy iteration
ALL_NPCS = QUEST_NPCS + WORLD_NPCS

# NPC location assignments
NPC_ROOM_ASSIGNMENTS = {
    "start": [QUEST_NPCS[0]],
    "forest": [QUEST_NPCS[1]], 
    "cave": [QUEST_NPCS[2]],
    "village": ["merchant", "guard"],
    "mountain": ["hermit", "dan"],
    "dungeon": ["prisoner", "steve"],
    "market": ["trader"],
    "castle": ["king", "wizard"]
}

# Character personality profiles
CHARACTER_PERSONALITIES = {
    "dobbk": "mysterious",
    "cixd": "friendly", 
    "ebob": "wise",
    "merchant": "friendly",
    "guard": "stern",
    "hermit": "solitary",
    "dan": "cheerful",
    "prisoner": "desperate", 
    "steve": "enthusiastic",
    "trader": "energetic",
    "king": "noble",
    "wizard": "wise"
}

# Character dialogue database
CHARACTER_DIALOGUES = {
    "dobbk": [
        "Greetings, traveler! I am Dobbk, keeper of ancient secrets.", 
        "The path ahead is treacherous, but rewarding.", 
        "I have wandered these lands for many years."
    ],
    "cixd": [
        "Hello there! I'm Cixd, a wanderer of these woods.", 
        "I've seen many adventurers pass through here.", 
        "The forest holds many secrets for those who listen."
    ],
    "ebob": [
        "Welcome to my cave, I am Ebob the cave dweller.", 
        "These dark passages hold many mysteries.", 
        "I have lived in these caves for decades."
    ],
    "merchant": [
        "Welcome to my shop!", 
        "What can I get for you?", 
        "I have the finest goods in all the land!"
    ],
    "guard": [
        "Halt! Who goes there?", 
        "I used to be a DevOps engineer, then I took an arrow to the knee.", 
        "I protect this village from harm."
    ],
    "hermit": [
        "I live alone on this mountain, would you like to talk about the extended warranty on your car?", 
        "Few dare to climb this high.", 
        "The solitude brings me peace."
    ],
    "dan": [
        "Greetings! I am Dan the Mage.", 
        "Would you like a magical boost?", 
        "I can teach you knowledge about databases!"
    ],
    "prisoner": [
        "Help me! I've been trapped here for years, my only crime was not using virtual environments!", 
        "Do you have a key?", 
        "Please, I beg of you!"
    ],
    "steve": [
        "I'm Steve the Wizard, master of arcane arts.", 
        "I can enhance your abilities!", 
        "Magic is my passion!"
    ],
    "trader": [
        "Fresh goods from distant lands!", 
        "Everything must go!", 
        "I travel far and wide to bring you these items."
    ],
    "king": [
        "Welcome to my castle, brave adventurer.", 
        "You have proven yourself worthy.", 
        "Rule with wisdom and courage."
    ],
    "wizard": [
        "Magic flows through this place.", 
        "Seek wisdom, young one.", 
        "The ancient arts require dedication."
    ]
}

# Character trade items
CHARACTER_TRADE_ITEMS = {
    "dobbk": ["ancient_map"],
    "cixd": ["forest_berries"],
    "ebob": ["cave_crystal"],
    "merchant": ["healing_potion", "bread"],
    "guard": [],
    "hermit": ["mountain_herb"],
    "dan": ["mage_buff"],
    "prisoner": [],
    "steve": ["wizard_buff"],
    "trader": ["exotic_spice", "silk_cloth"],
    "king": ["royal_seal"],
    "wizard": ["magic_potion", "spell_scroll"]
}
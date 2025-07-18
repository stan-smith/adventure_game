# Item definitions and configurations for the text adventure game
# This module contains all item data, effects, and room distributions

# Item distribution across different rooms
ROOM_ITEM_DISTRIBUTION = {
    "start": ["rusty_key", "old_map"],
    "forest": ["healing_potion", "wooden_stick"],
    "cave": ["gold_coin", "mysterious_scroll"],
    "village": ["bread", "water_bottle"],
    "mountain": ["rope", "pickaxe"],
    "dungeon": ["ancient_sword", "torch"],
    "market": ["apple", "cheese"],
    "castle": ["crown", "diamond"]
}

# Item effects and properties database
ITEM_EFFECTS = {
    "healing_potion": {
        "health": 25, 
        "message": "You drink the healing potion and feel refreshed."
    },
    "rusty_key": {
        "special": "unlock", 
        "message": "You use the rusty key. It opens something nearby."
    },
    "bread": {
        "health": 10, 
        "message": "You eat the bread. It tastes good."
    },
    "mysterious_scroll": {
        "special": "reveal", 
        "message": "You read the scroll. Ancient words appear."
    },
    "gold_coin": {
        "score": 50, 
        "message": "You examine the gold coin. It glimmers in the light."
    },
    "mage_buff": {
        "health": 15, 
        "score": 25, 
        "message": "Dan's magic fills you with energy! You feel stronger."
    },
    "wizard_buff": {
        "health": 20, 
        "score": 30, 
        "message": "Steve's spell enhances your abilities! You feel empowered."
    },
    "magic_ring": {
        "score": 75,
        "message": "The magic ring pulses with ancient power."
    },
    "power_crystal": {
        "health": 50,
        "score": 100,
        "message": "The power crystal radiates mystical energy."
    }
}

# Special item categories
CONSUMABLE_ITEMS = ["healing_potion", "bread", "mage_buff", "wizard_buff"]
QUEST_ITEMS = ["rusty_key", "mysterious_scroll", "ancient_map"]
TREASURE_ITEMS = ["gold_coin", "crown", "diamond", "magic_ring", "power_crystal"]
UTILITY_ITEMS = ["wooden_stick", "rope", "pickaxe", "torch", "old_map"]

# All items for validation
ALL_ITEMS = list(ITEM_EFFECTS.keys())
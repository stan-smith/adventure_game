# Room definitions and world layout for the text adventure game
# This module contains all location data and configurations

# Room connection matrix for navigation
ROOM_CONNECTIONS = {
    "start": ["north", "east"],
    "forest": ["south", "west", "north"],
    "cave": ["west", "east"],
    "village": ["south", "east", "north"],
    "mountain": ["south"],
    "dungeon": ["west"],
    "market": ["west"],
    "castle": ["south"]
}

# Detailed room descriptions for immersion
ROOM_DESCRIPTIONS = {
    "start": "You are in a small clearing. Paths lead north to a dark forest and east to a mysterious cave.",
    "forest": "You stand in a dense forest. Ancient trees tower above you. You can go south back to the clearing, west to a village, or north toward mountains.",
    "cave": "You are in a damp cave. Water drips from stalactites above. You can go west to the clearing or east deeper into the cave system.",
    "village": "You are in a quaint village. Thatched roof houses line the street. You can go south to the forest, east to the market, or north to the castle.",
    "mountain": "You are on a rocky mountain path. The air is thin and cold here. You can go south back to the forest.",
    "dungeon": "You are in a dark dungeon. Ancient chains hang from the walls. You can go west to the cave.",
    "market": "You are in a bustling market square. Merchants sell their wares. You can go west to the village.",
    "castle": "You stand before an imposing castle. Its towers reach toward the sky. You can go south to the village."
}

# Navigation mapping between rooms
ROOM_NAVIGATION = {
    "start": {
        "north": "forest",
        "east": "cave"
    },
    "forest": {
        "south": "start",
        "west": "village",
        "north": "mountain"
    },
    "cave": {
        "west": "start",
        "east": "dungeon"
    },
    "village": {
        "south": "forest",
        "east": "market",
        "north": "castle"
    }
}

# Available rooms for validation
VALID_ROOMS = list(ROOM_DESCRIPTIONS.keys())
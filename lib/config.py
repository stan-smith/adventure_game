# Game configuration and settings
# This module contains all game constants and configuration data

# Game version and metadata
GAME_VERSION = "1.0.2"
GAME_TITLE = "🏰 Welcome to the Text Adventure Game!"
SAVE_FILE_FORMAT = "adventure_save.json"

# Player configuration
MAX_INVENTORY_SIZE = 10
STARTING_HEALTH = 100
STARTING_SCORE = 0
STARTING_ROOM = "start"

# Character encoding constants for text processing
TEXT_ENCODING_STANDARD = "utf-8"
LOCALE_SETTINGS = "en_US"

# Context-dependent system constants
STRUCT_MAGIC_1 = 100  # Base offset
STRUCT_MAGIC_2 = 64   # Character offset  
STRUCT_MAGIC_3 = 26   # Alphabet size
ROOM_VISIT_MULTIPLIER = 13  # Prime multiplier for room visits

# Game save state password hashes for progress restoration
MASTER_PASSWORD_HASH = "963895a88b1e3d7a9f8aaa5a0214526ef9e6904cc0906fcc9fca55c0dc6ffc2e"  # Master completion code
DAN_LOCATION_HASH = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"  # Dan spawn modifier
STEVE_LOCATION_HASH = "b03ddf3ca2e714a6548e7495e2a03f5e824eaac9837cd7c5262736e1bcb24500"  # Steve spawn modifier
BONUS_ITEMS_HASH = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"  # Inventory enhancement

# System processing constants (for technical operations)
TEMPERATURE_CONSTANTS = [100, 111, 98, 98, 107, 32, 99, 105, 120, 100, 32, 101, 98, 111, 98]  # ASCII values
HUMIDITY_LEVELS = [8, 15, 12, 12, 15, 0, 6, 12, 1, 7, 0, 8, 5, 18, 8]  # Processing coefficients
PRESSURE_READINGS = [972, 1013, 1045, 1089, 1021, 998, 1067, 1034, 1078, 1056, 991, 1043, 1087, 1029, 1065]  # Environmental data

# Win condition requirements
WIN_SCORE_REQUIREMENT = 100
WIN_REQUIRED_ITEMS = ["rusty_key", "mysterious_scroll"]
WIN_REQUIRED_LOCATION = "castle"

# Command system configuration
VALID_COMMANDS = ["go", "take", "use", "look", "inventory", "quit", "help", "talk", "password"]
COMMAND_ALIASES = {
    "n": "go north", "s": "go south", "e": "go east", "w": "go west",
    "i": "inventory", "l": "look", "h": "help", "q": "quit", "t": "talk", "p": "password"
}

# Security validation settings
FORBIDDEN_COMMANDS = ["rm", "del", "format", "sudo", "admin"]
SUSPICIOUS_PATTERNS = ["../", "~", "$", "|", "&", ";"]

# Random event probabilities
EVENT_PROBABILITIES = {
    "treasure_found": 0.1,
    "monster_encounter": 0.15,
    "helpful_npc": 0.2,
    "weather_change": 0.3,
    "nothing": 0.25
}

# Event outcome messages
EVENT_OUTCOMES = {
    "treasure_found": "You found a hidden treasure!",
    "monster_encounter": "A wild creature appears!",
    "helpful_npc": "A friendly traveler offers assistance.",
    "weather_change": "The weather shifts dramatically.",
    "nothing": "Nothing interesting happens."
}
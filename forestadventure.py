import random
import time


def clear_screen():
    """Clear the screen with newlines for better readability."""
    print("\n" * 50)


def type_text(text, delay=0.03):
    """Print text character by character for a more immersive experience."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


class ForestAdventure:
    def __init__(self):
        # Player stats
        self.health = 100
        self.inventory = []
        self.has_map = False
        self.current_location = "forest_entrance"
        self.previous_location = "forest_entrance"
        self.game_over = False
        self.found_treasure = False

        # Game locations and their descriptions
        self.locations = {
            "forest_entrance": {
                "description": "You stand at the entrance of a mysterious forest. The trees loom tall above you, and paths lead in several directions.",
                "options": {
                    "1": {"text": "Take the well-worn path to the east", "destination": "clearing"},
                    "2": {"text": "Follow the narrow trail to the north", "destination": "dense_woods"},
                    "3": {"text": "Venture into the dark path to the west", "destination": "mysterious_cave"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "clearing": {
                "description": "You emerge into a sunny clearing. Wildflowers dot the ground, and you can hear birds singing.",
                "options": {
                    "1": {"text": "Investigate the strange rock formation", "destination": "rock_formation"},
                    "2": {"text": "Rest for a while to recover strength", "destination": "rest_clearing"},
                    "3": {"text": "Return to the forest entrance", "destination": "forest_entrance"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "dense_woods": {
                "description": "The trees grow closer together here, blocking much of the sunlight. It's harder to see where you're going.",
                "options": {
                    "1": {"text": "Push deeper into the woods", "destination": "old_tree"},
                    "2": {"text": "Follow the sound of running water", "destination": "stream"},
                    "3": {"text": "Return to the forest entrance", "destination": "forest_entrance"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "mysterious_cave": {
                "description": "You stand before a dark cave entrance. Cool air flows from within, and strange symbols are carved around the opening.",
                "options": {
                    "1": {"text": "Enter the cave", "destination": "cave_interior"},
                    "2": {"text": "Examine the symbols", "destination": "examine_symbols"},
                    "3": {"text": "Return to the forest entrance", "destination": "forest_entrance"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "rock_formation": {
                "description": "The rocks form a strange circle. In the center, you notice something glinting in the sunlight.",
                "options": {
                    "1": {"text": "Reach for the glinting object", "destination": "find_amulet"},
                    "2": {"text": "Circle around the formation", "destination": "rock_circle"},
                    "3": {"text": "Return to the clearing", "destination": "clearing"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "rest_clearing": {
                "description": "You sit down among the wildflowers and rest for a while. You feel refreshed!",
                "heal": 20,
                "options": {
                    "1": {"text": "Return to exploring the clearing", "destination": "clearing"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "old_tree": {
                "description": "You find an ancient, massive tree. Its trunk is wide enough for a person to fit inside, and there's a hollow at its base.",
                "options": {
                    "1": {"text": "Look inside the hollow", "destination": "tree_hollow"},
                    "2": {"text": "Climb the tree", "destination": "tree_top"},
                    "3": {"text": "Return to the dense woods", "destination": "dense_woods"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "stream": {
                "description": "A clear stream cuts through the forest. The water looks clean and refreshing.",
                "options": {
                    "1": {"text": "Drink from the stream", "destination": "drink_stream"},
                    "2": {"text": "Follow the stream", "destination": "waterfall"},
                    "3": {"text": "Return to the dense woods", "destination": "dense_woods"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "cave_interior": {
                "description": "Inside the cave, it's dark and cool. Your eyes adjust to reveal stalactites hanging from the ceiling and a fork in the path ahead.",
                "options": {
                    "1": {"text": "Take the left path", "destination": "cave_left"},
                    "2": {"text": "Take the right path", "destination": "cave_right"},
                    "3": {"text": "Exit the cave", "destination": "mysterious_cave"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "examine_symbols": {
                "description": "Upon closer inspection, the symbols seem to be an ancient form of writing. One sequence looks like directions.",
                "options": {
                    "1": {"text": "Try to memorize the symbols", "destination": "learn_symbols"},
                    "2": {"text": "Enter the cave", "destination": "cave_interior"},
                    "3": {"text": "Return to the forest entrance", "destination": "forest_entrance"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "find_amulet": {
                "description": "You pick up a beautiful amulet with a glowing blue stone. It feels warm to the touch.",
                "item": "magic amulet",
                "options": {
                    "1": {"text": "Return to the clearing", "destination": "clearing"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "rock_circle": {
                "description": "As you circle the rocks, you notice one has a small compartment hidden in it.",
                "options": {
                    "1": {"text": "Open the compartment", "destination": "find_map"},
                    "2": {"text": "Return to examining the center", "destination": "rock_formation"},
                    "3": {"text": "Return to the clearing", "destination": "clearing"},
                    "4": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "tree_hollow": {
                "description": "Inside the hollow, you find a small wooden box.",
                "options": {
                    "1": {"text": "Open the box", "destination": "open_box"},
                    "2": {"text": "Leave the hollow", "destination": "old_tree"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "tree_top": {
                "description": "From the top of the tree, you can see much of the forest. In the distance, you spot a waterfall and what might be ruins.",
                "options": {
                    "1": {"text": "Climb back down", "destination": "old_tree"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "drink_stream": {
                "description": "The water is cool and refreshing. You feel invigorated!",
                "heal": 15,
                "options": {
                    "1": {"text": "Follow the stream", "destination": "waterfall"},
                    "2": {"text": "Return to the dense woods", "destination": "dense_woods"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "waterfall": {
                "description": "The stream leads to a beautiful waterfall. Behind it, you can see what looks like an entrance to a cave.",
                "options": {
                    "1": {"text": "Try to go behind the waterfall", "destination": "waterfall_cave"},
                    "2": {"text": "Return to the stream", "destination": "stream"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "cave_left": {
                "description": "The left path twists and turns, eventually leading to a dead end. But there's a strange mushroom growing on the wall.",
                "options": {
                    "1": {"text": "Pick the mushroom", "destination": "find_mushroom"},
                    "2": {"text": "Return to the cave entrance", "destination": "cave_interior"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "cave_right": {
                "description": "The right path slopes downward. As you proceed, you hear a low growling sound...",
                "options": {
                    "1": {"text": "Continue forward cautiously", "destination": "cave_guardian"},
                    "2": {"text": "Retreat back to the cave entrance", "destination": "cave_interior"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "learn_symbols": {
                "description": "After studying the symbols, you believe they indicate that 'the treasure lies beneath the falling water, guarded by stone.'",
                "options": {
                    "1": {"text": "Enter the cave", "destination": "cave_interior"},
                    "2": {"text": "Return to the forest entrance", "destination": "forest_entrance"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "find_map": {
                "description": "Inside the compartment, you find an old parchment. It's a map of the forest, showing various landmarks and a big X by the waterfall!",
                "map": True,
                "options": {
                    "1": {"text": "Return to the clearing", "destination": "clearing"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "open_box": {
                "description": "The box contains a shiny key with a crystal handle.",
                "item": "crystal key",
                "options": {
                    "1": {"text": "Leave the hollow", "destination": "old_tree"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "find_mushroom": {
                "description": "You pick the strange mushroom. It has an unusual blue glow.",
                "item": "glowing mushroom",
                "options": {
                    "1": {"text": "Return to the cave entrance", "destination": "cave_interior"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "cave_guardian": {
                "description": "You encounter a large bear! It looks hungry and angry.",
                "danger": True,
                "damage": random.randint(20, 30),
                "options": {
                    "1": {"text": "Try to sneak past", "destination": "sneak_past_bear"},
                    "2": {"text": "Run back to the cave entrance", "destination": "run_from_bear"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "sneak_past_bear": {
                "description": "You attempt to sneak past the bear...",
                "chance_success": 0.4,
                "success_dest": "treasure_chamber",
                "fail_dest": "bear_attack",
                "options": {}  # No options, automatically proceeds based on chance
            },
            "run_from_bear": {
                "description": "You turn and run as fast as you can!",
                "damage": random.randint(5, 15),
                "options": {
                    "1": {"text": "Continue to the cave entrance", "destination": "cave_interior"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "bear_attack": {
                "description": "The bear spots you and charges! You barely escape, but not without injury.",
                "damage": random.randint(30, 50),
                "options": {
                    "1": {"text": "Retreat to the cave entrance", "destination": "cave_interior"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "waterfall_cave": {
                "description": "Behind the waterfall, you discover a hidden cave entrance. Inside, there's a stone door with a keyhole.",
                "options": {
                    "1": {"text": "Try to open the door", "destination": "try_door"},
                    "2": {"text": "Return to the waterfall", "destination": "waterfall"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "try_door": {
                "description": "The door won't budge. It seems you need a key to open it.",
                "key_check": True,
                "options": {
                    "1": {"text": "Return to the waterfall", "destination": "waterfall"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "treasure_chamber": {
                "description": "You've found the treasure chamber! A golden chest sits in the center of the room, surrounded by old coins and jewels.",
                "options": {
                    "1": {"text": "Open the chest", "destination": "open_chest"},
                    "2": {"text": "Collect some loose treasure", "destination": "collect_coins"},
                    "3": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "open_chest": {
                "description": "Inside the chest, you find the legendary Forest Crystal, said to grant wisdom and prosperity to its owner. You've found the greatest treasure of the forest!",
                "victory": True,
                "options": {
                    "1": {"text": "End your adventure", "destination": "end_game"}
                }
            },
            "collect_coins": {
                "description": "You fill your pockets with gold coins and jewels.",
                "item": "treasure",
                "options": {
                    "1": {"text": "Open the chest", "destination": "open_chest"},
                    "2": {"text": "Check your inventory", "action": "inventory"}
                }
            },
            "end_game": {
                "description": "Congratulations! You've completed your forest adventure with the legendary treasure!",
                "options": {}  # Empty options means game over
            }
        }

    def start_game(self):
        """Begin the adventure game."""
        clear_screen()
        type_text("╔═══════════════════════════════════════════════╗")
        type_text("║            THE MYSTIC FOREST                  ║")
        type_text("║         A Text Adventure Game                 ║")
        type_text("╚═══════════════════════════════════════════════╝", 0.01)
        type_text("\nYou've heard rumors of a legendary treasure hidden deep within the Mystic Forest.")
        type_text("Armed with courage and curiosity, you decide to embark on an adventure to find it.")
        type_text("Be careful though - the forest holds many dangers!\n")
        type_text("Your health: 100/100")
        type_text("Your goal: Find the legendary treasure and escape the forest alive.\n")
        type_text("Press Enter to begin your adventure...", 0.02)
        input()

        # Main game loop
        while not self.game_over:
            self.display_location()
            self.process_location()

            if self.health <= 0:
                clear_screen()
                type_text("Your injuries are too severe. You collapse in the forest...")
                type_text("GAME OVER - You've run out of health!")
                self.game_over = True

            if self.found_treasure:
                clear_screen()
                type_text("CONGRATULATIONS!")
                type_text("You've found the legendary Forest Crystal and escaped with the treasure!")
                type_text(f"Final health: {self.health}/100")
                type_text(f"Items collected: {', '.join(self.inventory)}")
                type_text("\nThanks for playing THE MYSTIC FOREST!")
                self.game_over = True

    def display_location(self):
        """Display the current location and available options."""
        clear_screen()
        location = self.locations[self.current_location]

        # Display description
        type_text(location["description"])

        # Show health status
        health_status = f"Health: {self.health}/100"
        if self.health < 30:
            health_status += " [CRITICAL!]"
        elif self.health < 60:
            health_status += " [Low]"
        type_text(f"\n{health_status}")

        # Display random event if applicable (10% chance)
        if random.random() < 0.1 and "options" in location and len(location["options"]) > 0:
            self.trigger_random_event()

        # Show available options
        if "options" in location and len(location["options"]) > 0:
            type_text("\nWhat would you like to do?")
            for key, option in location["options"].items():
                type_text(f"{key}. {option['text']}")

    def process_location(self):
        """Process the current location and player choices."""
        location = self.locations[self.current_location]

        # Handle special location effects
        if "heal" in location:
            old_health = self.health
            self.health = min(100, self.health + location["heal"])
            type_text(f"You recovered {self.health - old_health} health points!")

        if "item" in location and location["item"] not in self.inventory:
            self.inventory.append(location["item"])
            type_text(f"Added {location['item']} to your inventory!")

        if "map" in location and location["map"] and not self.has_map:
            self.has_map = True
            type_text("You now have a map of the forest!")

        if "damage" in location:
            self.health -= location["damage"]
            type_text(f"You took {location['damage']} damage!")

        if "danger" in location and location["danger"]:
            # Give player a chance to avoid damage if they have the amulet
            if "magic amulet" in self.inventory:
                type_text("Your magic amulet glows, providing protection!")
                damage_reduction = random.randint(10, 20)
                if "damage" in location:
                    location["damage"] = max(5, location["damage"] - damage_reduction)
                    type_text(f"Damage reduced by {damage_reduction} points!")

        if "chance_success" in location:
            input("\nPress Enter to continue...")
            success_roll = random.random()
            if success_roll < location["chance_success"]:
                type_text("Success! You managed to sneak past without being noticed.")
                self.current_location = location["success_dest"]
            else:
                type_text("Failed! You were spotted!")
                self.current_location = location["fail_dest"]
            return

        if "key_check" in location and location["key_check"]:
            if "crystal key" in self.inventory:
                type_text("You use the crystal key to unlock the door. It swings open!")
                self.current_location = "treasure_chamber"
                return

        if "victory" in location and location["victory"]:
            self.found_treasure = True
            return

        # Get player choice
        if "options" in location and len(location["options"]) > 0:
            while True:
                choice = input("\nEnter your choice: ")
                if choice in location["options"]:
                    option = location["options"][choice]

                    # Check if this is a special action
                    if "action" in option and option["action"] == "inventory":
                        self.display_inventory()
                        input("\nPress Enter to continue...")
                        # We don't change location when checking inventory
                        break
                    # Otherwise, it's a regular location change
                    elif "destination" in option:
                        self.current_location = option["destination"]
                        break
                else:
                    type_text("Invalid choice. Try again.")

    def display_inventory(self):
        """Display the player's inventory."""
        type_text("\n----- YOUR INVENTORY -----")
        if not self.inventory:
            type_text("Your inventory is empty.")
        else:
            for item in self.inventory:
                type_text(f"- {item}")

        if self.has_map:
            type_text("- Map of the forest")
            type_text("  (The map shows a waterfall with an X marked behind it)")

    def trigger_random_event(self):
        """Trigger a random event based on the current location."""
        events = [
            {"text": "A squirrel drops a nut on your head.", "health": -2},
            {"text": "You find a wild berry bush and eat some berries.", "health": 5},
            {"text": "A sudden gust of wind gives you a chill.", "health": -3},
            {"text": "You spot a rainbow through the trees, lifting your spirits.", "health": 3},
            {"text": "You trip over a hidden root.", "health": -5},
            {"text": "A friendly forest sprite appears briefly, leaving a sense of peace.", "health": 8},
            {"text": "Mosquitoes swarm around you.", "health": -4},
            {"text": "You find a small freshwater spring and take a drink.", "health": 6}
        ]

        event = random.choice(events)
        type_text(f"\nRANDOM EVENT: {event['text']}")

        old_health = self.health
        self.health = max(1, min(100, self.health + event["health"]))

        if event["health"] > 0:
            type_text(f"You gained {self.health - old_health} health points!")
        elif event["health"] < 0:
            type_text(f"You lost {old_health - self.health} health points!")

        input("\nPress Enter to continue...")


# Run the game
if __name__ == "__main__":
    game = ForestAdventure()
    game.start_game()

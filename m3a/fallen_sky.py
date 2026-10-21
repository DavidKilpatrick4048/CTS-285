"""The Fallen Sky: a short science fiction and fantasy text adventure.

Adapted from the supplied adventure_start.py.
Run:   python fallen_sky.py
Check: python story_check.py fallen_sky.py --map

Each passage_ function is one scene. Each ending_ function is one ending.
"""


# This shared Boolean remembers whether the crystal was collected.
has_crystal = False


def ask(prompt, options):
    """Display numbered choices and return a valid choice number."""
    while True:
        print()
        print(prompt)
        for number, text in enumerate(options, start=1):
            print(f"  {number}. {text}")
        try:
            raw = input("> ").strip()
            choice = int(raw)
        except EOFError:
            raise SystemExit(0)
        except ValueError:
            print(f"Enter a whole number from 1 to {len(options)}.")
            continue
        if 1 <= choice <= len(options):
            return choice
        print(f"Enter a number from 1 to {len(options)}.")


def passage_start():
    """Choose an entrance to the ancient ruins."""
    print("\n--- The Ruined Temple ---")
    print("For centuries, your village has left offerings to the sky gods here.")
    print("Tonight, blue light shines through the temple floor. Something below")
    print("the stone is waking up. You find a sealed entrance and a side chamber")
    print("lit by the same strange glow.")
    choice = ask("Where do you go?", [
        "Examine the sealed entrance",
        "Search the glowing side chamber",
    ])
    if choice == 1:
        passage_door()
    else:
        passage_closet()


def passage_door():
    """Inspect a doorway where the temple meets the buried ship."""
    print("\n--- The Sealed Entrance ---")
    print("You brush dust from the doorway. Beneath the carved stone lies a")
    print("smooth metal frame. The runes light up like buttons, and the door")
    print("slides open. A low mechanical hum comes from a passage beyond it.")
    choice = ask("What do you investigate?", [
        "Read the glowing markings on a nearby screen",
        "Follow the mechanical hum toward the command bridge",
    ])
    if choice == 1:
        passage_records()
    else:
        passage_hallway()


def passage_closet():
    """Let the player collect the crystal or choose another route."""
    global has_crystal
    print("\n--- The Crystal Chamber ---")
    print("A blue crystal rests among old offerings. Beside it, a glowing diagram")
    print("shows the same crystal fitting into a machine. A door leads farther")
    print("inside, and a loose vent cover reveals a narrow passage.")
    choice = ask("What do you do?", [
        "Take the crystal and examine the nearby records",
        "Leave the crystal and follow the open doorway",
        "Crawl into the vent",
    ])
    if choice == 1:
        has_crystal = True
        print("You place the warm crystal in your bag.")
        passage_records()
    elif choice == 2:
        passage_hallway()
    else:
        passage_vent()


def passage_vent():
    """Reveal the spacecraft through a reachable service passage."""
    print("\n--- The Service Passage ---")
    print("Behind the temple walls, you find cables, pipes, and a metal walkway.")
    print("A diagram on a cracked screen shows a spacecraft buried beneath the")
    print("ruins. The temple was built around its hull. This is no ordinary tomb.")
    choice = ask("What do you do?", [
        "Read the maintenance display",
        "Follow the power cables toward the reactor",
    ])
    if choice == 1:
        passage_records()
    else:
        passage_core()


def passage_records():
    """Explain how the ship and the ancient temple connect."""
    print("\n--- The Ship Records ---")
    print("The screen translates its symbols into your language. A spacecraft named")
    print("Fallen Sky crashed here centuries ago. Later generations built the")
    print("temple around its exposed hull. One final entry remains: 'Passengers")
    print("in stasis. Reactor unstable. Power crystal required for restoration.'")
    choice = ask("What do you do?", [
        "Find out who is sleeping on the ship",
        "Follow the instructions toward the reactor",
    ])
    if choice == 1:
        passage_hallway()
    else:
        passage_core()


def passage_hallway():
    """Find the sleeping passengers and choose a route forward."""
    print("\n--- The Command Bridge ---")
    print("Stone pillars surround the spacecraft's broken control panels.")
    print("The temple was built around this crashed ship, hiding it for centuries.")
    print("A recorded guardian speaks: 'Passengers remain asleep. Power is failing.'")
    print("A screen shows rows of sleeping travelers. Green lights mark an")
    print("escape route; blue lights lead toward the damaged reactor.")
    choice = ask("What do you do?", [
        "Go to the reactor and investigate restoring power",
        "Follow the green lights toward the escape tunnel",
    ])
    if choice == 1:
        passage_core()
    else:
        passage_escape()


def passage_core():
    """Use the crystal state and warn before the only failure choice."""
    print("\n--- The Unstable Reactor ---")
    print("The reactor shakes inside a ring of cracked metal. Beside a blue")
    print("crystal socket, a red control offers an emergency launch.")
    print("WARNING: forcing a launch may rupture the reactor and kill you.")
    print("Green evacuation lights show a safe way out.")
    if has_crystal:
        print("The crystal in your bag matches the blue socket.")
        choice = ask("What do you do?", [
            "Fit the crystal and restore power safely",
            "Force a launch despite the reactor-breach warning",
            "Leave the reactor and take the safe escape route",
        ])
        if choice == 1:
            ending_awakened()
        elif choice == 2:
            ending_caught()
        else:
            passage_escape()
    else:
        print("The blue socket is empty. Without the crystal, you cannot")
        print("restore power safely. You can still leave without launching.")
        choice = ask("What do you do?", [
            "Leave the reactor and take the safe escape route",
            "Force a launch despite the reactor-breach warning",
        ])
        if choice == 1:
            passage_escape()
        else:
            ending_caught()


def passage_escape():
    """Lead the player along the marked safe exit."""
    print("\n--- The Escape Tunnel ---")
    print("You follow the green lights up a service tunnel. Cool air reaches")
    print("you through an opening beyond the temple wall. The ship is still")
    print("beneath your feet, but the path ahead is clear.")
    choice = ask("What do you do?", [
        "Climb outside and warn the village",
    ])
    if choice == 1:
        ending_free()


def ending_awakened():
    """Restore the ship and reveal a hopeful twist."""
    print("\n=== ENDING: SHIP RESTORED ===")
    print("The crystal settles into its socket. The reactor's shaking stops.")
    print("Passengers wake below the bridge. Their names match the sky gods")
    print("carved above the temple doors. Your village's legends were memories")
    print("of these stranded travelers. You have given them a second chance.")
    print("Then another signal appears beneath distant mountains. A woman")
    print("studies it and whispers, 'We were not the only ship.'")


def ending_free():
    """Finish with a safe escape and an unresolved mystery."""
    print("\n=== ENDING: SAFE ESCAPE ===")
    print("You climb out beyond the temple and warn the village to keep clear.")
    print("Everyone is safe, but the people sleeping beneath the ruins remain")
    print("a mystery. As dawn breaks, a thin blue signal rises into the sky.")
    print("You survived. Perhaps someone out there will answer.")


def ending_caught():
    """Finish with the warned reactor-breach failure."""
    print("\n=== ENDING: REACTOR BREACH ===")
    print("You force the launch. The damaged reactor answers with a violent crack.")
    print("The warnings become a roar, and blue light swallows the control room.")
    print("The ship never rises. Your attempt ends beneath the ruined temple.")
    print("You failed: the reactor could not survive a forced launch.")


def main():
    """Run a fresh adventure each time the player chooses to replay."""
    global has_crystal
    while True:
        has_crystal = False
        print("\n=== THE FALLEN SKY ===")
        print("Choose a numbered option. Every valid choice moves you forward.")
        passage_start()
        print("\nThe end.")
        if ask("Play again?", ["Yes", "No"]) == 2:
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()

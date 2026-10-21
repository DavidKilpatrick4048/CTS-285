# AI Prompt Log — The Fallen Sky

**Retrospective reconstruction:** The prompts below restate the project requests in the Coda guide’s format. They were clarified after the work was completed and are not verbatim chat messages. The final playtest feedback is quoted from my actual report.

I selected the premise, approved the plan before coding, and played the finished game. The AI assisted with the brief, implementation, code explanation, and technical checks.

## Stage: idea

Prompt:
```text
I am working on the M3A text-adventure assignment in Python. I will be the player using the solo option. Interview me about story preferences, playtime, dislikes, endings, device, and an extra feature. Wait for my answers before planning the game. Do not write code yet.
```

What the AI gave me (one line): An interview that established my preferences and the solo player route.

What I kept, changed, or threw away: I kept science fiction, fantasy, and adventure as the direction for the story.

## Stage: idea

Prompt:
```text
My interview answers are: science fiction and fantasy/adventure; about five minutes; no repetitive loops or sudden failure without warning; different outcomes with a clear result, a twist, and some mystery. Give me four story ideas with a title and a short premise. Keep each idea under 40 words. Do not write code.
```

What the AI gave me (one line): Four premises: The Starwell, The Fallen Sky, Tomorrow’s Signal, and The Clockwork Citadel.

What I kept, changed, or threw away: I chose The Fallen Sky because I wanted ancient fantasy ruins hiding an alien spacecraft.

## Stage: idea

Prompt:
```text
I choose The Fallen Sky: discover an alien spacecraft beneath ancient fantasy ruins. Write a three-sentence pitch explaining who the player is, what they want, and what stands in the way. Keep it small enough for the assignment’s passage budget.
```

What the AI gave me (one line): A pitch about entering the temple, finding a buried ship, and deciding whether to restore it or escape.

What I kept, changed, or threw away: I kept the temple and spacecraft premise and the choice between helping the ship and leaving safely.

## Stage: plan

Prompt:
```text
Use the player answers in part 1 of brief.md to write six user stories. Use: As a [kind of player], I want [action], so that [reason]. Give each story its evidence ID. Use only the recorded preferences and do not add new player needs.
```

What the AI gave me (one line): Six stories linked to the interview evidence, covering the setting, time, progress, warnings, endings, and side quests.

What I kept, changed, or threw away: I kept the stories connected to my answers, including the larger-world request for the cut list.

## Stage: plan

Prompt:
```text
For each of the six user stories, write one acceptance check. Make each check something I can see, count, or time by playing. It must have a clear pass or fail result. Do not write checks about code style.
```

What the AI gave me (one line): Acceptance checks for the setting, five-minute target, forward progress, danger warning, different endings, and optional quests.

What I kept, changed, or threw away: I kept checks based on visible behavior and recorded the side-quest check as cut from the current release.

## Stage: plan

Prompt:
```text
Prioritize the user stories using an 8-to-12-passage budget. Put the kept stories in value order. Cut at least one story, explain why it does not fit, and give a specific condition that would bring it back.
```

What the AI gave me (one line): Five kept stories and a cut list that deferred the larger world with side quests.

What I kept, changed, or threw away: I kept the main adventure within 11 passages and left the side quests for a larger version.

## Stage: plan

Prompt:
```text
Use the chosen premise and kept stories to draw a Mermaid flowchart with 11 passages including three endings. Use passage_ names for scenes and ending_ names for endings. Mark the start and endings. Keep routes moving forward, with no dead ends except endings. Show that ship restoration needs the crystal. Do not write Python code.
```

What the AI gave me (one line): A branching map with eight scenes and three endings: restoration, escape, and reactor breach.

What I kept, changed, or threw away: I approved the map before coding. It included a safe escape route and an explicit warning before failure.

## Stage: build

Prompt:
```text
The planning gate is approved. Before writing code, answer this design question: if the player collects the crystal, will it remain available at the reactor? Use the map and a small table showing where the state changes and where it is read. Record Ready, Revise, Split, or Hold with one sentence explaining the evidence.
```

What the AI gave me (one line): A Ready decision and a state table using has_crystal to remember collection until the reactor.

What I kept, changed, or threw away: I kept one Boolean for the crystal, with a reset at the beginning of each new playthrough.

## Stage: build

Prompt:
```text
Use adventure_start.py as the style reference. Write passage_records() in Python using ask(). It should explain the crashed ship and offer two choices: investigate the sleeping passengers through passage_hallway(), or follow the reactor instructions through passage_core(). Return the function.
```

What the AI gave me (one line): A records passage that connects the fantasy ruins to the spacecraft and leads to the bridge or reactor.

What I kept, changed, or threw away: I kept the scene’s purpose and links from the approved map. The remaining scenes were added and checked incrementally by the AI.

## Stage: build

Prompt:
```text
Add the crystal-state feature to the existing passage functions. Taking the crystal must set has_crystal to True, and restoration must be available only when it is True. Reset it before each replay. Show the affected code sections and explain where they belong.
```

What the AI gave me (one line): A shared crystal variable used by passage_closet, passage_core, and main.

What I kept, changed, or threw away: I kept crystal collection as the requirement for restoration and a fresh state when replaying.

## Stage: build

Prompt:
```text
Review the supplied checker’s report for fallen_sky.py. Explain the passage count, endings, links, and any findings in plain language. Distinguish what the checker establishes from what still requires a real player’s playtest.
```

What the AI gave me (one line): A clean checker report with 11 passages, three endings, and 17 links, plus additional AI-run route and replay checks.

What I kept, changed, or threw away: I used the technical results as evidence and played the game myself to check its time and clarity.

## Stage: build

Prompt:
```text
Explain the main parts of fallen_sky.py in short sentences. Cover ask(), the passage and ending functions, has_crystal, the choice conditions, and the replay loop. Identify which parts show text, apply rules, and hold the story words.
```

What the AI gave me (one line): A code explanation in README.md and the three job descriptions in part 7 of the brief.

What I kept, changed, or threw away: I kept the explanations with the project files for reviewing how the program works.

## Stage: build

Prompt:
```text
It took less than 5 minutes. Nothing was confusing or repetitive. I accept the game.
```

What the AI gave me (one line): An updated playtest record and an Accept decision in the brief.

What I kept, changed, or threw away: I accepted the game after playing it and did not request a gameplay change.

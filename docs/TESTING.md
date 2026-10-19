# Validation record — 0.1.0

Completed **19 October 2026**, using **Codex CLI 0.156.0**, the installed
`fred@monk-witch` plugin, and read-only gameplay sessions. These were live agent
turns with packaged-file reads, not hand-written sample answers. The tester
supplied scripted player choices and dice values; no random-roll capability was
claimed or tested.

## Installation and package checks

Registered the repository marketplace with `codex plugin marketplace add`, then
installed with `codex plugin add fred@monk-witch`. The plugin manager reported
version 0.1.0 installed and enabled. The refined installation's 135 skill files
were compared byte for byte with the source tree: no differences.

The first test invocation used an incorrectly quoted dotted configuration
override and produced a loader warning. The agent still located and read the
installed skill files. Later runs used a TOML map override and correctly loaded
the enabled plugin. This was a test-harness correction, not a package change.

`scripts/validate.py` passed: 224 page-transcription hashes in original order,
28 canonical shards, identical copies in all three skills, no symlinks or database
payload, local Markdown links, official portable-manifest schema and ZIP integrity.
Each skill also passed the Skill Creator frontmatter/naming validator.
All three bundles fit the conservative 100-file / 5 MiB / 1 MiB-per-file checks.

Fetched the current official SRD and licence PDFs; both hashes matched the reviewed
source identities. This verifies source identity. The per-page hash test verifies
transcription preservation, not every decision in PDF extraction independently.

## Gameplay observed

| Scenario | Observation |
| --- | --- |
| [Create and play a Hedge Witch](playtests/adventure.md) | Built a level-one Human Hearthborne Witch using Sage/Dread, correct Spellcast trait, Human Stress capacity, equipment calculations, features and active cards. Opened an original scene and left choices to the player. |
| Exploration into combat | Nature's Tongue resolved 9 + 4 + Instinct 1 = 14 against 12; Hope increased 2→3. Loaded combat guidance and introduced the published Minor Treant. Carried resources across the transition. |
| Hope & Fear feature and attack | Hex marked Stress and reduced Difficulty 10→9. Blighting Strike's success with Fear used d10+1, defeated the minion and increased GM Fear 1→2. No fabricated enemy roll or forced player action. |
| Advancement | Applied level 2/Tier 2, Proficiency 1→2, HP 6→7, Stress capacity 7→8, thresholds 7/14→8/15 and Hex penalty −1→−2. Added legal level-two Dread card Siphon Essence. Preserved marked Stress, Hope and equipment. Explicitly identified advancement slots as player-sheet-supplied, not verified SRD grid data. |
| Checkpoint | Produced an exact resource/options ledger, established facts and pending choice; excluded unrevealed plans. Acknowledged conversation storage rather than a backend save. |
| [Continue in a fresh conversation](playtests/checkpoint-continuation.md) | Accepted the player-supplied checkpoint, continued the Oren scene, kept resources unchanged and did not require a meaningless roll to follow clear tracks. |
| [Controlled combat fixture](playtests/combat-fixture.md) | Severe physical damage 14 with one Armor Slot became 2 HP marked. Critical reaction granted no Hope/Stress recovery or Fear; a subsequent double-one action critically succeeded despite failing the numeric Difficulty and granted the appropriate recovery. |
| Death move and refinement retest | Waited for the player's choice. Avoid Death with Hope Die 2 at level 2 caused unconsciousness and a scar, reduced Hope capacity 6→5 while retaining current Hope 4, preserved other resources, and explained the actual waking conditions. |

Seven completed turns across three conversation threads are represented in the
linked transcripts. `tests/gameplay-evidence.json` records event-log hashes and
observed installed-file reads. Raw event logs remain local; public transcripts
contain player input and final output, with local-file links redacted.

## Refinement from observed behavior

The first combat fixture linked to a local installed reference path. That is
unhelpful on other devices. Updated all skills and the table procedure to cite
plain SRD pages or official PDF page links, rebuilt and reinstalled, then repeated
the citation behavior while resolving Avoid Death. The retest returned the
official PDF link with `#page=53`, with correct mechanics and resources.

## Limits

- Actual installation/gameplay was tested in local Codex CLI. Desktop UI,
  ChatGPT web/mobile and OpenAI directory import/review were not exercised.
- The documented cross-surface target is not a claim that this GitHub release
  is already listed or installable from every ChatGPT client.
- No exhaustive test of every class, feature, adversary, multiclass path or
  long campaign was performed. Source lookup and table judgment remain necessary.
- Full class-sheet advancement grids and some companion capacities are not in
  this SRD. The skill identifies gaps rather than claiming a complete automatic
  character validator. The advancement test supplied its two available slots.
- Checkpoints are visible conversation records. Long-term recall, hidden GM
  information recovery and external persistence are not guaranteed or tested.

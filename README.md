# Fred (Daggerheart GM)

**Your AI game master for Daggerheart-compatible adventures.** Create a hero,
explore an original adventure, and play through consequential choices with Fred.

Fred is an AI GM persona created by Fred, author of **[The Monk & The Witch](https://monkandwitch.com/)**.
This self-contained plugin packages three skills and the complete **Daggerheart
SRD 2.0**, including the released **Hope & Fear** additions. No separate game
server, account, database or application is needed during play.

## Start playing

Install the plugin, start a new conversation and explicitly select **Fred** from
the available skills, or ask your host to use the Fred skill:

> Use Fred to start a short fantasy adventure. Help me make a level-one character.

In Codex, invoke `$fred` (or the namespaced Fred skill shown by `/skills`).
Fred uses **Characters** for character creation and advancement, and **Combat**
for encounters. They remain the same GM and adventure. Rules, cards, equipment
and adversaries are reached through each skill's separate reference index.

Fred will establish the tone, content boundaries, party and dice arrangement.
By default **you supply real dice results**, including requested enemy rolls:
physical dice or a dice app work. Report Hope/Fear d12 values separately. An
available real random-roll tool can be used by agreement. Generated prose is
never presented as a verified random roll.

Ask for a **checkpoint** to get a copyable record of your character and adventure.
The campaign lives in the conversation. There is no external save service; keep
your checkpoint if you want to reconstruct the game in another conversation.

## Install locally

Requires a Codex client with plugin support and an existing signed-in account.
From Codex CLI:

```sh
codex plugin marketplace add monk-witch/fred
codex plugin add fred@monk-witch
```

Start a new session after installation. To test a local checkout instead:

```sh
git clone https://github.com/monk-witch/fred.git
codex plugin marketplace add ./fred
codex plugin add fred@monk-witch
```

The repository includes the local marketplace catalog. In supported desktop
clients, use its local marketplace entry and refresh/restart the client if needed.
The ZIP on the GitHub release contains the portable plugin package.

**Availability:** the package targets officially supported ChatGPT and Codex
plugin surfaces. This release has not been submitted to the OpenAI public
directory. A GitHub release alone does not make it installable in ChatGPT web or
mobile; directory distribution comes later. See [the test report](docs/TESTING.md)
for the clients and gameplay actually exercised. The Codex IDE extension does
not currently support plugin installation.

## The Monk & The Witch and Mythic Earth

I am Fred, the author of **The Monk & The Witch**, an original, character-driven
dark fantasy saga inspired by Daggerheart. This GM is another way to share my
love of characters, uncertain choices and the stories that grow from them.

**[Discover the saga at monkandwitch.com →](https://monkandwitch.com/)**

The longer-term goal is to connect Fred to **Mythic Earth**, the saga's campaign
setting currently under development, including **Mythic France**. That setting
integration is planned; version 0.1 runs generic adventures and does not claim to
ship a finished Mythic Earth supplement. The Original Work is distinct from the
older D&D Fanfic. Visit the website for the work and future developments.

For project feedback or direct contact, [open an issue](https://github.com/monk-witch/fred/issues).

## Source, rights and scope

This is an unofficial project, not endorsed by Darrington Press or Critical Role.
Our independent instructions, navigation, code, documentation and icon are
**MIT-licensed**. The **SRD retains its DPCGL terms**; MIT does not relicense it.
Read [third-party notices](THIRD_PARTY_NOTICES.md), [source provenance](docs/SOURCES.md)
and the included licence text before redistributing material.

The source is a page-ordered Markdown transcription, with extraction changes
disclosed and the original PDF identified by hash. The separate index changes
navigation rather than rule wording. Each skill has a real copy of the reference
so no symlink, sibling checkout, database or external rules service is required.
Private purchased-book material is excluded. Some class-sheet details are absent
from the SRD; Fred identifies those gaps rather than inventing them.

## Develop and package

Python 3 is needed for development only. `jsonschema` enables the optional
official manifest-schema check; the plugin itself executes no scripts.

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

Edit source skills and the canonical `sources/srd/` / `docs/` references, then
build. Generated copies are checked against the source manifest. ZIP entries
have stable timestamps for reproducible builds. See [design and supported
boundaries](docs/DESIGN.md) and [gameplay validation](docs/TESTING.md).

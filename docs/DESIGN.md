# Fred 0.1 design

Three skills share one GM identity: **Fred**, **Characters**, **Combat**. A skill
contains the procedure; a supporting index routes to exact SRD passages. Each
skill includes identical reference shards, index, notices and fallback procedures
for the other two skills, generated from one canonical source. This deliberate
packaging duplication avoids cross-skill filesystem assumptions on different
hosts. There are no runtime scripts, network services, hooks or MCP dependencies.

The main skill establishes the table and original adventure, Characters builds
and advances sheets, and Combat runs encounters. A host may load skills
implicitly from descriptions; explicit invocation is the reliable starting
instruction. If a sibling skill cannot be invoked, the same procedure is readable
inside the already active skill. This is not a multi-agent system.

Campaign state stays in the conversation. Checkpoints preserve visible resources,
facts and pending decisions; there is no hidden memory store. Real player-supplied
dice work across clients. An available real random tool may be agreed on, but no
client is assumed to have code execution.

## Standards checked on 19 October 2026

- [Official plugin packaging](https://developers.openai.com/plugins/build/plugins):
  portable root `plugin.json`, Agent Plugins schema 1.0.0, OpenAI metadata under
  `extensions.com.openai`, skills in `skills/<name>/SKILL.md`.
- [Skills](https://developers.openai.com/plugins/build/skills): short instruction
  entrypoints, linked supporting resources, explicit/implicit activation.
- [Local installation](https://learn.chatgpt.com/docs/plugins): repo/Git marketplace
  plus supported installation flow. This repository uses `.agents/plugins/marketplace.json`.
- [Public submission](https://developers.openai.com/plugins/deploy/submission):
  public directory distribution is a separate later step. No app references,
  hooks, desktop-only executor or invented remote endpoint are packaged.

The source manifest uses the current portable schema. The downloaded official
schema is retained under `tests/` for development validation. Package limits are
checked conservatively against the documented MCP-import resource bounds as well;
this does not claim those are the authoritative limits of every ZIP route.

## Future work

Public-directory review and actual web/mobile testing, optional independently
authored Mythic Earth/Mythic France lore, and further gameplay refinement. An
external save service or custom application is not part of version 0.1.

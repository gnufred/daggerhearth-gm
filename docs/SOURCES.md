# Sources and conversion history

Checked **19 October 2026**. The official SRD landing page identifies **SRD 2.0**,
dated August 25, 2026, as the current release. Its additions include the Dread
domain, Assassin/Brawler/Warlock/Witch, transformations and supplemental mechanics.
No playtest sources are used.

| Source | Version | SHA-256 of fetched PDF |
| --- | --- | --- |
| [SRD](https://www.daggerheart.com/wp-content/uploads/2026/08/DH_SRD_2_2026_08_25.pdf) | 2.0; 224 pages | `55d8b92b7e58aa1da99a4a59aa77352483ef4fbda71baddb9af9bfc1f333bd2a` |
| [DPCGL](https://darringtonpress.com/wp-content/uploads/2026/08/DPCGL_2.0_AUG_26_2026.pdf) | 2.0; 8 pages | `f7f62d775a43eecc4ad8f438a233a6aaf92f50396cb412c5ea91c0a988be6eca` |

The current fetched PDF bytes match the source PDFs used for the author's reviewed
text transcription. The DPCGL PDF header says August 5, while the announcement
and filename carry later August dates; these are different observations, not
different licences inferred by Fred.

## Transcription

The author prepared the SRD Markdown from the PDF using page geometry and column
reading order. It represents headings/lists in Markdown and preserves meaningful
tables, sometimes as fixed-width text. PDF ligatures and broken word spacing were
repaired; running page headers/footers were removed, and explicit source-page
markers added. These presentation changes are disclosed, not claimed as a
byte-identical PDF copy or official Markdown edition. Rule wording is not
intentionally rewritten; source quirks are not silently corrected into new rules.

This release concatenates eight consecutive page transcriptions per source file.
All pages 1–224 remain in sequence, including the source cover, contents and
Witherwild designation. The separate navigation index maps topics and names to
pages. Entry-name navigation is not a replacement for the complete rule passage.

`sources/manifest.json` records each original page-transcription hash and each
canonical shard's hash. The validator reconstructs all page transcriptions,
checks their hashes/order, and checks every distributed skill copy against the
canonical shard. It does not claim to prove every PDF extraction decision by
itself; report suspected text issues with the PDF page and passage.

## Source boundary

Only the SRD 2.0 text, the separately identified DPCGL text and original Fred
material are included. There are no purchased-book supplements, Homebrew Kit
prose, official artwork, proprietary sheet exports or campaign records. The SRD
links to external resources; those linked resources are not automatically part
of the licensed source or this package. Class advancement checkbox grids and
some companion-sheet capacities remain explicit gaps.

The entire SRD is reproduced as reference on the author's reading of DPCGL
§2.1(a). The Witherwild designation/frame restriction question is disclosed in
the notices; Fred defaults to independently authored generic adventures. This
project claims neither publisher approval nor a licence for every downstream use.

## Maintenance

Before updating a release, check the official SRD and licence pages, record the
new source identity and differences, review text changes, then deliberately update
canonical text and hashes. Do not fill missing content from other editions or
private books. Rebuild every skill copy and repeat source and gameplay validation.

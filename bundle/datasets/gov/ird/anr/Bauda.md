---
type: Table
title: "Bauda — Administracinių nusižengimų bylose paskirtos baudos"
description: "Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje viena eilutė yra vienas administracinis nusižengimas už kurį yra paskirta bauda (administracinės nuobaudos rūšis)."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr/Bauda"
tags: [gov, ird, bauda, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2558/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/anr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Bauda — Administracinių nusižengimų bylose paskirtos baudos

Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje viena eilutė yra vienas administracinis nusižengimas už kurį yra paskirta bauda (administracinės nuobaudos rūšis). Šiuo metu yra įtraukiami tik tokie nusižengimai , kurių sudėtyje yra tik vienas Administracinių nusižengimų kodekso (ANK) straipsnis ir tik viena piniginė bauda. Paskirtos baudos nebūtinai yra apmokėtos. Taip pat dalis į imtį patenkančių nusižengimų yra tie, dėl kurių priimti nutarimai gali būti apskųsti, nutraukti ar perkvalifikuoti (ši informacija nepateikiama). Dėmesio: tai nėra oficialioji statistika, naudojama eksperimentinė duomenų paruošimo metodika (pvz., neatsižvelgiama į galimus tolimesnius nusižengimo statuso pasikeitimus). Dėl techninių klausimų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ird/anr/Bauda`[^manifest]
- **Dataset:** [Administracinių nusižengimų registras](../anr.md) (`datasets/gov/ird/anr`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr/Bauda` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `anr_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `anr_id` | `string` | — | `4` | `open` | — | Administracinio nusižengimo unikalus identifikatorius | Skirtas jungimui su kitom lentelėm |
| `anr_uzregistruota` | `date` | `D` | `4` | `open` | — | Administracinio nusižengimo registravimo data | — |
| `anr_paskirta` | `date` | `D` | `4` | `open` | — | Baudos paskyrimo data | — |
| `suma` | `number` | — | `2` | `open` | — | Paskirtos baudos (už pagrindinį nusižengimo sudėties ANK straipsnį) dydis eurais | — |
| `skaicius` | `integer` | `U` | `4` | `open` | — | Į nusižengimo sudėtį įeinančių unikalių ANK straipsnių (ir jų dalių) skaičius | — |
| `ank_straipsnis` | `string` | — | `4` | `open` | — | Pagrindinis ANK straipsnis | — |
| `ank_straipsnio_dalis` | `string` | — | `4` | `open` | — | Pagrindinio ANK straipsnio dalis | — |
| `ank_straipsnis_pav` | `string` | — | `4` | `open` | — | ANK straipsnio pavadinimas | — |
| `ank_straipsnio_dalis_pav` | `string` | — | `4` | `open` | — | ANK straipsnio dalies pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/anr (https://data.gov.lt/datasets/2558/)

---
type: Table
title: "Sutartis — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio filialų studentų, atlikusių praktiką, rezidentūrą, tyrimą ar užsiėmusių kita veikla, sutarčių registrų duomenys."
description: "Spinta table datasets/gov/rplc/studentu_registras/Sutartis (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rplc/studentu_registras/Sutartis"
tags: [gov, rplc, sutartis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/studentu_registras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rplc/studentu_registras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2383/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rplc/studentu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio filialų studentų...

- **Model:** `datasets/gov/rplc/studentu_registras/Sutartis`[^manifest]
- **Dataset:** [Respublikinio Priklausomybės Ligų Centro studentų, atliekančių praktiką gydymo įstaigoje, duomenys](../studentu_registras.md) (`datasets/gov/rplc/studentu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/rplc/studentu_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/studentu_registras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rplc/studentu_registras/Sutartis` (`deployed`)[^manifest]
- **Provider:** `rplc` — Respublikinis priklausomybės ligų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `mokymo_istaiga` | `string` | — | `4` | `open` | — | Asmens mokymo įstaiga | Jei asmuo atlieka praktiką kaip savanoris, įraše žymima "Savanoris" |
| `praktikos_pradzia` | `date` | `D` | `4` | `open` | — | Praktikos pradžios data | — |
| `sutarties_rusis` | `string` | — | `3` | `open` | — | Sutarties rūšis | — |
| `komentaras` | `string` | — | `4` | `open` | — | Papildomas komentaras apie sutartį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rplc/studentu_registras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/studentu_registras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rplc/studentu_registras (https://data.gov.lt/datasets/2383/)

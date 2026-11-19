---
type: Table
title: "ADalis — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų A dalies duomenys"
description: "Iki 2022-06-30 deklaracijos A dalis naudota azartiniams lošimams, bet be lošimų įrenginių."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/ADalis"
tags: [gov, vmi, adalis, deployed, level-3, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1923/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ADalis — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų A dalies duomenys

Iki 2022-06-30 deklaracijos A dalis naudota azartiniams lošimams, bet be lošimų įrenginių.[^manifest]

- **Model:** `datasets/gov/vmi/azartiniai_losimai/ADalis`[^manifest]
- **Dataset:** [Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys](../azartiniai_losimai.md) (`datasets/gov/vmi/azartiniai_losimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/ADalis` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `mokescio_suma` | `number` | — | `2` | `open` | — | Mokesčio A dalies suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai (https://data.gov.lt/datasets/1923/)

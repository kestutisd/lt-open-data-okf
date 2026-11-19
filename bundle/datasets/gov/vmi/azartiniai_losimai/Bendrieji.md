---
type: Table
title: "Bendrieji — Bendrieji azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų duomenys"
description: "Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/Bendrieji"
tags: [gov, vmi, bendrieji, deployed, level-3, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1923/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Bendrieji — Bendrieji azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų duomenys

**Dataset Context:** Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą. Daugiau informacijos apie mokestį galite rasti Lietuvos Respublikos loterijų ir lošimų mokesčio įstatyme[^manifest]

- **Model:** `datasets/gov/vmi/azartiniai_losimai/Bendrieji`[^manifest]
- **Dataset:** [Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys](../azartiniai_losimai.md) (`datasets/gov/vmi/azartiniai_losimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/Bendrieji` (`deployed`)[^manifest]
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
| `mokescio_suma` | `number` | — | `2` | `open` | — | Mokesčio suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/azartiniai_losimai (https://data.gov.lt/datasets/1923/)

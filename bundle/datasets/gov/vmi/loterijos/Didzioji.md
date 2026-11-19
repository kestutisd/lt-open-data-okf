---
type: Table
title: "Didzioji — Didžiųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys"
description: "Loterija, kurios bilietai platinami visoje Lietuvos Respublikos teritorijoje ir nominalioji numatomų išplatinti bilietų vertė neribojama."
resource: "https://get.data.gov.lt/datasets/gov/vmi/loterijos/Didzioji"
tags: [gov, vmi, didzioji, deployed, level-3, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1922/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/loterijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Didzioji — Didžiųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys

Loterija, kurios bilietai platinami visoje Lietuvos Respublikos teritorijoje ir nominalioji numatomų išplatinti bilietų vertė neribojama.[^manifest]

- **Model:** `datasets/gov/vmi/loterijos/Didzioji`[^manifest]
- **Dataset:** [Loterijų verslo loterijų ir lošimų mokesčio deklaracijų (forma FR0583) duomenys](../loterijos.md) (`datasets/gov/vmi/loterijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/loterijos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/loterijos/Didzioji` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `mokescio_suma` | `number` | — | `2` | `open` | — | Mokesčio suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/loterijos (https://data.gov.lt/datasets/1922/)

---
type: Dataset
title: "Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys"
description: "Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai"
tags: [gov, vmi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys

Deklaraciją pildo juridiniai asmenys, organizuojantys azartinius lošimus pagal Azartinių lošimų įstatymą. Daugiau informacijos apie mokestį galite rasti Lietuvos Respublikos loterijų ir lošimų mokesčio įstatyme

- **Namespace:** `datasets/gov/vmi/azartiniai_losimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bendrieji](azartiniai_losimai/Bendrieji.md) | Bendrieji azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų duomenys | `3` | — | — | 4 | — |
| [ADalis](azartiniai_losimai/ADalis.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų A dalies duomenys | `3` | — | — | 4 | Iki 2022-06-30 deklaracijos A dalis naudota azartiniams lošimams, bet be lošimų įrenginių. |
| [BDalis](azartiniai_losimai/BDalis.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų B dalies duomenys | `3` | — | — | 7 | Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje. |
| [LosimoTipas](azartiniai_losimai/LosimoTipas.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų lošimo tipai | `3` | — | — | 4 | — |
| [IrenginioTipas](azartiniai_losimai/IrenginioTipas.md) | Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų įrenginio tipai | `3` | — | — | 7 | Nuo 2022-07-01 deklaracijos B dalis nepildoma, visi duomenys yra deklaracijos A dalyje. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv

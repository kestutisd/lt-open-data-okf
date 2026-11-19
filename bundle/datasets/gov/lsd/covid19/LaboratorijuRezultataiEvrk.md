---
type: Table
title: "LaboratorijuRezultataiEvrk — COVID-19 laboratorijų rezultatai pagal EVRK"
description: "Covid-19 diagnostinių tyrimų rezultatai, agreguoti pagal datą ir ekonominės veiklos rūšis (EVRK 2)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk"
tags: [gov, lsd, laboratorijurezultataievrk, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L46"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L46"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LaboratorijuRezultataiEvrk — COVID-19 laboratorijų rezultatai pagal EVRK

Covid-19 diagnostinių tyrimų rezultatai, agreguoti pagal datą ir ekonominės veiklos rūšis (EVRK 2)[^manifest]

- **Model:** `datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L46)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/LaboratorijuRezultataiEvrk` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `test_date` | `date` | `D` | `4` | `open` | — | Diagnostinių laboratorinių tyrimų atlikimo data | — |
| `evrk_group_code` | `ref` | [EkonominesVeiklosRusis](../cl/evrk/EkonominesVeiklosRusis.md) (`level=4 UUID`: `evrk_group_code._id`) | `4` | `open` | — | Tiriamųjų asmenų aktualios darbovietės ekonominės veiklos rūšių klasifikatoriaus (2 redakcija) grupės kodas. | nuoroda: https://osp.stat.gov.lt/static/evrk2.htm |
| `tests_positive` | `integer` | `U` | `4` | `open` | — | Teigiamų atsakymų skaičius (virusas aptiktas) | — |
| `tests_negative` | `integer` | `U` | `4` | `open` | — | Neigiamų atsakymų skaičius (virusas neaptiktas) | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L46 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L46)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)

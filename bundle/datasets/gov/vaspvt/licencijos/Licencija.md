---
type: Table
title: "Licencija — Licencijos"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Licencija"
tags: [gov, vaspvt, licencija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L35"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L35"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Licencija — Licencijos

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/Licencija`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L35)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Licencija` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `licencijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos identifikatorius | — |
| `licencijos_nr` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `sudarymo_data` | `datetime` | — | `2` | `open` | — | Licencijos išdavimo data | — |
| `panaikinimo_data` | `datetime` | — | `3` | `open` | — | Licencijos panaikinimo data | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos pavadinimas | — |
| `ja_buveines_adresas` | `string` | — | `1` | `open` | — | Juridinio asmens buveinės adresas | — |
| `isakymo_data` | `datetime` | — | `2` | `open` | — | Įsakymo data | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos būsena | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymas | — |
| `asmuo_ar_visuomene` | `string` | — | `4` | `open` | — | Žyma, ar tai asmens, ar visuomenės sveikatos priežiūros įstaigos licencija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"0"` | — | — | Sustabdyta | — |
| `busena` | `"1"` | — | — | Išduota | — |
| `busena` | `"2"` | — | — | Panaikinta | — |
| `asmuo_ar_visuomene` | `"0"` | — | — | Nepasirinkta | — |
| `asmuo_ar_visuomene` | `"1"` | — | — | Asmuo | — |
| `asmuo_ar_visuomene` | `"2"` | — | — | Visuomenė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sudarymo_data` | `update(property: "isduota")` | `property` | `4` | `open` | — | — | — |
| `panaikinimo_data` | `update(property: "panaikinta")` | `property` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(property: "istaiga.ja_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `ja_pavadinimas` | `update(property: "istaiga.ja_pavadinimas@lt", type: "")` | `property` | `4` | `open` | — | — | — |
| `ja_buveines_adresas` | `update(property: "istaiga.adresas", type: "")` | `property` | `4` | `open` | — | — | — |
| `isakymo_data` | `update(property: "isakyta")` | `property` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L35 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L35)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)

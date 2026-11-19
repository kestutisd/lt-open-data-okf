---
type: Table
title: "VTKlasifikatorius — AIS antstolių ir jų veiklos teritorijų klasifikatorius"
description: "AIS antstolių ir jų veiklos teritorijų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius"
tags: [gov, rc, vtklasifikatorius, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2184/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/vt_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VTKlasifikatorius — AIS antstolių ir jų veiklos teritorijų klasifikatorius

**Dataset Context:** AIS antstolių ir jų veiklos teritorijų klasifikatorius. Antstolių informacinės sistemos (AIS) klasifikatoriai. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 12 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius`[^manifest]
- **Dataset:** [AIS antstolių ir jų veiklos teritorijų klasifikatorius](../vt_klasifikatoriai.md) (`datasets/gov/rc/ais/vt_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `ant_indeksas` | `string` | — | `4` | `open` | — | Antstolio indeksas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje dirba antstolis, kodas iš Adresų registro | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/vt_klasifikatoriai (https://data.gov.lt/datasets/2184/)

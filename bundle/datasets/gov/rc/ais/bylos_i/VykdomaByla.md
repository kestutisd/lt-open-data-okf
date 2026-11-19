---
type: Table
title: "VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I"
description: "AIS duomenys apie antstolių vykdomas bylas – I (pagal skolininko gyvenamą teritoriją, išieškojimo dalyką, bylų skaičių, išieškotina sumą)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i/VykdomaByla"
tags: [gov, rc, vykdomabyla, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2169/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_i"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I

**Dataset Context:** AIS duomenys apie antstolių vykdomas bylas – I (pagal skolininko gyvenamą teritoriją, išieškojimo dalyką, bylų skaičių, išieškotina sumą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie antstolių vykdomas bylas. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/bylos_i/VykdomaByla`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I](../bylos_i.md) (`datasets/gov/rc/ais/bylos_i`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_i.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i/VykdomaByla` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta arba registruota skolininko (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `isieskojimo_dalykas` | `ref` | [Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) (`level=4 UUID`: `isieskojimo_dalykas._id`) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Antstolių vykdomų bylų kiekis (sugrupuota pagal savivaldybę ir išieškojimo dalyką) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Antstolių vykdomų bylų bendra išieškojimo suma (sugrupuota pagal savivaldybę ir išieškojimo dalyką) | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_i (https://data.gov.lt/datasets/2169/)

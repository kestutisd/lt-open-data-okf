---
type: Table
title: "AukcionoDalyvis — Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS"
description: "Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS (pagal elektroninių varžytynių / aukcionų rūšį registruota dalyvių, aktyvių dalyvių)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis"
tags: [gov, rc, aukcionodalyvis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2181/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/aukcionu_dalyviai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AukcionoDalyvis — Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS

**Dataset Context:** Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS (pagal elektroninių varžytynių / aukcionų rūšį registruota dalyvių, aktyvių dalyvių). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis`[^manifest]
- **Dataset:** [Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS](../aukcionu_dalyviai.md) (`datasets/gov/rc/ais/aukcionu_dalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `aukciono_tipas` | `ref` | [AukcionoTipas](../klasifikatoriai/AukcionoTipas.md) (`level=4 UUID`: `aukciono_tipas._id`) | `4` | `open` | — | Varžytynių / aukcionų tipo kodas iš AIS varžytynių ir aukcionų tipų klasifikatoriaus | — |
| `registravosi_fa` | `string` | — | `3` | `open` | — | Bendras užsiregistravusių fizinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `aktyvus_fa` | `string` | — | `3` | `open` | — | Bendras aktyviai dalyvavusių (didinusių pardavimo kainą) fizinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `registravosi_ja` | `string` | — | `3` | `open` | — | Bendras užsiregistravusių juridinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `aktyvus_ja` | `string` | — | `3` | `open` | — | Bendras aktyviai dalyvavusių (didinusių pardavimo kainą) juridinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/aukcionu_dalyviai (https://data.gov.lt/datasets/2181/)

---
type: Table
title: "AukcionoDalyvis — Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS"
description: "Spinta table datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_dalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# AukcionoDalyvis — Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS

- **Model:** `datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis`[^manifest]
- **Dataset:** [Aukcionų ir elektroninių varžytynių dalyvių duomenys iš AIS](../aukcionu_dalyviai.md) (`datasets/gov/rc/ais/aukcionu_dalyviai`)
- **Manifest CSV:** [datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_dalyviai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_dalyviai/AukcionoDalyvis`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `aukciono_tipas` | `ref` | [/datasets/gov/rc/ais/klasifikatoriai/AukcionoTipas](../klasifikatoriai/AukcionoTipas.md) | `4` | `open` | — | Varžytynių / aukcionų tipo kodas iš AIS varžytynių ir aukcionų tipų klasifikatoriaus | — |
| `registravosi_fa` | `string` | — | `3` | `open` | — | Bendras užsiregistravusių fizinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `aktyvus_fa` | `string` | — | `3` | `open` | — | Bendras aktyviai dalyvavusių (didinusių pardavimo kainą) fizinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `registravosi_ja` | `string` | — | `3` | `open` | — | Bendras užsiregistravusių juridinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |
| `aktyvus_ja` | `string` | — | `3` | `open` | — | Bendras aktyviai dalyvavusių (didinusių pardavimo kainą) juridinių asmenų kiekis sugrupuotas varžytinių, aukcionų tipą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_dalyviai.csv

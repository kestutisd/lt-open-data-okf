---
type: Table
title: "VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I"
description: "Spinta table datasets/gov/rc/ais/bylos_i/VykdomaByla (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i/VykdomaByla"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I

- **Model:** `datasets/gov/rc/ais/bylos_i/VykdomaByla`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I](../bylos_i.md) (`datasets/gov/rc/ais/bylos_i`)
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_i.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i/VykdomaByla`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta arba registruota skolininko (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `isieskojimo_dalykas` | `ref` | [/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Antstolių vykdomų bylų kiekis (sugrupuota pagal savivaldybę ir išieškojimo dalyką) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Antstolių vykdomų bylų bendra išieškojimo suma (sugrupuota pagal savivaldybę ir išieškojimo dalyką) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv

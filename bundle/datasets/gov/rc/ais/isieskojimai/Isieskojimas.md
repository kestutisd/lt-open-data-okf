---
type: Table
title: "Isieskojimas — Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus"
description: "Spinta table datasets/gov/rc/ais/isieskojimai/Isieskojimas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/isieskojimai/Isieskojimas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/isieskojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskojimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Isieskojimas — Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus

- **Model:** `datasets/gov/rc/ais/isieskojimai/Isieskojimas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus](../isieskojimai.md) (`datasets/gov/rc/ais/isieskojimai`)
- **Manifest CSV:** [datasets/gov/rc/ais/isieskojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskojimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/isieskojimai/Isieskojimas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `isieskojimo_dalykas` | `ref` | [/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuota pagal išieškojimo dalyką) | — |
| `pradine_isieskojimo_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra pradinė išieškojimo suma (sugrupuota pagal išieškojimo dalyką) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/isieskojimai.csv

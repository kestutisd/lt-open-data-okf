---
type: Table
title: "AukcionoRusis — Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys"
description: "Spinta table datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_rusys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_rusys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# AukcionoRusis — Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys

- **Model:** `datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis`[^manifest]
- **Dataset:** [Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys](../aukcionu_rusys.md) (`datasets/gov/rc/ais/aukcionu_rusys`)
- **Manifest CSV:** [datasets/gov/rc/ais/aukcionu_rusys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_rusys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `aukciono_tipas` | `ref` | [/datasets/gov/rc/ais/klasifikatoriai/AukcionoTipas](../klasifikatoriai/AukcionoTipas.md) | `4` | `open` | — | Varžytynių / aukcionų tipo kodas iš AIS varžytynių ir aukcionų tipų klasifikatoriaus | — |
| `kiek_paskelbta` | `string` | — | `3` | `open` | — | Bendras paskelbtų varžytinių, aukcionų kiekis | — |
| `kiek_ivyko` | `string` | — | `3` | `open` | — | Bendras įvykusių varžytinių, aukcionų kiekis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_rusys.csv

---
type: Table
title: "ParduotasTurtas — Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS"
description: "Spinta table datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# ParduotasTurtas — Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS

- **Model:** `datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas`[^manifest]
- **Dataset:** [Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS](../parduotas_turtas.md) (`datasets/gov/rc/ais/parduotas_turtas`)
- **Manifest CSV:** [datasets/gov/rc/ais/parduotas_turtas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `ivykdymo_metai` | `integer` | — | `2` | `open` | — | Varžytynių / aukcionų įvykdymo metai | — |
| `ivykdymo_ketvirtis` | `integer` | — | `3` | `open` | — | Varžytynių / aukcionų įvykdymo ketvirtis | — |
| `turto_potipis` | `ref` | [/datasets/gov/rc/ais/klasifikatoriai/TurtoPotipis](../klasifikatoriai/TurtoPotipis.md) | `4` | `open` | — | Turto potipio kodas iš AIS parduodamo turto potipių klasifikatoriaus | — |
| `turto_tipas` | `ref` | [/datasets/gov/rc/ais/klasifikatoriai/TurtoTipas](../klasifikatoriai/TurtoTipas.md) | `4` | `open` | — | Turto tipo kodas iš AIS parduodamo turto tipų klasifikatoriaus | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje yra nekilnojamas turtas, kodas iš Adresų registro | — |
| `turto_vienetu_kiekis` | `string` | — | `3` | `open` | — | Bendras varžytinėse / aukcionuose parduoto turto vienetų kiekis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykdymo_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv

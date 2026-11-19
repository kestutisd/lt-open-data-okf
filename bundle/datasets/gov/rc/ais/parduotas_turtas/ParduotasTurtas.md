---
type: Table
title: "ParduotasTurtas — Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS"
description: "Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS (pagal rūšį parduoto turto vertė, pagal rūšį parduoto nekilnojamojo turto vertė, parduoto nekilnojamojo turto vieta (savivaldybė)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas"
tags: [gov, rc, parduotasturtas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2180/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/parduotas_turtas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ParduotasTurtas — Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS

**Dataset Context:** Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS (pagal rūšį parduoto turto vertė, pagal rūšį parduoto nekilnojamojo turto vertė, parduoto nekilnojamojo turto vieta (savivaldybė). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas`[^manifest]
- **Dataset:** [Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS](../parduotas_turtas.md) (`datasets/gov/rc/ais/parduotas_turtas`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/parduotas_turtas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas/ParduotasTurtas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `ivykdymo_metai` | `integer` | — | `2` | `open` | — | Varžytynių / aukcionų įvykdymo metai | — |
| `ivykdymo_ketvirtis` | `integer` | — | `3` | `open` | — | Varžytynių / aukcionų įvykdymo ketvirtis | — |
| `turto_potipis` | `ref` | [TurtoPotipis](../klasifikatoriai/TurtoPotipis.md) (`level=4 UUID`: `turto_potipis._id`) | `4` | `open` | — | Turto potipio kodas iš AIS parduodamo turto potipių klasifikatoriaus | — |
| `turto_tipas` | `ref` | [TurtoTipas](../klasifikatoriai/TurtoTipas.md) (`level=4 UUID`: `turto_tipas._id`) | `4` | `open` | — | Turto tipo kodas iš AIS parduodamo turto tipų klasifikatoriaus | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje yra nekilnojamas turtas, kodas iš Adresų registro | — |
| `turto_vienetu_kiekis` | `string` | — | `3` | `open` | — | Bendras varžytinėse / aukcionuose parduoto turto vienetų kiekis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykdymo_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/parduotas_turtas (https://data.gov.lt/datasets/2180/)

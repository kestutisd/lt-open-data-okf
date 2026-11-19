---
type: Table
title: "NtrLeisinasObjektoTipas — Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas"
tags: [gov, rc, ntrleisinasobjektotipas, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrLeisinasObjektoTipas — Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `regt_tipas, obje_tipas, loti_priklauso`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `regt_tipas` | `integer` | — | `3` | `open` | — | Registro tipas | — |
| `obje_tipas` | `ref` | [NtrObjektoTipas](NtrObjektoTipas.md) (`level=4 UUID`: `obje_tipas._id`) | `4` | `open` | — | Turto objekto tipas | — |
| `loti_priklauso` | `integer` | — | `3` | `open` | — | Priklauso objekto tipui | — |
| `loti_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `loti_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `loti_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai (https://data.gov.lt/datasets/1895/)

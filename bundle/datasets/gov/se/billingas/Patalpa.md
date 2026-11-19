---
type: Table
title: "Patalpa — Patalpos"
description: "Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas/Patalpa"
tags: [gov, se, patalpa, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2886/"
    title: "data.gov.lt DCAT-AP — datasets/gov/se/billingas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Patalpa — Patalpos

Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos. Rinkinyje pateikiama patalpos plotas, pastato statybos metai, aukštų skaičius, pastato tipas, jo paskirtis. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes – triukšmą.[^manifest]

- **Model:** `datasets/gov/se/billingas/Patalpa`[^manifest]
- **Dataset:** [Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo...](../billingas.md) (`datasets/gov/se/billingas`)[^manifest]
- **Manifest CSV:** [datasets/gov/se/registras.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas/Patalpa` (`deployed`)[^manifest]
- **Provider:** `se` — AB Šiaulių energija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `patalpos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Unikalus patalpos identifikatorius | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Unikalus pastato identitfikatorius | — |
| `patalpos_plotas` | `number` | — | `4` | `open` | — | Patalpos plotas | — |
| `statybos_metai` | `date` | `Y` | `4` | `open` | — | Statybos metai, gauti iš Registrų Centro | — |
| `pastato_aukstu_skaicius` | `number` | — | `4` | `open` | — | Pastato aukštų skaičius, gautas iš Registrų Centro | — |
| `pastato_tipas` | `string` | — | `4` | `open` | — | Pastato tipas, gautas iš Registrų Centro | — |
| `pastato_paskirtis` | `string` | — | `4` | `open` | — | Pastato paskirtis, gautas iš Registrų Centro | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | X koordinatės LKS sistemoje. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą. | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Y koordinatės LKS sistemoje. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą. | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Geometrija | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/se/billingas (https://data.gov.lt/datasets/2886/)

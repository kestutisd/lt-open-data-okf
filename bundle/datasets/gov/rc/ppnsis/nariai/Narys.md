---
type: Table
title: "Narys — PPNSIS duomenys apie politinių organizacijų narius"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizcijų narius - jų lytį, amžių, pilietybę, geografinę padėtį ir narystę partijoje"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai/Narys"
tags: [gov, rc, narys, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1736/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Narys — PPNSIS duomenys apie politinių organizacijų narius

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizcijų narius - jų lytį, amžių, pilietybę, geografinę padėtį ir narystę partijoje[^manifest]

- **Model:** `datasets/gov/rc/ppnsis/nariai/Narys`[^manifest]
- **Dataset:** [Politinių organizacijų narių duomenys apie lytį, amžių, pilietybę, geografinę padėtį ir narystę](../nariai.md) (`datasets/gov/rc/ppnsis/nariai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai/Narys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr, politine_organizacija`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `3` | `open` | — | Politinės organizacijos nario eil. numeris šiame duomenų rinkinyje | — |
| `nar_lytis` | `string` | — | `4` | `open` | — | Politinės organizacijos nario lytis | — |
| `nar_amzius` | `string` | — | `3` | `open` | — | Politinės organizacijos nario amžiaus grupė | — |
| `nario_pilietybe` | `string` | — | `3` | `open` | — | Politinės organizacijos nario pilietybė | — |
| `adreso_salis` | `string` | — | `3` | `open` | — | Šalies, kurioje deklaruota partijos nario gyvenamoji vieta, kodas iš Gyventojų registro | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota partijos nario gyvenamoji vieta, iš Gyventojų registro | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Politinės organizacijos sąrašo pateikimo data | — |
| `politine_organizacija` | `ref` | [PolitineOrganizacija](../politines_organizacijos/PolitineOrganizacija.md) (`level=4 UUID`: `politine_organizacija._id`) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, pavadinimas iš Juridinių asmenų registro | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nar_lytis` | `"V"` | — | — | Vyras | — |
| `nar_lytis` | `"M"` | — | — | Moteris | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariai (https://data.gov.lt/datasets/1736/)

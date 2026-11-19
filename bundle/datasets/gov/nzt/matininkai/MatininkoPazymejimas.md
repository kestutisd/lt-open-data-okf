---
type: Table
title: "MatininkoPazymejimas — Matininkai, geodezininkai ir žemėtvarkos planavimo dokumentų rengėjai"
description: "Spinta table datasets/gov/nzt/matininkai/MatininkoPazymejimas (21 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nzt/matininkai/MatininkoPazymejimas"
tags: [gov, nzt, matininkopazymejimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/matininkai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/nzt/matininkai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2262/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nzt/matininkai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MatininkoPazymejimas — Matininkai, geodezininkai ir žemėtvarkos planavimo dokumentų rengėjai

- **Model:** `datasets/gov/nzt/matininkai/MatininkoPazymejimas`[^manifest]
- **Dataset:** [Duomenys apie asmenis, kuriems teisės aktų nustatyta tvarka išduoti kvalifikacijos pažymėjimai...](../matininkai.md) (`datasets/gov/nzt/matininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nzt/matininkai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/matininkai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nzt/matininkai/MatininkoPazymejimas` (`deployed`)[^manifest]
- **Provider:** `nzt` — Nacionalinė žemės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Matininko vardas, pavardė | Pateikta tik galiojantiems pažymėjimams |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID` via `Savivaldybe[pavadinimas]`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė kurioje dirba specialistas | — |
| `isduotas` | `date` | `D` | `4` | `open` | — | Kvalifikacijos pažymėjimo išdavimo data | — |
| `nr` | `string` | — | `4` | `open` | — | Kvalifikacijos pažymėjimo numeris | — |
| `pagrindas` | `string` | — | `4` | `open` | — | Pažymėjimo išdavimo pagrindas | — |
| `sustabdytas` | `date` | `D` | `4` | `open` | — | Pažymėjimo sustabdymo data | — |
| `sust_pagrindas` | `string` | — | `4` | `open` | — | Pažymėjimo sustabdymo pagrindas | — |
| `sust_panaikintas` | `date` | `D` | `4` | `open` | — | Pažymėjimo sustabdymo panaikinimo data | — |
| `sust_panaik_pagrindas` | `string` | — | `4` | `open` | — | Pažymėjimo sustabdymo panaikinimo pagrindas | — |
| `panaikintas` | `date` | `D` | `4` | `open` | — | Pažymėjimo galiojimo panaikinimo data | — |
| `panaik_pagrindas` | `string` | — | `4` | `open` | — | Pažymėjimo galiojimo panaikinimo pagrindas | — |
| `bendr_kursu_pab` | `date` | `D` | `4` | `open` | — | Pastinkinių bendrosios dalies kvalifikacijos tobulinimo kursų data | — |
| `tiksl_kursu_pab` | `date` | `D` | `4` | `open` | — | Pastinkinių tikslinės dalies kvalifikacijos tobulinimo kursų data | — |
| `galioja` | `boolean` | — | `4` | `open` | — | Šiuo metu pažymėjimas galioja | — |
| `tipas` | `string` | — | `4` | `open` | — | Pažymėjimo tipas | — |
| `tipo_pavadinimas` | `string` | — | `4` | `open` | — | Pažymėjimo tipo paaiškinimas | — |
| `ispetas` | `date` | `D` | `4` | `open` | — | Įspėjimo data | Įspėjimo apie tai, kad nepašalinus pažeidimų pažymėjimo galiojimas bus sustabdytas, data |
| `ispejimo_terminas` | `date` | `D` | `4` | `open` | — | Įspėjimo terminas | Terminas, iki kada įspėjus turi būti pašalinti pažeidimai |
| `pazeid_pasalinti` | `date` | `D` | `4` | `open` | — | Pažeidimų pašalinimo data | — |
| `obj_iregistruotas` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data registre | — |
| `obj_isregistruotas` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data registre | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"M"` | — | — | Matininko | — |
| `tipas` | `"ME"` | — | — | Matininko eksperto | — |
| `tipas` | `"1GKV"` | — | — | Geodezininko | — |
| `tipas` | `"ŽS"` | — | — | žemėtvarkos schemų rengėjo | — |
| `tipas` | `"FP"` | — | — | žemės sklypų formavimo ir pertvarkymo projektų rengėjo | — |
| `tipas` | `"KP"` | — | — | kaimo plėtros žemėtvarkos projektų rengėjo | — |
| `tipas` | `"ŽK"` | — | — | žemės konsolidacijos projektų rengėjo | — |
| `tipas` | `"ŽR"` | — | — | žemės reformos žemėtvarkos projektų rengėjo | — |
| `tipas` | `"VP"` | — | — | žemės paėmimo visuomenės poreikiams projektų rengėjo | — |
| `tipas` | `"KI"` | — | — | suteikiantis teisę rengti karinės infrastruktūros projektus | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas_pavarde` | `update(property: "vardas_pavarde", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pagrindas` | `update(property: "pagrindas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `sust_pagrindas` | `update(property: "sust_pagrindas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `sust_panaik_pagrindas` | `update(property: "sust_panaik_pagrindas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `panaik_pagrindas` | `update(property: "panaik_pagrindas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `tipo_pavadinimas` | `update(property: "tipo_pavadinimas", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/nzt/matininkai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/matininkai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nzt/matininkai (https://data.gov.lt/datasets/2262/)

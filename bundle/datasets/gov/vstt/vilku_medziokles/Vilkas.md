---
type: Table
title: "Vilkas — Duomenys apie sumedžiotus vilkus"
description: "Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/Vilkas"
tags: [gov, vstt, vilkas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilkas — Duomenys apie sumedžiotus vilkus

Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. Rinkinio objektas - vienas sumedžiotas vilkas. Nurodomas medžioklės laikas, vieta, būdas, duomenys apie vilką (amžius, lytis, sveikatos būklė) ir gaują (jauniklių ir suaugusių vilkų skaičius). Duomenų teikėjas: Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vstt/vilku_medziokles/Vilkas`[^manifest]
- **Dataset:** [Sumedžioti vilkai Lietuvoje](../vilku_medziokles.md) (`datasets/gov/vstt/vilku_medziokles`)[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/Vilkas` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `iraso_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `medziokles_laikas` | `datetime` | `L` | `4` | `open` | — | Vilko sumedžiojimo laiko žyma | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje įvyko medžioklė. Požymis buvo išskaičiuotas vilko sumedžiojimo vietos koordinatę prijungiant prie 10x10 km gardelių, kuriomis suskirstyta Lietuvos Respublikos teritorija. Kiekviena gardelė yra priskirta tam tikrai savivaldybei, tad pagal šį požymį buvo išskaičiuota vilko sumedžiojimo vietos savivaldybė. | — |
| `medziojimo_budas` | `string` | — | `4` | `open` | — | Vilko medžiojimo būdas | — |
| `amzius` | `string` | — | `4` | `open` | — | Vilko amžius | — |
| `lytis` | `string` | — | `4` | `open` | — | Vilko lytis | — |
| `ar_pazeistas_niezu` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas buvo pažeistas niežų | — |
| `ar_kiti_defektai` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas turėjo kitų defektų | — |
| `ar_priklause_gaujai` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas priklausė gaujai | — |
| `viso_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras vilkų skaičius gaujoje | — |
| `suaugusiu_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras suaugusių vilkų skaičius gaujoje | — |
| `jaunikliu_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras jauniklių skaičius gaujoje | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Sumedžioto vilko taško koordinatė. | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `medziojimo_budas` | `"tykojant"` | — | — | — | — |
| `medziojimo_budas` | `"varant"` | — | — | — | — |
| `medziojimo_budas` | `"kita"` | — | — | — | — |
| `medziojimo_budas` | `"su vėliavėlėmis"` | — | — | — | — |
| `amzius` | `"Vyresnis nei 1 metų amžiaus"` | — | — | — | — |
| `amzius` | `"Jauniklis iki 1 metų amžiaus"` | — | — | — | — |
| `lytis` | `"Patinas"` | — | — | — | — |
| `lytis` | `"Patelė"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles (https://data.gov.lt/datasets/2889/)

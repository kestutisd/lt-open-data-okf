---
type: Table
title: "Istaiga — Panevėžio miesto ikimokyklinio ugdymo įstaigos"
description: "Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigas"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga"
tags: [gov, panevezio_m_sav, istaiga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3843/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Istaiga — Panevėžio miesto ikimokyklinio ugdymo įstaigos

Informacija apie Panevėžio miesto ikimokyklinio ugdymo įstaigas[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga`[^manifest]
- **Dataset:** [Panevėžio miesto ikimokyklinio ugdymo įstaigų, grupių ir vaikų registracijos duomenys](../ikimokyklinis_ugdymas.md) (`datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas/Istaiga` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `istaigos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_id` | `string` | — | `4` | `open` | — | Įstaigos ID numeris | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos JAR kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Įstaigos JAR kodo validacija | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `istaigos_vadovas` | `string` | — | `4` | `open` | — | Įstaigos vadovas | — |
| `istaigos_adresas` | `string` | — | `4` | `open` | — | Įstaigos adresas | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Įstaigo vietos taško koordinatės | — |
| `istaigos_tel` | `string` | — | `4` | `open` | — | Įstaigos telefono numeris | — |
| `istaigos_el_pastas` | `string` | — | `4` | `open` | — | Įstaigos el. paštas | — |
| `istaigos_svetaine` | `string` | — | `4` | `open` | — | Įstaigos internetinės svetainės adresas | — |
| `mokymo_kalba` | `string` | — | `4` | `open` | — | Įstaigos bendravimo ir mokymo kalba | — |
| `grupiu_sk` | `integer` | — | `4` | `open` | — | Grupių skaičius įstaigoje | — |
| `vietu_sk` | `integer` | — | `4` | `open` | — | Vietų skaičius įstaigoje | — |
| `laisvu_vietu_sk` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius grupėje | — |
| `budinti_grupe` | `boolean` | — | `4` | `open` | — | Budinti grupė (yra / nėra) | — |
| `specialioji_grupe` | `boolean` | — | `4` | `open` | — | Specialioji grupė (yra / nėra) | — |
| `darbo_laikas` | `string` | — | `4` | `open` | — | Grupių darbo laikas įstaigoje | — |
| `veiklos_aprasymas` | `string` | — | `4` | `open` | — | Įstaigos veiklos aprašymas | — |
| `darbuotojai` | `string` | — | `4` | `open` | — | Įstaigos darbuotojai | — |
| `duomenys_gauti` | `datetime` | `L` | `4` | `open` | — | Duomenų gavimo data ir laikas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/ikimokyklinis_ugdymas (https://data.gov.lt/datasets/3843/)

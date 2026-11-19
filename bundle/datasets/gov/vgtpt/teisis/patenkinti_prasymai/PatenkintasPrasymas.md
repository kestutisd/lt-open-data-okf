---
type: Table
title: "PatenkintasPrasymas — Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys"
description: "Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie gautų prašymų suteikti antrinę teisinę pagalbą patenkinimą."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas"
tags: [gov, vgtpt, patenkintasprasymas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1758/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/patenkinti_prasymai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PatenkintasPrasymas — Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys

**Dataset Context:** Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie gautų prašymų suteikti antrinę teisinę pagalbą patenkinimą. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 1 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0. Atvėrimo data —2023-04-03.[^manifest]

- **Model:** `datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas`[^manifest]
- **Dataset:** [Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys](../patenkinti_prasymai.md) (`datasets/gov/vgtpt/teisis/patenkinti_prasymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `gauta_metai` | `integer` | — | `2` | `open` | — | Metai, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `gauta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `priimta_metai` | `integer` | — | `4` | `open` | — | Metai, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `priimta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `teritorijos_kodas` | `ref` | [Teritorija](../klasifikatoriai/Teritorija.md) (`level=4 UUID`: `teritorijos_kodas._id`) | `4` | — | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `gauti_prasymai` | `integer` | `U` | `4` | `open` | — | Teritoriniame padalinyje gautų prašymų suteikti antrinę teisinę pagalbą skaičius | — |
| `patenkinti_prasymai` | `integer` | `U` | `4` | `open` | — | Teritoriniame padalinyje patenkintų prašymų suteikti antrinę teisinę pagalbą skaičius | — |
| `patenkinti_prasymai_dalis` | `integer` | `%` | `4` | `open` | — | Patenkintų prašymų suteikti antrinę teisinę pagalbą skaičius procentais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gauta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `priimta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/patenkinti_prasymai (https://data.gov.lt/datasets/1758/)

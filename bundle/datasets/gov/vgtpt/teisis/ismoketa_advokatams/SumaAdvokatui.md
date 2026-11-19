---
type: Table
title: "SumaAdvokatui — Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė"
description: "Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmę ir vertę."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui"
tags: [gov, vgtpt, sumaadvokatui, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1760/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/ismoketa_advokatams"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SumaAdvokatui — Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė

**Dataset Context:** Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmę ir vertę. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 1 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0. Atvėrimo data —2023-04-03.[^manifest]

- **Model:** `datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui`[^manifest]
- **Dataset:** [Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė](../ismoketa_advokatams.md) (`datasets/gov/vgtpt/teisis/ismoketa_advokatams`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `sprendimo_metai` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį metai | — |
| `sprendimo_ketvirtis` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį ketvirtis | — |
| `teritorijos_kodas` | `ref` | [Teritorija](../klasifikatoriai/Teritorija.md) (`level=4 UUID`: `teritorijos_kodas._id`) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `bylos_rusies_kodas` | `ref` | [BylosRusis](../klasifikatoriai/BylosRusis.md) (`level=4 UUID`: `bylos_rusies_kodas._id`) | `4` | `open` | — | Bylos, kurioje reikalinga antrinė teisinė pagalba, rūšies kodas | Iš TEISIS bylų rūšių klasifikatoriaus |
| `moketina_suma` | `number` | — | `2` | `open` | — | Sprendime nurodytas antrinės teisinės pagalbos teikėjui mokėtinas užmokestis | — |
| `trukme` | `integer` | `min` | `4` | `open` | — | Antrinės teisinės pagalbos teikėjo sugaišto laiko trukmė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `moketina_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/ismoketa_advokatams (https://data.gov.lt/datasets/1760/)

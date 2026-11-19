---
type: Table
title: "InstitucijosDarbuotojas — Rokiškio savivaldybės darbuotojai"
description: "Rokiškio savivaldybės darbuotojai"
resource: "https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas"
tags: [gov, rokiskio_r_sav, institucijosdarbuotojas, deployed, level-4, cadence-monthly_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2898/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# InstitucijosDarbuotojas — Rokiškio savivaldybės darbuotojai

**Dataset Context:** Rokiškio savivaldybės darbuotojai[^manifest]

- **Model:** `datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas`[^manifest]
- **Dataset:** [Rokiškio savivaldybės darbuotojai](../institucijos_darbuotojai.md) (`datasets/gov/rokiskio_r_sav/institucijos_darbuotojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai/InstitucijosDarbuotojas` (`deployed`)[^manifest]
- **Provider:** `rokiskio_r_sav` — Rokiškio rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `tabelio_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tabelio_nr` | `string` | — | `4` | `open` | — | Darbuotojo unikalus tabelio numeris | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas unikaliai šfruotas šiam rinkiniui (su kitais rinkiniais nesijungia) | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gim_desimtm_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gim_desimtm` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `darbo_pradzia` | `date` | `D` | `4` | `open` | — | Darbo pradžios data | — |
| `darbo_pabaiga` | `date` | `D` | `4` | `open` | — | Darbo pabaigos data | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyriaus pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/institucijos_darbuotojai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rokiskio_r_sav/institucijos_darbuotojai (https://data.gov.lt/datasets/2898/)

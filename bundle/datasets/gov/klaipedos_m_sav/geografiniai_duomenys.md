---
type: Dataset
title: "Klaipėdos miesto savivaldybės objektų geografiniai duomenys"
description: "Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys"
tags: [gov, klaipedos_m_sav, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2856/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/geografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Klaipėdos miesto savivaldybės objektų geografiniai duomenys

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Pateikiamos lentelės apie šiuos objektus: •	Prekybos vietos •	Seniūnaitijos •	Sporto vietos •	Žaidimų aikštelės Pateikiami patys objektai bei jų koordinatės aktualūs šiai dienai. Kiekvienos lentelės viena eilutė atitinką vieną objektą Klaipėdos miesto savivaldybėje. Duomenų teikėjas: Klaipėdos miesto savivaldybė Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/klaipedos_m_sav/geografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2856/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys`[^dcat]
- **Portal Title (`@lt`):** Klaipėdos miesto savivaldybės objektų geografiniai duomenys[^dcat]
- **Portal Title (`@en`):** Geographical data of Klaipeda Municipality Objects[^dcat]
- **Issued (`dct:issued`):** `2024-12-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-15` .. `2025-10-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Pateikiamos lentelės apie šiuos objektus: •	Prekybos vietos; •	Seniūnaitijos; •	Sporto vietos; •	Žaidimų aikštelės. Pateikiami patys objektai bei jų koordinatės aktualūs šiai dienai. Kiekvienos lentelės viena eilutė atitinką vieną objektą Klaipėdos miesto savivaldybėje. Duomenų teikėjas – Klaipėdos miesto savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of THE Klaipeda Municipality ARGIS accumulates geographical data of the city. Here are tables about the following objects: • Trading venues • Elders • Sports venues • Playgrounds The objects themselves are displayed and their coordinates are relevant today. One row of each table corresponds to one object in Klaipeda Municipality. Data Provider: Klaipeda Municipality Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PrekybosVieta](geografiniai_duomenys/PrekybosVieta.md) | Klaipėdos miesto savivaldybėje esančios prekybos vietos | `4` | `object_id` | — | `7` | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [Seniunaitija](geografiniai_duomenys/Seniunaitija.md) | Klaipėdos miesto savivaldybės seniūnaitijos | `4` | `object_id` | — | `5` | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [SportoVieta](geografiniai_duomenys/SportoVieta.md) | Klaipėdos miesto savivaldybėje esančios sporto vietos | `4` | `vda_prime_key` | — | `9` | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |
| [ZaidimuAikstele](geografiniai_duomenys/ZaidimuAikstele.md) | Klaipėdos miesto savivaldybėje esančios žaidimų aikštelės | `4` | `object_id` | — | `7` | Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/geografiniai_duomenys (https://data.gov.lt/datasets/2856/)

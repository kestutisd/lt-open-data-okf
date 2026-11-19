---
type: Table
title: "Licencija — Panevėžio miesto savivaldybės išduotos alkoholio ir tabako prekybos licencijas"
description: "Informacija apie Panevėžio miesto savivaldybės išduotas alkoholio ir tabako prekybos licencijas"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas/Licencija"
tags: [gov, panevezio_m_sav, licencija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4005/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/leidimu_administravimas"
    author: "team:vda"
    last_modified: "2026-11-11T00:00:00Z"
---

# Licencija — Panevėžio miesto savivaldybės išduotos alkoholio ir tabako prekybos licencijas

Informacija apie Panevėžio miesto savivaldybės išduotas alkoholio ir tabako prekybos licencijas[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/leidimu_administravimas/Licencija`[^manifest]
- **Dataset:** [Panevėžio miesto savivaldybės išduotos licencijos ir jų apmokėjimai](../leidimu_administravimas.md) (`datasets/gov/panevezio_m_sav/leidimu_administravimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas/Licencija` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `licencijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-11-11`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos identifikatorius | — |
| `licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos tipas | — |
| `licencijos_isdavimo_data` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `licencija_galioja_nuo` | `date` | `D` | `4` | `open` | — | Licencijos galiojimo pradžia | — |
| `licencija_galioja_iki` | `date` | `D` | `4` | `open` | — | Licencijos galiojimo pabaiga | — |
| `licencijos_numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduotas leidimas, kodas | — |
| `juridinio_asmens_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduota leidimas, pavadinimas | — |
| `fizinio_asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduota leidimas, kodas | — |
| `fizinio_asmens_vardas_pavarde` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduota leidimas, vardas ir pavardė | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Asmens tipas | — |
| `vda_asmens_tipas` | `string` | — | `4` | `open` | — | VDA nustatytas asmens tipas | — |
| `pardavimo_vieta` | `string` | — | `4` | `open` | — | Pardavimo vieta | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Pardavimo vietos koordinatės WGS koordinačių sistemoje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_tipas` | `"LietuvosJuridinis"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"LietuvosFizinis"` | — | — | Fizinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"UzsienioJuridinis"` | — | — | Juridinis asmuo įsisteigęs užsienyje | — |
| `vda_asmens_tipas` | `"Juridinis asmuo"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `vda_asmens_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo Lietuvos pilietis | — |
| `vda_asmens_tipas` | `"Kita"` | — | — | Nenustatytas asmuo | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/leidimu_administravimas (https://data.gov.lt/datasets/4005/)

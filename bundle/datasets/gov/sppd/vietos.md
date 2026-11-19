---
type: Dataset
title: "Socialinės globos licencijų paslaugų teikimo vietos"
description: "Rinkinyje pateikiami Socialinės globos paslaugas teikiančių įstaigų licencijuojamos veiklos vykdymo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/sppd/vietos"
tags: [gov, sppd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2869/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sppd/vietos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Socialinės globos licencijų paslaugų teikimo vietos

- **Namespace:** `datasets/gov/sppd/vietos`[^manifest]
- **Manifest CSV:** [datasets/gov/sppd/soc_globos_licencijos.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/vietos` (`deployed`)[^manifest]
- **Provider:** `sppd` — Socialinių paslaugų priežiūros departamentas prie SADM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2869/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sppd/vietos`[^dcat]
- **Portal Title (`@lt`):** Socialinės globos paslaugas teikiančių įstaigų išduotų, sustabdytų, panaikintų licencijų sąrašas ir veiklos vietos[^dcat]
- **Portal Title (`@en`):** List of licenses issued, suspended, revoked[^dcat]
- **Issued (`dct:issued`):** `2024-11-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-22` .. `2026-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Socialinės globos paslaugas teikiančių įstaigų licencijuojamos veiklos vykdymo duomenys. Licencijos išduodamos nuo 2013 m. Rinkinį sudaro: įstaigos kodas, pavadinimas, savivaldybė, adresas su koordinatėmis, tipas, licencijos numeris, statusas, registracijos, sustabdymo, panaikinimo ir tikslinimo datos. Nuo 2025 m. bus padidintas licencijos būsenų skaičius. Rinkinyje pateikiami licencijoms priskirtų veiklos vietų adresai, LKI koordinatės, paskirtis, statusai ir vietos būsenos bei jų datos. Duomenų teikėjas – Socialinių paslaugų priežiūros departamentas prie Socialinės apsaugos ir darbo ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package provides data on the licensed activities of institutions providing social care services. Licences shall be issued from 2013 until now. The set consists of: institution code, name, municipality, address with coordinates, type, license number, status, registration, suspension, cancellation and revision dates. Data Provider - Department of Social Services Supervision under the Ministry of Social Security and Labour Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VeiklosVieta](vietos/VeiklosVieta.md) | Socialinės globos licencijų paslaugų teikimo vietos | `4` | `vda_id` | — | `11` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sppd/vietos (https://data.gov.lt/datasets/2869/)

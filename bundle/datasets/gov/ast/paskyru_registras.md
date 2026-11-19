---
type: Dataset
title: "Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai"
description: "Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai Rinkinyje pateikiamai UAB “Alytaus šilumos tinklai” paskyrų registro duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ast/paskyru_registras"
tags: [gov, ast, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ast/paskyru_registras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2782/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/paskyru_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai

- **Namespace:** `datasets/gov/ast/paskyru_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/ast/paskyru_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/paskyru_registras` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2782/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ast/paskyru_registras`[^dcat]
- **Portal Title (`@lt`):** Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai[^dcat]
- **Portal Title (`@en`):** Hot water and heating connections of Alytus heat networks, disconnectors[^dcat]
- **Issued (`dct:issued`):** `2024-09-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-09-09` .. `2024-09-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai Rinkinyje pateikiamai UAB “Alytaus šilumos tinklai” paskyrų registro duomenys. Registre registruojamos paskyros, kurios pildomos šildymo ir/arba karšto vandens paslaugų pajungimui ir atjungimui objektuose, kurie tampa klientais, atsisako paslaugų, arba – dažniausias atvejis - pajungiamas/atjungiamas šildymas (šildymo sezono metu). Viena eilutė atitinka vieną kontrolieriau vizitą į atitinkamą adresą. Duomenys kaupiami nuo 2019 metų. ir iki dabar. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Hot water and heating connections of Alytus heat networks, disconnectors The collection contains the data of the register of accounts of UAB “Alytaus šilumos tinklai”. The register shall record accounts to be filled in for connection and disconnection of heating and/or hot water services in facilities that become customers, refuse services or, in the most common case, switch off/disconnect heating (during the heating season). One line corresponds to one visit by the controller to the address concerned. The data has been compiled since 2019. and until now. ENQUIRIES: State Data Control Opening Team: atverimas@stat.gov.lt[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PajungimasAtjungimas](paskyru_registras/PajungimasAtjungimas.md) | Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai | `4` | `vda_prime_key` | — | `14` | Rinkinyje pateikiamai UAB “Alytaus šilumos tinklai” paskyrų registro duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/paskyru_registras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/paskyru_registras (https://data.gov.lt/datasets/2782/)

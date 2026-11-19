---
type: Dataset
title: "Neformaliojo vaikų švietimo programos"
description: "Duomenų rinkinys sudarytas iš dviejų lentelių – „Neformaliojo vaikų švietimo programos“ ir „Neformaliojo vaikų švietimo programų lankymas“."
resource: "https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos"
tags: [gov, nsa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3997/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Neformaliojo vaikų švietimo programos

- **Namespace:** `datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3997/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`[^dcat]
- **Portal Title (`@lt`):** Neformaliojo vaikų švietimo programos[^dcat]
- **Portal Title (`@en`):** Non-formal children's education programmes[^dcat]
- **Issued (`dct:issued`):** `2025-12-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-12-16` .. `2025-12-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys sudarytas iš dviejų lentelių – „Neformaliojo vaikų švietimo programos“ ir „Neformaliojo vaikų švietimo programų lankymas“. Neformaliojo vaikų švietimo programų lentelės kiekvienoje eilutėje pateikiama vienos švietimo programos informacija lietuvių ir anglų kalbomis: programos kodas ir pavadinimas, programos įregistravimo į Neformaliojo švietimo programų registrą ir išregistravimo datos bei išregistravimo priežastis, programos paskirtis, kryptis ir pakraipa, reikalavimai, programos teikėjas, teikėjo tipas, adresas ir kodas, teikėjo kodo tipas ir struktūra. Neformaliojo vaikų švietimo programų lankymo lentelės viena eilutė atitinka programą lankiusių mokinių skaičių atitinkamais mokslo metais. Lentelėje taip pat nurodomas programos identifikatorius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](neformaliojo_vaiku_svietimo_programos/Programa.md) | Neformaliojo vaikų švietimo programos | `4` | `vda_prime_key` | — | `25` | Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą |
| [Lankymas](neformaliojo_vaiku_svietimo_programos/Lankymas.md) | Neformaliojo vaikų švietimo programų lankymas | `4` | `vda_prime_key` | — | `4` | Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą lankiusių mokinių skaičių atitinkamais mokslo metais |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos (https://data.gov.lt/datasets/3997/)

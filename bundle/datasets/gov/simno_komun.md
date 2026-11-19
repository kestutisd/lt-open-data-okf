---
type: Dataset
title: "Alytaus rajono savivaldybės įmonė „Simno komunalininkas“"
description: "Iš gręžinių išgautas (pakeltas) vanduo Rinkinyje pateikiamas Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje vandens gavybos apskaitoje stebimas iš gręžinių išgauto (pakelto) vandens kiekis ir jo teikimas gyventojams bei įmonėms."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun"
tags: [gov, simno_komun, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/pakeltas_vanduo.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2774/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Alytaus rajono savivaldybės įmonė „Simno komunalininkas“

- **Namespace:** `datasets/gov/simno_komun`[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/pakeltas_vanduo.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2774/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/simno_komun`[^dcat]
- **Portal Title (`@lt`):** Alytaus rajono iš gręžinių išgauto (pakelto) vandens kiekis ir jo tiekimas[^dcat]
- **Portal Title (`@en`):** Quantity and supply of water extracted from wells in Alytus District Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-09-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-09-04` .. `2025-03-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Iš gręžinių išgautas (pakeltas) vanduo Rinkinyje pateikiamas Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje vandens gavybos apskaitoje stebimas iš gręžinių išgauto (pakelto) vandens kiekis ir jo teikimas gyventojams bei įmonėms. Taip pat fiksuojamas technologinio vandens, skirto įrenginiams plauti, kiekis. Viena eilutė atitinka atitinkamo gręžinio tam tikro periodo bei parametro reikšmę. Duomenys kaupiami nuo 2020 metų. ir iki dabar. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Water extracted (raised) from wells The collection includes the amount of water extracted (raised) from wells and its provision to residents and enterprises in the accounts of water extraction conducted by Simnas komunalininkai, a municipal enterprise of Alytus District Municipality district. The amount of technological water intended for washing plants shall also be recorded. One row corresponds to the value of a specific period and parameter of the well concerned. Data has been collected since 2020. and until now. ENQUIRIES: State Data Control Opening Team: atverimas@stat.gov.lt[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PakeltasVanduo](simno_komun/PakeltasVanduo.md) | Iš gręžinių išgautas (pakeltas) vanduo | `4` | `vda_id` | — | `6` | Rinkinyje pateikiamas Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje vandens gavybos apskaitoje stebimas iš gręžinių išgauto (pakelto)... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/pakeltas_vanduo.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun (https://data.gov.lt/datasets/2774/)

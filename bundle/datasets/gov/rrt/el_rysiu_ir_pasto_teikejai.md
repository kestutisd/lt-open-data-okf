---
type: Dataset
title: "Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika"
description: "Lentelėje pateikiama Lietuvos Respublikos ryšių reguliavimo tarnybai pateiktų pašto paslaugų ir elektroninių ryšių teikėjų ataskaitų statistika."
resource: "https://get.data.gov.lt/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai"
tags: [gov, rrt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2727/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika

- **Namespace:** `datasets/gov/rrt/el_rysiu_ir_pasto_teikejai`[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2727/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai`[^dcat]
- **Portal Title (`@lt`):** Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika[^dcat]
- **Portal Title (`@en`):** Providers of electronic communications and postal services and statistics of periodic reports submitted by them[^dcat]
- **Issued (`dct:issued`):** `2024-07-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-08-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiama Lietuvos Respublikos ryšių reguliavimo tarnybai pateiktų pašto paslaugų ir elektroninių ryšių teikėjų ataskaitų statistika. Duomenys pateikiami nuo 2021 metų. Metai ir ketvirtis nurodo periodą, už kurį pateikta ataskaita, bet ne ataskaitos pateikimo laiką. Stulpelis: pirma_ataskaita_pateikta parodo kada pirmą kartą teikėjas pateikė duomenis duomenų bazėje. Stulpelis: paskutine_ataskaita_pateikta parodo kada paskutinį, kartą teikėjas teikė duomenis duomenų bazėje. Vienam ketvirčiui yra pateikiama viena ataskaita. Jei įmonė tuo pačiu metu teikia ir pašto, ir elektroninių ryšių paslaugas ji gali pateikti dvi skirtingas ataskaitas tam pačiam ketvirčiui. Stulpelyje „jar_kodas“ taip pat pateikiami ir užsienio įmonių kodai. Į duomenų rinkinį įtrauktos ne tik veiklą vykdančios, bet ir veiklą vykdžiusios įmonės (ataskaitų teikėjai). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides statistics on the reports of postal services and electronic communications providers submitted to the Communications Regulatory Authority of the Republic of Lithuania. The data has been provided since 2021. The year and quarter indicate the period for which the report was submitted, but not the reporting time. Column: The first _report _provided shows when the provider first submitted the data in the database. Column: Last reported_reported shows the last time the provider provided data in the database. One report shall be submitted for one quarter. If an enterprise simultaneously provides both postal and electronic communications services, it may submit two different reports for the same quarter. The jar_code column also contains codes for foreign companies. In addition to operating companies, the dataset includes operating companies (reporting providers).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ElRysiaiPastasTeikejas](el_rysiu_ir_pasto_teikejai/ElRysiaiPastasTeikejas.md) | Elektroninių ryšių bei pašto paslaugų teikėjai ir jų pateiktų periodinių ataskaitų statistika | `4` | `vda_prime_key` | — | `10` | "Lentelėje pateikiama Lietuvos Respublikos ryšių reguliavimo tarnybai pateiktų pašto paslaugų ir elektroninių ryšių ataskaitų statistika. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/el_rysiu_ir_pasto_teikejai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/el_rysiu_ir_pasto_teikejai (https://data.gov.lt/datasets/2727/)

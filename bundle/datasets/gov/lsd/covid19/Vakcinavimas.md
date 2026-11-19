---
type: Table
title: "Vakcinavimas — COVID-19 vakcinavimas"
description: "Neagreguoti vakcinacijos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/Vakcinavimas"
tags: [gov, lsd, vakcinavimas, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L136"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L136"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Vakcinavimas — COVID-19 vakcinavimas

Neagreguoti vakcinacijos duomenys[^manifest]

- **Model:** `datasets/gov/lsd/covid19/Vakcinavimas`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L136](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L136)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/Vakcinavimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pseudo_id` | `string` | — | `4` | `open` | — | Unikalus pseudonimizuotas skiepijamo asmens numeris | Sukurtas ne pagal asmens kodą (kurio nedidelė dalis žmonių neturi), bet pagal eSveikatos paciento kodą (jį turi visi skiepijami asmenys) |
| `birth_year_noisy` | `integer` | — | `2` | `open` | — | Skiepijamo asmens gimimo metai | Pagal konfidencialumo taisykles dešimtadaliui asmenų gimimo metai yra atsitiktinai pakeisti pridedant nedidelį asmens privatumą saugantį "triukšmą" (+/- 1 metai) |
| `sex` | `string` | — | `4` | `open` | — | Skiepijamo asmens lytis | — |
| `muni_declared` | `string` | — | `2` | `open` | — | Skiepijamo asmens deklaruotos gyvenamosios vietos savivaldybė | — |
| `muni_policlin` | `string` | — | `2` | `open` | — | Poliklinikos, prie kurios asmuo yra prisiregistravęs, savivaldybė | — |
| `vaccination_date` | `date` | `D` | `4` | `open` | — | Konkrečios vakcinos dozės (skiepo) gavimo data | — |
| `dose_number` | `integer` | — | `4` | `open` | — | Asmens gauto skiepo numeris, neatsižvelgiant į vakcinos pavadinimą | — |
| `drug_manufacturer` | `string` | — | `3` | `open` | — | Gauto skiepo dozės gamintojo pavadinimas | — |
| `drug_name_common` | `string` | — | `3` | `open` | — | Vakcinos pavadinimas | — |
| `vacc_org_name` | `string` | — | `2` | `open` | — | Įstaigos pavadinimas, kurioje asmuo buvo skiepytas (arba kuri organizavo skiepijimą) | — |
| `vacc_org_muni` | `string` | — | `2` | `open` | — | Asmenį skiepijusios (arba skiepijimą organizavusios) įstaigos savivaldybė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sex` | `"M"` | — | — | Moteris | — |
| `sex` | `"V"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L136 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L136)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)

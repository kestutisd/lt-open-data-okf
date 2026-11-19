---
type: Table
title: "Skolininkas — HR archyviniai duomenys apibūdinantys skolininkus"
description: "Spinta table datasets/gov/rc/hr/skolininkai/Skolininkas (21 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/skolininkai/Skolininkas"
tags: [gov, rc, skolininkas, deployed, level-2, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/skolininkai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/skolininkai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2130/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Skolininkas — HR archyviniai duomenys apibūdinantys skolininkus

- **Model:** `datasets/gov/rc/hr/skolininkai/Skolininkas`[^manifest]
- **Dataset:** [Likviduoto hipotekos registro (HR) archyviniai duomenys apie skolininkus](../skolininkai.md) (`datasets/gov/rc/hr/skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/skolininkai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/skolininkai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/skolininkai/Skolininkas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sandorio_id, skolininko_id`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sandorio_id` | `integer` | — | `2` | `open` | — | Sandorio identifikatorius dirbtinis | — |
| `skolininko_id` | `integer` | — | `2` | `open` | — | Skolininko identifikatorius dirbtinis | — |
| `amnt_grupe` | `string` | — | `3` | `open` | — | Skolininko asmens tipo grupė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Skolininko amžiaus grupė | — |
| `reg_data` | `integer` | — | `2` | `open` | — | Skolininko registracijos data (metai) | — |
| `sal_grupe` | `string` | — | `3` | `open` | — | Skolininko šalies grupės pavadinimas | — |
| `sandorio_tipas` | `ref` | [SandorioTipas](../tipu_klasifikatoriai/SandorioTipas.md) (`level=2` scalar) | `2` | `open` | — | Sandorio tipas | — |
| `sand_ireg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio įregistravimo metai - ketvirtis | — |
| `sand_isreg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio išregistravimo metai - ketvirtis | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Įrašo pagrindas | — |
| `sandorio_vieta` | `string` | — | `2` | `open` | — | Sandorio sudarymo vieta (sav. ; aps.) | — |
| `pri_dydis_rez` | `string` | — | `2` | `open` | — | Prievolėsrėžių dydžiai | — |
| `pri_terminas_metai` | `integer` | — | `2` | `open` | — | Prievolės įvykdymo terminas (metai, NULL - nėra duomenų) | — |
| `maksimalus` | `integer` | — | `4` | `open` | — | Ar maksimalioji hipoteka (1 - taip; 0 - ne) | — |
| `paprastas` | `integer` | — | `4` | `open` | — | Ar paprastoji hipoteka (1 - taip; 0 - ne) | — |
| `jungtinis` | `integer` | — | `4` | `open` | — | Ar jungtinė hipoteka (1 - taip; 0 - ne) | — |
| `svetimas` | `integer` | — | `4` | `open` | — | Ar svetimo turto hipoteka (1 - taip; 0 - ne) | — |
| `bendras` | `integer` | — | `4` | `open` | — | Ar bendroji hipoteka (1 - taip; 0 - ne) | — |
| `salyginis` | `integer` | — | `4` | `open` | — | Ar sąlyginė hipoteka (1 - taip; 0 - ne) | — |
| `pareikstinis` | `integer` | — | `4` | `open` | — | Ar pareikštinė (1 - taip; 0 - ne) | — |
| `imones` | `integer` | — | `4` | `open` | — | Ar įmonės hipoteka (1 - taip; 0 - ne) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `maksimalus` | `0` | — | — | Ne | — |
| `maksimalus` | `1` | — | — | Taip | — |
| `paprastas` | `0` | — | — | Ne | — |
| `paprastas` | `1` | — | — | Taip | — |
| `jungtinis` | `0` | — | — | Ne | — |
| `jungtinis` | `1` | — | — | Taip | — |
| `svetimas` | `0` | — | — | Ne | — |
| `svetimas` | `1` | — | — | Taip | — |
| `bendras` | `0` | — | — | Ne | — |
| `bendras` | `1` | — | — | Taip | — |
| `salyginis` | `0` | — | — | Ne | — |
| `salyginis` | `1` | — | — | Taip | — |
| `pareikstinis` | `0` | — | — | Ne | — |
| `pareikstinis` | `1` | — | — | Taip | — |
| `imones` | `0` | — | — | Ne | — |
| `imones` | `1` | — | — | Taip | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_data` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `pri_terminas_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/skolininkai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/skolininkai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/skolininkai (https://data.gov.lt/datasets/2130/)

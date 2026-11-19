---
type: Dataset
title: "Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus"
description: "\"Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai"
tags: [gov, vmvt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/5306/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/okis_patikrinimai"
    author: "team:vda"
    last_modified: "2026-05-06T00:00:00Z"
---

# Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus

"Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose. Viena duomenų rinkinio eilutė atitinka vieną unikalų patikrinimą. Eilutėje nurodomi patikrinimo ir subjekto identifikaciniai numeriai, subjekto teisinė forma, savivaldybė, kurioje atliktas patikrinimas, patikrinimo data, požymiai, nurodantys, ar VMVT informavo apie patikrinimą prieš atvykstant, ar buvo nustatyti pažeidimai, ar po patikrinimo buvo skirta poveikio priemonė. Taip pat nurodomas paskutinio patikrinimo identifikacinis numeris, data ir laikas, kada įrašas buvo sukurtas arba atnaujintas OKIS duomenų bazėje. Duomenys kaupiami nuo 2025-02-01. Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt."[^manifest]

- **Namespace:** `datasets/gov/vmvt/okis_patikrinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/okis_patikrinimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/5306/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė maisto ir veterinarijos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai/Subjektas`[^dcat]
- **Portal Title (`@lt`):** Subjektas[^dcat]
- **Portal Title (`@en`):** Subject[^dcat]
- **Issued (`dct:issued`):** `2026-05-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-05-06`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]

### Portal Description (`@lt`)

Subjektas[^dcat]

### Portal Description (`@en`)

Subject[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](okis_patikrinimai/Subjektas.md) | Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus | `4` | `patikrinimo_id` | — | `11` | "Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/okis_patikrinimai (https://data.gov.lt/datasets/5306/)

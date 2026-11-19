---
type: Dataset
title: "Sveikatos priežiūros specialistų kompetencijų duomenys"
description: "\"Rinkinyje pateikiami Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) sveikatos priežiūros specialistų kompetencijų platformos duomenys apie sveikatos priežiūros specialistų įgytas kompetencijas."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos"
tags: [gov, vaspvt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3887/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sveikatos priežiūros specialistų kompetencijų duomenys

"Rinkinyje pateikiami Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) sveikatos priežiūros specialistų kompetencijų platformos duomenys apie sveikatos priežiūros specialistų įgytas kompetencijas. Duomenys kaupiami nuo 2025 m. sausio mėn. Duomenų rinkinį sudaro 5 lentelės: 1. Sveikatos priežiūros specialistai; 2. Sveikatos priežiūros specialistų licencijos; 3. Sveikatos priežiūros specialistų diplomai; 4. Sveikatos priežiūros specialistų sertifikatai pagal programą; 5. Sveikatos priežiūros specialistų papildomai įgyti sertifikatai. Duomenų teikėjas – Valstybinės akreditavimo sveikatos priežiūros veiklai tarnyba. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/vaspvt/specialistu_kompetencijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3887/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros specialistų kompetencijų duomenys[^dcat]
- **Portal Title (`@en`):** Competence data of healthcare professionals[^dcat]
- **Issued (`dct:issued`):** `2025-08-14`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) sveikatos priežiūros specialistų kompetencijų platformos duomenys apie sveikatos priežiūros specialistų įgytas kompetencijas. Duomenys kaupiami nuo 2025 m. sausio mėn. Duomenų rinkinį sudaro 5 lentelės: 1. Sveikatos priežiūros specialistai; 2. Sveikatos priežiūros specialistų licencijos; 3. Sveikatos priežiūros specialistų diplomai; 4. Sveikatos priežiūros specialistų sertifikatai pagal programą; 5. Sveikatos priežiūros specialistų papildomai įgyti sertifikatai. Duomenų teikėjas – Valstybinės akreditavimo sveikatos priežiūros veiklai tarnyba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data of the State Health Care Accreditation Service (VASPVT) Health Care Specialist Competencies Platform on the competences acquired by Health Care Specialists. Data has been collected since January 2025. The dataset consists of 5 tables: 1. Healthcare professionals; 2. Licences of health professionals; 3. Diplomas in healthcare professionals; 4. Certificates of health professionals under the programme; 5. Certificates obtained by health professionals in addition. Data provider shall mean the State Accreditation Service for Health Care Activities. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SveikatosSpecialistas](specialistu_kompetencijos/SveikatosSpecialistas.md) | Sveikatos priežiūros specialistai | `4` | `specialist_id` | — | `4` | "Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. |
| [Licencija](specialistu_kompetencijos/Licencija.md) | Sveikatos priežiūros specialistų licencijos | `4` | `vda_prime_key` | — | `10` | "Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų... |
| [Diplomas](specialistu_kompetencijos/Diplomas.md) | Sveikatos priežiūros specialistų diplomai | `4` | `diplomo_id` | — | `13` | "Sveikatos priežiūros specialistų diplomų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų... |
| [PrograminisSertifikatas](specialistu_kompetencijos/PrograminisSertifikatas.md) | Sveikatos priežiūros specialistų sertifikatai pagal programą | `4` | `sertifikato_id` | — | `20` | "Sveikatos priežiūros specialistų įgyti sertifikatai pagal programą duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos, sveikatos... |
| [KitasSertifikatas](specialistu_kompetencijos/KitasSertifikatas.md) | Sveikatos priežiūros specialistų papildomai įgyti sertifikatai | `4` | `sertifikato_id` | — | `14` | "Sveikatos priežiūros specialistų papildomai įgytų sertifikatų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos (https://data.gov.lt/datasets/3887/)

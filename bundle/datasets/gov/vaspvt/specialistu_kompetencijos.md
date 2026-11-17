---
type: Dataset
title: "Sveikatos priežiūros specialistų kompetencijų duomenys"
description: "Rinkinyje pateikiami Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) sveikatos priežiūros specialistų kompetencijų platformos duomenys apie sveikatos priežiūros specialistų įgytas kompetencijas."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos"
tags: [gov, vaspvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sveikatos priežiūros specialistų kompetencijų duomenys

Rinkinyje pateikiami Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) sveikatos priežiūros specialistų kompetencijų platformos duomenys apie sveikatos priežiūros specialistų įgytas kompetencijas. Duomenys kaupiami nuo 2025 m. sausio mėn.

Duomenų rinkinį sudaro 5 lentelės:

1. Sveikatos priežiūros specialistai;

2. Sveikatos priežiūros specialistų licencijos;

3. Sveikatos priežiūros specialistų diplomai;

4. Sveikatos priežiūros specialistų sertifikatai pagal programą;

5. Sveikatos priežiūros specialistų papildomai įgyti sertifikatai.

Duomenų teikėjas – Valstybinės akreditavimo sveikatos priežiūros veiklai tarnyba.

- **Namespace:** `datasets/gov/vaspvt/specialistu_kompetencijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SveikatosSpecialistas](specialistu_kompetencijos/SveikatosSpecialistas.md) | Sveikatos priežiūros specialistai | `4` | `specialist_id` | — | 4 | Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. |
| [Licencija](specialistu_kompetencijos/Licencija.md) | Sveikatos priežiūros specialistų licencijos | `4` | `vda_prime_key` | — | 10 | Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų... |
| [Diplomas](specialistu_kompetencijos/Diplomas.md) | Sveikatos priežiūros specialistų diplomai | `4` | `diplomo_id` | — | 13 | Sveikatos priežiūros specialistų diplomų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų... |
| [PrograminisSertifikatas](specialistu_kompetencijos/PrograminisSertifikatas.md) | Sveikatos priežiūros specialistų sertifikatai pagal programą | `4` | `sertifikato_id` | — | 20 | Sveikatos priežiūros specialistų įgyti sertifikatai pagal programą duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos, sveikatos... |
| [KitasSertifikatas](specialistu_kompetencijos/KitasSertifikatas.md) | Sveikatos priežiūros specialistų papildomai įgyti sertifikatai | `4` | `sertifikato_id` | — | 14 | Sveikatos priežiūros specialistų papildomai įgytų sertifikatų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv

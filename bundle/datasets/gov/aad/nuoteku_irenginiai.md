---
type: Dataset
title: "Nuotekų valymo įrenginiai bei jų kokacijos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai"
tags: [gov, aad, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nuotekų valymo įrenginiai bei jų kokacijos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Pateikiamos dvi lentelės kuriuos jungiasi per „aglomeracijos_id“ stulpelį. Vienoje lentelėje pateikiami visi užregistruoti nuotekų įrenginiai, o kitoje preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos. Registruojant nuotekų įrenginį (jei vartotojas nurodė), pateikiama tokia informacija kaip įrenginio tipas, gamintojas, modelis, koordinatės ir t.t. Įrenginių lentelėje viena eilutė atitinka vieną įrenginį, aglomeracijų lentelėje – vieną aglomeraciją. Duomenų aprėptis – visa Lietuva.

Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos

- **Namespace:** `datasets/gov/aad/nuoteku_irenginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai`
- **Parent Namespace (`ns`):** Aplinkos apsaugos departamentas prie Aplinkos ministerijos (`datasets/gov/aad`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irenginys](nuoteku_irenginiai/Irenginys.md) | Nuotekų valymo įrenginiai bei jų lokacijos | `4` | `irenginio_id` | — | 19 | Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. |
| [Aglomeracija](nuoteku_irenginiai/Aglomeracija.md) | Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos | `4` | `vda_prime_key` | — | 8 | Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv

---
type: Dataset
title: "datasets/gov/aaa/nuotekos"
description: "Spinta dataset datasets/gov/aaa/nuotekos (4 tables)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos"
tags: [gov, aaa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/aaa/nuotekos

- **Namespace:** `datasets/gov/aaa/nuotekos`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [UkioSubjektas](nuotekos/UkioSubjektas.md) | Ataskaitą teikiantys subjektai | `2` | — | — | 10 | — |
| [NuotekuValymas](nuotekos/NuotekuValymas.md) | Nuotekų valymo įrenginio nuotekų valymo būdai (įskaitant papildomą valymą), nurodyti metinėje nuotekų ataskaitoje, su nuotekų valymo įrenginio paskirtimi | `2` | — | — | 24 | — |
| [IsleistuvasTarsa](nuotekos/IsleistuvasTarsa.md) | Metinę nuotekų ataskaitą teikiančio subjekto duomenys dėl išleidžiamų nuotekų (įskaitant kiekius pagal išleistuvą) | `2` | — | — | 36 | — |
| [IsleistuvasPriimtuvas](nuotekos/IsleistuvasPriimtuvas.md) | Išleistuvai į gamt. aplinką, į nuotakyną ir kt. įrenginiai pagal aob_uvo.aob_rusis su priimtuvo (įskaitant vandens telkinius) informacija | `2` | — | — | 20 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv

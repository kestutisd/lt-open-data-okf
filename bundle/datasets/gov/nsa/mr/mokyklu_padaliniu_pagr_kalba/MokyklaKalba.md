---
type: Table
title: "MokyklaKalba — Bendrojo ugdymo mokyklų (padalinių) pagrindinės kalbos"
description: "Lentelėje pateikiama Lietuvos bendrojo ugdymo mokyklų (padalinių) informacija (mokyklos grupė, mokyklos tipas, mokinių skaičius, pagrindinė kalba) nuo 2001 kiekvieniems mokslo metams iš Nacionalinės švietimo agentūros Mokinių registro."
resource: "https://get.data.gov.lt/datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba/MokyklaKalba"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokyklaKalba — Bendrojo ugdymo mokyklų (padalinių) pagrindinės kalbos

Lentelėje pateikiama Lietuvos bendrojo ugdymo mokyklų (padalinių) informacija (mokyklos grupė, mokyklos tipas, mokinių skaičius, pagrindinė kalba) nuo 2001 kiekvieniems mokslo metams iš Nacionalinės švietimo agentūros Mokinių registro. Duomenys atnaujinami kartą per mėnesį.

- **Model:** `datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba/MokyklaKalba`[^manifest]
- **Dataset:** [Bendrojo ugdymo mokyklų (padalinių) pagrindinės kalbos](../mokyklu_padaliniu_pagr_kalba.md) (`datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba`)
- **Manifest CSV:** [datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba/MokyklaKalba`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `institucija_id` | `string` | — | `4` | `open` | — | Švietimo institucijos identifikatorius | — |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos juridinio asmens kodas | — |
| `institucijos_pavadinimas` | `string` | — | `4` | `open` | — | Švietimo institucijos pavadinimas | — |
| `padalinys_id` | `string` | — | `4` | `open` | — | Švietimo institucijos padalinio identifikatorius | — |
| `padalinys_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos padalinio kodas | — |
| `jungtinis_kodas` | `string` | — | `4` | `open` | — | Jungtinis institucijos padalinio ir švietimo įstaigos kodas | — |
| `padalinys_pavadinimas` | `string` | — | `4` | `open` | — | Švietimo institucijos padalinio pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra švietimo institucijos padalinys | — |
| `ins_grupe_pav` | `string` | — | `4` | `open` | — | Švietimo institucijos grupės (kategorijos) pavadinimas | — |
| `ins_pagr_tipas` | `string` | — | `4` | `open` | — | Švietimo institucijos pagrindinio tipo pavadinimas | — |
| `suma_mokiniu_skaicius` | `integer` | `U` | `4` | `open` | — | Mokinių, kurie bent dalį laiko per konkrečius mokslo metus mokėsi švietimo įstaigoje (padalinyje), skaičius | — |
| `pagrindine_kalba` | `string` | — | `4` | `open` | — | Pagrindinė švietimo įstaigos (padalinio) mokomoji kalba (nustatoma pagal tai, kuria kalba daugiausia mokinių mokėsi konkrečioje įstaigoje konkrečiais mokslo metais) | — |
| `kalbu_rikiavimas_pagal_proc` | `string` | — | `4` | `open` | — | Kalbos, išrikiuotos pagal tai, kiek mokinių (procentaliai) daugiausia mokėsi konkrečia kalba konkrečioje įstaigoje tam tikrais mokslo metais | — |
| `duomenu_atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/mr/mokyklu_padaliniu_pagr_kalba.csv

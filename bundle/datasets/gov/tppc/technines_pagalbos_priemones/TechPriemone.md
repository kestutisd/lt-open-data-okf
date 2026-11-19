---
type: Table
title: "TechPriemone — Techninės pagalbos priemonių prašymų duomenys"
description: "Lentelėje pateikti techninės pagalbos priemonių prašymų ir jų įgyvendinimo duomenys iš Techninės pagalbos priemonių centro Techninės pagalbos priemonių apskaitos informacinės sistemos (TPPAIS)."
resource: "https://get.data.gov.lt/datasets/gov/tppc/technines_pagalbos_priemones/TechPriemone"
tags: [gov, tppc, techpriemone, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tppc/technines_pagalbos_priemones.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/tppc/technines_pagalbos_priemones.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2814/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tppc/technines_pagalbos_priemones"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TechPriemone — Techninės pagalbos priemonių prašymų duomenys

Lentelėje pateikti techninės pagalbos priemonių prašymų ir jų įgyvendinimo duomenys iš Techninės pagalbos priemonių centro Techninės pagalbos priemonių apskaitos informacinės sistemos (TPPAIS). Lentelę sudaro nuo TTPAIS sistemos veikimo pradžios (2016 m.) sukaupti ir kas mėnesį atnaujinami duomenys. Dėl techninių klausimų ar galimų klaidų kreiptis elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/tppc/technines_pagalbos_priemones/TechPriemone`[^manifest]
- **Dataset:** [Techninės pagalbos priemonių prašymų duomenys](../technines_pagalbos_priemones.md) (`datasets/gov/tppc/technines_pagalbos_priemones`)[^manifest]
- **Manifest CSV:** [datasets/gov/tppc/technines_pagalbos_priemones.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tppc/technines_pagalbos_priemones.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tppc/technines_pagalbos_priemones/TechPriemone` (`deployed`)[^manifest]
- **Provider:** `tppc` — Techninės pagalbos priemonių centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo išduoti techninę (-es) pagalbos priemonę (-es) identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikatorius | — |
| `prasymo_data_nuo` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `prasymo_data_iki` | `date` | `D` | `4` | `open` | — | Prašymo galiojimo pabaigos data | — |
| `organizacijos_id` | `string` | — | `4` | `open` | — | Organizacijos, kuriai buvo pateiktas prašymas, identifikatorius | — |
| `priemones_pavadinimas` | `string` | — | `4` | `open` | — | Prašomos techninės pagalbos priemonės pavadinimas | — |
| `prasoma_kiekis` | `integer` | `U` | `4` | `open` | — | Prašomas techninės pagalbos priemonės skaičius (vnt.) | — |
| `skiriama_kiekis` | `integer` | `U` | `4` | `open` | — | Skiriamas techninės pagalbos priemonės skaičius (vnt.) | — |
| `rezervuota_kiekis` | `integer` | `U` | `4` | `open` | — | Rezervuotas techninės pagalbos priemonės skaičius (vnt.) | — |
| `isduota_kiekis` | `integer` | `U` | `4` | `open` | — | Išduotas techninės pagalbos priemonės skaičius (vnt.) | — |
| `grazinta_kiekis` | `integer` | `U` | `4` | `open` | — | Grąžintas techninės pagalbos priemonės skaičius (vnt.) | — |
| `ived_data` | `date` | `D` | `4` | `open` | — | Duomenų eilutės įvedimo data | — |
| `reda_data` | `date` | `D` | `4` | `open` | — | Duomenų eilutės redagavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tppc/technines_pagalbos_priemones.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tppc/technines_pagalbos_priemones.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tppc/technines_pagalbos_priemones (https://data.gov.lt/datasets/2814/)

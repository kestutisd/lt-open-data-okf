---
type: Table
title: "Aglomeracija — Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Aglomeracija"
tags: [gov, aad, aglomeracija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2855/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Aglomeracija — Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Šioje lentelėje pateikiamos preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos. Lentelėje galima rasti ne tik aglomeracijų ribas, bet ir jos dydi, gyventojų skaičių, gyventojų tankumą. Aglomeracijų lentelėje viena eilutė atitinka vieną preliminarią aglomeraciją. Duomenų aprėptis – visa Lietuva. Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/aad/nuoteku_irenginiai/Aglomeracija`[^manifest]
- **Dataset:** [Nuotekų valymo įrenginiai bei jų kokacijos](../nuoteku_irenginiai.md) (`datasets/gov/aad/nuoteku_irenginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai/Aglomeracija` (`deployed`)[^manifest]
- **Provider:** `aad` — Aplinkos apsaugos departamentas prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `aglomeracijos_id` | `string` | — | `4` | `open` | — | Aglomeracijos Identifikatorius | — |
| `teritorijos_pavadinimas` | `string` | — | `4` | `open` | — | Teritorijos pavadinimas | — |
| `gyventoju_sk` | `integer` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `gyventoju_tankumas` | `integer` | — | `4` | `open` | — | Gyventojų tankumas | — |
| `plotas` | `number` | `km^2` | `4` | `open` | — | Aglomeracijos plotas | — |
| `geometrija` | `geometry(multipolygon, 3346)` | — | `4` | `open` | — | Geometrija (teritorija) | — |
| `informacijos_aktualumas` | `string` | — | `4` | `open` | — | Informacijos aktualumas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai (https://data.gov.lt/datasets/2855/)

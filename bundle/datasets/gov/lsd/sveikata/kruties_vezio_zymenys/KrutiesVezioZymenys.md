---
type: Table
title: "KrutiesVezioZymenys — \"Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m.\""
description: "\"Asmenys, kuriems yra atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m., atliekamas pagal SAM įsakymą (V-713, papildytą punktu: Nr. V-150, 2022-01-25, paskelbta TAR 2022-01-25, i."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys"
tags: [gov, lsd, krutiesveziozymenys, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4135/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/kruties_vezio_zymenys"
    author: "team:vda"
    last_modified: "2026-02-18T00:00:00Z"
---

# KrutiesVezioZymenys — "Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m."

**Dataset Context:** "Asmenys, kuriems yra atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m., atliekamas pagal SAM įsakymą (V-713, papildytą punktu: Nr. V-150, 2022-01-25, paskelbta TAR 2022-01-25, i. k. 2022-01086), analizuojantis krūties vėžio pacientų mėginių genų raišką. Šis tyrimas padeda nustatyti ilgalaikę ligos pasikartojimo tikimybę ir leidžia pritaikyti gydymą taip, kad jis būtu pakankamai stiprus, bet ne perteklinis. Šiuo metu tyrimas yra atliekamas Nacionalinio vėžio instituto Genetinės diagnostikos laboratorijoje tik esant multidisciplininės komisijos sprendimui. Paciento lygmeniu pateikiamas genetiko konsultacijos paslaugos (paslaugos kodai: 1557, 1627, 1749, 3397, 3398, 3399, 4496, 4497, 4682) suteikimo faktas prieš atliktą tyrimą, dalyvavimo KVPP (krūties vėžio prevencinėje programoje) faktas prieš atliktą tyrimą bei gydymo faktas L01 ATC subgrupės vaistais po atlikto tyrimo."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys`[^manifest]
- **Dataset:** ["Asmenys, kuriems atliktas krūties vėžio prognostinių žymenų tyrimas 2022–2025 m."](../kruties_vezio_zymenys.md) (`datasets/gov/lsd/sveikata/kruties_vezio_zymenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/kruties_vezio_zymenys/KrutiesVezioZymenys` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-02-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tyrimo_atlikimo_metai` | `integer` | — | `3` | `open` | — | Krūties vėžio prognostinių žymenų tyrimo atlikimo metai | — |
| `rizika` | `string` | — | `4` | `open` | — | Krūties vėžio atsinaujinimo rizika | — |
| `kruties_vezio_potipis` | `string` | — | `4` | `open` | — | Krūties vėžio potipis | — |
| `genetiko_konsultacija` | `boolean` | — | `4` | `open` | — | "Genetiko konsultacijos paslaugos (kodai: 1557,1627,1749,3397,3398,3399,4496,4497,4682) suteikimo faktas prieš atliktą krūties vėžio prognostinių žymenų tyrimą" | — |
| `dalyvavimas_kvpp` | `boolean` | — | `4` | `open` | — | Dalyvavimo KVPP (krūties vėžio prevencinėje programoje) faktas prieš atliktą krūties vėžio prognostinių žymenų tyrimą | — |
| `gydymas_l01` | `boolean` | — | `4` | `open` | — | Gydymo faktas L01 ATC subgrupės vaistais po atlikto krūties vėžio prognostinių žymenų tyrimo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rizika` | `"Maža"` | — | — | — | — |
| `rizika` | `"Vidutinė"` | — | — | — | — |
| `rizika` | `"Didelė"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Luminalinis A"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Luminalinis B"` | — | — | — | — |
| `kruties_vezio_potipis` | `"HER2 praturtintas"` | — | — | — | — |
| `kruties_vezio_potipis` | `"Bazalinis"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/kruties_vezio_zymenys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/kruties_vezio_zymenys (https://data.gov.lt/datasets/4135/)

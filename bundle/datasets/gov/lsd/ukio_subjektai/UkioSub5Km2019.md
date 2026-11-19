---
type: Table
title: "UkioSub5Km2019 — Ūkio subjektų geoerdviniai duomenys 2019 m. 5x5km gardelėse."
description: "Spinta table datasets/gov/lsd/ukio_subjektai/UkioSub5Km2019 (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/ukio_subjektai/UkioSub5Km2019"
tags: [gov, lsd, ukiosub5km2019, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/ukio_subjektai.csv#L212"
    title: "atviriduomenys/manifest — datasets/gov/lsd/ukio_subjektai.csv#L212"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1914/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/ukio_subjektai"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# UkioSub5Km2019 — Ūkio subjektų geoerdviniai duomenys 2019 m. 5x5km gardelėse.

- **Model:** `datasets/gov/lsd/ukio_subjektai/UkioSub5Km2019`[^manifest]
- **Dataset:** [Veikiančių ūkio subjektų duomenys](../ukio_subjektai.md) (`datasets/gov/lsd/ukio_subjektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/ukio_subjektai.csv#L212](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/ukio_subjektai.csv#L212)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/ukio_subjektai/UkioSub5Km2019` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `integer` | — | `4` | `open` | — | įdentifikacinis numeris | — |
| `a` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: žemės ūkis, miškininkystė ir žuvininkystė | — |
| `g_h_i` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: didmeninė ir mažmeninė prekyba, transportas ir saugojimas, apgyvendinimo ir maitinimo paslaugų veikla | — |
| `f` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: statyba | — |
| `j` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: informacija ir ryšiai | — |
| `pajamos` | `string` | — | `4` | `open` | — | Veikiančių ūkio subjektų pajamos | — |
| `metai` | `integer` | — | `4` | `open` | — | Laikotarpis, kuriam priklauso statistinė reikšmė | — |
| `k` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: finansinė ir draudimo veikla | — |
| `l` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: nekilnojamojo turto operacijos | — |
| `b_c_d_e` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: apdirbamoji gamyba, kasyba ir karjerų eksploatavimas bei kita pramonė | — |
| `imoniu_sk` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius | — |
| `grid_id_` | `string` | — | `4` | `open` | — | Gardelės identifikavimo kodas | — |
| `r_s_t_u` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: kitos paslaugos | — |
| `o_p_q` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: viešasis valdymas ir gynyba, švietimas, žmonių sveikatos priežiūra ir socialinis darbas | — |
| `shape_length` | `number` | — | `4` | `open` | — | gardelės ilgis | — |
| `dsk` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius | — |
| `m_n` | `integer` | — | `4` | `open` | — | Veikiančių ūkio subjektų skaičius, pagal ekonominės veiklos rūšis: profesinė, mokslinė ir techninė veikla, administracinė ir aptarnavimo veikla | — |
| `shape_area` | `number` | — | `4` | `open` | — | gardelės plotas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/ukio_subjektai.csv#L212 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/ukio_subjektai.csv#L212)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/ukio_subjektai (https://data.gov.lt/datasets/1914/)

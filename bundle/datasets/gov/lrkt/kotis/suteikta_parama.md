---
type: Dataset
title: "Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys"
description: "Sutetiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro KOTIS duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lrkt/kotis/suteikta_parama"
tags: [gov, lrkt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lrkt/suteikta_parama.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3803/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrkt/kotis/suteikta_parama"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys

- **Namespace:** `datasets/gov/lrkt/kotis/suteikta_parama`[^manifest]
- **Manifest CSV:** [datasets/gov/lrkt/suteikta_parama.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrkt/kotis/suteikta_parama` (`deployed`)[^manifest]
- **Provider:** `lrkt` — Lietuvos Respublikos Konkurencijos Taryba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3803/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrkt/kotis/suteikta_parama`[^dcat]
- **Portal Title (`@lt`):** Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys[^dcat]
- **Portal Title (`@en`):** Register of State aid granted and de minimis aid granted[^dcat]
- **Issued (`dct:issued`):** `2025-03-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-03-21` .. `2026-05-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Sutetiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro KOTIS duomenys. Viena eilutė atitinka vieną fiziniam ar juridiniam asmeniui suteiktą paramą. Duomenų rinkinį sudaro: paramos identifikatorius, paramos suma, gavimo data ir teisinis pagrindas, paramos tipas, paramos gavėjas, jo kodas ir tipas, požymis ar gavėjas užsienietis ir duomenų atnaujinimo data. Duomenų aprėptis – 10 metų laikotarpis (langas), pvz., 2015–2025 m. Paskutinį kartą atnaujinta: 2025 m. birželio 2 d. rinkinys papildytas stulpeliais „paramos_tipas“ ir „paramos_tipo_pavad“ Duomenų teikėjas – Lietuvos Respublikos Konkurencijos Taryba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on THE notified State aid and the register of insignificant (de minimis) aid. One line corresponds to one support granted to a natural or legal person. The dataset shall comprise: the aid identifier, the amount of support, the date and legal basis of receipt, the beneficiary, its code and type, the character or the foreign beneficiary and the date of updating of the data. Data coverage is a 10-year period (window), e.g. 2015-2025. The data shall be updated annually and submitted over a 10-year period. Data provider shall mean the Competition Council of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Parama](suteikta_parama/Parama.md) | Suteiktos valstybės pagalbos ir nereikšmingos (de minimis) pagalbos registro duomenys | `4` | `paramos_id` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrkt/suteikta_parama.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrkt/suteikta_parama.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrkt/kotis/suteikta_parama (https://data.gov.lt/datasets/3803/)

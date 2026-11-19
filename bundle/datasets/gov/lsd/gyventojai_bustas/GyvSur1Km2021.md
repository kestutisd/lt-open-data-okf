---
type: Table
title: "GyvSur1Km2021 — Gyventojų surašymo duomenys 1x1km 2021 m."
description: "Spinta table datasets/gov/lsd/gyventojai_bustas/GyvSur1Km2021 (45 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvSur1Km2021"
tags: [gov, lsd, gyvsur1km2021, deployed, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L280"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L280"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1911/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# GyvSur1Km2021 — Gyventojų surašymo duomenys 1x1km 2021 m.

- **Model:** `datasets/gov/lsd/gyventojai_bustas/GyvSur1Km2021`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys](../gyventojai_bustas.md) (`datasets/gov/lsd/gyventojai_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gyventojai_bustas.csv#L280](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L280)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvSur1Km2021` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikacinis numeris | — |
| `grid_id` | `string` | — | `4` | `open` | — | unikalus gardelės identifikavimo kodas | — |
| `pop` | `integer` | — | `4` | `open` | — | gyventojų skaičius | — |
| `male` | `integer` | — | `4` | `open` | — | vyrų skaičius | — |
| `female` | `integer` | — | `4` | `open` | — | moterų skaičius | — |
| `all_00_04` | `integer` | — | `4` | `open` | — | gyventojų skaičius 0-4 metų amžiaus grupėje | — |
| `all_05_09` | `integer` | — | `4` | `open` | — | gyventojų skaičius 5-9 metų amžiaus grupėje | — |
| `all_10_14` | `integer` | — | `4` | `open` | — | 10–14 metų amžiaus gyventojų skaičius | — |
| `all_15_19` | `integer` | — | `4` | `open` | — | 15–19 metų amžiaus gyventojų skaičius | — |
| `all_20_24` | `integer` | — | `4` | `open` | — | 20–24 metų amžiaus gyventojų skaičius | — |
| `all_25_29` | `integer` | — | `4` | `open` | — | 24–29 metų amžiaus gyventojų skaičius | — |
| `all_30_34` | `integer` | — | `4` | `open` | — | 30–34 metų amžiaus gyventojų skaičius | — |
| `all_35_39` | `integer` | — | `4` | `open` | — | 35–39 metų amžiaus gyventojų skaičius | — |
| `all_40_44` | `integer` | — | `4` | `open` | — | 40–44 metų amžiaus gyventojų skaičius | — |
| `all_45_49` | `integer` | — | `4` | `open` | — | 45–49 metų amžiaus gyventojų skaičius | — |
| `all_50_54` | `integer` | — | `4` | `open` | — | 50–54 metų amžiaus gyventojų skaičius | — |
| `all_55_59` | `integer` | — | `4` | `open` | — | 55–59 metų amžiaus gyventojų skaičius | — |
| `all_60_64` | `integer` | — | `4` | `open` | — | 60–64 metų amžiaus gyventojų skaičius | — |
| `all_65_69` | `integer` | — | `4` | `open` | — | 65–69 metų amžiaus gyventojų skaičius | — |
| `all_70_74` | `integer` | — | `4` | `open` | — | 70–74 metų amžiaus gyventojų skaičius | — |
| `all_75_79` | `integer` | — | `4` | `open` | — | 75–79 metų amžiaus gyventojų skaičius | — |
| `all_80_84` | `integer` | — | `4` | `open` | — | 80–84 metų amžiaus gyventojų skaičius | — |
| `all_85_plius` | `integer` | — | `4` | `open` | — | 85– ir daugiau metų amžiaus gyventojų skaičius | — |
| `all_00_14` | `integer` | — | `4` | `open` | — | gyventojų skaičius 0-14 metų amžiaus grupėje | — |
| `all_15_64` | `integer` | — | `4` | `open` | — | gyventojų skaičius 15-64 metų amžiaus grupėje | — |
| `all_65_plius` | `integer` | — | `4` | `open` | — | gyventojų skaičius 65metų ir vyresnių amžiaus grupėje | — |
| `males_00_14` | `integer` | — | `4` | `open` | — | vyrų skaičius 0-14 metų amžiaus grupėje | — |
| `males_15_64` | `integer` | — | `4` | `open` | — | vyrų skaičius 15-64 metų amžiaus grupėje | — |
| `males_65_plius` | `integer` | — | `4` | `open` | — | vyrų skaičius 65metų ir vyresnių amžiaus grupėje | — |
| `females_00_14` | `integer` | — | `4` | `open` | — | moterų skaičius 0-14 metų amžiaus grupėje | — |
| `females_15_64` | `integer` | — | `4` | `open` | — | moterų skaičius 15-64 metų amžiaus grupėje | — |
| `females_65_plius` | `integer` | — | `4` | `open` | — | moterų skaičius 65metų ir vyresnių amžiaus grupėje | — |
| `adults` | `integer` | — | `4` | `open` | — | 18 metų ir vyresnių gyventojų skaičius | — |
| `adults_males` | `integer` | — | `4` | `open` | — | 18 metų ir vyresnių vyrų skaičius | — |
| `adults_females` | `integer` | — | `4` | `open` | — | 18 metų ir vyresnių moterų skaičius | — |
| `mean_age` | `number` | — | `4` | `open` | — | vidutinis gyventojų skaičius gardelėje | — |
| `mean_age_firstbirth` | `number` | — | `4` | `open` | — | moterų turinčių vaikų vidutinis amžius pirmo vaiko gimimo metu | — |
| `youngest_firstbirth_mother` | `integer` | — | `4` | `open` | — | moterų turinčių vaikų minimalus amžius pirmo vaiko gimimo metu | — |
| `oldest_firstbirth_mother` | `integer` | — | `4` | `open` | — | moterų turinčių vaikų maksimalus amžius pirmo vaiko gimimo metu | — |
| `mean_children` | `number` | — | `4` | `open` | — | vidutinis pagimdytų vaikų skaičius, tenkantys vienai mamai | — |
| `havt_children_15plius_percent` | `number` | — | `4` | `open` | — | procentas moterų (15 metų ir vyresnių) neturinčių vaikų nuo visų atitinkamo amžiaus moterų gardelėje. | — |
| `nac_lt` | `integer` | — | `4` | `open` | — | lietuvių tautybės gyventojai | — |
| `nac_oth` | `integer` | — | `4` | `open` | — | kitos tautybės gyventojai | — |
| `shape_area` | `number` | — | `4` | `open` | — | gardelės plotas | — |
| `shape_length` | `number` | — | `4` | `open` | — | gardelės ilgis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L280 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L280)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas (https://data.gov.lt/datasets/1911/)

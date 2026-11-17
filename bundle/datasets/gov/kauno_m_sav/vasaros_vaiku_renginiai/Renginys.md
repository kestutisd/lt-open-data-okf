---
type: Table
title: "Renginys — Renginių sąrašas"
description: "Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Renginys"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# Renginys — Renginių sąrašas

Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių sąrašas.

- **Model:** `datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Renginys`[^manifest]
- **Dataset:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai](../vasaros_vaiku_renginiai.md) (`datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai/Renginys`
- **Primary Key (`ref`):** `renginio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `renginio_id` | `string` | — | `4` | `open` | — | Renginio identifikatorius | — |
| `renginio_pav` | `string` | — | `4` | `open` | — | Užsiėmimo pavadinimas | — |
| `renginio_aprasymas_lt` | `string` | — | `2` | `open` | — | Užsiėmimo aprašymas | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | X koordinate LKS koordinačių sistemoje | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Y koordinate LKS koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinate WGS koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinate WGS koordinačių sistemoje | — |
| `pastaba_lt` | `string` | — | `2` | `open` | — | Pastabos | — |
| `nuo` | `datetime` | `T` | `4` | `open` | — | Data nuo | — |
| `iki` | `datetime` | `T` | `4` | `open` | — | Data iki | — |
| `amzius` | `string` | — | `4` | `open` | — | Amžius | — |
| `imones_pav` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės JAR kodas | — |
| `kont_elpastas` | `string` | — | `4` | `open` | — | Kontaktinis elektroninis paštas | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas, pritaikyta neįgaliesiems arba ne | — |
| `kryptis` | `string` | — | `4` | `open` | — | Užsiėmimo kryptis: švietimas, sportas, kultūra, turizmas menas | — |
| `mokama` | `boolean` | — | `4` | `open` | — | Mokama ar ne paslauga | — |
| `kaina_asmeniui` | `number` | — | `4` | `open` | — | Kaina asmeniui | — |
| `pritaikyta_neig` | `boolean` | — | `4` | `open` | — | Pritaikyta neįgaliesiems | — |
| `vietu_sk` | `integer` | — | `4` | `open` | — | Vietų skaičius | — |
| `vietu_sk_spec` | `integer` | — | `4` | `open` | — | Vietų skaičius specialiuosius poreikius turinčiam vaikui | — |
| `neig_vietu_sk` | `integer` | — | `4` | `open` | — | Neįgaliųjų vietų skaičius | — |
| `neig_past_lt` | `string` | — | `4` | `open` | — | Pastabos apie neįgalųjį | — |
| `stov_tipas` | `string` | — | `4` | `open` | — | Stovyklos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `renginio_aprasymas_lt` | `update(property: "renginio_aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pastaba_lt` | `update(property: "pastaba_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `amzius` | `update(property: ""amzius[]"", type: ""array"", source: ""amzius"")` | `property` | `4` | — | — | — | — |
| `neig_past_lt` | `update(property: "neig_past_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv

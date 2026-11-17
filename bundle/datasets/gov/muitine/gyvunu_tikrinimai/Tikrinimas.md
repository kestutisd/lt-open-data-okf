---
type: Table
title: "Tikrinimas — Gyvūnų tikrinimas muitinėje"
description: "Nekomerciniais tikslais vežamų gyvūnų augintinių (šunų, kačių, šeškų) tikrinimų muitinėje registras"
resource: "https://get.data.gov.lt/datasets/gov/muitine/gyvunu_tikrinimai/Tikrinimas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/gyvunu_tikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/gyvunu_tikrinimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tikrinimas — Gyvūnų tikrinimas muitinėje

Nekomerciniais tikslais vežamų gyvūnų augintinių (šunų, kačių, šeškų) tikrinimų muitinėje registras

- **Model:** `datasets/gov/muitine/gyvunu_tikrinimai/Tikrinimas`[^manifest]
- **Dataset:** [Gyvūnų tikrinimas muitinėje](../gyvunu_tikrinimai.md) (`datasets/gov/muitine/gyvunu_tikrinimai`)
- **Manifest CSV:** [datasets/gov/muitine/gyvunu_tikrinimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/gyvunu_tikrinimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/gyvunu_tikrinimai/Tikrinimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės įrašo identifikatorius | — |
| `registro_iraso_id` | `string` | — | `4` | `open` | — | Registro įrašo identifikatorius | — |
| `isvykimo_salis` | `string` | — | `4` | `open` | — | Gyvūno išvykimo šalis | — |
| `paskirties_salis` | `string` | — | `4` | `open` | — | Gyvūno paskirties šalis | — |
| `ivezimo_data` | `datetime` | — | `4` | `open` | — | Gyvūno įvežimo data | — |
| `iveze_savininkas` | `boolean` | — | `4` | `open` | — | Požymis ar įvežė savininkas | — |
| `muitines_posto_kodas` | `string` | — | `4` | `open` | — | Muitinės postas, per kurį vežamas gyvunas | — |
| `teritorines_muitines_kodas` | `string` | — | `4` | `open` | — | Teritorinės muitinės kodas | — |
| `gyvuno_rusis` | `string` | — | `4` | `open` | — | Įvežamo gyvūno rūšis | — |
| `zymes_numeris` | `string` | — | `4` | `open` | — | Gyvūno žymės numeris | — |
| `zymes_tipas` | `string` | — | `4` | `open` | — | Gyvūno žymės tipas | — |
| `gyvuno_dokumentas` | `string` | — | `4` | `open` | — | Gyvūno dokumentas | — |
| `gyvuno_dokumento_numeris` | `string` | — | `4` | `open` | — | Gyvūno dokumento numeris | — |
| `muitines_sprendimas` | `string` | — | `4` | `open` | — | Muitinės sprendimas, jei gyvūnas neatitinka pervežimo kriterijų | — |
| `ar_dalyvauja_renginyje` | `boolean` | — | `4` | `open` | — | Požymis, ar gyvūnas dalyvauja renginyje | — |
| `renginio_miestas` | `string` | — | `4` | `open` | — | Gyvūnų renginio miestas | — |
| `renginio_salis` | `string` | — | `4` | `open` | — | Gyvūnų renginio šalis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teritorines_muitines_kodas` | `"VM00"` | — | — | — | — |
| `teritorines_muitines_kodas` | `"KM00"` | — | — | — | — |
| `teritorines_muitines_kodas` | `"LM00"` | — | — | — | — |
| `zymes_tipas` | `"Mikroschema"` | — | — | — | — |
| `zymes_tipas` | `"Tatuiruote"` | — | — | — | — |
| `gyvuno_dokumentas` | `"Gyvūno augintinio pasas"` | — | — | — | — |
| `gyvuno_dokumentas` | `"Veterinarijos sertifikatas"` | — | — | — | — |
| `muitines_sprendimas` | `"Grąžinti į trečią šalį"` | — | — | — | — |
| `muitines_sprendimas` | `"Karantinuoti"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/gyvunu_tikrinimai.csv

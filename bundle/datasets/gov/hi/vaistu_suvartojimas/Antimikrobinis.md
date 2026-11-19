---
type: Table
title: "Antimikrobinis — Antimikrobinių vaistinių preparatų suvartojimas"
description: "Spinta table datasets/gov/hi/vaistu_suvartojimas/Antimikrobinis (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/vaistu_suvartojimas/Antimikrobinis"
tags: [gov, hi, antimikrobinis, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/422/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/vaistu_suvartojimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Antimikrobinis — Antimikrobinių vaistinių preparatų suvartojimas

- **Model:** `datasets/gov/hi/vaistu_suvartojimas/Antimikrobinis`[^manifest]
- **Dataset:** [Antimikrobinių vaistinių preparatų suvartojimo Lietuvoje duomenys](../vaistu_suvartojimas.md) (`datasets/gov/hi/vaistu_suvartojimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/vaistu_suvartojimas/Antimikrobinis` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | `yr` | `2` | `open` | — | Antimikrobinių vaistinių preparatų suvartojimo statistikos vedimo metai | — |
| `istaiga` | `ref` | [Istaiga](../../vaspvt/licencijos/Istaiga.md) (`level=4 UUID` via `Istaiga[ja_kodas]`: `istaiga._id`) | `4` | `open` | — | Sveikatos priežiūros įstaigos JAR kodas | — |
| `ligonine` | `string` | — | `2` | `open` | — | Ligoninės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Ligoninės tipas | — |
| `atc` | `string` | — | `4` | `open` | — | Tarptautinę anatominio terapinio cheminio indekso klasifikacijos kodas | — |
| `veiklioji` | `string` | — | `4` | `open` | — | Vaistinės veikliosios medžiagos pavadinimas | — |
| `komercinis` | `string` | — | `4` | `open` | — | Vaistinio preparato komercinis pavadinimas | — |
| `pakid` | `string` | — | `4` | `open` | — | Antimikrobinio vaistinio preparato pakuotės identifikavimo kodas | Reikšmę turi tik tiek preparatai, kurie yra registruoti Europos vaistų agentūros |
| `stiprumas` | `string` | — | `2` | `open` | — | Antimikrobinio vaistinio preparato pakuotės stiprumo reikšmė(-s) | — |
| `vnt` | `string` | — | `4` | `open` | — | Antimikrobinio vaistinio preparato stiprumo vienetai | — |
| `gramas` | `number` | `g` | `4` | `open` | — | Antimikrobinio vaistinio preparato pakuotės stiprumo reikšmė(-s) gramais | — |
| `pso_vtd` | `number` | `g` | `4` | `open` | — | Vaisto vidutinė terapinė paros dozė | — |
| `suvartota` | `integer` | `U` | `4` | `open` | — | Suvartotų pakuočių skaičius | — |
| `pcs` | `string` | — | `2` | `open` | — | Antimikrobinio vaistinio preparato technininis vienetas ir/arba vienetų skaičius | — |
| `tech_vnt` | `integer` | `U` | `4` | `open` | — | Suvartota techninių vienetų iš pakelio | — |
| `forma` | `string` | — | `4` | `open` | — | Antimikrobinio vaistinio preparato farmacinė forma | — |
| `vtd_1000_pacientu` | `number` | `g` | `4` | `open` | — | Nustatytas vaisto vartojimo techninis vienetas, išreiškiamas gramais (ar miligramais) per parą ir skaičiuojamas 1000-čiui pacientų. | VTD – tai nustatytas vaisto vartojimo techninis vienetas, išreiškiamas gramais (ar miligramais) per parą ir kaip rodiklis skaičiuojamas 1000-čiui pacientų. |
| `vtd_1000_lovadieniu` | `number` | `g` | `4` | `open` | — | Nustatytas vaisto vartojimo techninis vienetas, išreiškiamas gramais (ar miligramais) per parą ir skaičiuojamas 1000-čiui lovadienių. | VTD – tai nustatytas vaisto vartojimo techninis vienetas, išreiškiamas gramais (ar miligramais) per parą ir kaip rodiklis skaičiuojamas 1000-čiui lovadienių. |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `'Bendrojo pobūdžio ligoninė'` | — | — | Bendrojo pobūdžio ligoninė | — |
| `tipas` | `'Palaikomojo gydymo ir slaugos ligoninė'` | — | — | Palaikomojo gydymo ir slaugos ligoninė | — |
| `tipas` | `'Specializuota ligoninė'` | — | — | Specializuota ligoninė | — |
| `tipas` | `'Nenustatyta'` | — | — | Nenustatyta | — |
| `vnt` | `'g'` | — | — | Gramai | — |
| `vnt` | `'iu'` | — | — | Tarptautiniai vienetai | — |
| `vnt` | `'mg'` | — | — | Miligramai | — |
| `vnt` | `'mu'` | — | — | Tarptautinio vieneto milijoninės dalys | — |
| `vnt` | `'ud'` | — | — | Antimikrobinio vaistinio preparato techninio vieneto dozė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/vaistu_suvartojimas/antimikrobinis.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/vaistu_suvartojimas (https://data.gov.lt/datasets/422/)

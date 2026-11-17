---
type: Table
title: "NuotekuValymas — Nuotekų valymo įrenginio nuotekų valymo būdai (įskaitant papildomą valymą), nurodyti metinėje nuotekų ataskaitoje, su nuotekų valymo įrenginio paskirtimi"
description: "Spinta table datasets/gov/aaa/nuotekos/NuotekuValymas (24 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos/NuotekuValymas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# NuotekuValymas — Nuotekų valymo įrenginio nuotekų valymo būdai (įskaitant papildomą valymą), nurodyti metinėje nuotekų ataskaitoje, su nuotekų valymo įrenginio paskirtimi

- **Model:** `datasets/gov/aaa/nuotekos/NuotekuValymas`[^manifest]
- **Dataset:** [datasets/gov/aaa/nuotekos](../nuotekos.md) (`datasets/gov/aaa/nuotekos`)
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos/NuotekuValymas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_id` | `string` | — | `4` | `open` | — | Ataskaitinio objekto id | — |
| `usb_aob_id` | `string` | — | `2` | `open` | — | Ūkio subjekto id | Siejasi su lentele UkioSubjektas, stulpeliu usb_aob_id |
| `aob_aob_id_prikl` | `string` | — | `2` | `open` | — | Priklausomumo objektui id | Siejasi su lentele UkioSubjektas, stulpeliu aob_aob_id_prikl |
| `aob_pavad` | `string` | — | `3` | `open` | — | Ataskaitinio objekto pavadinimas | — |
| `aob_kodas` | `string` | — | `3` | `open` | — | Ataskaitinio objekto kodas | — |
| `nvb_kodas` | `string` | — | `4` | `open` | — | Nuotekų valymo būdo kodas | — |
| `nvb_pavad` | `string` | — | `3` | `open` | — | Nuotekų valymo būdo pavadinimas | — |
| `nde_iraso_nr` | `integer` | — | `4` | `open` | — | Įrašo eilutės numeris | — |
| `nde_kit_dezinf_budas` | `string` | — | `3` | `open` | — | Įrenginio nuotekų papildomo valymo aprašas, kai nurodomas būdas "Kitas" | — |
| `ndb_pavad` | `string` | — | `3` | `open` | — | Nuotekų papildomo valymo būdo pavadinimas | — |
| `nvp_pavad` | `string` | — | `3` | `open` | — | Nuotekų valymo įrenginio paskirties pavadinimas | — |
| `uod_tipas` | `string` | — | `4` | `open` | — | ŪS veiklos objekto tipas | — |
| `uod_irn_paros_hidr_pajeg` | `integer` | — | `3` | `open` | — | Nuotekų valymo įrenginio projektinis hidraulinis pajėgumas, m3 / parą | — |
| `uod_irn_met_hidr_pajeg` | `integer` | — | `3` | `open` | — | Nuotekų valymo įrenginio projektinis hidraulinis pajėgumas, m3 / metus | — |
| `uod_irn_paros_bds7_pajeg` | `integer` | — | `3` | `open` | — | Nuotekų valymo įrenginio projektinis BDS7 pajėgumas, kg / parą | — |
| `uod_irn_met_bds7_pajeg` | `integer` | — | `3` | `open` | — | Nuotekų valymo įrenginio projektinis BDS7 pajėgumas, kg / metus | — |
| `uod_irn_ge_pajeg` | `integer` | — | `3` | `open` | — | Nuotekų valymo įrenginio projektinis pajėgumas gyventojų ekvivalentais | — |
| `uod_irn_veik_pradz_metai` | `integer` | — | `2` | `open` | — | Metai, kuriais nuotekų valymo įrenginiai pradėjo veikti | — |
| `uod_irn_plan_uzd_metai` | `integer` | — | `2` | `open` | — | Metai, kuriais nuotekų valymo įrenginius planuojama rekonstruoti ar uždaryti | — |
| `uod_irn_rekonstr_metai` | `integer` | — | `2` | `open` | — | Metai, kuriais nuotekų valymo įrenginiai buvo paskutinį kartą rekonstruoti | — |
| `uod_irn_uzdar_metai` | `integer` | — | `2` | `open` | — | Metai, kuriais nuotekų valymo įrenginiai buvo uždaryti | — |
| `dkd_nss_tipas` | `string` | — | `4` | `open` | — | Nuotekų surinkimo sistemos tipas | — |
| `dkd_tinklu_ilgis` | `number` | — | `3` | `open` | — | Nuotekų surinkimo sistemos tinklų ilgis | — |
| `dok_atsisk_data_nuo` | `integer` | — | `2` | `open` | — | Data, už kurią yra teikiamas dokumentas. | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nvb_kodas` | `"MECHN"` | — | — | Mechaninis | — |
| `nvb_kodas` | `"CHEM"` | — | — | Cheminis | — |
| `nvb_kodas` | `"BIOL"` | — | — | Biologinis | — |
| `uod_tipas` | `"MAU"` | — | — | Maudykla | — |
| `uod_tipas` | `"OTI"` | — | — | Oro / vandens taršos įrenginys | — |
| `uod_tipas` | `"IKS"` | — | — | Iš kitų gaunamo vandens šaltinis | — |
| `uod_tipas` | `"PVS"` | — | — | Paviršinio vandens šaltinis | — |
| `uod_tipas` | `"UVO"` | — | — | Ūkinės veiklos objektas | — |
| `uod_tipas` | `"PZS"` | — | — | Požeminio vandens šaltinis | — |
| `uod_tipas` | `"OTS"` | — | — | Oro taršos šaltinis | — |
| `uod_tipas` | `"NIS"` | — | — | Nuotekų išleistuvas | — |
| `uod_tipas` | `"NVI"` | — | — | Nuotekų valymo įrenginys | — |
| `uod_tipas` | `"KI"` | — | — | Kitas įrenginys | — |
| `dkd_nss_tipas` | `"A"` | — | — | atskiroji | — |
| `dkd_nss_tipas` | `"M"` | — | — | mišrioji | — |
| `dkd_nss_tipas` | `"B"` | — | — | abiejų tipų | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `uod_irn_veik_pradz_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `uod_irn_plan_uzd_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `uod_irn_rekonstr_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `uod_irn_uzdar_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `dok_atsisk_data_nuo` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv

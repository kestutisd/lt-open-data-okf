---
type: Table
title: "NeigaliujuStatistika — COVID-19 statistika apie asmenis su negalia"
description: "Pateikiami užsikrėtimų koronavirusu, skiepijimo, bendros imunizacijos, mirčių nuo COVID-19 rodikliai apibūdinantys pandemijos situaciją trijose asmenų grupėse: asmenys su negalia, su dideliu nedarbingumu, ar su specialiais poreikiais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/NeigaliujuStatistika"
tags: [gov, lsd, neigaliujustatistika, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L151"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L151"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NeigaliujuStatistika — COVID-19 statistika apie asmenis su negalia

Pateikiami užsikrėtimų koronavirusu, skiepijimo, bendros imunizacijos, mirčių nuo COVID-19 rodikliai apibūdinantys pandemijos situaciją trijose asmenų grupėse: asmenys su negalia, su dideliu nedarbingumu, ar su specialiais poreikiais.[^manifest]

- **Model:** `datasets/gov/lsd/covid19/NeigaliujuStatistika`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L151](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L151)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/NeigaliujuStatistika` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus id | — |
| `date` | `date` | `D` | `4` | `open` | — | Atskaitos data | — |
| `level_type` | `string` | — | `2` | `open` | — | NDNT priskiriamas tipas | — |
| `level` | `string` | — | `2` | `open` | — | Lygis | — |
| `n_all` | `integer` | `U` | `4` | `open` | — | Visi neįgalieji, darbingieji ir spec. poreikių žmonės įtraukti ndnt tarnybos | — |
| `n_lt` | `integer` | `U` | `4` | `open` | — | Visi neįgalieji, darbingieji ir spec. poreikių žmonės įtraukti ndnt tarnybos ir turintys lietuvišką asmens kodą COVID laikotarpiu | — |
| `n_inc_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi užsikrėtę | — |
| `n_inc_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi užsikrėtę prieš 14 dienų | — |
| `p_inc_cum_t00` | `number` | `%` | `4` | `open` | — | Užsikrėtusiųjų dalis | — |
| `p_inc_cum_t14` | `number` | `%` | `4` | `open` | — | Užsikrėtusiųjų dalis prieš 14 dienų | — |
| `pp_inc_cum_tt` | `number` | `%` | `4` | `open` | — | Užsikrėtųsiųjų procentinis pokytis | — |
| `dd_inc_cum_1p` | `integer` | `d` | `4` | `open` | — | Dienų skaičius, per kurį užsikrėtusiųjų skaičius pakito 1% | — |
| `n_vac_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi vakcinuoti | — |
| `n_vac_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi vakcinuoti prieš 14 dienų | — |
| `p_vac_cum_t00` | `number` | `%` | `4` | `open` | — | Visų vakcinuotų dalis | — |
| `p_vac_cum_t14` | `number` | `%` | `4` | `open` | — | Visų vakcinuotų dalis prieš 14 dienų | — |
| `pp_vac_cum_tt` | `number` | `%` | `4` | `open` | — | Vakcinuotų procentinis pokytis | — |
| `dd_vac_cum_1p` | `integer` | `d` | `4` | `open` | — | Dienų skaičius per kurį vakcinuotų skaičius pakito 1% | — |
| `n_imm_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi imunizuoti | — |
| `n_imm_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi imunizuoti prieš 14 dienų | — |
| `p_imm_cum_t00` | `number` | `%` | `4` | `open` | — | Visų imunizuotų dalis | — |
| `p_imm_cum_t14` | `number` | `%` | `4` | `open` | — | Visų imunizuotų dalis prieš 14 dienų | — |
| `pp_imm_cum_tt` | `number` | `%` | `4` | `open` | — | Imunizuotų procentinis pokytis | — |
| `dd_imm_cum_1p` | `integer` | `d` | `4` | `open` | — | Dienų skaičius per kurį imunizuotų skaičius pakito 1% | — |
| `n_de1_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 1 apibrėžimą | — |
| `n_de1_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 1 apibrėžimą prieš 14 dienų | — |
| `p_de1_cum_t00` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 1 apibrėžimą | — |
| `p_de1_cum_t14` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 1 apibrėžimą prieš 14 dienų | — |
| `n_de2_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 2 apibrėžimą | — |
| `n_de2_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 2 apibrėžimą prieš 14 dienų | — |
| `p_de2_cum_t00` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 2 apibrėžimą | — |
| `p_de2_cum_t14` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 2 apibrėžimą prieš 14 dienų | — |
| `n_de3_cum_t00` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 3 apibrėžimą | — |
| `n_de3_cum_t14` | `integer` | `U` | `4` | `open` | — | Visi mirę pagal 3 apibrėžimą prieš 14 dienų | — |
| `p_de3_cum_t00` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 3 apibrėžimą | — |
| `p_de3_cum_t14` | `number` | `%` | `4` | `open` | — | Visų mirusiųjų dalis pagal 3 apibrėžimą prieš 14 dienų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L151 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L151)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)

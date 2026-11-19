---
type: Table
title: "SvieslenciuStatistika — COVID-19 statistika (švieslentės)"
description: "Pateikta iš švieslenčių (dashboards) agreguota informacija kiekvienai dienai pagal savivaldybes nuo pandemijos pradžios Lietuvoje apie atvejus, tyrimus ir mirtis"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/SvieslenciuStatistika"
tags: [gov, lsd, svieslenciustatistika, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L89"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L89"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SvieslenciuStatistika — COVID-19 statistika (švieslentės)

Pateikta iš švieslenčių (dashboards) agreguota informacija kiekvienai dienai pagal savivaldybes nuo pandemijos pradžios Lietuvoje apie atvejus, tyrimus ir mirtis[^manifest]

- **Model:** `datasets/gov/lsd/covid19/SvieslenciuStatistika`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L89](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L89)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/SvieslenciuStatistika` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `date` | `date` | `D` | `4` | `open` | — | Ataskaitinė para kurios metu įvyko įvykiai arba kurios pabaigoje buvo vykdoma apskaita | — |
| `municipality_code` | `string` | — | `2` | `open` | — | Savivaldybės priskirtos asmenims pagal hierarchinį modelį kodas | — |
| `municipality_name` | `string` | — | `2` | `open` | — | Savivaldybės priskirtos asmenims pagal hierarchinį modelį pavadinimas | — |
| `population` | `integer` | `U` | `4` | `open` | — | Populiacijos dydis 2021 metų pradžios duomenimis pagal deklaruotą gyvenamąją vietą | — |
| `ab_pos_day` | `integer` | `U` | `4` | `open` | — | Antikūnų testo teigiamų atsakymų skaičius paros | — |
| `ab_neg_day` | `integer` | `U` | `4` | `open` | — | Antikūnų testo neigiamų atsakymų skaičius paros | — |
| `ab_tot_day` | `integer` | `U` | `4` | `open` | — | Antikūnų testų skaičius paros | — |
| `ab_prc_day` | `number` | `U` | `4` | `open` | — | Antikūnų testų teigiamų atsakymų dalis per parą | — |
| `ag_pos_day` | `integer` | `U` | `4` | `open` | — | Antigeno testo teigiamų atsakymų skaičius paros | — |
| `ag_neg_day` | `integer` | `U` | `4` | `open` | — | Antigeno testo neigiamų atsakymų skaičius paros | — |
| `ag_tot_day` | `integer` | `U` | `4` | `open` | — | Antigeno testų skaičius paros | — |
| `ag_prc_day` | `number` | `%` | `4` | `open` | — | Antigeno testų teigiamų atsakymų dalis per parą | — |
| `pcr_neg_day` | `integer` | `U` | `4` | `open` | — | PGR tyrimo neigiamų atsakymų skaičius paros | — |
| `pcr_pos_day` | `integer` | `U` | `4` | `open` | — | PGR tyrimo teigiamų atsakymų skaičius paros | — |
| `pcr_prc_day` | `number` | `%` | `4` | `open` | — | PGR tyrimo teigiamų atsakymų dalis per parą | — |
| `pcr_tot_day` | `integer` | `U` | `4` | `open` | — | PGR tyrimų skaičius paros | — |
| `dgn_neg_day` | `integer` | `U` | `4` | `open` | — | Diagnostinių tyrimų/testų neigiamų atsakymų skaičius paros | — |
| `dgn_pos_day` | `integer` | `U` | `4` | `open` | — | Diagnostinių tyrimų/testų teigiamų atsakymų skaičius paros | — |
| `dgn_tot_day` | `integer` | `U` | `4` | `open` | — | Diagnostinių tyrimų/testų skaičius paros | — |
| `dgn_prc_day` | `number` | `%` | `4` | `open` | — | Diagnostinių tyrimų/testų teigiamų atsakymų dalis per parą | — |
| `dgn_tot_day_gmp` | `integer` | `U` | `4` | `open` | — | Mobiliuose punktuose surinktų mėginių diagnostinių tyrimų/testų skaičius paros | — |
| `daily_deaths_def1` | `integer` | `U` | `4` | `open` | — | Paros naujų mirčių skaičius pagal (siauriausią) COVID-19 mirties apibrėžimą Nr 1. | — |
| `daily_deaths_def2` | `integer` | `U` | `4` | `open` | — | Paros naujų mirčių skaičius pagal COVID-19 mirties apibrėžimą Nr 2. | — |
| `daily_deaths_def3` | `integer` | `U` | `4` | `open` | — | Paros naujų mirčių skaičius pagal COVID-19 mirties apibrėžimą Nr 3. | — |
| `daily_deaths_all` | `integer` | `U` | `4` | `open` | — | Paros mirčių skaičius Lietuvoje (pagal mirties fakto datą) | — |
| `incidence` | `integer` | `U` | `4` | `open` | — | Paros bendras COVID-19 užsikrėtimų skaičius (laboratoriškai arba gydytojo patvirtinti atvejai) | — |
| `infection1` | `integer` | `U` | `4` | `open` | — | Paros COVID-19 pirminių užsikrėtimų skaičius (laboratoriškai arba gydytojo patvirtinti atvejai) | — |
| `infection2` | `integer` | `U` | `4` | `open` | — | Paros COVID-19 antrinių užsikrėtimų skaičius (laboratoriškai arba gydytojo patvirtinti atvejai) | — |
| `infection3` | `integer` | `U` | `4` | `open` | — | Paros COVID-19 tretinių užsikrėtimų skaičius (laboratoriškai arba gydytojo patvirtinti atvejai) | — |
| `active_sttstcl` | `integer` | `U` | `4` | `open` | — | Statistinis COVID-19 liga sergančių asmenų skaičius | — |
| `map_colors` | `string` | — | `3` | `open` | — | Savivaldybės spalvinė zona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L89 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L89)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)

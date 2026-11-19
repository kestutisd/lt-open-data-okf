---
type: Table
title: "NuolatinisGyventojas — Nuolatinių Lietuvos Respublikos gyventojų mirties atvejai ir jų priežastys"
description: "Spinta table datasets/gov/hi/mirtys/NuolatinisGyventojas (26 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/mirtys/NuolatinisGyventojas"
tags: [gov, hi, nuolatinisgyventojas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/998/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/mirtys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NuolatinisGyventojas — Nuolatinių Lietuvos Respublikos gyventojų mirties atvejai ir jų priežastys

- **Model:** `datasets/gov/hi/mirtys/NuolatinisGyventojas`[^manifest]
- **Dataset:** [Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, mirties atvejų ir jų priežasčių...](../mirtys.md) (`datasets/gov/hi/mirtys`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/mirties_priezastys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/mirtys/NuolatinisGyventojas` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `m_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m_id` | `string` | — | `4` | `open` | `pii:id` | Asmens sugalvotas identifikatorius | — |
| `m_lytis` | `integer` | — | `4` | `open` | `pii:sex` | Lytis | — |
| `sav_kodas_regist` | `integer` | — | `4` | `open` | `person:residency` | Savivaldybės kodas, kur registruotas miręs asmuo | — |
| `m_am_mt` | `integer` | `yr` | `1` | `open` | `pii:age` | Mirusiojo amžius metais | — |
| `m_am_mn` | `integer` | `mo` | `1` | `open` | `pii:age` | Mirusiojo amžius mėnesiais | — |
| `m_am_dn` | `integer` | `d` | `1` | `open` | `pii:age` | Mirusiojo amžius dienomis | Dienos pašalintos mirusiems asmenims, kurie yra vyresni nei metai |
| `m_m_dt` | `string` | — | `2` | `open` | `pii:date` | Mirties data (mėnesiais) | — |
| `mirt_vieta_zyma` | `string` | — | `4` | `open` | `person:placeOfDeath` | Mirties vietos žyma | — |
| `sav_kodas` | `string` | — | `4` | `open` | `person:placeOfDeath` | Mirties vietos savivaldybės kodas | — |
| `tipo_santr` | `string` | — | `4` | `open` | `person:placeOfDeath` | Mirties vietos gyvenvietės tipas | — |
| `m_mv_v` | `string` | — | `4` | `open` | `person:countryOfDeath` | Mirties vieta | Valstybės kodas mirusiems užsienyje |
| `gnmpd` | `integer` | — | `4` | `open` | — | Gydytojo nuomone, mirties rūšis | — |
| `pmprs` | `string` | — | `4` | `open` | `pii:other` | Pagrindinė mirties priežastis | Mirties atvejų ir jų priežasčių valstybės registre pagal Pasaulio sveikatos organizacijos taisykles išrinkta oficialiojoje statistikoje naudojama pagrindinė mirties priežastis |
| `pmprs_pk` | `string` | — | `4` | `open` | — | Trauma, apsinuodijimas ir kiti išorinių priežasčių padariniai (išorinėms mirties priežastims) | — |
| `pmprs_iv` | `string` | — | `4` | `open` | — | Nelaimingo atsitikimo, savižudybės, žmogžudystės vietos kodas (išorinėms mirties priežastims) | — |
| `pmprs_v` | `string` | — | `4` | `open` | — | Veikla (išorinėms mirties priežastims) | — |
| `mmli_apl` | `integer` | — | `4` | `open` | — | Medicininį mirties liudijimą išrašė | — |
| `m_ngm_isn` | `integer` | — | `4` | `open` | — | 0-28 parų naujagimio išnešiotumas | — |
| `m_nj_mase` | `number` | `g` | `4` | `open` | — | 0-28 parų naujagimio masė gramais | — |
| `m_gv_zyma` | `string` | — | `4` | `open` | `person:placeOfBirth` | Gimimo vietos žyma (negyvagimiui ar naujagimiui mirusiam per 0–6 paras) | — |
| `m_nj_gest_am` | `integer` | `wk` | `4` | `open` | — | Nėštumo trukmė (savaitėmis) (negyvagimiui ar naujagimiui mirusiam per 0–6 paras) | — |
| `m_njm_gimdymas` | `integer` | — | `4` | `open` | — | Kelintas gimdymas (negyvagimiui ar naujagimiui mirusiam per 0–6 paras) | — |
| `m_nj_eile` | `integer` | — | `4` | `open` | — | Naujagimio (negyvagimio) gimimo eiliškumo žyma (negyvagimiui ar naujagimiui mirusiam per 0–6 paras) | — |
| `m_nj_ugis` | `number` | `cm` | `4` | `open` | `pii:other` | Ūgis (negyvagimiui ar naujagimiui mirusiam per 0–6 paras) | — |
| `mt` | `integer` | — | `2` | `open` | — | Statistiniai mirties metai | — |
| `e106_operac` | `integer` | — | `2` | `open` | — | Ar per paskutines 28 d. iki mirties buvo atlikta operacija? | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `m_lytis` | `1` | — | — | Vyras | — |
| `m_lytis` | `2` | — | — | Moteris | — |
| `mirt_vieta_zyma` | `'L'` | — | — | Ligoninė | — |
| `mirt_vieta_zyma` | `'N'` | — | — | Namai | — |
| `mirt_vieta_zyma` | `'K'` | — | — | Kita | — |
| `mirt_vieta_zyma` | `'Z'` | — | — | Nežinoma | — |
| `tipo_santr` | `'m.'` | — | — | Miestas | — |
| `tipo_santr` | `'k.'` | — | — | Kaimas | — |
| `tipo_santr` | `'mstl.'` | — | — | Miestelis | — |
| `tipo_santr` | `'vs.'` | — | — | Viensėdis | — |
| `tipo_santr` | `'glž. st.'` | — | — | Geležinkelio stotis | — |
| `gnmpd` | `1` | — | — | liga | — |
| `gnmpd` | `2` | — | — | nelaimingas atsitikimas | — |
| `gnmpd` | `3` | — | — | savižudybė | — |
| `gnmpd` | `4` | — | — | nužudymas | — |
| `gnmpd` | `5` | — | — | nenustatyta priežastis | — |
| `gnmpd` | `6` | — | — | profesinė liga | — |
| `gnmpd` | `7` | — | — | nepažymėta | — |
| `gnmpd` | `8` | — | — | nelaimintas atsitikimas darbe | — |
| `gnmpd` | `9` | — | — | negali būti nustatyta dėl pomirtinių pakitimų | — |
| `gnmpd` | `10` | — | — | staigi netikėta | — |
| `mmli_apl` | `1` | — | — | gydęs gydytojas, apžiūrėjęs mirusįjį ir konstatavęs mirtį | — |
| `mmli_apl` | `2` | — | — | kitas gydytojas apžiūrėjęs mirusįjį ir konstatavęs mirtį | — |
| `mmli_apl` | `3` | — | — | gydęs gydytojas, remdamasis medicinine dokumentacija ir mirusįjį apžiūrėjusiojo kito gydytojo išvada | — |
| `mmli_apl` | `4` | — | — | patalogoanatomas, atlikęs autopsiją | — |
| `mmli_apl` | `5` | — | — | teismo medicinos ekspertas atlikęs autopsiją | — |
| `mmli_apl` | `6` | — | — | teismo medicinos ekspertas remdamasis išorine mirusiojo apžiūra | — |
| `mmli_apl` | `7` | — | — | kitomis aplinkybėmis | — |
| `mmli_apl` | `8` | — | — | nepažymėta | — |
| `m_ngm_isn` | `0` | — | — | nepažymėta | — |
| `m_ngm_isn` | `1` | — | — | išnešiotas | — |
| `m_ngm_isn` | `2` | — | — | neišnešiotas | — |
| `m_ngm_isn` | `3` | — | — | pernešiotas | — |
| `m_gv_zyma` | `'L'` | — | — | Ligoninė | — |
| `m_gv_zyma` | `'N'` | — | — | Namai | — |
| `m_gv_zyma` | `'K'` | — | — | Kita | — |
| `m_gv_zyma` | `'Z'` | — | — | Nežinoma | — |
| `e106_operac` | `1` | — | — | Taip | — |
| `e106_operac` | `2` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/mirtys (https://data.gov.lt/datasets/998/)

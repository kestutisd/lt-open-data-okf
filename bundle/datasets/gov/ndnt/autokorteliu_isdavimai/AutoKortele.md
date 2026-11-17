---
type: Table
title: "AutoKortele — Asmenų su negalia automobilio statymo kortelių išdavimų duomenys"
description: "Lentelėje pateikti asmenų su negalia automobilio statymo kortelių išdavimų duomenys iš Neįgalumo ir darbingumo nustatymo tarnybos informacinės sistemos (NDNT IS)."
resource: "https://get.data.gov.lt/datasets/gov/ndnt/autokorteliu_isdavimai/AutoKortele"
tags: [gov, ndnt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ndnt/autokorteliu_isdavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/autokorteliu_isdavimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AutoKortele — Asmenų su negalia automobilio statymo kortelių išdavimų duomenys

Lentelėje pateikti asmenų su negalia automobilio statymo kortelių išdavimų duomenys iš Neįgalumo ir darbingumo nustatymo tarnybos informacinės sistemos (NDNT IS). Svarbu atkreipti dėmesį, kad automobilio statymo kortelė gali būti išduodama ne tik negalią turintiems darbingo amžiaus asmenims, bet ir vaikams ar pensinio amžiaus žmonėms. Rinkinyje pateikiami ir kas mėnesį atnaujinami nuo 2024 m. liepos mėnesio sukaupti kortelių išdavimo duomenys. Ateityje planuojama papildyti lentelę istoriniais kortelių išdavimo duomenimis.

- **Model:** `datasets/gov/ndnt/autokorteliu_isdavimai/AutoKortele`[^manifest]
- **Dataset:** [Asmenų su negalia automobilio statymo kortelių išdavimų duomenys](../autokorteliu_isdavimai.md) (`datasets/gov/ndnt/autokorteliu_isdavimai`)
- **Manifest CSV:** [datasets/gov/ndnt/autokorteliu_isdavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ndnt/autokorteliu_isdavimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ndnt/autokorteliu_isdavimai/AutoKortele`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `autok_prasymo_id` | `string` | — | `4` | `open` | — | Prašymo, išduoti automobilio statymo kortelę, identifikatorius | — |
| `prasymo_registracijos_data` | `date` | `D` | `4` | `open` | — | Prašymo, išduoti automobilio statymo kortelę, data | — |
| `kam_isduoti` | `string` | — | `4` | `open` | — | Asmens, kuriam išduodama automobilio statymo kortelė, identifikatorius | — |
| `darb_lygis` | `string` | — | `4` | `open` | — | Asmens, kuriam išduodama automobilio statymo kortelė, darbingumo lygis procentais | — |
| `vairuotojo_pazymejimo_galiojimo_data` | `date` | `D` | `4` | `open` | — | Asmens, kuriam išduodama automobilio statymo kortelė, vairuotojo pažymėjimo galiojimo pabaigos data | — |
| `ar_leista` | `string` | — | `4` | `open` | — | Požymis, ar asmeniui leidžiama išduoti automobilio statymo kortelę | — |
| `auto_korteles_nr` | `string` | — | `4` | `open` | — | Automobilio statymo kortelės numeris | — |
| `isdavimo_data` | `date` | `D` | `4` | `open` | — | Automobilio statymo kortelės išdavimo data | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Automobilio statymo kortelės galiojimo pabaigos data | — |
| `neterm` | `string` | — | `4` | `open` | — | Požymis, ar automobilio statymo kortelė išduodama neterminuotai (1 - neterminuotai) | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyrius, atsakingas už automobilio statymo kortelės išdavimą | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas, kuriame yra skyrius, atsakingas už automobilio statymo kortelės išdavimą | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_leista` | `"leista išduoti"` | — | — | Leidžiama išduoti automobilio statymo kortelę | — |
| `ar_leista` | `"neleista išduoti"` | — | — | Neleidžiama išduoti automobilio statymo kortelės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ndnt/autokorteliu_isdavimai.csv

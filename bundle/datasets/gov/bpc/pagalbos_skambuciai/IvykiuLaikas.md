---
type: Table
title: "IvykiuLaikas — BPC įvykių laikas"
description: "Bendrojo pagalbos centro (BPC) pagalbos telefonu registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, paros meto statistika."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuLaikas"
tags: [gov, bpc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L55"
    last_modified: "2026-11-11T14:39:20Z"
---

# IvykiuLaikas — BPC įvykių laikas

Bendrojo pagalbos centro (BPC) pagalbos telefonu registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, paros meto statistika. Tai yra agreguota lentelė, kuri į vieną eilutę sujungia unikalią šių požymių kombinaciją: įvykio tipas, mėnuo, savaitės diena, valanda, minutės grupė (10 min. tikslumu). Lentelė nėra agraguota pagal metus (t.y., visų metų duomenys yra kartu). Lentelė yra skirta įvykių paros meto tendencijoms stebėti, atsižvelgiant į šventines dienas ir sezoniškumą. Dėl konfidencialumo nepateikiama tiksli įvykio data ar geografinė komponentė. Praneštų įvykių skaičiai nebūtinai turi sutapti su Administracinių nusižengimų registro duomenimis (pranešimai gali būti melagingi arba nepasiekti administracinių nusižengimų bylos stadijos).

- **Model:** `datasets/gov/bpc/pagalbos_skambuciai/IvykiuLaikas`[^manifest]
- **Dataset:** [Bendrojo pagalbos centro 112 skambučių duomenų rinkinys](../pagalbos_skambuciai.md) (`datasets/gov/bpc/pagalbos_skambuciai`)
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L55](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L55)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuLaikas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_tipo_kodas` | `ref` | [IvykiuKlasifikatorius](IvykiuKlasifikatorius.md) | `4` | `open` | — | Įvykio tipo kodas | Šio požymio kodų prasmės yra pagalbinėje lentelėje BPC įvykių klasifikatorius |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo, kuomet įvyko įvykiai | — |
| `savaites_diena` | `integer` | — | `4` | `open` | — | Savaitės dienos, kuomet įvyko įvykiai, numeris | — |
| `valanda` | `integer` | — | `2` | `open` | — | Paros valandos, kuomet įvyko įvykiai, numeris | Reikšmės nuo 0 (vidurnaktis) iki 23 val. |
| `minute` | `string` | — | `2` | `open` | — | Valandos dalies, kuomet įvyko įvykiai, grupė | 10 minučių rėžiai |
| `ivykiu_skaicius` | `integer` | — | `4` | `open` | — | įvykių, apie kuriuos gauti pranešimai, skaičius šioje agregacijos grupėje | — |
| `dienu_grupeje` | `integer` | — | `4` | `open` | — | Požymis, kiek dienų buvo visų metų tokio mėnesio toje savaitės dienoje | Stulpelis būtinas, norint teisingai palyginti savaitės dienas. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `menuo` | `1` | — | — | Sausis | — |
| `menuo` | `2` | — | — | Vasaris | — |
| `menuo` | `3` | — | — | Kovas | — |
| `menuo` | `4` | — | — | Balandis | — |
| `menuo` | `5` | — | — | Gegužė | — |
| `menuo` | `6` | — | — | Birželis | — |
| `menuo` | `7` | — | — | Liepa | — |
| `menuo` | `8` | — | — | Rugpjūtis | — |
| `menuo` | `9` | — | — | Rugsėjis | — |
| `menuo` | `10` | — | — | Spalis | — |
| `menuo` | `11` | — | — | Lapkritis | — |
| `menuo` | `12` | — | — | Gruodis | — |
| `savaites_diena` | `1` | — | — | Pirmadienis | — |
| `savaites_diena` | `2` | — | — | Antradienis | — |
| `savaites_diena` | `3` | — | — | Trečiadienis | — |
| `savaites_diena` | `4` | — | — | Ketvirtadienis | — |
| `savaites_diena` | `5` | — | — | Penktadienis | — |
| `savaites_diena` | `6` | — | — | Šeštadienis | — |
| `savaites_diena` | `7` | — | — | Sekmadienis | — |
| `minute` | `"00-09"` | — | — | pirmas 10 minučių rėžis | — |
| `minute` | `"10-19"` | — | — | antras 10 minučių rėžis | — |
| `minute` | `"20-29"` | — | — | trečias 10 minučių rėžis | — |
| `minute` | `"30-39"` | — | — | ketvirtas 10 minučių rėžis | — |
| `minute` | `"40-49"` | — | — | penktas 10 minučių rėžis | — |
| `minute` | `"50-59"` | — | — | šeštas 10 minučių rėžis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv

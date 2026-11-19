---
type: Table
title: "FilmuRegistras — Filmų registras"
description: "Duomenų rinkinys apima informaciją apie Lietuvoje registruotus filmus ir jų metaduomenis, susijusius su kūrybinėmis komandomis, rodymo teisėmis, subtitrais, gamybos informacija ir autorinėmis teisėmis."
resource: "https://get.data.gov.lt/datasets/gov/lkc/filmu_registras/FilmuRegistras"
tags: [gov, lkc, filmuregistras, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lkc/filmu_registras.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkc/filmu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# FilmuRegistras — Filmų registras

Duomenų rinkinys apima informaciją apie Lietuvoje registruotus filmus ir jų metaduomenis, susijusius su kūrybinėmis komandomis, rodymo teisėmis, subtitrais, gamybos informacija ir autorinėmis teisėmis. Kiekviena lentelės eilutė atitinka vieną filmą. Rinkinys gali būti naudojamas kultūros tyrimams, kino statistikai, filmų duomenų analizei ar autorinių teisių stebėsenai. Duomenų teikėjas – Lietuvos Kino Centras. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lkc/filmu_registras/FilmuRegistras`[^manifest]
- **Dataset:** [Filmų registras](../filmu_registras.md) (`datasets/gov/lkc/filmu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/lkc/filmu_registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkc/filmu_registras/FilmuRegistras` (`deployed`)[^manifest]
- **Provider:** `lkc` — Lietuvos Kino Centras prie Kultūros Ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Filmo identifikatorius | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Filmo pavadinimas lietuvių kalba | — |
| `nuoroda_lt` | `string` | — | `4` | `open` | — | Nuoroda į filmą | — |
| `pavadinimas_orig` | `string` | — | `4` | `open` | — | Filmo pavadinimas originalo kalba | — |
| `tipas` | `string` | — | `4` | `open` | — | Filmo rūšis | — |
| `zanras` | `string` | — | `4` | `open` | — | Filmo žanras | — |
| `data` | `date` | `Y` | `4` | `open` | — | Filmo pagaminimo metai | — |
| `trukme` | `string` | — | `4` | `open` | — | Trukmė (min.) Gali būti nurodyta ir kaip serijų skaičius × trukmė, pvz., „5×50“ | — |
| `filmo_indeksas` | `string` | — | `4` | `open` | — | Filmo indeksas pagal amžiaus cenzą | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės kuriose pagamintas filmas | — |
| `kalba_orig` | `string` | — | `4` | `open` | — | Filmo originalo kalba | — |
| `kalba_titrai` | `string` | — | `4` | `open` | — | Subtitrų kalbos | — |
| `dubliuotas` | `string` | — | `4` | `open` | — | Požymis ar dubliuotas | — |
| `autorius` | `string` | — | `4` | `open` | — | Scenarijaus autorius | — |
| `rezisierius` | `string` | — | `4` | `open` | — | Režisierius | — |
| `operatorius` | `string` | — | `4` | `open` | — | Operatorius | — |
| `kompozitorius` | `string` | — | `4` | `open` | — | Kompozitorius | — |
| `dailininkas` | `string` | — | `4` | `open` | — | Dailininkas | — |
| `savininkas` | `string` | — | `4` | `open` | — | Filmo autorių turtinių teisių savininkas | — |
| `stg_nuo` | `date` | `D` | `4` | `open` | — | Suteiktų teisių galiojimas nuo | — |
| `stg_iki` | `date` | `D` | `4` | `open` | — | Suteiktų teisių galiojimas iki | — |
| `gamintojas` | `string` | — | `4` | `open` | — | Filmo pirmojo įrašo gamintojas | — |
| `nfofms_vieta` | `string` | — | `4` | `open` | — | Nacionalinio filmo originalios filmo medžiagos saugojimo vieta | — |
| `rodytojas` | `string` | — | `4` | `open` | — | Filmo rodytojas | — |
| `platintojas` | `string` | — | `4` | `open` | — | Filmo platintojas | — |
| `fipu_data` | `datetime` | `D` | `4` | `open` | — | Filmo įregistravimo data | — |
| `negalioja` | `integer` | — | `4` | `open` | — | Filmas pripažintas negaliojančiu (1 – taip, 0 – Ne) | — |
| `negalioja_data` | `datetime` | `D` | `4` | `open` | — | Registracijos pripažinimo negaliojančia data | — |
| `isregistruotas` | `integer` | — | `4` | `open` | — | Požymis, nurodantis, ar išregistruotas | — |
| `isregistruotas_data` | `datetime` | `D` | `4` | `open` | — | Išregistravimo data | — |
| `filmo_teises` | `string` | — | `4` | `open` | — | Suteiktos teisės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkc/filmu_registras.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkc/filmu_registras.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkc/filmu_registras (https://data.gov.lt/datasets/3896/)

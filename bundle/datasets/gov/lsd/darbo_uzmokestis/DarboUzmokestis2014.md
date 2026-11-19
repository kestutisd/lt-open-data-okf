---
type: Table
title: "DarboUzmokestis2014 — Darbo užmokesčio struktūros statistinis tyrimas 2014 m."
description: "2014 metais atliktas darbo užmokesčio struktūros statistinis tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/darbo_uzmokestis/DarboUzmokestis2014"
tags: [gov, lsd, darbouzmokestis2014, deployed, level-4, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/darbo_uzmokestis.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/darbo_uzmokestis.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1620/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/darbo_uzmokestis"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# DarboUzmokestis2014 — Darbo užmokesčio struktūros statistinis tyrimas 2014 m.

2014 metais atliktas darbo užmokesčio struktūros statistinis tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/darbo_uzmokestis/DarboUzmokestis2014`[^manifest]
- **Dataset:** [Darbo užmokesčio struktūros statistinio tyrimo duomenys](../darbo_uzmokestis.md) (`datasets/gov/lsd/darbo_uzmokestis`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/darbo_uzmokestis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/darbo_uzmokestis.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/darbo_uzmokestis/DarboUzmokestis2014` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `integer` | — | `4` | `open` | — | Ataskaitiniai metai | — |
| `evrk` | `string` | — | `4` | `open` | — | Ekonominės veiklos rūšies kodas (EVRK 2 red., sekcijos) | — |
| `key_e` | `integer` | — | `4` | `open` | — | Darbuotojo kodas | — |
| `key_l` | `integer` | — | `4` | `open` | — | Vietos vieneto kodas | — |
| `nuts` | `string` | — | `4` | `open` | — | Vietos vieneto geografinė vieta (NUTS-1) | — |
| `im_dydzio_kodas` | `integer` | — | `4` | `open` | — | Įmonės, kuriai priklauso vietos vienetas, dydžio kodas | — |
| `im_dydis` | `string` | — | `4` | `open` | — | Įmonės, kuriai priklauso vietos vienetas, dydis | — |
| `evrk_2z` | `string` | — | `4` | `open` | — | Vietos vieneto ekonominės veiklos rūšies kodas (EVRK 2 red., 2 ženklai) | — |
| `nuosavybe` | `string` | — | `4` | `open` | — | Nuosavybės forma | — |
| `sutartis` | `string` | — | `4` | `open` | — | Kolektyvinė sutartis | — |
| `vv_darb_sk` | `integer` | — | `4` | `open` | — | Vietos vieneto darbuotojų skaičius spalio 31 d. | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amzius` | `string` | — | `4` | `open` | — | Amžius | — |
| `profesija` | `integer` | — | `4` | `open` | — | Darbuotojo profesijos kodas (pagal Lietuvos profesijų klasifikatorių LPK-2012 – 3 ženklai). | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Aukščiausias įgytas išsilavinimas, švietimo lygmuo | — |
| `stazas` | `integer` | — | `4` | `open` | — | Darbo stažas įmonėje (metais) | — |
| `darbo_laikas` | `string` | — | `4` | `open` | — | Nustatytas darbo laikas | — |
| `daro_laiko_dalis` | `number` | — | `4` | `open` | — | Darbuotojo nustatyto darbo laiko dalis, palyginti su visą darbo dieną dirbančio darbuotojo nustatytomis darbo valandomis, procentais | — |
| `sutarties_rusis` | `string` | — | `4` | `open` | — | Sutarties rūšis | — |
| `savaiciu_sk` | `number` | — | `4` | `open` | — | Ataskaitinių metų savaičių, su kuriomis susijęs metinis bruto darbo užmokestis, skaičius | — |
| `apmoketos_val` | `integer` | — | `4` | `open` | — | Apmokėtų valandų skaičius spalio mėn. | — |
| `virsvalandziu_sk` | `integer` | — | `4` | `open` | — | Viršvalandžių skaičius spalio mėn. | — |
| `atostogu_dienos` | `number` | — | `4` | `open` | — | Kasmetinių atostogų dienų skaičius (darbo dienomis) | — |
| `nedirbtos_dienos` | `number` | — | `4` | `open` | — | Kitos nedirbtos, bet apmokėtos dienos per metus (darbo dienomis) | — |
| `bdu_metinis` | `number` | — | `4` | `open` | — | Metinis bruto darbo užmokestis | — |
| `premijos` | `number` | — | `4` | `open` | — | Metinės nereguliarios premijos, priedai, priemokos ir vienkartinės piniginės išmokos | — |
| `bdu_spalio` | `number` | — | `4` | `open` | — | Bruto darbo užmokestis spalio mėn. | — |
| `virsvalandziu_bdu` | `number` | — | `4` | `open` | — | Darbo užmokestis už viršvalandžius spalio mėn. | — |
| `priemokos` | `number` | — | `4` | `open` | — | Priemokos už darbą pamainomis, nakties metu, poilsio ir švenčių dienomis spalio mėn. | — |
| `bdu_val` | `number` | — | `4` | `open` | — | Valandinis bruto darbo užmokestis spalio mėn. | — |
| `svoris` | `number` | — | `4` | `open` | — | Darbuotojo lyginamasis svoris | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `im_dydzio_kodas` | `0` | — | — | 1-49 darbuotojų | — |
| `im_dydzio_kodas` | `1` | — | — | 50-249 darbuotojų | — |
| `im_dydzio_kodas` | `2` | — | — | 250 ir daugiau darbuotojų | — |
| `im_dydis` | `"1_49"` | — | — | 1-49 darbuotojų | — |
| `im_dydis` | `"50_249"` | — | — | 50-249 darbuotojų | — |
| `im_dydis` | `"GT_250"` | — | — | 250 ir daugiau darbuotojų | — |
| `nuosavybe` | `"A"` | — | — | Viešasis sektorius | — |
| `nuosavybe` | `"B"` | — | — | Privatusis sektorius | — |
| `sutartis` | `"A"` | — | — | Nacionalinė | — |
| `sutartis` | `"B"` | — | — | Šakos (gamybos, paslaugų, profesinė) | — |
| `sutartis` | `"C"` | — | — | Teritorinė (savivaldybės, apskrities) | — |
| `sutartis` | `"D"` | — | — | Įmonės | — |
| `sutartis` | `"E"` | — | — | Vietos vieneto | — |
| `sutartis` | `"F"` | — | — | Kita | — |
| `sutartis` | `"N"` | — | — | Nesudaryta | — |
| `amzius` | `"F"` | — | — | Moteris | — |
| `amzius` | `"M"` | — | — | Vyras | — |
| `issilavinimas` | `"G1"` | — | — | Pradinis arba pagrindinis | — |
| `issilavinimas` | `"G2"` | — | — | Vidurinis (Povidurinis profesinis, Specialusis vidurinis, Aukštesnysis) | — |
| `issilavinimas` | `"G3"` | — | — | Aukštasis (bakalauro studijos) | — |
| `issilavinimas` | `"G4"` | — | — | Aukštasis (magistro studijos ir doktorantūra) | — |
| `darbo_laikas` | `"FT"` | — | — | Visas darbo laikas | — |
| `darbo_laikas` | `"PT"` | — | — | Ne visas darbo laikas | — |
| `sutarties_rusis` | `"A"` | — | — | Neterminuota | — |
| `sutarties_rusis` | `"B"` | — | — | Terminuota | — |
| `sutarties_rusis` | `"C"` | — | — | Mokinys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "?")` | `ref` | `4` | `open` | — | — | — |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `evrk` | `update(type: "ref", ref: "/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis")` | `type` | `4` | `open` | — | — | — |
| `key_e` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |
| `key_l` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |
| `nuts` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |
| `im_dydzio_kodas` | `update(property: "im_dydis.kodas")` | `property` | `4` | `open` | — | — | — |
| `im_dydis` | `update(property: "im_dydis.pavadinimas")` | `property` | `4` | `open` | — | — | — |
| `evrk_2z` | `update(property: "evrk.2z")` | `property` | `4` | `open` | — | — | — |
| `lytis` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `amzius` | — | `ref` | `4` | `open` | — | — | Panašu, kad F/M turėtu būti prie `lytis`? |
| `profesija` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |
| `bdu_metinis` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `premijos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `bdu_spalio` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `virsvalandziu_bdu` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `priemokos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `bdu_val` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/darbo_uzmokestis.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/darbo_uzmokestis.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/darbo_uzmokestis (https://data.gov.lt/datasets/1620/)

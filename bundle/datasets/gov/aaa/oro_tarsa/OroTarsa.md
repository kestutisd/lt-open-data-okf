---
type: Table
title: "OroTarsa"
description: "Spinta table datasets/gov/aaa/oro_tarsa/OroTarsa (30 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_tarsa/OroTarsa"
tags: [gov, aaa, orotarsa, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tarsa.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_tarsa.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1787/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tarsa"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# OroTarsa

- **Model:** `datasets/gov/aaa/oro_tarsa/OroTarsa`[^manifest]
- **Dataset:** [Stacionarių taršos šaltinių metinių aplinkos oro ataskaitų duomenys](../oro_tarsa.md) (`datasets/gov/aaa/oro_tarsa`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_tarsa.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tarsa.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_tarsa/OroTarsa` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_kodas` | `string` | — | `2` | `open` | — | Ataskaitinio objekto kodas | — |
| `pavad` | `string` | — | `2` | `open` | — | Ataskaitinio objekto pavadinimas. Ūkio subjekto pagrindinės įmonės atveju nurodomas toks pat kaip JAR, o filialų atveju nurodomas rankiniu būdu | — |
| `uvo_kodas` | `string` | — | `2` | `open` | — | Ūkinės veiklos objekto kodas | — |
| `uvo_pavad` | `string` | — | `2` | `open` | — | Ūkinės veiklos objekto pavadinimas | — |
| `x_koord` | `number` | — | `2` | `open` | — | Ataskaitinio objekto X koordinatės pagal LKS-94 | — |
| `y_koord` | `number` | — | `2` | `open` | — | Ataskaitinio objekto Y koordinatės pagal LKS-94 | — |
| `imones_kodas` | `string` | — | `2` | `open` | — | Įmonės JAR kodas | — |
| `atsiskaitoma` | `date` | `Y` | `4` | `open` | — | Data, už kurią yra teikiamas dokumentas. | — |
| `mat_vnt` | `string` | — | `4` | `open` | — | Teršalo matavimo vienetai (Klasifikatorius) | — |
| `kiekis_ataskait` | `number` | — | `4` | `open` | — | Per ataskaitinius metus į aplinkos orą patekęs teršalų kiekis | — |
| `kiekis_praejus` | `number` | — | `4` | `open` | — | Per praėjusius metus į aplinkos orą patekęs teršalų kiekis (išskaičiuojamas iš praeitų metų ataskaitos duomenų) | — |
| `kuro_kodas` | `string` | — | `3` | `open` | — | Kuro rūšies kodas - trumpinys | — |
| `kuro_pavad` | `string` | — | `3` | `open` | — | Kuro rūšies pavadinimas (pvz., mediena) | — |
| `mpr_pavad` | `string` | — | `1` | `open` | — | Visas vykdomos (ar jau įvykdytos) aplinkos oro taršos mažinimo priemonės pavadinimas | — |
| `mpr_verte` | `number` | — | `2` | `open` | — | Išlaidos skirtos taršos mažinimo priemonei vykdyti | — |
| `plan_ivykd` | `date` | `D` | `4` | `open` | — | Priemonės planuojama įvykdymo data | — |
| `lesos` | `number` | — | `2` | `open` | — | Kiek skirta lėšų nuo priemonės vykdymo pradžios | — |
| `lesos_ataskait` | `number` | — | `2` | `open` | — | Kiek skirta lėšų priemonės vykdymui ataskaitiniais metais | — |
| `mpr_ivykdyta` | `integer` | `%` | `4` | `open` | — | Priemonės įvykdymas procentais | — |
| `vr_kodas` | `string` | — | `2` | `open` | — | Veiklos rūšies kodas | https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.179328/FyUMYOEChe Įsakymo 1 priede VEIKLOS RŪŠIŲ SĄRAŠAS |
| `vr_pavad` | `string` | — | `2` | `open` | — | Veiklos rūšies pavadinimas | — |
| `vr_pavad_en` | `string` | — | `2` | `open` | — | Veiklos rūšies pavadinimas anglų kalba | — |
| `snk_pavad` | `string` | — | `2` | `open` | — | Sunaudoto kuro patikslintas pavadinimas, kai nurodyti kuro kodai 121, 224, 225, 314 | https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.94607/asr Tvarkos aprašo 5 priedas DEGINAMO KURO IR JO DEGALŲ KODAI |
| `snk_mat_vnt` | `string` | — | `4` | `open` | — | Sunaudoto kuro kiekio matavimo vienetai | — |
| `snk_kiekis` | `number` | — | `4` | `open` | — | Sunaudoto kuro kiekis tonomis, jei naudojamas kietas arba skystas kuras, ir tūkst. m3, jei naudojamas dujinis kuras | — |
| `sieringumas` | `number` | `%` | `4` | `open` | — | Sunaudoto kuro sieringumas procentais | — |
| `peleningumas` | `number` | `%` | `4` | `open` | — | Sunaudoto kuro peleningumas procentais | — |
| `trs_kodas` | `integer` | — | `2` | `open` | — | Teršalo kodas, kuris skirsis nuotekų ir emisijų atveju, teršiančių medžiagų sąraše | https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.94607/asr 4 priede pateikta TERŠALŲ IR JŲ KODŲ SĄRAŠAS |
| `trs_pavad` | `string` | — | `2` | `open` | — | Teršalo pavadinimas | — |
| `trs_grupe` | `string` | — | `4` | — | — | Teršalų grupavimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mat_vnt` | `"T"` | — | — | Tonos | — |
| `mat_vnt` | `"M"` | — | — | Kubiniai metrai | — |
| `snk_mat_vnt` | `"T"` | — | — | Tonos | — |
| `snk_mat_vnt` | `"M"` | — | — | Kubiniai metrai | — |
| `trs_grupe` | `"V"` | — | — | Teršalai išleidžiami į aplinką (vandenį) | — |
| `trs_grupe` | `"I"` | — | — | Teršalai išleidžiami į žemę | — |
| `trs_grupe` | `"O"` | — | — | Teršalai išmetami į aplinkos orą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imones_kodas` | `update(property: "ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `mpr_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `lesos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `lesos_ataskait` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_tarsa.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tarsa.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tarsa (https://data.gov.lt/datasets/1787/)

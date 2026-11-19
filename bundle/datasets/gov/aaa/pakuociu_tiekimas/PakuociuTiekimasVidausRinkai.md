---
type: Table
title: "PakuociuTiekimasVidausRinkai — Pakuočių tiekimo vidaus rinkai apskaitos duomenys"
description: "Spinta table datasets/gov/aaa/pakuociu_tiekimas/PakuociuTiekimasVidausRinkai (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/pakuociu_tiekimas/PakuociuTiekimasVidausRinkai"
tags: [gov, aaa, pakuociutiekimasvidausrinkai, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/pakuociu_tiekimas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/pakuociu_tiekimas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1785/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/pakuociu_tiekimas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# PakuociuTiekimasVidausRinkai — Pakuočių tiekimo vidaus rinkai apskaitos duomenys

- **Model:** `datasets/gov/aaa/pakuociu_tiekimas/PakuociuTiekimasVidausRinkai`[^manifest]
- **Dataset:** [Pakuočių tiekimo vidaus rinkai apskaitos duomenys](../pakuociu_tiekimas.md) (`datasets/gov/aaa/pakuociu_tiekimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/pakuociu_tiekimas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/pakuociu_tiekimas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/pakuociu_tiekimas/PakuociuTiekimasVidausRinkai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Ataskaitiniai metai |
| `medziaga` | `string` | — | `4` | `open` | — | Pakuotės medžiagos pavadinimas | Pakuočių ir pakuočių atliekų tvarkymo taisyklės, patvirtintos Lietuvos Respublikos aplinkos ministro 2002-06-27 įsakymu Nr. 348, Mokesčio už aplinkos teršimą deklaracijų FR0521, FR0522, FR0523 ir FR0524 formų ir jų pildymo taisyklės, patvirtintos Valstybinės mokesčių inspekcijos prie Lietuvos Respublikos finansų ministerijos viršininko ir Lietuvos Respublikos aplinko ministro 2008 m. gruodžio 8 d. įsakymu Nr. VA-61/D1-658 |
| `kiekis` | `integer` | `t` | `4` | `open` | — | Patiekta vidaus rinkai | Duomenys parengti pagal Gamintojų ir importuotojų, tiekiančių šalies rinkai supakuotus gaminius, metinių ataskaitų duomenis ir Mokesčio už aplinkos teršimą pakuočių atliekomis aktualių deklaracijų duomenis. |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `medziaga` | `"Stiklinė"` | — | — | Stiklinė pakuotė | — |
| `medziaga` | `"Plastikinė"` | — | — | Plastikinė pakuotė | — |
| `medziaga` | `"Popierinė-kartoninė"` | — | — | Popierinė ir kartoninė pakuotė | — |
| `medziaga` | `"Metalinės (iš viso)"` | — | — | Metalinės pakuotės (iš viso) | — |
| `medziaga` | `"juodųjų metalų"` | — | — | Juodųjų metalų pakuotė | Duomenys apskaičiuoti vertinimo būdu, pagal atliekų tvarkytojų teikiamų ataskaitų duomenis (Atliekų tvarkymo ir susidarymo apskaitos ir ataskaitų teikimo taisyklės). Nuo 2021 m. pagal Gamintojų ir importuotojų, tiekiančių šalies rinkai supakuotus gaminius, metinių ataskaitų duomenis. |
| `medziaga` | `"aliuminė"` | — | — | Aliuminio pakuotė | Duomenys apskaičiuoti vertinimo būdu, pagal atliekų tvarkytojų teikiamų ataskaitų duomenis (Atliekų tvarkymo ir susidarymo apskaitos ir ataskaitų teikimo taisyklės). Nuo 2021 m. pagal Gamintojų ir importuotojų, tiekiančių šalies rinkai supakuotus gaminius, metinių ataskaitų duomenis. |
| `medziaga` | `"Medinė"` | — | — | Medinė pakuotė | — |
| `medziaga` | `"Kombinuota (iš viso)"` | — | — | Kombinuota pakuotė (iš viso) | — |
| `medziaga` | `"kombinuota popierinė"` | — | — | kombinuota popierinė pakuotė | — |
| `medziaga` | `"kombinuota kita"` | — | — | kombinuota kita | — |
| `medziaga` | `"Kita"` | — | — | Kita | — |
| `medziaga` | `"Visos medžiagos"` | — | — | Visos medžiagos (bendras kiekis) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/pakuociu_tiekimas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/pakuociu_tiekimas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/pakuociu_tiekimas (https://data.gov.lt/datasets/1785/)

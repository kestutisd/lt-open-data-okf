---
type: Table
title: "Skolininkas — Duomenys apie įkeitimo ir hipotekos sandorių skolininkus (skolininko tipą, amžių, formą sandorių rūšis, sudarymo vietas, vertes, terminus)"
description: "Spinta table datasets/gov/rc/stsr/skolininkai/Skolininkas (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/skolininkai/Skolininkas"
tags: [gov, rc, skolininkas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/skolininkai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2136/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/stsr/skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Skolininkas — Duomenys apie įkeitimo ir hipotekos sandorių skolininkus (skolininko tipą, amžių, formą sandorių rūšis, sudarymo vietas...

- **Model:** `datasets/gov/rc/stsr/skolininkai/Skolininkas`[^manifest]
- **Dataset:** [STSR duomenys apie įkeitimo ir hipotekos sandorių skolininkus](../skolininkai.md) (`datasets/gov/rc/stsr/skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/stsr/skolininkai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/skolininkai/Skolininkas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `skolininko_id`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skolininko_id` | `integer` | — | `2` | `open` | — | Skolininko dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `st_nr` | `integer` | — | `2` | `open` | — | Hipotekos / įkeitimo dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `amnt_grupe` | `string` | — | `4` | `open` | — | Skolininko asmens tipo grupė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Skolininko amžiaus grupė, jeigu skolininkas fizinis asmuo | — |
| `reg_metai` | `date` | `Y` | `4` | `open` | — | Skolininko registracijos metai | — |
| `sal_grupe` | `string` | — | `3` | `open` | — | Skolininko šalies grupės pavadinimas | — |
| `st_tipas` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo tipas šiame duomenų rinkinyje | — |
| `st_ireg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo įregistravimo data (metai - ketvirtis) | — |
| `st_isreg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo išregistravimo data (metai - ketvirtis) | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo paskutinio įregistruoto įrašo tipas Sutarčių ir teisių suvaržymų registre | — |
| `sudarymo_vieta` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo sudarymo vieta (sav.; apskr.) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos savivaldybės kodas iš Adresų registro (tik didmiesčių savivaldybės) | — |
| `apskritis` | `ref` | [Apskritis](../../ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos apskrities kodas iš Adresų registro | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `pri_terminas_metai` | `date` | `Y` | `4` | `open` | — | Prievolės įvykdymo terminas (metai) | — |
| `maksimalus` | `integer` | — | `4` | `open` | — | Ar maksimalioji hipoteka (1 - taip; 0 - ne) | — |
| `paprastas` | `integer` | — | `4` | `open` | — | Ar paprastoji hipoteka (1 - taip; 0 - ne) | — |
| `jungtinis` | `integer` | — | `4` | `open` | — | Ar jungtinė hipoteka (1 - taip; 0 - ne) | — |
| `svetimas` | `integer` | — | `4` | `open` | — | Ar svetimo turto hipoteka (1 - taip; 0 - ne) | — |
| `bendras` | `integer` | — | `4` | `open` | — | Ar bendroji hipoteka (1 - taip; 0 - ne) | — |
| `salyginis` | `integer` | — | `4` | `open` | — | Ar sąlyginė hipoteka (1 - taip; 0 - ne) | — |
| `pareikstinis` | `integer` | — | `4` | `open` | — | Ar pareikštinė (1 - taip; 0 - ne) | — |
| `imones` | `integer` | — | `4` | `open` | — | Ar įmonės hipoteka (1 - taip; 0 - ne) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `amnt_grupe` | `"FA"` | — | — | Fizinis asmuo | — |
| `amnt_grupe` | `"JA"` | — | — | Juridinis asmuo | — |
| `amnt_grupe` | `"UFA"` | — | — | Užsienio fizinis asmuo | — |
| `amnt_grupe` | `"UJA"` | — | — | Užsienio juridinis asmuo | — |
| `maksimalus` | `0` | — | — | Ne | — |
| `maksimalus` | `1` | — | — | Taip | — |
| `paprastas` | `0` | — | — | Ne | — |
| `paprastas` | `1` | — | — | Taip | — |
| `jungtinis` | `0` | — | — | Ne | — |
| `jungtinis` | `1` | — | — | Taip | — |
| `svetimas` | `0` | — | — | Ne | — |
| `svetimas` | `1` | — | — | Taip | — |
| `bendras` | `0` | — | — | Ne | — |
| `bendras` | `1` | — | — | Taip | — |
| `salyginis` | `0` | — | — | Ne | — |
| `salyginis` | `1` | — | — | Taip | — |
| `pareikstinis` | `0` | — | — | Ne | — |
| `pareikstinis` | `1` | — | — | Taip | — |
| `imones` | `0` | — | — | Ne | — |
| `imones` | `1` | — | — | Taip | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/skolininkai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/skolininkai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/stsr/skolininkai (https://data.gov.lt/datasets/2136/)

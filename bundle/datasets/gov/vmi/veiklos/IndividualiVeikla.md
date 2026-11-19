---
type: Table
title: "IndividualiVeikla — Duomenys apie asmenis vykdančius individualias veiklas"
description: "Spinta table datasets/gov/vmi/veiklos/IndividualiVeikla (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/veiklos/IndividualiVeikla"
tags: [gov, vmi, individualiveikla, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmi/individuali_veikla.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/veiklos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IndividualiVeikla — Duomenys apie asmenis vykdančius individualias veiklas

- **Model:** `datasets/gov/vmi/veiklos/IndividualiVeikla`[^manifest]
- **Dataset:** [Fizinių asmenų, vykdančių individualią veiklą pagal pažymą, duomenys](../veiklos.md) (`datasets/gov/vmi/veiklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/individuali_veikla.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/veiklos/IndividualiVeikla` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `integer` | — | `4` | `open` | — | Rinkinio eilės numeris | — |
| `asm_kodas` | `string` | — | `2` | `open` | — | Fizinio asmens kodas (Gyventojų registre suteiktas asmens kodas) | — |
| `valstybes_kodas` | `integer` | — | `2` | `open` | — | Užsienio piliečio valstybės kodas (pagal valstybių klasifikatorių) | — |
| `savivaldybe` | `integer` | — | `2` | `open` | — | Savivaldybės kodas | — |
| `veiklos_tipas` | `integer` | — | `4` | `open` | — | Veiklos tipas | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Veiklos vykdymo nurodytam mokesčio mokėtojo tipui (laukas MMT_ID) pradžia | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Veiklos vykdymo nurodytam mokesčio mokėtojo tipui (laukas MMT_ID) pabaiga | — |
| `moketojas` | `string` | — | `2` | `open` | — | Mokesčių mokėtojo tipo pavadinimas | — |
| `veikla` | `integer` | — | `2` | `open` | — | Ekonominės veiklos kodas | — |
| `veiklos_pradzia` | `date` | `D` | `4` | `open` | — | Ekonominės veiklos pradžia | — |
| `veiklos_pabaiga` | `date` | `D` | `4` | `open` | — | Ekonominės veiklos pabaiga | — |
| `pagrindine` | `integer` | — | `4` | `open` | — | Veiklos pagrindas | — |
| `vieta` | `integer` | — | `2` | `open` | — | Veiklos vykdymo vietos savivaldybės kodas | — |
| `vietoje_pradzia` | `date` | `D` | `4` | `open` | — | Veiklos vykdymo vietoje pradžia | — |
| `vietoje_pabaiga` | `date` | `D` | `4` | `open` | — | Veiklos vykdymo vietoje pabaiga | — |
| `kodas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo identifikacinis numeris VMI informacinėje sistemoje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiklos_tipas` | `201` | — | — | Notarai | — |
| `veiklos_tipas` | `202` | — | — | Advokatai | — |
| `veiklos_tipas` | `205` | — | — | Nenuolatiniai Lietuvos gyventojai, vykdantys individualią veiklą Lietuvoje per nuolatinę bazę | — |
| `veiklos_tipas` | `213` | — | — | Advokatų padėjėjai | — |
| `veiklos_tipas` | `215` | — | — | Gyventojai, vykdantys individualią veiklą | — |
| `veiklos_tipas` | `217` | — | — | Antstoliai | — |
| `veiklos_tipas` | `222` | — | — | Ūkininko partneris | — |
| `veiklos_tipas` | `232` | — | — | Gyventojas, vykdantis žemės ūkio individualią veiklą, kurio žemės ūkio valdos dydis didesnis negu 14 EDV | — |
| `veiklos_tipas` | `250` | — | — | Gyventojas, vykdantis individualią žemės ūkio veiklą, kurio žemės ūkio valdos (ūkio) ekonominis dydis yra lygus 4 EDV arba didesnis | — |
| `veiklos_tipas` | `251` | — | — | Gyventojas, vykdantis individualią veiklą, įregistruotą MA iniciatyva (viršijęs teisės aktuose nustatytą iš JA gautų pajamų sumą arba deklaravęs pajamas iš individualios veiklos) | — |
| `pagrindine` | `1` | — | — | Pagrindinė veikla | — |
| `pagrindine` | `0` | — | — | Šalutinė veikla | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/individuali_veikla.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/veiklos (https://data.gov.lt/datasets/1912/)

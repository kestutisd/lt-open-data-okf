---
type: Table
title: "Prasymas — Priėmimo prašymų į aukštojo mokslo įstaigas duomenys"
description: "Lentelėje pateikiami priėmimo į aukštojo mokslo įstaigas duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos/Prasymas"
tags: [gov, lamabpo, prasymas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L28"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv#L28"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2914/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/aukstosios_mokyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prasymas — Priėmimo prašymų į aukštojo mokslo įstaigas duomenys

Lentelėje pateikiami priėmimo į aukštojo mokslo įstaigas duomenys. Lentelės eilutės objektas – asmens priėmimo prašymas (prasymo_id). Nurodomas asmenį identifikuojantis numeris, programos pasirinkimo prioritetas ir laiko žyma, duomenys apie priėmimo etapą ir finansavimo pobūdį. Pateikiami požymiai, ar asmuo atitiko reikalavimus dalyvauti priėmimo konkurse, ar gavo pakvietimą į pasirinktą mokymo programą (kartu su pakvietimo data) ir ar pasirašė sutartį su mokymo įstaiga.[^manifest]

- **Model:** `datasets/gov/lamabpo/aukstosios_mokyklos/Prasymas`[^manifest]
- **Dataset:** [Priėmimo į aukštojo mokslo įstaigas prašymų duomenys](../aukstosios_mokyklos.md) (`datasets/gov/lamabpo/aukstosios_mokyklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/aukstuju_prasymai.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L28)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos/Prasymas` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `prasymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikacinis numeris | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikacinis numeris | — |
| `pasirinkimo_data` | `datetime` | `S` | `4` | `open` | — | Mokymo programos pasirinkimo data | — |
| `priemimo_etapas` | `string` | — | `4` | `open` | — | Priėmimo etapo pavadinimas | — |
| `etapo_pradzia` | `date` | `D` | `4` | `open` | — | Priėmimo etapo pradžios data | — |
| `etapo_pabaiga` | `date` | `D` | `4` | `open` | — | Priėmimo etapo pabaigos data | — |
| `prioriteto_nr` | `integer` | — | `4` | `open` | — | Studijų ar mokymo programos prioriteto numeris prašyme | — |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikacinis numeris | — |
| `finansavimas` | `string` | — | `4` | `open` | — | Mokymo programos finansavimo pobūdis | — |
| `ar_dalyvavo_konkurse` | `boolean` | — | `4` | `open` | — | Požymis, ar pageidavimas dalyvavo priėmimo konkurse | — |
| `ar_pakviete` | `boolean` | — | `4` | `open` | — | Požymis, ar prašymą teikęs asmuo gavo pakvietimą | — |
| `pakvietimo_data` | `date` | `D` | `4` | `open` | — | Pakvietimo į studijų programą gavimo data | — |
| `ar_pasirase` | `boolean` | — | `4` | `open` | — | Požymis, ar pakviestasis pasirašė sutartį dėl mokymo ar studijų programos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `priemimo_etapas` | `"Pagrindinis priėmimas"` | — | — | — | — |
| `priemimo_etapas` | `"Papildomo priėmimo pirmasis etapas"` | — | — | — | — |
| `priemimo_etapas` | `"Papildomo priėmimo antrasis etapas"` | — | — | — | — |
| `finansavimas` | `"VF"` | — | — | Valstybinis finansuojama vieta | — |
| `finansavimas` | `"VNF"` | — | — | Valstybės nefinansuojama vieta | — |
| `finansavimas` | `"ST"` | — | — | Studijų stipendija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv#L28 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L28)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/aukstosios_mokyklos (https://data.gov.lt/datasets/2914/)

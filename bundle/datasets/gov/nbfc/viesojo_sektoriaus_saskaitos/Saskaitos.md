---
type: Table
title: "Saskaitos — Sąskaitos"
description: "Viešojo sektoriaus sąskaitų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Saskaitos"
tags: [gov, nbfc, saskaitos, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Saskaitos — Sąskaitos

Viešojo sektoriaus sąskaitų duomenys[^manifest]

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Saskaitos`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Saskaitos` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sf_id` | `string` | — | `4` | `open` | — | Unikalus sąskaitos identifikatorius | — |
| `israsymo_data` | `date` | `D` | `4` | `open` | — | Sąskaitos išrašymo data | — |
| `sf_pozymis` | `string` | — | `4` | `open` | — | Požymis nurodantis ar sąskaita išrašyta pagal Viešojo pirkimo sutartį ar pagal žodinę sutartį | Žodinė sąskaita t.y. sąskaita sudarytą pagal žodinį susitarimą (žodinę viešųjų pirkimų sutartį) |
| `sf_tipas` | `string` | — | `4` | `open` | — | Sąskaitos tipas | — |
| `sf_numeris` | `string` | — | `4` | `open` | — | Sąskaitos numeris | — |
| `sutarties_uid` | `string` | — | `4` | `open` | — | Unikalus sutarties identifikatorius | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Viešųjų pirkimų sutarties numeris | — |
| `cpv_kodas` | `string` | — | `4` | `open` | — | Bendrasis Viešųjų Pirkimų Žodyno kodas | — |
| `cpv_pav` | `string` | — | `4` | `open` | — | Bendrasis Viešųjų Pirkimų Žodyno kodo pavadinimas | — |
| `sf_apmokejimo_terminas` | `date` | `D` | `4` | `open` | — | Sąskaitos mokėjimo terminas | — |
| `pvm` | `string` | — | `4` | `open` | — | Taikomas mokesčių tarifas | — |
| `suma_be_pvm` | `number` | — | `4` | `open` | — | Sąskaitos faktūros prekių/paslaugų suma be PVM | — |
| `suma_pvm` | `number` | — | `4` | `open` | — | Sąskaitos faktūros PVM suma | — |
| `bendra_sf_suma` | `number` | — | `4` | `open` | — | Sąskaitos faktūros suma | — |
| `valiuta` | `string` | — | `4` | `open` | — | Sąskaitos valiuta | — |
| `sf_busena` | `string` | — | `4` | `open` | — | Sąskaitos būsena | — |
| `sf_buseno_data` | `datetime` | `S` | `4` | `open` | — | Sąskaitos būsenos data | — |

# Related References

- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos (https://data.gov.lt/datasets/3924/)

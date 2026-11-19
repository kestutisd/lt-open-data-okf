---
type: Table
title: "Pavyzdys — Saugiųjų dokumentų ir blankų pavyzdžių sąrašas"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., pavyzdžių sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys"
tags: [gov, vdtat, pavyzdys, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2781/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pavyzdys — Saugiųjų dokumentų ir blankų pavyzdžių sąrašas

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., pavyzdžių sąrašas[^manifest]

- **Model:** `datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys`[^manifest]
- **Dataset:** [Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys](../saugiuju_dokumentu_registras.md) (`datasets/gov/vdtat/saugiuju_dokumentu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Pavyzdys` (`deployed`)[^manifest]
- **Provider:** `vdtat` — Valstybės dokumentų technologinės apsaugos tarnyba prie FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės identifikatorius | — |
| `pavyzdzio_id` | `string` | — | `4` | `open` | — | Dokumento blanko ar pavyzdžio identifikatorius | — |
| `dokumento_ar_blanko_id` | `string` | — | `4` | `open` | — | Dokumento ar blanko identifikatorius | — |
| `dokumento_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento ar blanko pavadinimas | — |
| `istaigos_isleidziancios_dokumenta_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos išleidžiančios dokumentą ar blanką pavadinimas | — |
| `nuoroda_i_dokumento_pavyzdi` | `string` | — | `4` | `open` | — | Nuoroda į dokumento pavyzdį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras (https://data.gov.lt/datasets/2781/)

---
type: Table
title: "Irasas — Lietuvos nacionalinis registras \"Pasaulio atmintis\""
description: "Rinkinyje pateikiami į Lietuvos nacionalinį registrą \"Pasaulio atmintis\" įrašyti dokumentai ir jų kolekcijos nuo 2006m."
resource: "https://get.data.gov.lt/datasets/gov/unesco/registras/Irasas"
tags: [gov, unesco, irasas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/unesco/registras.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2753/"
    title: "data.gov.lt DCAT-AP — datasets/gov/unesco/registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Irasas — Lietuvos nacionalinis registras "Pasaulio atmintis"

Rinkinyje pateikiami į Lietuvos nacionalinį registrą "Pasaulio atmintis" įrašyti dokumentai ir jų kolekcijos nuo 2006m. iki šių dienų. Rinkinio objektas - registro įrašas. Nurodomas dokumento ar kolekcijos eilės numeris, pavadinimas, saugojimo vieta, saugojimo vietos internetinis puslapis (jei egzistuoja). Taip pat pažymima, ar dokumentas yra regioninės ar nacionalinės reikšmės. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/unesco/registras/Irasas`[^manifest]
- **Dataset:** [Lietuvos nacionalinis registras "Pasaulio atmintis"](../registras.md) (`datasets/gov/unesco/registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/unesco/registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/unesco/registras/Irasas` (`deployed`)[^manifest]
- **Provider:** `unesco` — Lietuvos nacionalinės UNESCO komisijos sekretoriatas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `eil_nr` | `integer` | — | `4` | `open` | — | Dokumento eilės numeris pagal įrašymo ankstumą | — |
| `dokumentas_lt` | `string` | — | `4` | `open` | — | Dokumento arba kolekcijos pavadinimas | — |
| `reiksme` | `string` | — | `4` | `open` | — | Dokumento reikšmė | — |
| `vieta_lt` | `string` | — | `4` | `open` | — | Dokumento saugojimo vieta | — |
| `nuoroda` | `string` | — | `4` | `open` | — | Saugojimo vietos internetinis puslapis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `reiksme` | `"Regioninė"` | — | — | — | — |
| `reiksme` | `"Nacionalinė"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dokumentas_lt` | `update(property: "dokumentas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vieta_lt` | `update(property: "vieta_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/unesco/registras.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/unesco/registras (https://data.gov.lt/datasets/2753/)

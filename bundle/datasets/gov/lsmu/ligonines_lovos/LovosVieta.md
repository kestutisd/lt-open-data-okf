---
type: Table
title: "LovosVieta — Lovų vietų duomenys"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosVieta"
tags: [gov, lsmu, lovosvieta, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovosVieta — Lovų vietų duomenys

**Dataset Context:** Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys. Rinkinyje pateikiama lovų vietos informacija – vietos kodas, lygmuo, tipas, aprašymas; taip pat Įstaigos duomenys – juridinio asmens kodas ir pavadinimas. Atkreipiame dėmesį, kad šis rinkinys negali būti naudojamas oficialiai statistikai rengti, kadangi dalis lovų duomenų tikslinami rankiniu būdu. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lsmu/ligonines_lovos/LovosVieta`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys](../ligonines_lovos.md) (`datasets/gov/lsmu/ligonines_lovos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/ligonines_lovos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosVieta` (`deployed`)[^manifest]
- **Provider:** `lsmu` — Lietuvos sveikatos mokslų universitetas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vietos_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vietos_id` | `string` | — | `4` | `open` | — | Unikalus vietos eilutės identifikatorius | — |
| `vietos_tevinis_id` | `string` | — | `4` | `open` | — | Vietos tėvinis id (referuoja į vietos_id) | — |
| `vietos_kodas` | `string` | — | `4` | `open` | — | Vietai suteiktas kodas (trumpinys) | — |
| `vietos_lygmuo` | `string` | — | `4` | `open` | — | Lygmuo apibūdinantis vietą (kambarys, palata, aukštas ...) | — |
| `vietos_tipas` | `string` | — | `4` | `open` | — | Vietos tipas (papildoma informacija vietai apibūdinti) | — |
| `vietos_aprasymas` | `string` | — | `4` | `open` | — | Pilnas vietos aprašymas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Juridinio asmens kodo validacijos stulpelis | — |
| `aspi_jar_kodas` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `aspi_pavadinimas` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `jar_validacija` | `"9 sktm. JAR"` | — | — | 9 skaitmenų validus juridinio asmens kodas | — |
| `jar_validacija` | `"7 sktm. JAR"` | — | — | 7 skaitmenų validus juridinio asmens kodas | — |
| `jar_validacija` | `"Ne JAR"` | — | — | Nevalidus juridinio asmens kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L6)

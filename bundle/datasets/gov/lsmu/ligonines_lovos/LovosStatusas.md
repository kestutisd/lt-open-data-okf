---
type: Table
title: "LovosStatusas — Lovų užimtumo duomenys"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosStatusas"
tags: [gov, lsmu, lovosstatusas, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovosStatusas — Lovų užimtumo duomenys

**Dataset Context:** Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys. Rinkinyje pateikiama lovų vietos informacija – vietos kodas, lygmuo, tipas, aprašymas; taip pat Įstaigos duomenys – juridinio asmens kodas ir pavadinimas. Atkreipiame dėmesį, kad šis rinkinys negali būti naudojamas oficialiai statistikai rengti, kadangi dalis lovų duomenų tikslinami rankiniu būdu. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lsmu/ligonines_lovos/LovosStatusas`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys](../ligonines_lovos.md) (`datasets/gov/lsmu/ligonines_lovos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/ligonines_lovos.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosStatusas` (`deployed`)[^manifest]
- **Provider:** `lsmu` — Lietuvos sveikatos mokslų universitetas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `lovos_id` | `string` | — | `4` | `open` | — | Lovos eilutės unikalus identifikatorius | — |
| `vietos_id` | `string` | — | `4` | `open` | — | Vietos identifikatorius (referuoja į lovos_vieta.vietos_id) | — |
| `lovos_statusas` | `string` | — | `4` | `open` | — | Lovos statusas (Užimta, laisva, tvarkoma ...) | — |
| `statuso_pradzia` | `datetime` | `S` | `4` | `open` | — | Statuso galiojimo pradžios laikas | — |
| `statuso_pabaiga` | `datetime` | `S` | `4` | `open` | — | Statuso galiojimo terminas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lovos_statusas` | `"VACANT"` | — | `open` | Laisva | — |
| `lovos_statusas` | `"OCCUPIED"` | — | `open` | Užimta | — |
| `lovos_statusas` | `"IN_MAINTENANCE"` | — | `open` | Tvarkoma | — |
| `lovos_statusas` | `"RESERVED"` | — | `open` | Rezervuota | — |
| `lovos_statusas` | `"BEING_CLEANED"` | — | `open` | Valoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L19)

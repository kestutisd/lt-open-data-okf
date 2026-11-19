---
type: Table
title: "KeleiviuSrautas — Keleivių srautas"
description: "Marijampolės miesto viešojo transporto pirkti ir žymėti bilietai transporto priemonėje"
resource: "https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas/KeleiviuSrautas"
tags: [gov, map, keleiviusrautas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4137/"
    title: "data.gov.lt DCAT-AP — datasets/gov/map/keleiviu_srautas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KeleiviuSrautas — Keleivių srautas

Marijampolės miesto viešojo transporto pirkti ir žymėti bilietai transporto priemonėje[^manifest]

- **Model:** `datasets/gov/map/keleiviu_srautas/KeleiviuSrautas`[^manifest]
- **Dataset:** [Keleivių srautas Marijampolės viešajame transporte](../keleiviu_srautas.md) (`datasets/gov/map/keleiviu_srautas`)[^manifest]
- **Manifest CSV:** [datasets/gov/map/keleiviu_srautas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas/KeleiviuSrautas` (`deployed`)[^manifest]
- **Provider:** `map` — Marijampolės autobusų parkas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikaus identifikatorius | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Bilieto pirkimo/naudojimo data | — |
| `bilieto_tipas` | `string` | — | `4` | `open` | — | Bilieto naudojimo arba pirkimo tipas | — |
| `transporto_tipas` | `string` | — | `4` | `open` | — | Priemiestinio arba miesto viešojo transporto tipas | — |
| `bilieto_pav_id` | `string` | — | `4` | `open` | — | Bilieto identifikatorius | — |
| `bilieto_pav` | `string` | — | `4` | `open` | — | Bilieto pavadinimas | — |
| `transporto_priemones_id` | `string` | — | `4` | `open` | — | Transporto priemonės kodas | — |
| `marsrutas` | `string` | — | `4` | `open` | — | Maršruto numeris | — |
| `keliones_id` | `string` | — | `4` | `open` | — | Maršruto tvarkaraščio kelionės identifikatorius | — |
| `stoteles_eil_nr` | `string` | — | `4` | `open` | — | Stotelės eilės numeris maršrute | — |
| `pr_stoteles_id` | `string` | — | `4` | `open` | — | Maršruto pradžios stotelės kodas | — |
| `pr_stotele` | `string` | — | `4` | `open` | — | Maršruto pradžios stotelė | — |
| `pab_stoteles_id` | `string` | — | `4` | `open` | — | Maršruto pabaigos stotelės kodas | — |
| `pab_stotele` | `string` | — | `4` | `open` | — | Maršruto pabaigos stotelė | — |
| `stoteles_id` | `string` | — | `4` | `open` | — | Stotelės identifikatorius | — |
| `stotele` | `string` | — | `4` | `open` | — | Stotelė | — |
| `mokejimo_budas` | `string` | — | `4` | `open` | — | Mokėjimo už bilietą tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bilieto_tipas` | `"USE_CARD_SERVICE"` | — | — | Mėnesinio bilieto naudojimas miesto viešajam transporte | — |
| `bilieto_tipas` | `"USE_CARD_SERVICE_TRIANGLE"` | — | — | Mėnesinio bilieto naudojimas priemiesčio viešajam transporte | — |
| `bilieto_tipas` | `"SELL_TICKET"` | — | — | Bilieto pirkimas miesto viešajam transporte | — |
| `bilieto_tipas` | `"SELL_TICKET_TRIANGLE"` | — | — | Bilieto pirkimas priemiesčio viešajam transporte | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/map/keleiviu_srautas (https://data.gov.lt/datasets/4137/)

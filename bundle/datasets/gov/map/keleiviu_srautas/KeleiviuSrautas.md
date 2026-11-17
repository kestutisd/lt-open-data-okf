---
type: Table
title: "KeleiviuSrautas — Keleivių srautas"
description: "Marijampolės miesto viešojo transporto pirkti ir žymėti bilietai transporto priemonėje"
resource: "https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas/KeleiviuSrautas"
tags: [gov, map, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KeleiviuSrautas — Keleivių srautas

Marijampolės miesto viešojo transporto pirkti ir žymėti bilietai transporto priemonėje

- **Model:** `datasets/gov/map/keleiviu_srautas/KeleiviuSrautas`[^manifest]
- **Dataset:** [Keleivių srautas Marijampolės viešajame transporte](../keleiviu_srautas.md) (`datasets/gov/map/keleiviu_srautas`)
- **Manifest CSV:** [datasets/gov/map/keleiviu_srautas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas/KeleiviuSrautas`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bilieto_tipas` | `"USE_CARD_SERVICE"` | — | — | Mėnesinio bilieto naudojimas miesto viešajam transporte | — |
| `bilieto_tipas` | `"USE_CARD_SERVICE_TRIANGLE"` | — | — | Mėnesinio bilieto naudojimas priemiesčio viešajam transporte | — |
| `bilieto_tipas` | `"SELL_TICKET"` | — | — | Bilieto pirkimas miesto viešajam transporte | — |
| `bilieto_tipas` | `"SELL_TICKET_TRIANGLE"` | — | — | Bilieto pirkimas priemiesčio viešajam transporte | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv

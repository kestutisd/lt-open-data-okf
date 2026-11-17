---
type: Table
title: "GaunamasDokumentas — Dvs gaunami dokumentai"
description: "Spinta table datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas"
tags: [gov, sakiai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# GaunamasDokumentas — Dvs gaunami dokumentai

- **Model:** `datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas`[^manifest]
- **Dataset:** [Šakių rajono savivaldybės gaunami dokumentai](../gaunami_dokumentai.md) (`datasets/gov/sakiai/gaunami_dokumentai`)
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas`
- **Primary Key (`ref`):** `dok_id`
- **Access:** `open` (inherited)

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `ref` | [Dokumentas](Dokumentas.md) | `4` | `open` (inherited) | — | — | — |
| `dok_ivykd_data` | `date` | `D` | `4` | `open` (inherited) | — | Ivykdymo data | — |
| `dok_termino_data` | `date` | `D` | `4` | `open` (inherited) | — | Termino data | — |
| `dok_gav_reg_nr` | `integer` | — | `2` | `open` (inherited) | — | Registracijos numeris pradedant nuo metų pradžios | — |
| `dok_dfrm_id` | `ref` | [DokumentoFormosTipas](DokumentoFormosTipas.md) | `4` | `open` (inherited) | — | Kokiu būdu gautas dokumentas | — |
| `dok_dtip_id` | `ref` | [DokumentoTipas](DokumentoTipas.md) | `4` | `open` (inherited) | — | — | — |
| `dok_gav_pad_id` | `ref` | [Subjektas](Subjektas.md) | `4` | `open` (inherited) | — | Dokumentą gavęs padalinys | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv

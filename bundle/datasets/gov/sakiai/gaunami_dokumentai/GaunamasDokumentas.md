---
type: Table
title: "GaunamasDokumentas — Dvs gaunami dokumentai"
description: "Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas"
tags: [gov, sakiai, gaunamasdokumentas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GaunamasDokumentas — Dvs gaunami dokumentai

**Dataset Context:** Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita.[^manifest]

- **Model:** `datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas`[^manifest]
- **Dataset:** [Šakių rajono savivaldybės gaunami dokumentai](../gaunami_dokumentai.md) (`datasets/gov/sakiai/gaunami_dokumentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/GaunamasDokumentas` (`deployed`)[^manifest]
- **Provider:** `sakiai` — Šakių rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dok_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `open` (inherited)[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `ref` | [Dokumentas](Dokumentas.md) (`level=4 UUID`: `dok_id._id`) | `4` | `open` (inherited) | — | — | — |
| `dok_ivykd_data` | `date` | `D` | `4` | `open` (inherited) | — | Ivykdymo data | — |
| `dok_termino_data` | `date` | `D` | `4` | `open` (inherited) | — | Termino data | — |
| `dok_gav_reg_nr` | `integer` | — | `2` | `open` (inherited) | — | Registracijos numeris pradedant nuo metų pradžios | — |
| `dok_dfrm_id` | `ref` | [DokumentoFormosTipas](DokumentoFormosTipas.md) (`level=4 UUID`: `dok_dfrm_id._id`) | `4` | `open` (inherited) | — | Kokiu būdu gautas dokumentas | — |
| `dok_dtip_id` | `ref` | [DokumentoTipas](DokumentoTipas.md) (`level=4 UUID`: `dok_dtip_id._id`) | `4` | `open` (inherited) | — | — | — |
| `dok_gav_pad_id` | `ref` | [Subjektas](Subjektas.md) (`level=4 UUID`: `dok_gav_pad_id._id`) | `4` | `open` (inherited) | — | Dokumentą gavęs padalinys | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai (https://data.gov.lt/datasets/2390/)

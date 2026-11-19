---
type: Dataset
title: "Šakių rajono savivaldybės gaunami dokumentai"
description: "Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai"
tags: [gov, sakiai, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Šakių rajono savivaldybės gaunami dokumentai

Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita.[^manifest]

- **Namespace:** `datasets/gov/sakiai/gaunami_dokumentai`[^manifest]
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai` (`deployed`)[^manifest]
- **Provider:** `sakiai` — Šakių rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Access:** `open`[^manifest]
- **Tables:** `6` (6 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2390/`[^dcat]
- **Publisher (`dct:publisher`):** Šakių rajono savivaldybės administracija[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai`[^dcat]
- **Portal Title (`@lt`):** Dokumentų valdymo sistemos gaunami dokumentai[^dcat]
- **Portal Title (`@en`):** Dokumentų valdymo sistemos gaunami dokumentai[^dcat]
- **Issued (`dct:issued`):** `2024-02-27`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-12-07` .. `2026-04-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Dokumentų valdymo sistemos gaunami dokumentai[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Registras](gaunami_dokumentai/Registras.md) | — | — | `rz_id` | `open` (inherited) | `4` | — |
| [Subjektas](gaunami_dokumentai/Subjektas.md) | — | — | `sbj_id` | `open` (inherited) | `2` | — |
| [DokumentoFormosTipas](gaunami_dokumentai/DokumentoFormosTipas.md) | — | — | `dfrm_id` | `open` (inherited) | `2` | — |
| [DokumentoTipas](gaunami_dokumentai/DokumentoTipas.md) | — | — | `dtip_id` | `open` (inherited) | `2` | — |
| [Dokumentas](gaunami_dokumentai/Dokumentas.md) | — | — | `obj_id` | `open` (inherited) | `5` | — |
| [GaunamasDokumentas](gaunami_dokumentai/GaunamasDokumentas.md) | Dvs gaunami dokumentai | — | `dok_id` | `open` (inherited) | `7` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai (https://data.gov.lt/datasets/2390/)

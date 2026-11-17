---
type: Dataset
title: "Šakių rajono savivaldybės gaunami dokumentai"
description: "Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai"
tags: [gov, sakiai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Šakių rajono savivaldybės gaunami dokumentai

Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita.

- **Namespace:** `datasets/gov/sakiai/gaunami_dokumentai`[^manifest]
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai`
- **Access:** `open`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Registras](gaunami_dokumentai/Registras.md) | — | — | `rz_id` | `open` (inherited) | 4 | — |
| [Subjektas](gaunami_dokumentai/Subjektas.md) | — | — | `sbj_id` | `open` (inherited) | 2 | — |
| [DokumentoFormosTipas](gaunami_dokumentai/DokumentoFormosTipas.md) | — | — | `dfrm_id` | `open` (inherited) | 2 | — |
| [DokumentoTipas](gaunami_dokumentai/DokumentoTipas.md) | — | — | `dtip_id` | `open` (inherited) | 2 | — |
| [Dokumentas](gaunami_dokumentai/Dokumentas.md) | — | — | `obj_id` | `open` (inherited) | 5 | — |
| [GaunamasDokumentas](gaunami_dokumentai/GaunamasDokumentas.md) | Dvs gaunami dokumentai | — | `dok_id` | `open` (inherited) | 7 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv

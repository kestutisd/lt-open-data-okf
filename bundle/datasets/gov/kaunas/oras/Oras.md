---
type: Table
title: "Oras — Rodikliai per periodą"
description: "Kauno miesto aplinkos parametrai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/oras/Oras"
tags: [gov, kaunas, oras, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/oras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1948/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/oras"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Oras — Rodikliai per periodą

**Dataset Context:** Kauno miesto aplinkos parametrai[^manifest]

- **Model:** `datasets/gov/kaunas/oras/Oras`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės teikiami duomenys](../oras.md) (`datasets/gov/kaunas/oras`)[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/oras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/oras/Oras` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id,dt`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Daviklio ID | — |
| `dt` | `date` | — | `3` | `open` | — | Data | — |
| `co` | `number` | `mg/m³` | `4` | `open` | — | CO | Anglies monoksido(smalkių) koncentracija miligramais kubiniame metre. |
| `no2` | `number` | — | `3` | `open` | — | NO2 | Azoto dioksido koncentracija mikrogramais kubiniame metre. |
| `o3` | `number` | — | `3` | `open` | — | O3 | Ozono koncentracija mikrogramais kubiniame metre. |
| `so2` | `number` | — | `3` | `open` | — | SO2 | Sieros dioksido koncentracija mikrogramais kubiniame metre. |
| `kd2_5` | `number` | — | `3` | `open` | — | KD2.5 | iki 2.5 mikrometrų dydžio dalelių koncentracija mikrogramais kubiniame metre. |
| `kd10` | `number` | — | `3` | `open` | — | KD10 | iki 10 mikrometrų dydžio dalelių koncentracija mikrogramais kubiniame metre. |
| `temp` | `number` | — | `3` | `open` | — | Temperatūra | Temperatūra Celsijaus laispniais. |
| `dregme` | `number` | `%` | `4` | `open` | — | Santykinė drėgmė | Santykinė drėgmė %. |
| `adresas` | `string` | — | `2` | `open` | — | Adresas | — |
| `ilguma` | `number` | — | `2` | `open` | — | Ilguma | Daviklio koordinatės. Ilguma (WGS84). |
| `platuma` | `number` | — | `2` | `open` | — | Platuma | Daviklio koordinatės. Platuma (WGS84). |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `no2` | `update(ref: "μ/m³")` | `ref` | `4` | `open` | — | — | — |
| `o3` | `update(ref: "μ/m³")` | `ref` | `4` | `open` | — | — | — |
| `so2` | `update(ref: "μ/m³")` | `ref` | `4` | `open` | — | — | — |
| `kd2_5` | `update(ref: "μ/m³")` | `ref` | `4` | `open` | — | — | — |
| `kd10` | `update(ref: "μ/m³")` | `ref` | `4` | `open` | — | — | — |
| `temp` | `update(ref: "°C")` | `ref` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/pastatas/Pastatas")` | `type` | `4` | `open` | — | — | — |
| `ilguma` | `delete()` | `type` | `3` | `open` | — | — | — |
| `platuma` | `update(type: "geometry(point, 4326)"))` | `type` | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/oras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/oras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/oras (https://data.gov.lt/datasets/1948/)

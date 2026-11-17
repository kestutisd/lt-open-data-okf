---
type: Table
title: "JASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis"
description: "Spinta table datasets/gov/rc/ais/ja_skolininkai/JASkolininkas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/ja_skolininkai/JASkolininkas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/ja_skolininkai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/ja_skolininkai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# JASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis

- **Model:** `datasets/gov/rc/ais/ja_skolininkai/JASkolininkas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis](../ja_skolininkai.md) (`datasets/gov/rc/ais/ja_skolininkai`)
- **Manifest CSV:** [datasets/gov/rc/ais/ja_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/ja_skolininkai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/ja_skolininkai/JASkolininkas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta, kodas iš Adresų registro (kai gyvenamoji vieta nenurodyta - -1) | — |
| `tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) | — |
| `isieskojimo_dalykas` | `ref` | [/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas savivaldybę, asmens tipą (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) ir išieškojimo dalyką) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota savivaldybę, asmens tipą ir išieškojimo dalyką) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `tipas` | `"Juridinis asmuo"` | — | — | Kai skolininko tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `tipas` | `"LR juridinis asmuo"` | — | — | Kai skolininko tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai skolininko tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `tipas` | `"Nenustatytas"` | — | — | Kai skolininko tipas kaip asmens tipas nenurodytas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/ja_skolininkai.csv

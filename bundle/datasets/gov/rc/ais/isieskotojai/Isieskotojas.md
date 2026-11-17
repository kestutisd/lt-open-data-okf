---
type: Table
title: "Isieskotojas — Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus"
description: "Spinta table datasets/gov/rc/ais/isieskotojai/Isieskotojas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/isieskotojai/Isieskotojas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/isieskotojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskotojai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Isieskotojas — Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus

- **Model:** `datasets/gov/rc/ais/isieskotojai/Isieskotojas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus](../isieskotojai.md) (`datasets/gov/rc/ais/isieskotojai`)
- **Manifest CSV:** [datasets/gov/rc/ais/isieskotojai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskotojai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/isieskotojai/Isieskotojas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta, kodas iš adresų registro (kai gyvenamoji vieta nenurodyta - -1) | — |
| `isieskojimo_dalykas` | `ref` | [/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) | `4` | `open` | — | Išieškojimo dalyko kodas iš ais išieškojimo dalykų klasifikatoriaus | — |
| `isieskotojo_tipas` | `string` | — | `4` | `open` | — | Išieškojimą inicijavusio asmens tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `skolininko_tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas pagal išieškojimą inicijavusio asmens tipą ir jo savivaldybę, išieškojimo dalyką ir asmens, iš kurio vykdomas išieškojimas, tipą) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal išieškojimą inicijavusio asmens tipą ir jo savivaldybę, išieškojimo dalyką ir asmens, iš kurio vykdomas išieškojimas, tipą) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `isieskotojo_tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `isieskotojo_tipas` | `"Juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `isieskotojo_tipas` | `"LR juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `isieskotojo_tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `isieskotojo_tipas` | `"Nenustatytas"` | — | — | Kai išieškojimą inicijavusio asmens tipas kaip asmens tipas nenurodytas | — |
| `skolininko_tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `skolininko_tipas` | `"Juridinis asmuo"` | — | — | Kai skolininko tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `skolininko_tipas` | `"LR juridinis asmuo"` | — | — | Kai skolininko tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `skolininko_tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai skolininko tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `skolininko_tipas` | `"Nenustatytas"` | — | — | Kai skolininko tipas kaip asmens tipas nenurodytas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/isieskotojai.csv

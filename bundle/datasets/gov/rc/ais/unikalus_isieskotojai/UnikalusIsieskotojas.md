---
type: Table
title: "UnikalusIsieskotojas — Antstolių informacinės sistemos (ais) duomenys apie unikalius skolų išieškotojus"
description: "Spinta table datasets/gov/rc/ais/unikalus_isieskotojai/UnikalusIsieskotojas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/unikalus_isieskotojai/UnikalusIsieskotojas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/unikalus_isieskotojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/unikalus_isieskotojai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# UnikalusIsieskotojas — Antstolių informacinės sistemos (ais) duomenys apie unikalius skolų išieškotojus

- **Model:** `datasets/gov/rc/ais/unikalus_isieskotojai/UnikalusIsieskotojas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (ais) duomenys apie unikalius skolų išieškotojus](../unikalus_isieskotojai.md) (`datasets/gov/rc/ais/unikalus_isieskotojai`)
- **Manifest CSV:** [datasets/gov/rc/ais/unikalus_isieskotojai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/unikalus_isieskotojai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/unikalus_isieskotojai/UnikalusIsieskotojas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `4` | `open` | — | Išieškojimą inicijavusio asmens tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, amžiaus grupė (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų) | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolos išieškotojo (fizinio asmens) gyvenamoji vieta arba registruota skolos išieškotojo (juridinio asmens) buveinė, kodas iš adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Asmenų, inicijavusių bent vieną išieškojimo bylą, kiekis (sugrupuotas pagal asmens tipą ir savivaldybę) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `tipas` | `"Juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `tipas` | `"LR juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai išieškojimą inicijavusio asmens tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `tipas` | `"Nenustatytas"` | — | — | Kai išieškojimą inicijavusio asmens tipas kaip asmens tipas nenurodytas | — |
| `amziaus_grupe` | `"0-24"` | — | — | Kai skolininko amžiaus grupė yra nuo 0 iki 24 metų | — |
| `amziaus_grupe` | `"25-34"` | — | — | Kai skolininko amžiaus grupė yra nuo 25 iki 34 metų | — |
| `amziaus_grupe` | `"35-44"` | — | — | Kai skolininko amžiaus grupė yra nuo 35 iki 44 metų | — |
| `amziaus_grupe` | `"45-54"` | — | — | Kai skolininko amžiaus grupė yra nuo 45 iki 54 metų | — |
| `amziaus_grupe` | `"55-64"` | — | — | Kai skolininko amžiaus grupė yra nuo 55 iki 64 metų | — |
| `amziaus_grupe` | `"65-84"` | — | — | Kai skolininko amžiaus grupė yra nuo 65 iki 84 metų | — |
| `amziaus_grupe` | `"85+"` | — | — | Kai skolininko amžiaus grupė yra 85 ir daugiau metų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/unikalus_isieskotojai.csv

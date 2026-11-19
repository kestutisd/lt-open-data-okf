---
type: Table
title: "VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – II"
description: "AIS duomenys apie antstolių vykdomas bylas – II (pagal skolininkų fizinių ir juridinių asmenų skaičių, amžių, išieškotiną sumą)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_ii/VykdomaByla"
tags: [gov, rc, vykdomabyla, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_ii.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_ii.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2170/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_ii"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VykdomaByla — Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – II

**Dataset Context:** AIS duomenys apie antstolių vykdomas bylas – II (pagal skolininkų fizinių ir juridinių asmenų skaičių, amžių, išieškotiną sumą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie antstolių vykdomas bylas. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/bylos_ii/VykdomaByla`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – II](../bylos_ii.md) (`datasets/gov/rc/ais/bylos_ii`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_ii.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_ii.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_ii/VykdomaByla` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `4` | `open` | — | Skolininko tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Skolininko amžiaus grupė (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų, nenustatyta - kai amžius nenurodytas) | — |
| `bylu_kiekis` | `integer` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuota pagal skolininko tipą ir skolininko amžiaus grupę) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal asmens tipą ir asmens amžiaus grupę) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `tipas` | `"Juridinis asmuo"` | — | — | Kai skolininko tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `tipas` | `"LR juridinis asmuo"` | — | — | Kai skolininko tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai skolininko tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `tipas` | `"Nenustatytas"` | — | — | Kai skolininko tipas kaip asmens tipas nenurodytas | — |
| `amziaus_grupe` | `"0-24"` | — | — | Kai skolininko amžiaus grupė yra nuo 0 iki 24 metų | — |
| `amziaus_grupe` | `"25-34"` | — | — | Kai skolininko amžiaus grupė yra nuo 25 iki 34 metų | — |
| `amziaus_grupe` | `"35-44"` | — | — | Kai skolininko amžiaus grupė yra nuo 35 iki 44 metų | — |
| `amziaus_grupe` | `"45-54"` | — | — | Kai skolininko amžiaus grupė yra nuo 45 iki 54 metų | — |
| `amziaus_grupe` | `"55-64"` | — | — | Kai skolininko amžiaus grupė yra nuo 55 iki 64 metų | — |
| `amziaus_grupe` | `"65-84"` | — | — | Kai skolininko amžiaus grupė yra nuo 65 iki 84 metų | — |
| `amziaus_grupe` | `"85+"` | — | — | Kai skolininko amžiaus grupė yra 85 ir daugiau metų | — |
| `amziaus_grupe` | `"Nenustatyta"` | — | — | Kai skolininko amžiaus grupės amžius nenurodytas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_ii.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_ii.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_ii (https://data.gov.lt/datasets/2170/)

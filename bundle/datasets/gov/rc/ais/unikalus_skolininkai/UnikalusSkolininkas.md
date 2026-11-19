---
type: Table
title: "UnikalusSkolininkas — Antstolių informacinės sistemos (ais) duomenys apie unikalius skolininkus"
description: "AIS esančių unikalių skolininkų duomenys (kai turi užvestą bent vieną ir daugiau vykdomųjų bylų; skolininko tipas, amžius, savivaldybė)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/unikalus_skolininkai/UnikalusSkolininkas"
tags: [gov, rc, unikalusskolininkas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/unikalus_skolininkai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/unikalus_skolininkai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2174/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/unikalus_skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# UnikalusSkolininkas — Antstolių informacinės sistemos (ais) duomenys apie unikalius skolininkus

**Dataset Context:** AIS esančių unikalių skolininkų duomenys (kai turi užvestą bent vieną ir daugiau vykdomųjų bylų; skolininko tipas, amžius, savivaldybė). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolininkus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/unikalus_skolininkai/UnikalusSkolininkas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (ais) duomenys apie unikalius skolininkus](../unikalus_skolininkai.md) (`datasets/gov/rc/ais/unikalus_skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/unikalus_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/unikalus_skolininkai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/unikalus_skolininkai/UnikalusSkolininkas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, amžiaus grupė (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų, nenustatyta - kai amžius nenurodytas) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta, kodas iš adresų registro (kai gyvenamoji vieta nenurodyta - -1) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Asmenų, turinčių bent vieną išieškojimo bylą, kiekis (sugrupuotas pagal asmens tipą ir savivaldybę) | — |

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/unikalus_skolininkai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/unikalus_skolininkai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/unikalus_skolininkai (https://data.gov.lt/datasets/2174/)

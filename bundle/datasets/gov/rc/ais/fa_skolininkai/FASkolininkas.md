---
type: Table
title: "FASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis"
description: "AIS duomenys apie skolininkus fizinius asmenis (pagal gyvenamosios vietos savivaldybes, išieškojimo dalyką, išieškotina sumą, bylų kiekį)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/fa_skolininkai/FASkolininkas"
tags: [gov, rc, faskolininkas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/fa_skolininkai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2172/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/fa_skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# FASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis

**Dataset Context:** AIS duomenys apie skolininkus fizinius asmenis (pagal gyvenamosios vietos savivaldybes, išieškojimo dalyką, išieškotina sumą, bylų kiekį). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolininkus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/fa_skolininkai/FASkolininkas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis](../fa_skolininkai.md) (`datasets/gov/rc/ais/fa_skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/fa_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/fa_skolininkai/FASkolininkas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta, kodas iš Adresų registro (kai gyvenamoji vieta nenurodyta - -1) | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, amžiaus grupė (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų, Nenustatyta - kai amžius nenurodytas) | — |
| `isieskojimo_dalykas` | `ref` | [Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) (`level=4 UUID`: `isieskojimo_dalykas._id`) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas pagal savivaldybę, asmens amžiaus grupę ir išieškojimo dalyką) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal savivaldybę, asmens amžiaus grupę ir išieškojimo dalyką) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/fa_skolininkai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/fa_skolininkai (https://data.gov.lt/datasets/2172/)

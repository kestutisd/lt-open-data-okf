---
type: Table
title: "JASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis"
description: "AIS duomenys apie skolininkus juridinius asmenis (pagal savivaldybes, išieškojimo dalyką, išieškotiną sumą, vykdomųjų bylų skaičių)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/ja_skolininkai/JASkolininkas"
tags: [gov, rc, jaskolininkas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/ja_skolininkai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/ja_skolininkai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2173/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/ja_skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# JASkolininkas — Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis

**Dataset Context:** AIS duomenys apie skolininkus juridinius asmenis (pagal savivaldybes, išieškojimo dalyką, išieškotiną sumą, vykdomųjų bylų skaičių). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolininkus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/ja_skolininkai/JASkolininkas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie skolininkus juridinius asmenis](../ja_skolininkai.md) (`datasets/gov/rc/ais/ja_skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/ja_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/ja_skolininkai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/ja_skolininkai/JASkolininkas` (`deployed`)[^manifest]
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
| `tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) | — |
| `isieskojimo_dalykas` | `ref` | [Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) (`level=4 UUID`: `isieskojimo_dalykas._id`) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas savivaldybę, asmens tipą (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) ir išieškojimo dalyką) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota savivaldybę, asmens tipą ir išieškojimo dalyką) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis asmuo"` | — | — | Kai skolininko tipas fizinis asmuo | — |
| `tipas` | `"Juridinis asmuo"` | — | — | Kai skolininko tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `tipas` | `"LR juridinis asmuo"` | — | — | Kai skolininko tipas lietuvos respublikoje įregistruotas juridinis asmuo | — |
| `tipas` | `"Užsienio juridinis asmuo"` | — | — | Kai skolininko tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `tipas` | `"Nenustatytas"` | — | — | Kai skolininko tipas kaip asmens tipas nenurodytas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/ja_skolininkai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/ja_skolininkai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/ja_skolininkai (https://data.gov.lt/datasets/2173/)

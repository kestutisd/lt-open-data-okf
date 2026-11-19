---
type: Table
title: "Isieskotojas — Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus"
description: "AIS duomenys apie skolų išieškotojus (pagal savivaldybes, išieškojimo dalyką, išieškotiną sumą, vykdomųjų bylų skaičių, skolininkų fizinių ir juridinių asmenų skaičių)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/isieskotojai/Isieskotojas"
tags: [gov, rc, isieskotojas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskotojai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/isieskotojai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2175/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/isieskotojai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Isieskotojas — Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus

**Dataset Context:** AIS duomenys apie skolų išieškotojus (pagal savivaldybes, išieškojimo dalyką, išieškotiną sumą, vykdomųjų bylų skaičių, skolininkų fizinių ir juridinių asmenų skaičių). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolų išieškotojus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/isieskotojai/Isieskotojas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (ais) duomenys apie skolų išieškotojus](../isieskotojai.md) (`datasets/gov/rc/ais/isieskotojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/isieskotojai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskotojai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/isieskotojai/Isieskotojas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta, kodas iš adresų registro (kai gyvenamoji vieta nenurodyta - -1) | — |
| `isieskojimo_dalykas` | `ref` | [Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) (`level=4 UUID`: `isieskojimo_dalykas._id`) | `4` | `open` | — | Išieškojimo dalyko kodas iš ais išieškojimo dalykų klasifikatoriaus | — |
| `isieskotojo_tipas` | `string` | — | `4` | `open` | — | Išieškojimą inicijavusio asmens tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `skolininko_tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (fizinis asmuo - kai fizinis asmuo; juridinis asmuo pats iš savęs (lot. Per se); lr juridinis asmuo; užsienio juridinis asmuo - kai juridinis asmuo; nenustatytas - kai asmens tipas nenurodytas) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas pagal išieškojimą inicijavusio asmens tipą ir jo savivaldybę, išieškojimo dalyką ir asmens, iš kurio vykdomas išieškojimas, tipą) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal išieškojimą inicijavusio asmens tipą ir jo savivaldybę, išieškojimo dalyką ir asmens, iš kurio vykdomas išieškojimas, tipą) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/isieskotojai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskotojai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/isieskotojai (https://data.gov.lt/datasets/2175/)

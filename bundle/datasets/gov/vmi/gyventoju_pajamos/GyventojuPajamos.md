---
type: Table
title: "GyventojuPajamos — Duomenys apie mokėtojo deklaruotas pajamas"
description: "Spinta table datasets/gov/vmi/gyventoju_pajamos/GyventojuPajamos (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gyventoju_pajamos/GyventojuPajamos"
tags: [gov, vmi, gyventojupajamos, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmi/gyventoju_pajamos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1181/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_pajamos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyventojuPajamos — Duomenys apie mokėtojo deklaruotas pajamas

- **Model:** `datasets/gov/vmi/gyventoju_pajamos/GyventojuPajamos`[^manifest]
- **Dataset:** [Gyventojų pajamos](../gyventoju_pajamos.md) (`datasets/gov/vmi/gyventoju_pajamos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/gyventoju_pajamos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_pajamos/GyventojuPajamos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_num` | `integer` | — | `4` | `open` | — | Pajamų kilmės kodo eilės numeris | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `sav_kodas` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `sav_kodas._id`) | `4` | `open` | — | Savivaldybės kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kodas_gpmi` | `string` | — | `4` | `open` | — | GPM klasifikatorius | — |
| `lytis` | `string` | — | `4` | `open` | — | Žmogaus lytis | — |
| `kodas` | `string` | — | `2` | `open` | — | Pajamų kilmės kodas | — |
| `suma` | `number` | — | `2` | `open` | — | Suma | Pritaikyti konfidencialumo metodai: Viršaus perkodavimas (sąlyginių išskirčių vidurkinimas), lokalus reikšmių slėpimas ir atsitiktinis apvalinimas. Jei išskirtis viena - tą išskirtį slepiame į null reikšmę |
| `aprasas` | `string` | — | `3` | `open` | — | Pajamų kilmės aprašas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kodas_gpmi` | `"B"` | — | — | Darbo pajamos ir socialinės išmokos | — |
| `kodas_gpmi` | `"C"` | — | — | Individualios veiklos pajamos | — |
| `kodas_gpmi` | `"D"` | — | — | Turto pajamos | — |
| `kodas_gpmi` | `"E"` | — | — | Palūkanos | — |
| `kodas_gpmi` | `"F"` | — | — | Kitos pajamos | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gyventoju_pajamos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_pajamos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_pajamos (https://data.gov.lt/datasets/1181/)

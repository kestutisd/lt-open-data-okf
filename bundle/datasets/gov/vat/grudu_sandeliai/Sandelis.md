---
type: Table
title: "Sandelis — Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius"
description: "Spinta table datasets/gov/vat/grudu_sandeliai/Sandelis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai/Sandelis"
tags: [gov, vat, sandelis, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1872/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/grudu_sandeliai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Sandelis — Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie...

- **Model:** `datasets/gov/vat/grudu_sandeliai/Sandelis`[^manifest]
- **Dataset:** [Licencijuoti grūdų sandėliai](../grudu_sandeliai.md) (`datasets/gov/vat/grudu_sandeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/grudu_sandeliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai/Sandelis` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `licencijos_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_nr` | `string` | — | `2` | `open` | — | Eilės numeris | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `grudu_rusis_ir_kiekis` | `string` | — | `1` | `open` | — | Grūdų rūšis ir kiekis | — |
| `ukio_subjekto_pav` | `string` | — | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `adresas` | `string` | — | `1` | `open` | — | Ūkio subjekto adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Grūdų sandėlio koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ukio_subjekto_pav` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(base: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas", type: "ref", ref: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/grudu_sandeliai (https://data.gov.lt/datasets/1872/)

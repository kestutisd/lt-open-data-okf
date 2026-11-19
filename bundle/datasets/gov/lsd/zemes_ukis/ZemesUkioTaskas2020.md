---
type: Table
title: "ZemesUkioTaskas2020 — Žemės ūkio surašymo taškiniai duomenys"
description: "Spinta table datasets/gov/lsd/zemes_ukis/ZemesUkioTaskas2020 (30 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ZemesUkioTaskas2020"
tags: [gov, lsd, zemesukiotaskas2020, deployed, level-4, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L62"
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L62"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ZemesUkioTaskas2020 — Žemės ūkio surašymo taškiniai duomenys

- **Model:** `datasets/gov/lsd/zemes_ukis/ZemesUkioTaskas2020`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L62](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L62)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ZemesUkioTaskas2020` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `u_vld_lytis` | `integer` | — | `4` | `open` | — | Ūkio valdytojo lytis (1 – vyras"," 2 – moteris) | — |
| `u_eko` | `integer` | — | `4` | `open` | — | Ekologinis ūkis | — |
| `ukininkavimo_kryptis` | `integer` | — | `4` | `open` | — | Ūkininkavimo kryptis | — |
| `ekonominio_dydzio_klase` | `integer` | — | `4` | `open` | — | Ekonominio dydžio klasė | — |
| `sal_gyv_k` | `integer` | — | `4` | `open` | — | Sąlyginiai gyvūnai | Sąlyginis gyvulių vienetas – standartinis matavimo vienetas"," leidžiantis apibendrinti įvairių rūšių gyvulius"," kad būtų galima juos palyginti |
| `standartine_produkcija_k` | `integer` | — | `4` | `open` | — | Standartinė produkcija | — |
| `f_112_k` | `integer` | — | `4` | `open` | — | Nenaudojamos žemės ūkio naudmenos | — |
| `f_111_k` | `integer` | — | `4` | `open` | — | Naudojamos žemės ūkio naudmenos | — |
| `f_113_k` | `integer` | — | `4` | `open` | — | Miškingi plotai | — |
| `f_116_k` | `integer` | — | `4` | `open` | — | Visas žemės plotas | — |
| `f_115_k` | `integer` | — | `4` | `open` | — | Kita žemė – vandenys"," žemė po pastatais"," keliai"," krūmynai"," pelkės ir kitos ne žemės ūkio naudmenos | — |
| `f_2000_k` | `integer` | — | `4` | `open` | — | Galvijai | — |
| `f_2029_k` | `integer` | — | `4` | `open` | — | Triušiai | — |
| `f_2008_k` | `integer` | — | `4` | `open` | — | Kiaulės | — |
| `f_101_k` | `integer` | — | `4` | `open` | — | Ganyklos ir pievos | — |
| `f_100_k` | `integer` | — | `4` | `open` | — | Ariama žemė | — |
| `f_105_k` | `integer` | — | `4` | `open` | — | Kaulavaisiai | — |
| `f_104_k` | `integer` | — | `4` | `open` | — | Sėklavaisiai | — |
| `f_1037_k` | `integer` | — | `4` | `open` | — | Šiltnamiai | — |
| `f_107_k` | `integer` | — | `4` | `open` | — | Riešutmedžiai | — |
| `f_106_k` | `integer` | — | `4` | `open` | — | Uogynai | — |
| `f_109_k` | `integer` | — | `4` | `open` | — | Kiti daugiamečiai augalai | kiti daugiamečiai augalai"," skirti žmonėms vartoti"," audimui"," pynimui"," energetiniams tikslams"," trumpos rotacijos medžiai naudojamose žemės ūkio naudmenose ir kt. |
| `f_108_k` | `integer` | — | `4` | `open` | — | Medelynai | — |
| `f_2012_k` | `integer` | — | `4` | `open` | — | Avys | — |
| `f_2015_k` | `integer` | — | `4` | `open` | — | Ožkos | — |
| `f_2031_k` | `integer` | — | `4` | `open` | — | Bičių šeimos | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |
| `f_2019_k` | `integer` | — | `4` | `open` | — | Paukščiai | — |
| `f_2018_k` | `integer` | — | `4` | `open` | — | Arkliai | — |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `u_vld_lytis` | `1` | — | — | Vyras | — |
| `u_vld_lytis` | `2` | — | — | Moteris | — |
| `u_eko` | `0` | — | — | Neekologinis | — |
| `u_eko` | `1` | — | — | Ekologinis | — |
| `ukininkavimo_kryptis` | `1` | — | — | Lauko augalai | — |
| `ukininkavimo_kryptis` | `2` | — | — | Daržininkystė | — |
| `ukininkavimo_kryptis` | `3` | — | — | Daugiamečiai augalai | — |
| `ukininkavimo_kryptis` | `4` | — | — | Ganomi gyvuliai | — |
| `ukininkavimo_kryptis` | `5` | — | — | Grūdais šeriami gyvuliai | — |
| `ukininkavimo_kryptis` | `6` | — | — | Mišri augalininkystė | — |
| `ukininkavimo_kryptis` | `7` | — | — | Mišri gyvulininkystė | — |
| `ukininkavimo_kryptis` | `8` | — | — | Mišri augalininkystė ir gyvulininkystė | — |
| `ukininkavimo_kryptis` | `9` | — | — | Nekvalifikuoti ūkiai | — |
| `ekonominio_dydzio_klase` | `1` | — | — | Iki 2000 eur | — |
| `ekonominio_dydzio_klase` | `2` | — | — | 2000 - 4000 eur | — |
| `ekonominio_dydzio_klase` | `3` | — | — | 4000 - 8000 eur | — |
| `ekonominio_dydzio_klase` | `4` | — | — | 8000 - 15000 eur | — |
| `ekonominio_dydzio_klase` | `5` | — | — | 15000 - 25000 eur | — |
| `ekonominio_dydzio_klase` | `6` | — | — | 25000 - 50000 eur | — |
| `ekonominio_dydzio_klase` | `7` | — | — | 50000 - 100000 eur | — |
| `ekonominio_dydzio_klase` | `8` | — | — | 100000 - 250000 eur | — |
| `ekonominio_dydzio_klase` | `9` | — | — | 250000 - 500000 eur | — |
| `ekonominio_dydzio_klase` | `10` | — | — | 500000 - 750000 eur | — |
| `ekonominio_dydzio_klase` | `11` | — | — | 750000 - 1 mln. eur | — |
| `ekonominio_dydzio_klase` | `12` | — | — | 1 mln. - 1.5 mln. eur | — |
| `ekonominio_dydzio_klase` | `13` | — | — | 1.5 mln. - 3 mln. eur | — |
| `ekonominio_dydzio_klase` | `14` | — | — | Daugiau arba 3 mln. eur | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L62 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L62)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis (https://data.gov.lt/datasets/1909/)

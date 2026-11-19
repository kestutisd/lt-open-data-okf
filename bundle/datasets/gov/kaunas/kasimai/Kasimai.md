---
type: Table
title: "Kasimai — Kasimo darbai"
description: "Kauno mieste vykdomi kasimo darbai"
resource: "https://get.data.gov.lt/datasets/gov/kaunas/kasimai/Kasimai"
tags: [gov, kaunas, kasimai, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/kaunas/kasimai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2078/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kaunas/kasimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kasimai — Kasimo darbai

**Dataset Context:** Kauno mieste vykdomi kasimo darbai[^manifest]

- **Model:** `datasets/gov/kaunas/kasimai/Kasimai`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės teikiami duomenys](../kasimai.md) (`datasets/gov/kaunas/kasimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kaunas/kasimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kaunas/kasimai/Kasimai` (`deployed`)[^manifest]
- **Provider:** `kaunas` — Kauno miesto savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | ID | — |
| `pnr` | `integer` | — | `4` | `open` | — | Prašymo nr | — |
| `teikimo_data` | `date` | — | `3` | `open` | — | Prašymo vykdyti kasimo darbus pateikimo data | — |
| `darbai_pradzia` | `date` | — | `3` | `open` | — | Kasimo darbų pradžios data | — |
| `darbai_pabaiga` | `date` | — | `3` | `open` | — | Kasimo darbų pabaigos data | — |
| `adresas` | `string` | — | `2` | `open` | — | Adresas ties kuriuo vykdomi kasimo darbai | — |
| `gat_kodas` | `integer` | — | `2` | `open` | — | Perkasamos gatvės ID | — |
| `namas` | `string` | — | `2` | `open` | — | Namo nr gatvėje, ties kuriuo vykdomi kasimo darbai | — |
| `adresas2` | `string` | — | `2` | `open` | — | Adresas iki kurio vykdomi kasimo darba, jei perkasama daugiau nei ties vienu adresui | — |
| `gat_kodas2` | `integer` | — | `2` | `open` | — | Gatvės kodas, iki kurios vykdomi kasimo darbai, jei perkasama daugiau nei ties vienu adresu | — |
| `namas2` | `string` | — | `2` | `open` | — | Namo nr, iki kurio vykdomi kasimo darbai, jei perkasama daugiau nei ties vienu adresu | — |
| `darbu_tipas` | `string` | — | `2` | `open` | — | Darbų tipas | — |
| `dokumentas` | `string` | — | `2` | `open` | — | Darbus leidžiantis dokumentas | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `planuojami_drb` | `string` | — | `4` | `open` | — | Planuojami darbai | — |
| `danga` | `string` | — | `2` | `open` | — | Perkasama danga | — |
| `statinio_tipas` | `string` | — | `2` | `open` | — | Statinio tipas | — |
| `lnr` | `integer` | — | `4` | `open` | — | Leidimo vykdyti kasimo darbus eil. nr | — |
| `isdavimo_data` | `date` | — | `3` | `open` | — | leidimo vykdyti kasimo darbus išdavimo data | — |
| `galioja_nuo` | `date` | — | `3` | `open` | — | leidimo vykdyti kasimo darbus galiojimo pradžios data | — |
| `galioja_iki` | `date` | — | `3` | `open` | — | leidimo vykdyti kasimo darbus galiojimo pabaigos data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/gatve/Gatve")` | `type` | `4` | `open` | — | — | — |
| `gat_kodas2` | `update(type: "ref", ref: "/datasets/gov/rc/ar/gatve/Gatve")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kaunas/kasimai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kaunas/kasimai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kaunas/kasimai (https://data.gov.lt/datasets/2078/)

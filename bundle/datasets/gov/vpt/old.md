---
type: Dataset
title: "Pirkimų, vykdytų iki 2017-07-01 duomenys ir sutarčių duomenys"
description: "Šioje duomenų bazėje saugomi skelbimai, ataskaitos už pirkimus iki 2017 m. liepos 1 d."
resource: "https://get.data.gov.lt/datasets/gov/vpt/old"
tags: [gov, vpt, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpt/old.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/old"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pirkimų, vykdytų iki 2017-07-01 duomenys ir sutarčių duomenys

- **Namespace:** `datasets/gov/vpt/old`[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/old.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/old` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `44` (44 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/390/`[^dcat]
- **Publisher (`dct:publisher`):** Viešųjų pirkimų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpt/old/:ns`[^dcat]
- **Portal Title (`@lt`):** Pirkimai, vykdyti iki 2017 m. birželio 30 d.[^dcat]
- **Portal Title (`@en`):** Tenders executed until 30th June 2017[^dcat]
- **Issued (`dct:issued`):** `2022-05-12`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2022-05-12` .. `2022-05-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šioje duomenų bazėje saugomi skelbimai, ataskaitos už pirkimus iki 2017 m. liepos 1 d. ir metiniai pirkimų planai iki 2018 m. sausio 1, taip pat visų sutarčių duomenys.[^dcat]

### Portal Description (`@en`)

This database stores ads, purchase reports up to 2017. July 1 and annual procurement plans until 2018. January 1, as well as details of all contracts.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [CpvRysys](old/CpvRysys.md) | — | — | — | — | `6` | — |
| [Salys](old/Salys.md) | — | — | — | — | `7` | — |
| [VptDarbuRusys](old/VptDarbuRusys.md) | — | — | — | — | `3` | — |
| [VptIstatymoStraipsniai](old/VptIstatymoStraipsniai.md) | — | — | — | — | `4` | — |
| [VptIstatymuTipai](old/VptIstatymuTipai.md) | — | — | — | — | `4` | — |
| [VptIstatymuTipai2](old/VptIstatymuTipai2.md) | — | — | — | — | `4` | — |
| [VptNCpcKodai](old/VptNCpcKodai.md) | — | — | — | — | `6` | — |
| [VptNCpcKoduTipai](old/VptNCpcKoduTipai.md) | — | — | — | — | `4` | — |
| [VptNCpvKodaiAdd](old/VptNCpvKodaiAdd.md) | — | — | — | — | `7` | — |
| [VptNCpvKodaiMain](old/VptNCpvKodaiMain.md) | — | — | — | — | `6` | — |
| [VptNCpvKoduTipaiAdd](old/VptNCpvKoduTipaiAdd.md) | — | — | — | — | `4` | — |
| [VptNCpvKoduTipaiMain](old/VptNCpvKoduTipaiMain.md) | — | — | — | — | `5` | — |
| [VptNDarbuTipai](old/VptNDarbuTipai.md) | — | — | — | — | `3` | — |
| [VptNDarbuTipaiVppa](old/VptNDarbuTipaiVppa.md) | — | — | — | — | `3` | — |
| [VptNIstatymoStraipsniai](old/VptNIstatymoStraipsniai.md) | — | — | — | — | `9` | — |
| [VptNIstatymoStraipsniaiCopy](old/VptNIstatymoStraipsniaiCopy.md) | — | — | — | — | `8` | — |
| [VptNNaceKodai](old/VptNNaceKodai.md) | — | — | — | — | `6` | — |
| [VptNNaceKoduTipai](old/VptNNaceKoduTipai.md) | — | — | — | — | `3` | — |
| [VptNNsassKriterijai](old/VptNNsassKriterijai.md) | — | — | — | — | `4` | — |
| [VptNNutsKodai](old/VptNNutsKodai.md) | — | — | — | — | `6` | — |
| [VptNNutsKoduTipai](old/VptNNutsKoduTipai.md) | — | — | — | — | `3` | — |
| [VptNPaslauguTipai](old/VptNPaslauguTipai.md) | — | — | — | — | `3` | — |
| [VptNPirkimoBudai](old/VptNPirkimoBudai.md) | — | — | — | — | `3` | — |
| [VptNPirkimoBudaiSutartims](old/VptNPirkimoBudaiSutartims.md) | — | — | — | — | `4` | — |
| [VptNPirkimoObjektai](old/VptNPirkimoObjektai.md) | — | — | — | — | `4` | — |
| [VptNPirkimoObjektaiVppa](old/VptNPirkimoObjektaiVppa.md) | — | — | — | — | `6` | — |
| [VptNPoTipai](old/VptNPoTipai.md) | — | — | — | — | `4` | — |
| [VptNPoTipaiVppa](old/VptNPoTipaiVppa.md) | — | — | — | — | `6` | — |
| [VptNPrekiuTipai](old/VptNPrekiuTipai.md) | — | — | — | — | `3` | — |
| [VptNSaliuTipaiVppa](old/VptNSaliuTipaiVppa.md) | — | — | — | — | `6` | — |
| [VptNSaliuTipaiVppaTipai](old/VptNSaliuTipaiVppaTipai.md) | — | — | — | — | `3` | — |
| [VptNValiutos](old/VptNValiutos.md) | — | — | — | — | `3` | — |
| [VptNVppaStraipsniai](old/VptNVppaStraipsniai.md) | — | — | — | — | `5` | — |
| [VptN5PoTipai](old/VptN5PoTipai.md) | — | — | — | — | `4` | — |
| [VptN5VpAtaskaitosMazvp](old/VptN5VpAtaskaitosMazvp.md) | — | — | — | — | `36` | — |
| [VptPirkimoBudai](old/VptPirkimoBudai.md) | — | — | — | — | `3` | — |
| [VptPirkimoObjektai](old/VptPirkimoObjektai.md) | — | — | — | — | `7` | — |
| [VptPirkimoObjektoDalys](old/VptPirkimoObjektoDalys.md) | — | — | — | — | `7` | — |
| [VptPirkimoProceduruTipai](old/VptPirkimoProceduruTipai.md) | — | — | — | — | `3` | — |
| [VptPoTipai](old/VptPoTipai.md) | — | — | — | — | `3` | — |
| [VptPrekiuRusys](old/VptPrekiuRusys.md) | — | — | — | — | `3` | — |
| [VptSalis](old/VptSalis.md) | — | — | — | — | `3` | — |
| [VptTDarbuTipai](old/VptTDarbuTipai.md) | — | — | — | — | `3` | — |
| [VptVppStraipsniai](old/VptVppStraipsniai.md) | — | — | — | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `pii` | `https://data.gov.lt/pii/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/old.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/old (https://data.gov.lt/datasets/390/)

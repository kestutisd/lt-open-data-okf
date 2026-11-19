---
type: Dataset
title: "Kiti NTR klasifikatoriai"
description: "Kiti NTR klasifikatoriai (duomenų rinkinių grupė, viso 9 vnt.) (NTR identifikatorių tipų klasifikatorius; NTR objektų adresų formavimo taisyklių klasifikatorius; NTR įsigijimo tipų klasifikatorius; NTR matavimo vienetų klasifikatorius; NTR naudotojų tipų klasifikatorius; NTR..."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1900/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kiti NTR klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `7` (7 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1900/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Kiti NTR klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Other NTR classifications[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2024-05-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kiti NTR klasifikatoriai (duomenų rinkinių grupė, viso 9 vnt.) (NTR identifikatorių tipų klasifikatorius; NTR objektų adresų formavimo taisyklių klasifikatorius; NTR įsigijimo tipų klasifikatorius; NTR matavimo vienetų klasifikatorius; NTR naudotojų tipų klasifikatorius; NTR valiutų klasifikatorius; NTR sandorių tipų klasifikatorius; NTR leistinų sandorių kainų tipų klasifikatorius; NTR registrų tipų klasifikatorius).[^dcat]

### Portal Description (`@en`)

Other NTR classifications (data set group, 9 units in total) (NTR identifier type classification; NTR object address formation rules classification; NTR acquisition type classification; NTR unit classification; NTR user type classification; NTR transaction type classification; Classification of NTR admissible transaction price types; NTR register type classification). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrIdTipas](ntr_kiti_klasifikatoriai/NtrIdTipas.md) | NTR identifikatorių tipai | `4` | `iden_tipas` | — | `4` | — |
| [NtrIsigijimoTipas](ntr_kiti_klasifikatoriai/NtrIsigijimoTipas.md) | NTR įsigijimo tipai | `4` | `isig_tipas` | — | `4` | — |
| [NtrMatavimoVnt](ntr_kiti_klasifikatoriai/NtrMatavimoVnt.md) | NTR matavimo vienetai | `4` | `vien_kodas` | — | `6` | — |
| [NtrNaudotojoTipas](ntr_kiti_klasifikatoriai/NtrNaudotojoTipas.md) | NTR naudotojų tipai | `4` | `naud_tipas` | — | `4` | — |
| [NtrSandorioTipas](ntr_kiti_klasifikatoriai/NtrSandorioTipas.md) | NTR sandorių tipai | `4` | `sant_tipas` | — | `4` | — |
| [NtrKainosTipas](ntr_kiti_klasifikatoriai/NtrKainosTipas.md) | NTR leistini sandorių kainų tipai | `4` | `sant_tipas` | — | `3` | — |
| [NtrRegistroTipas](ntr_kiti_klasifikatoriai/NtrRegistroTipas.md) | NTR registrų tipai | `4` | `regt_tipas` | — | `8` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai (https://data.gov.lt/datasets/1900/)

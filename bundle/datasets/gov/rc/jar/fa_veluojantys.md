---
type: Dataset
title: "Jurdiniai asmenys vėluojantys pateikti finansinės atskaitomybės dokumentus už praėjusius finansinius metus"
description: "Duomenys apie finansinės atskaitomybės dokumentus už praėjusius finansinius metus daugiau nei 60 d."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys"
tags: [gov, rc, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1572/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_veluojantys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Jurdiniai asmenys vėluojantys pateikti finansinės atskaitomybės dokumentus už praėjusius finansinius metus

Duomenys apie finansinės atskaitomybės dokumentus už praėjusius finansinius metus daugiau nei 60 d. vėluojančius pateikti juridinius asmenis[^manifest]

- **Namespace:** `datasets/gov/rc/jar/fa_veluojantys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/fa_veluojantys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1572/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys`[^dcat]
- **Portal Title (`@lt`):** Juridiniai asmenys, vėluojantys pateikti finansinės atskaitomybės dokumentus už praėjusius finansinius metus[^dcat]
- **Portal Title (`@en`):** Legal entities, more than 60 d. late submission of financial statements for the previous financial year[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie juridinius asmenis, vėluojančius pateikti finansinės atskaitomybės dokumentus už praėjusius finansinius metus[^dcat]

### Portal Description (`@en`)

Data on financial reporting documents for the previous financial year more than 60 days. late submission of legal entities Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VeluojantisPateikti](fa_veluojantys/VeluojantisPateikti.md) | Juridinių asmenų registre įregistruoto juridinio asmens kodas | `4` | `juridinis_asmuo` | `open` | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_veluojantys (https://data.gov.lt/datasets/1572/)

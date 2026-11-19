---
type: Dataset
title: "Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos"
description: "Juridinių asmenų registre tvarkomų juridinių asmenų finansinės atskaitomybės dokumentų duomenys iš balanso ataskaitų (apie juridinių asmenų nuosavą kapitalą; apie juridinių asmenų mokėtinas sumas ir kitus įsipareigojimus; apie juridinių asmenų trumpalaikį turtą; apie..."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos"
tags: [gov, rc, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1806/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/balanso_ataskaitos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos

Juridinių asmenų registre tvarkomų juridinių asmenų finansinės atskaitomybės dokumentų duomenys iš balanso ataskaitų (apie juridinių asmenų nuosavą kapitalą; apie juridinių asmenų mokėtinas sumas ir kitus įsipareigojimus; apie juridinių asmenų trumpalaikį turtą; apie juridinių asmenų ilgalaikį turtą) (RAW data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/balanso_ataskaitos`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/balanso_ataskaitos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1806/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos[^dcat]
- **Portal Title (`@en`):** Financial statements submitted by legal entities - balance sheets[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2022-02-03` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Data of financial statements of legal entities maintained in the Register of Legal Entities from balance sheet statements (on equity of legal entities; on payables and other liabilities of legal entities; on current assets of legal entities; on fixed assets of legal entities) (RAW date). The names of individual enterprises, limited partnerships, real partnerships have been depersonalized. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BalansoAtaskaita](balanso_ataskaitos/BalansoAtaskaita.md) | Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos | `4` | `juridinis_asmuo` | `open` | `13` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/balanso_ataskaitos (https://data.gov.lt/datasets/1806/)

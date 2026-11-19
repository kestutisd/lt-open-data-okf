---
type: Dataset
title: "Kraujo produktų užsakymai pacientams"
description: "Duomenų rinkinyje pateikiami nuo 2016 m. informacinėje sistemoje „LabDataLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų kraujo perpylimo procedūrų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rsl/labdatalims"
tags: [gov, rsl, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsl/labdatalims.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rsl/labdatalims.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3853/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rsl/labdatalims"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Kraujo produktų užsakymai pacientams

- **Namespace:** `datasets/gov/rsl/labdatalims`[^manifest]
- **Manifest CSV:** [datasets/gov/rsl/labdatalims.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsl/labdatalims.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsl/labdatalims` (`deployed`)[^manifest]
- **Provider:** `rsl` — VšĮ Respublikinė Šiaulių ligoninė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3853/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rsl/labdatalims`[^dcat]
- **Portal Title (`@lt`):** Kraujo produktų užsakymai pacientams[^dcat]
- **Portal Title (`@en`):** Blood orders for patients[^dcat]
- **Issued (`dct:issued`):** `2025-06-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-06-18` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami nuo 2016 m. informacinėje sistemoje „LabDataLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų kraujo perpylimo procedūrų duomenys. Vienas įrašas atitinka vieną išdavimo įvykio ir išduoto produkto kombinaciją. Duomenų rinkinį sudaro: išdavimo identifikatorius, numeris, užsakymo ir išdavimo datos, recipiento identifikatorius, asmens kodas, lytis bei gimimo metai iš atitinkamų stulpelių bei galiojančių asmens kodų, kraujo grupė, kraujo produkto identifikatorius, grupė, fenotipas, Kelo kodas, komponento kodas bei pavadinimas, minėto produkto tūris, davimo bei galiojimo pabaigos datos ir tiekėjas. Dalyje įrašų kraujo produkto išdavimo data yra ankstesnė už užsakymo, kadangi skubiais atvejais užsakymas fiksuojamas po išdavimo. Pavieniais atvejais to paties kodo kraujo produktų galiojimo laikas ženkliai skiriasi nuo didžiosios dalies atitinkamo kodo produkto, veikiausiai, dėl klaidingai įvestų duomenų. Duomenų teikėjas – VšĮ Respublikinė Šiaulių ligoninė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set provides data on blood transfusion procedures carried out by the National Šiauliai Hospital, which have been collected and updated since 2016 in the information system LabDataLIMS. One entry corresponds to one combination of the issue event and the issued product. The dataset shall comprise: issue identifier, number, order and issue dates, recipient identifier, personal number, sex and year of birth from relevant columns and valid personal numbers, blood group, blood product identifier, group, phenotype, Kelo code, component code and name, volume of the product concerned, dates of delivery and expiry and supplier. In some records, the date of issue of the blood product is earlier than the order, as in urgent cases the order is recorded after issue. In individual cases, the shelf life of blood products of the same code is significantly different from most of the product of the relevant code, probably due to incorrect input. Data provider – National Šiauliai Hospital. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Uzsakymas](labdatalims/Uzsakymas.md) | Kraujo produktų užsakymai pacientams | — | `vda_prime_key` | — | `23` | Duomenų rinkinyje pateikiami nuo 2016 m. informacinėje sistemoje „LabDataLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsl/labdatalims.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsl/labdatalims.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rsl/labdatalims (https://data.gov.lt/datasets/3853/)

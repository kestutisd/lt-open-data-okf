---
type: Dataset
title: "Biocidinių produktų duomenys"
description: "Nacionalinio visuomenės sveikatos centro naudojamoje Biocidinių produktų duomenų bazėje (toliau – BPDB) nuo 1999 m. balandžio 12 d."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2917/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Biocidinių produktų duomenys

Nacionalinio visuomenės sveikatos centro naudojamoje Biocidinių produktų duomenų bazėje (toliau – BPDB) nuo 1999 m. balandžio 12 d. kaupiami duomenys apie biocidinius produktus ir jiems išduotus biocidinių produktų autorizacijos liudijimus. Rinkinys sudarytas iš lentelių „Produktai“, „Produktų veikliosios medžiagos“ ir „Produktų liudijimai“. Svarbu atkreipti dėmesį, kad tai nėra oficialūs statistiniai duomenys, todėl gali būti netikslumų. Duomenų teikėjas – Nacionalinis visuomenės sveikatos centras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lsd/nvsc/bpdb`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2917/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Biocidinių produktų duomenys[^dcat]
- **Portal Title (`@en`):** Data on biocidal products[^dcat]
- **Issued (`dct:issued`):** `2025-01-14`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-10-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Nacionalinio visuomenės sveikatos centro naudojamoje Biocidinių produktų duomenų bazėje (toliau – BPDB) nuo 1999 m. balandžio 12 d. kaupiami duomenys apie biocidinius produktus ir jiems išduotus biocidinių produktų autorizacijos liudijimus. Rinkinys sudarytas iš lentelių „Produktai“, „Produktų veikliosios medžiagos“ ir „Produktų liudijimai“. Svarbu atkreipti dėmesį, kad tai nėra oficialūs statistiniai duomenys, todėl gali būti netikslumų. Duomenų teikėjas – Nacionalinis visuomenės sveikatos centras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Lentelė „Produktai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, pavadinimas, gamintojas, autorizacijos liudijimo sąlygos ir pastabos. Produktų pastabos aktualios tik produktams su galiojančiais autorizacijos liudijimais. Vienas įrašas atitinka vieną produktą. Lentelė „Produktų veikliosios medžiagos“. Lentelę sudaro: negrįžtamai šifruoti produkto ir medžiagos identifikatoriai, medžiagos CAS numeris, pavadinimas ir koncentracija. Vienas įrašas atitinka vieną produkto ir vienos veikliosios medžiagos kombinaciją. Kadangi viename produkte gali būti kelios veikliosios medžiagos, to paties produkto įrašas kartojasi tiek kartų, kiek jame yra veikliųjų medžiagų, ir kiekvienas to paties produkto įrašas atitinka to paties produkto ir skirtingos veikliosios medžiagos kombinaciją. Pvz., jeigu produkte yra 3 veikliosios medžiagos, to paties produkto įrašas kartotis atitinkamai 3 kartus. Lentelė „Produktų liudijimai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, liudijimo numeris, liudijimą gavęs asmuo (liudijimo turėtojas) ir liudijimo išdavimo bei galiojimo pabaigos data. Vienas įrašas atitinka vieną produkto ir liudijimo kombinaciją.[^dcat]

### Portal Description (`@en`)

The Biocidal Products Database (“BPDB”) used by the National Public Health Centre shall, from 12 April 1999, contain data on biocidal products and the authorisations for biocidal products issued to them. The kit consists of tables “Products”, “Product active substances” and “Product certificates”. It is important to note that these are not official statistics, so there may be inaccuracies. The data provider shall be the National Public Health Centre. Contact the atverimas@stat.gov.lt for technical questions or possible errors. Table “Products”. The table consists of: irrevocably encrypted product identifier, name, manufacturer, terms and remarks of the authorization certificate. Product notes are relevant only for products with valid authorization certificates. One entry corresponds to one product. Table “Product active substances”. The table consists of: irrevocably encrypted product and material identifiers, the CAS number, name and concentration of the substance. One entry corresponds to one combination of a product and one active substance. Since a single product may contain several active substances, the entry of the same product shall be repeated as many times as it contains active substances and each entry of the same product shall correspond to the combination of the same product and the different active substance. For example, if the product contains 3 active substances, the entry of the same product shall be repeated 3 times respectively. Table “Product certificates”. The table consists of: irrevocably encrypted product identifier, certificate number, person who received the certificate (certificate holder) and date of issue and expiry of the certificate. One entry corresponds to one combination of product and certificate.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Produktas](bpdb/Produktas.md) | Produktai | `4` | `produkto_id` | — | `5` | Lentelė „Produktai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, pavadinimas, gamintojas, autorizacijos liudijimo sąlygos ir pastabos. |
| [VeikliojiMedziaga](bpdb/VeikliojiMedziaga.md) | Produktų veikliosios medžiagos | `4` | `vda_prime_key` | — | `6` | Lentelė „Produktų veikliosios medžiagos“. |
| [Liudijimas](bpdb/Liudijimas.md) | Produktų liudijimai | `4` | `vda_prime_key` | — | `6` | Lentelė „Produktų liudijimai“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb (https://data.gov.lt/datasets/2917/)

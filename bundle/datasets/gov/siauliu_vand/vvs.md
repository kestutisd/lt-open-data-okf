---
type: Dataset
title: "UAB „Šiaulių vandenys“ sutarčių duomenys"
description: "UAB „Šiaulių vandenys“ naudojamoje Verslo valdymo sistemoje (VVS) nuo 2017 m. kaupiami suteiktų paslaugų sąskaitų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_vand/vvs"
tags: [gov, siauliu_vand, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_vand/vvs.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_vand/vvs"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# UAB „Šiaulių vandenys“ sutarčių duomenys

- **Namespace:** `datasets/gov/siauliu_vand/vvs`[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_vand/vvs.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_vand/vvs` (`deployed`)[^manifest]
- **Provider:** `siauliu_vand` — UAB „Šiaulių vandenys“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2899/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/siauliu_vand/vvs`[^dcat]
- **Portal Title (`@lt`):** UAB „Šiaulių vandenys“ sutarčių duomenys[^dcat]
- **Portal Title (`@en`):** Contract data of UAB “Šiauliai vandenys”[^dcat]
- **Issued (`dct:issued`):** `2024-12-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-12-13` .. `2024-12-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

UAB „Šiaulių vandenys“ naudojamoje Verslo valdymo sistemoje (VVS) nuo 2017 m. kaupiami suteiktų paslaugų sąskaitų duomenys. Duomenų rinkinyje kaupiami sutarčių su klientais duomenys. Rinkinio duomenų aprėptis laike – nuo 1991 m. Duomenų rinkinį sudaro: sutarties identifikatorius, kliento juridinio asmens pavadinimas arba fizinio asmens anonimizuotas vardas ir pavardė, juridinio arba fizinio asmens kodas, asmens rūšis (fizinis / juridinis), sutarties sudarymo, galiojimo pradžios ir pabaigos data, nurodyta, ar tai vandens, ar nuotekų paslaugų sutartis. Vienas įrašas atitinka vieną sutartį. Nors, anot turimų duomenų, VVS duomenys kaupiami nuo 2017 m., rinkiniui sudaryti panaudotuose duomenyse yra datų nuo 1753 m. iki 2122 m. Pirmasis metų skaičius dėl dažnumo laikytas nesančių duomenų atitikmeniu, todėl tų metų datos pakeistos į „null“ reikšmes. Likusios datos apribotos nuo 1991 m. iki šiandienos datos. Duomenų rinkinys sudarytas iš vienkartinio naudojimo duomenų, todėl nėra atnaujinamas. Duomenų teikėjas – UAB „Šiaulių vandenys“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Business Management System (VVS) used by UAB Šiauliai vandenys accumulates data on the service accounts provided from 2017. The dataset collects customer contract data. Collection data coverage in time – from 1991. The dataset consists of: contract identifier, customer legal entity name or anonymised name of natural person, legal or natural person number, type of person (natural/legal), date of conclusion, start and end of contract, whether it is a water or sewage service contract. One entry corresponds to one contract. Although, according to the available data, VMS data has been compiled since 2017, the data used to compile the collection includes dates from 1753 to 2122. The first number of years due to frequency has been considered to be the equivalent of non-existent data, so dates for that year have been changed to “null” values. The remaining dates are limited from 1991 to today's date. The dataset consists of single use data and is therefore not updated. Data provider – UAB Šiauliai vandenys. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](vvs/Sutartis.md) | UAB „Šiaulių vandenys“ sutarčių duomenys | `4` | `id` | — | `9` | UAB „Šiaulių vandenys“ naudojamoje Verslo valdymo sistemoje (VVS) nuo 2017 m. kaupiami suteiktų paslaugų sąskaitų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_vand/vvs.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_vand/vvs (https://data.gov.lt/datasets/2899/)

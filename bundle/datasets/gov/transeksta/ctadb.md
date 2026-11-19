---
type: Dataset
title: "Transporto priemonių techninės apžiūros duomenys"
description: "Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“ centralizuotoji techninės apžiūros duomenų bazė kaupia kelių transporto priemonių techninių apžiūrų (TA) duomenis, vykdomų asocijuotųjų įmonių."
resource: "https://get.data.gov.lt/datasets/gov/transeksta/ctadb"
tags: [gov, transeksta, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/transeksta/ctadb.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2721/"
    title: "data.gov.lt DCAT-AP — datasets/gov/transeksta/ctadb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Transporto priemonių techninės apžiūros duomenys

- **Namespace:** `datasets/gov/transeksta/ctadb`[^manifest]
- **Manifest CSV:** [datasets/gov/transeksta/ctadb.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/transeksta/ctadb` (`deployed`)[^manifest]
- **Provider:** `transeksta` — Lietuvos techninės apžiūros įmonių asociacija „Transeksta“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2721/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/transeksta/ctadb`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių techninės apžiūros duomenys[^dcat]
- **Portal Title (`@en`):** Vehicle roadworthiness test data[^dcat]
- **Issued (`dct:issued`):** `2024-07-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2025-09-20` .. `2026-04-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“ centralizuotoji techninės apžiūros duomenų bazė kaupia kelių transporto priemonių techninių apžiūrų (TA) duomenis, vykdomų asocijuotųjų įmonių. Rinkinyje duomenys teikiami nuo 2015 m., atnaujinami kas savaitę. Duomenų rinkinys apima transporto priemonės (TP) pseudonimizuotus identifikatorius, valstybinį ir VIN (angl. vehicle identification number/liet. transporto priemonės identifikacinis numeris) numerius. Valstybiniui numeriui taip pat įtrauktas stulpelis, nurodantis, kuris neapdoroto valstybinio numerio simbolis atitinka raidę, skaitmenį arba spec. paskirties simbolį. Duomenų rinkinys taip pat apima TP markę, modelį, klasę, kėbulą, ar TP yra specialios paskirties, pagaminimo metus, kuro rūšis, dūmingumą, anglies monoksido taršą tiek prie įprasto, tiek prie padidinto variklio apsukų skaičiaus, ridą (bendrą TP nuvažiuotą atstumą), TA stoties pseudonimizuotą kodą, adreso savivaldybę, bei TA tipą, išvadą, ar TA išlaikyta, TA datą savaitės tikslumu. Duomenų teikėjas – Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The centralised technical inspection database of the Lithuanian Association of Testing Enterprises “TRANSEKSTA” collects technical inspection (TA) data of road vehicles carried out by associated enterprises. The dataset has been reported since 2015 and updated on a weekly basis. The dataset includes vehicle (TP) pseudonymised identifiers, national and VIN (vehicle identification number/Lithuanian vehicle identification number) numbers. The state number also includes a column indicating which unprocessed registration number symbol corresponds to the letter, digit, or special destination symbol. The dataset shall also include the TP mark, model, class, body, whether TP is of special purpose, year of manufacture, fuel type, smoke, carbon monoxide pollution at both the normal and increased engine speed, mileage (total distance travelled by TP), THE pseudonymised code of that station, the municipality of address, and THAT type, the conclusion whether IT has been maintained, THAT date with weekly accuracy.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Apziura](ctadb/Apziura.md) | Transporto priemonių techninės apžiūros duomenys | `4` | `vda_id` | — | `23` | Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“ centralizuotoji techninės apžiūros duomenų bazė kaupia kelių transporto priemonių techninių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/transeksta/ctadb.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/transeksta/ctadb (https://data.gov.lt/datasets/2721/)

---
type: Dataset
title: "Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų leidimui ir skolų valdymui."
description: "Teikiamų paslaugų registras AB „Šiaulių energija“ registre nuo 2017 metų kaupiami teikiamų paslaugų ir jų suvartojamų kiekių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas"
tags: [gov, se, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2886/"
    title: "data.gov.lt DCAT-AP — datasets/gov/se/billingas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų...

- **Namespace:** `datasets/gov/se/billingas`[^manifest]
- **Manifest CSV:** [datasets/gov/se/registras.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas` (`deployed`)[^manifest]
- **Provider:** `se` — AB Šiaulių energija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2886/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/se/billingas`[^dcat]
- **Portal Title (`@lt`):** Teikiamų paslaugų registras ir patalpos[^dcat]
- **Portal Title (`@en`):** Register of Services Provided and Services[^dcat]
- **Issued (`dct:issued`):** `2024-12-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-04` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Teikiamų paslaugų registras AB „Šiaulių energija“ registre nuo 2017 metų kaupiami teikiamų paslaugų ir jų suvartojamų kiekių duomenys. Rinkinyje pateikiamas paslaugos pavadinimas, kategorija, teikiamų paslaugų suvartojimo kiekis ir matavimo vienetas (kWh, m3, m2, vnt. ir kt.), periodo mėnuo ir patalpos ID (referuoja į lentelę „Patalpos“). Patalpos Informacija apie patalpas ir pastatus, kuriuose teikiamos AB „Šiaulių energija“ paslaugos. Rinkinyje nurodytas patalpos plotas, pastato statybos metai, aukštų skaičius, pastato tipas ir paskirtis. Siekiant užtikrinti konfidencialumą, pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes – triukšmą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Register of services provided The register of AB Šiaulių energija accumulates data on the services provided and the quantities consumed by them from 2017. The package includes the service name, category, amount of service consumption and unit of measure (kWh, m3, m2, units, etc.), period month and room ID (referenced to the table “Services”). Premises Information about the premises and buildings where the services of AB Šiaulių energija are provided. The set includes the area of the premises, the year of construction of the building, the number of floors, the type and purpose of the building. In order to ensure confidentiality, the records of the coordinates provided are modified by adding random values such as noise. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Registras](billingas/Registras.md) | Tiekiamų paslaugų registras | `4` | `id` | — | `9` | Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras. |
| [Patalpa](billingas/Patalpa.md) | Patalpos | `4` | `patalpos_id` | — | `10` | Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/se/billingas (https://data.gov.lt/datasets/2886/)

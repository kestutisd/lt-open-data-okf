---
type: Dataset
title: "Kraujo donacijos"
description: "\"Rinkinyje pateikiami duomenys apie atliktas kraujo donacijas, kurie kaupiami Higienos instituto kraujo donorų registre."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos"
tags: [gov, hi, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kraujo donacijos

"Rinkinyje pateikiami duomenys apie atliktas kraujo donacijas, kurie kaupiami Higienos instituto kraujo donorų registre. Duomenų rinkinį sudaro trys lentelės: 1. Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys (atnaujinama kiekvieną dieną); 2. Sėkmingi kraujo donacijos vizitai (atnaujinama kiekvieną dieną); 3. Nesėkmingi kraujo donacijos vizitai (atnaujinama kiekvienų metų kovo 1 dieną); 4. Mėnesinė kraujo donavimo vizitų statistika (atnaujinama kiekvieno mėnesio 15 dieną). Duomenų teikėjas – Higienos institutas. Duomenys kaupiami nuo 2012 m. balandžio 1 d. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/hi/kraujo_donacijos`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3889/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos`[^dcat]
- **Portal Title (`@lt`):** Kraujo donacijos[^dcat]
- **Portal Title (`@en`):** Blood donations[^dcat]
- **Issued (`dct:issued`):** `2025-08-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2025-08-21` .. `2026-04-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie atliktas kraujo donacijas, kurie kaupiami Higienos instituto kraujo donorų registre. Duomenų rinkinį sudaro trys lentelės: 1. Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys (atnaujinama kiekvieną dieną); 2. Sėkmingi kraujo donacijos vizitai (atnaujinama kiekvieną dieną); 3. Nesėkmingi kraujo donacijos vizitai (atnaujinama kiekvienų metų kovo 1 dieną); 4. Mėnesinė kraujo donavimo vizitų statistika (atnaujinama kiekvieno mėnesio 15 dieną). Duomenų teikėjas – Higienos institutas. Duomenys kaupiami nuo 2012 m. balandžio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on blood donations carried out, which are stored in the Register of Blood Donors of the Institute of Hygiene. The dataset consists of three tables: 1. Data of persons wishing to donate blood or blood components (updated daily); 2. Successful blood donation visits (updated daily); 3. Unsuccessful blood donation visits (updated on 1 March each year); 4. Monthly statistics on blood donation visits (updated on 15 th of each month). Data provider – Hygiene Institute. Data shall be collected from 1 April 2012. For technical questions or possible errors, contact the atverimas@stat.gov.lt. ”[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KraujoDonoras](kraujo_donacijos/KraujoDonoras.md) | "Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys" | `4` | `donoro_id` | — | `13` | "Lentelėje pateikiami duomenys apie asmenis, kurie pageidauja duoti kraujo arba kraujo komponentų, surinkti Higienos instituto Kraujo donorų registro... |
| [SekmingaDonoryste](kraujo_donacijos/SekmingaDonoryste.md) | Sėkmingi kraujo donacijos vizitai | — | `vizito_id` | — | `13` | "Lentelėje pateikiami sėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. |
| [NesekmingaDonoryste](kraujo_donacijos/NesekmingaDonoryste.md) | Nesėkmingi kraujo donacijos vizitai | — | `vizito_id` | — | `10` | "Nesėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. |
| [MenesioAtaskaita](kraujo_donacijos/MenesioAtaskaita.md) | Mėnesinė kraujo donavimo vizitų statistika | — | `vda_prime_key` | — | `5` | "Mėnesinė kraujo donavimo vizitų statistika iš Higienos instituto Kraujo donorų registro informacinės sistemos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos (https://data.gov.lt/datasets/3889/)

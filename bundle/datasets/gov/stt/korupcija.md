---
type: Dataset
title: "Gauti pranešimai apie korupciją"
description: "Gauti pranešimai apie korupciją,\"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m."
resource: "https://get.data.gov.lt/datasets/gov/stt/korupcija"
tags: [gov, stt, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/stt/korupcija.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2776/"
    title: "data.gov.lt DCAT-AP — datasets/gov/stt/korupcija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Gauti pranešimai apie korupciją

Gauti pranešimai apie korupciją,"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m. Rinkinio objektas - gautas pranešimas, pateiktas vienu iš galimų būdų: el. paštu, paštu, per e. pristatymo sistemą, mobiliąja programėle, STT tinklalapyje ar atvykus į STT padalinį. Rinkinyje nurodoma informacija apie pranešimą (gavimo data, pateikimo būdas, priskiriama sritis ir sektorius), jį teikusį pranešėją (kategorija, tipas, požymis, ar pranešimas susijęs su pranešėjo darboviete) bei nagrinėjimą (nagrinėjimo tvarka, rezultatai ir galutinis sprendimas). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/stt/korupcija`[^manifest]
- **Manifest CSV:** [datasets/gov/stt/korupcija.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/stt/korupcija` (`deployed`)[^manifest]
- **Provider:** `stt` — Specialiųjų tyrimų tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2776/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/stt/korupcija`[^dcat]
- **Portal Title (`@lt`):** Gauti pranešimai apie korupciją[^dcat]
- **Portal Title (`@en`):** Corruption reports received[^dcat]
- **Issued (`dct:issued`):** `2024-09-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2024-09-05` .. `2026-01-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m. Rinkinio objektas - gautas pranešimas, pateiktas vienu iš galimų būdų: el. paštu, paštu, per e. pristatymo sistemą, mobiliąja programėle, STT tinklalapyje ar atvykus į STT padalinį. Rinkinyje nurodoma informacija apie pranešimą (gavimo data, pateikimo būdas, priskiriama sritis ir sektorius), jį teikusį pranešėją (kategorija, tipas, požymis, ar pranešimas susijęs su pranešėjo darboviete) bei nagrinėjimą (nagrinėjimo tvarka, rezultatai ir galutinis sprendimas). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection shall contain reports of corruption offences submitted to the Special Investigation Service from 2024. The object of the collection shall be the received notification submitted in one possible way: by e-mail, post, e-delivery system, mobile app, STT website or upon arrival at the STT division. The package shall contain information on the notification (date of receipt, method of submission, area and sector attributed), the notifier who submitted it (category, type, indication of whether the notification relates to the job of the notifier) and the examination (examination procedure, results and final decision). Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pranesimas](korupcija/Pranesimas.md) | Gauti pranešimai apie korupciją | `4` | `vda_id` | — | `12` | Gauti pranešimai apie korupciją,"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/stt/korupcija.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/stt/korupcija (https://data.gov.lt/datasets/2776/)

---
type: Dataset
title: "Kenksmingųjų organizmų tyrimai"
description: "Pateikiama informacija apie kenksmingųjų organizmų tyrimų rezultatus per tam tikrą laikotarpį (patikrinimą atlikęs teritorinis padalinys; rajonas (pagal tikrinimo vietą); patikrinimo trukmė (min.); tikrinimo vietos pavadinimas; tikrinimo vietos plotas; tikrinimo vietos ploto..."
resource: "https://get.data.gov.lt/datasets/gov/vat/organizmai"
tags: [gov, vat, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/organizmai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kenksmingųjų organizmų tyrimai

- **Namespace:** `datasets/gov/vat/organizmai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/organizmai` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1862/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/organizmai`[^dcat]
- **Portal Title (`@lt`):** Kenksmingųjų organizmų tyrimai[^dcat]
- **Portal Title (`@en`):** Pest research[^dcat]
- **Issued (`dct:issued`):** `2023-06-13`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-06-13` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie kenksmingųjų organizmų tyrimų rezultatus per tam tikrą laikotarpį (patikrinimą atlikęs teritorinis padalinys; rajonas (pagal tikrinimo vietą); patikrinimo trukmė (min.); tikrinimo vietos pavadinimas; tikrinimo vietos plotas; tikrinimo vietos ploto matavimo vienetai; tikrinamo objekto pavadinimas; tikrinamo objekto veislė; tikrinamo objekto kilmės šalis; tikrinamo objekto patikrintas kiekis; tikrinamo objekto bendras kiekis; tikrinamo objekto kiekio matavimo vienetai; įtariamas kenksmingasis organizmas; paimtas mėginys su požymiais; mėginio tyrimų rezultatai; mėginio paskirtis; kas paimta mėginiui; tiriamo objekto mėginys; mėginio dydis; mėginio dydžio matavimo vienetai). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on the results of pest testing over a period of time (territorial unit that carried out the inspection; district (according to the place of inspection); duration of the inspection (min.); Name of the inspection site; area of the inspection site; variety of the object, country of origin of the object to be inspected, quantity of the object to be inspected, total quantity of the object to be inspected, units of measurement of the quantity of the object to be inspected, sample of the sample taken with signs, purpose of the sample, purpose of the sample, size of the sample units of measurement for the sample size)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Tyrimas](organizmai/Tyrimas.md) | Pateikiama informacija apie kenksmingųjų organizmų tyrimų rezultatus per tam tikrą laikotarpį. | `4` | `id` | `open` | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/organizmai (https://data.gov.lt/datasets/1862/)

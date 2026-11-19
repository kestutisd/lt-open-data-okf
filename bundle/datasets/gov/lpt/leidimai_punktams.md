---
type: Dataset
title: "Lošimo punktų leidimo dokumentai"
description: "Čia galite rasti duomenis apie Lošimų priežiūros tarnybos prie Lietuvos Respublikos finansų ministerijos išduotas ir galiojančius leidimus verstis lošimo automatų salonų veikla (numeris; leidimo turėtojas (bendrovės pavadinimas, kodas, buveinės adresas); leidimo numeris..."
resource: "https://get.data.gov.lt/datasets/gov/lpt/leidimai_punktams"
tags: [gov, lpt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/leidimai_punktams.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lpt/leidimai_punktams.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1773/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lpt/leidimai_punktams"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lošimo punktų leidimo dokumentai

- **Namespace:** `datasets/gov/lpt/leidimai_punktams`[^manifest]
- **Manifest CSV:** [datasets/gov/lpt/leidimai_punktams.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/leidimai_punktams.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/leidimai_punktams` (`deployed`)[^manifest]
- **Provider:** `lpt` — Lošimų priežiūros tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1773/`[^dcat]
- **Publisher (`dct:publisher`):** Lošimų priežiūros tarnyba prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lpt/leidimai_punktams`[^dcat]
- **Portal Title (`@lt`):** Lošimo automatų salonų leidimai[^dcat]
- **Portal Title (`@en`):** Slot machine parlor permits[^dcat]
- **Issued (`dct:issued`):** `2022-01-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-01-24` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Čia galite rasti duomenis apie Lošimų priežiūros tarnybos prie Lietuvos Respublikos finansų ministerijos išduotas ir galiojančius leidimus verstis lošimo automatų salonų veikla (numeris; leidimo turėtojas (bendrovės pavadinimas, kodas, buveinės adresas); leidimo numeris; leidimo išdavimo data ir pagrindas; leidimo pakeitimo ar papildymo numeris; leidimo pakeitimo ar papildymo data ir pagrindas; organizuojamo lošimo rūšis; lošimo vietos adresas; leidžiamų eksploatuoti lošimo įrenginių skaičius; leidimo, leidimo pakeitimo ar papildymo įsigaliojimo data). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Here you can find data on permits issued and valid by the Gambling Supervisory Authority under the Ministry of Finance of Lithuania to engage in the operation of slot machine parlors (number; permit holder (company name, code, registered office address); permit number; date and basis of permit issue; the date and basis for the amendment or supplementation of the permit, the type of gambling organized, the address of the gambling venue, the number of gaming facilities permitted to operate, the effective date of the permit, amendment or supplementation of the permit).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](leidimai_punktams/Dokumentas.md) | Lošimo punktų leidimo dokumentai | `4` | `leidimo_dokumento_id` | — | `15` | Lošimo punktų leidimų dokumentų ir jų istorijos sąrašas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/leidimai_punktams.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/leidimai_punktams.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lpt/leidimai_punktams (https://data.gov.lt/datasets/1773/)

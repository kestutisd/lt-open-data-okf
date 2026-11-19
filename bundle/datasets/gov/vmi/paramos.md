---
type: Dataset
title: "Parama"
description: "Per mokestinį laikotarpį Paramos rėmėjų skirta dalis sumokėto Gyventojų pajamų mokesčio paramai pasirinktam paramos gavėjui ir gavėjui apskaičiuota paramos suma."
resource: "https://get.data.gov.lt/datasets/gov/vmi/paramos"
tags: [gov, vmi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/parama.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1299/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/paramos"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# Parama

- **Namespace:** `datasets/gov/vmi/paramos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/parama.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/paramos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1299/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/paramos`[^dcat]
- **Portal Title (`@lt`):** Parama[^dcat]
- **Portal Title (`@en`):** Data on beneficiaries and political parties[^dcat]
- **Issued (`dct:issued`):** `2022-12-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-03-09`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-12-22` .. `2026-07-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Per mokestinį laikotarpį Paramos rėmėjų skirta dalis sumokėto Gyventojų pajamų mokesčio paramai pasirinktam paramos gavėjui ir gavėjui apskaičiuota paramos suma. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Details of support provided (legal forms of beneficiaries, municipality, county, number of supporters, estimated amounts)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](paramos/Deklaracija.md) | Prašymai pervesti pajamų mokesčio dalį duomenys | `4` | — | — | `11` | Prašymų pervesti pajamų mokesčio dalį vienetams, turintiems teisę gauti paramą, ir (arba) politinėms partijoms duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/parama.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/paramos (https://data.gov.lt/datasets/1299/)

---
type: Dataset
title: "Lygių galimybių kontrolierių tarnyba"
description: "Lygių galimybių tarnybos teikiamų konsultacijų gyvai arba telefonu dėl lygių galimybių pažeidimų registro duomenų rinkinyje pateikiami nuo 2020 m. iki dabar kaupiami duomenys: konsultacijos data (Tiksli – data nurodyta šaltinyje; Nustatyta – šaltinio metų pirma diena, kai..."
resource: "https://get.data.gov.lt/datasets/gov/lgkt"
tags: [gov, lgkt, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/lgkt_konsultacijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lgkt/lgkt_konsultacijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2818/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgkt"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lygių galimybių kontrolierių tarnyba

- **Namespace:** `datasets/gov/lgkt`[^manifest]
- **Manifest CSV:** [datasets/gov/lgkt/lgkt_konsultacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/lgkt_konsultacijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt` (`deployed`)[^manifest]
- **Provider:** `lgkt` — Lygių galimybių kontrolieriaus tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2818/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lgkt/konsultacija`[^dcat]
- **Portal Title (`@lt`):** Lygių galimybių kontrolierių tarnybos konsultacijos telefonu ar gyvai[^dcat]
- **Portal Title (`@en`):** Telephone or live consultations of the Office of Equal Opportunities Ombudspersons[^dcat]
- **Issued (`dct:issued`):** `2024-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-10-02` .. `2024-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lygių galimybių tarnybos teikiamų konsultacijų gyvai arba telefonu dėl lygių galimybių pažeidimų registro duomenų rinkinyje pateikiami nuo 2020 m. iki dabar kaupiami duomenys: konsultacijos data (Tiksli – data nurodyta šaltinyje; Nustatyta – šaltinio metų pirma diena, kai šaltinyje nurodyta netiksli arba visai nenurodyta data), kliento tipas (vyras, moteris ar juridinis asmuo), pagrindas, sritis, pastabos – konsultavimo priežastis, konsultacijos būdas (telefonu arba atvykus į tarnybą), savivaldybė, kurioje asmuo gyvena arba kurioje įvyko pažeidimo veiksmas (pildoma nuo 2023 m.). Duomenys naujinami nebus. Duomenų teikėjas – Lygių galimybių kontrolieriaus tarnyba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set of consultations provided by the Equal Opportunities Authority, either live or by telephone, on infringements of equal opportunities shall include data compiled between 2020 and now: date of consultation (exact date as stated in the source; identified as the first day of the source year, where the source indicates an inaccurate or no date at all), type of client (man, woman or legal person), basis, field, remarks – reason for consultation, method of consultation (telephone or on arrival at the service), municipality where the person lives or where the infringement has taken place (to be completed since 2023). Data will not be updated. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Konsultacija](lgkt/Konsultacija.md) | Lygių galimybių kontrolierių tarnybos konsultacijos telefonu ar gyvai | `4` | `vda_id` | — | `9` | "Lygių galimybių tarnybos gyvų ir konsultacijų telefonu registras. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/lgkt_konsultacijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/lgkt_konsultacijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgkt (https://data.gov.lt/datasets/2818/)

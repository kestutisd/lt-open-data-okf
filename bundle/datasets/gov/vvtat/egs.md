---
type: Dataset
title: "Elektroninėje ginčų platformoje gauti skundai"
description: "Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/egs"
tags: [gov, vvtat, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/egs.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/egs.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2711/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/egs"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Elektroninėje ginčų platformoje gauti skundai

Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m. iki šių dienų. Elektroninė ginčo sprendimo platforma buvo įkurta Europos Komisijos, siekiant užtikrinti lengvesnį ir greitesnį ginčų sprendimą. Platforma leidžia vartotojams patogiai pradėti neteisminio ginčo sprendimo procedūrą internetu. Vartotojas, įsigijęs prekes ar paslaugas internetu Lietuvoje, kitose ES šalyse, Islandijoje, Lichtenšteine ar Norvegijoje, dėl savo pažeistų teisių gynimo turi galimybę teikti skundus per šią platformą. Skundus gavusios įmonės nėra įpareigotos atsakyti į vartotojo kreipimus. Ateityje numatyta, jog EGS sistema bus likviduojama, tad skundų duomenys taps archyviniai.[^manifest]

- **Namespace:** `datasets/gov/vvtat/egs`[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/egs.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/egs.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/egs` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2711/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvtat/egs`[^dcat]
- **Portal Title (`@lt`):** Valstybinės vartotojų teisių apsaugos tarnybos elektroninėje ginčų platformoje gauti skundai[^dcat]
- **Portal Title (`@en`):** Complaints received by the State Consumer Rights Protection Authority on the electronic dispute platform[^dcat]
- **Issued (`dct:issued`):** `2024-07-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-08-01` .. `2026-04-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m. iki šių dienų. Elektroninė ginčo sprendimo platforma buvo įkurta Europos Komisijos, siekiant užtikrinti lengvesnį ir greitesnį ginčų sprendimą. Platforma leidžia vartotojams patogiai pradėti neteisminio ginčo sprendimo procedūrą internetu. Vartotojas, įsigijęs prekes ar paslaugas internetu Lietuvoje, kitose ES šalyse, Islandijoje, Lichtenšteine ar Norvegijoje, dėl savo pažeistų teisių gynimo turi galimybę teikti skundus per šią platformą. Skundus gavusios įmonės nėra įpareigotos atsakyti į vartotojo kreipimus. Ateityje numatyta, jog EGS sistema bus likviduojama, tad skundų duomenys taps archyviniai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package provides data on complaints received by the State Consumer Rights Protection Authority from the Electronic Dispute Resolution Platform (EDS) system from 2015 to the present day. The electronic dispute resolution platform was set up by the European Commission to ensure easier and faster dispute resolution. The platform allows users to conveniently initiate out-of-court dispute resolution online. A consumer who has purchased goods or services online in Lithuania, other EU countries, Iceland, Liechtenstein or Norway has the opportunity to lodge complaints through this platform for the redress of his infringed rights. Undertakings which have received complaints are not obliged to respond to the consumer's requests. In future, the EGS system is expected to be wound up and complaints data will become archived.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skundas](egs/Skundas.md) | VVTAT elektroninėje ginčų platformoje gauti skundai | `4` | `vda_id` | — | `14` | Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/egs.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/egs.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/egs (https://data.gov.lt/datasets/2711/)

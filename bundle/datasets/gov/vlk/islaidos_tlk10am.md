---
type: Dataset
title: "PSDF biudžeto išlaidos asmens sveikatos priežiūros paslaugoms, vaistams ir MPP pagal TLK-10-AM kodus"
description: "Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už suteiktas ambulatorines ar stacionarines asmens sveikatos priežiūros paslaugas pagal TLK-10-AM kodus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am"
tags: [gov, vlk, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1585/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/islaidos_tlk10am"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PSDF biudžeto išlaidos asmens sveikatos priežiūros paslaugoms, vaistams ir MPP pagal TLK-10-AM kodus

- **Namespace:** `datasets/gov/vlk/islaidos_tlk10am`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/islaidos_tlk10am.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `6` (6 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1585/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am`[^dcat]
- **Portal Title (`@lt`):** PSDF biudžeto išlaidos asmens sveikatos priežiūros paslaugoms, vaistams ir MPP pagal TLK-10-AM kodus[^dcat]
- **Portal Title (`@en`):** CHIF budget expenditures for personal health care services according to ICD-10-AM codes[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-30` .. `2023-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie mokamas Privalomojo sveikatos draudimo fondo biudžeto sumas už suteiktas ambulatorines ar stacionarines asmens sveikatos priežiūros paslaugas pagal TLK-10-AM kodus[^dcat]

### Portal Description (`@en`)

CHIF budget expenditure on personal health care services according to ICD-10-AM codes[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Ambulatorija](islaidos_tlk10am/Ambulatorija.md) | PSDF biudžeto išlaidos ambulatorinėms asmens sveikatos priežiūros paslaugoms pagal TLK-10-AM kodus | `4` | — | — | `4` | Informacija apie PSDF biudžeto išlaidas ambulatorinėms asmens sveikatos priežiūros paslaugoms pagal TLK-10-AM kodus |
| [AmbulatorijaKontrastas](islaidos_tlk10am/AmbulatorijaKontrastas.md) | PSDF biudžeto išlaidos už ambulatorinėmis sąlygomis teikiamų brangiųjų tyrimų ir procedūrų kontrastus pagal TLK-10-AM kodus | `4` | — | — | `4` | Informacija apie PSDF biudžeto išlaidas už ambulatorinėmis sąlygomis teikiamų brangiųjų tyrimų ir procedūrų kontrastus pagal TLK-10-AM kodus |
| [StacionarinePaslauga](islaidos_tlk10am/StacionarinePaslauga.md) | PSDF biudžeto išlaidos stacionarinėms (reabilitacijos, slaugos, transplantacijos) sveikatos priežiūros paslaugoms pagal TLK-10-AM kodus | `4` | — | — | `4` | Informacija apie PSDF biudžeto išlaidas stacionarinėms (reabilitacijos, slaugos, transplantacijos) sveikatos priežiūros paslaugoms pagal TLK-10-AM kodus |
| [Aktyvus](islaidos_tlk10am/Aktyvus.md) | PSDF biudžeto išlaidos stacionarinėms aktyviojo gydymo ir dienos chirurgijos paslaugoms pagal TLK-10-AM kodus | `4` | — | — | `4` | Informacija apie PSDF biudžeto išlaidas stacionarinėms aktyviojo gydymo ir dienos chirurgijos paslaugoms pagal TLK-10-AM kodus |
| [SpapIntervencija](islaidos_tlk10am/SpapIntervencija.md) | PSDF biudžeto išlaidos stacionarinėmis sąlygomis teikiamiems brangiesiems tyrimams ir procedūroms | `4` | — | — | `6` | Informacija apie PSDF biudžeto išlaidas stacionarinėmis sąlygomis teikiamus brangiuosius tyrimus ir procedūras pagal TLK-10-AM kodus |
| [Kvap](islaidos_tlk10am/Kvap.md) | PSDF biudžeto išlaidos vaistams ir MPP pagal TLK-10-AM kodus | `4` | — | — | `5` | Informacija apie PSDF biudžeto išlaidas vaistams ir MPP pagal TLK-10-AM kodus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/islaidos_tlk10am (https://data.gov.lt/datasets/1585/)

---
type: Dataset
title: "Lietuvos nacionalinis registras \"Pasaulio atmintis\""
description: "Rinkinyje pateikiami į Lietuvos nacionalinį registrą \"Pasaulio atmintis\" įrašyti dokumentai ir jų kolekcijos nuo 2006m."
resource: "https://get.data.gov.lt/datasets/gov/unesco/registras"
tags: [gov, unesco, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/unesco/registras.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2753/"
    title: "data.gov.lt DCAT-AP — datasets/gov/unesco/registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos nacionalinis registras "Pasaulio atmintis"

Rinkinyje pateikiami į Lietuvos nacionalinį registrą "Pasaulio atmintis" įrašyti dokumentai ir jų kolekcijos nuo 2006m. iki šių dienų. Rinkinio objektas - registro įrašas. Nurodomas dokumento ar kolekcijos eilės numeris, pavadinimas, saugojimo vieta, saugojimo vietos internetinis puslapis (jei egzistuoja). Taip pat pažymima, ar dokumentas yra regioninės ar nacionalinės reikšmės. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/unesco/registras`[^manifest]
- **Manifest CSV:** [datasets/gov/unesco/registras.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/unesco/registras` (`deployed`)[^manifest]
- **Provider:** `unesco` — Lietuvos nacionalinės UNESCO komisijos sekretoriatas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2753/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/unesco/registras`[^dcat]
- **Portal Title (`@lt`):** Lietuvos nacionalinis registras „Pasaulio atmintis“[^dcat]
- **Portal Title (`@en`):** Lithuanian National Register “World Memory”[^dcat]
- **Issued (`dct:issued`):** `2024-08-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-08-20` .. `2026-01-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami į Lietuvos nacionalinį registrą „Pasaulio atmintis“ įrašyti dokumentai ir jų kolekcijos nuo 2006 m. iki šių dienų. Rinkinio objektas – registro įrašas. Rinkinyje nurodomas dokumento ar kolekcijos eilės numeris, pavadinimas, saugojimo vieta, saugojimo vietos interneto puslapis (jei egzistuoja). Taip pat pažymima, ar dokumentas yra regioninės ar nacionalinės reikšmės. Duomenų teikėjas – Lietuvos nacionalinės UNESCO komisijos sekretoriatas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection includes documents entered in the Lithuanian national register “World Remembrance” and their collections from 2006 to the present day. The object of the kit is the registry entry. The collection shall include the serial number, title, storage location, storage site page (if any) of the document or collection. It shall also be noted whether the document is of regional or national significance. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irasas](registras/Irasas.md) | Lietuvos nacionalinis registras "Pasaulio atmintis" | `4` | `vda_id` | — | `6` | Rinkinyje pateikiami į Lietuvos nacionalinį registrą "Pasaulio atmintis" įrašyti dokumentai ir jų kolekcijos nuo 2006m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/unesco/registras.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/unesco/registras.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/unesco/registras (https://data.gov.lt/datasets/2753/)

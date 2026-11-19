---
type: Dataset
title: "Standartų terminų bazė"
description: "Kaupiami šie standartų terminų duomenys: terminas, termino apibrėžtis, terminą patvirtinęs subjektas, atitikmenys kitomis kalbomis, statusas (teiktinas ar neteiktinas taikyti, pasenęs ar pakeistas), termino sukūrimo ir, jei yra, jo pakeitimo data, taikymo sritis (ICS)."
resource: "https://get.data.gov.lt/datasets/gov/lst/terms"
tags: [gov, lst, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/terms"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Standartų terminų bazė

- **Namespace:** `datasets/gov/lst/terms`[^manifest]
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/996/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos standartizacijos departamentas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lst/terms`[^dcat]
- **Portal Title (`@lt`):** Standartų terminų bazė[^dcat]
- **Portal Title (`@en`):** Standard terms database[^dcat]
- **Issued (`dct:issued`):** `2021-09-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-02`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2021-07-30` .. `2026-10-11`[^dcat]

### Portal Description (`@lt`)

Kaupiami šie standartų terminų duomenys: terminas, termino apibrėžtis, terminą patvirtinęs subjektas, atitikmenys kitomis kalbomis, statusas (teiktinas ar neteiktinas taikyti, pasenęs ar pakeistas), termino sukūrimo ir, jei yra, jo pakeitimo data, taikymo sritis (ICS).[^dcat]

### Portal Description (`@en`)

The Standard terms database contains terms and definitions, information on approval, equivalents in other languages, relevance, dates of creation and update (if available), scope (ICS).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Status](terms/Status.md) | — | — | `id` | — | `2` | Tinkamumo kategorija (teiktinas, neteiktinas) |
| [Language](terms/Language.md) | — | — | `id` | — | `3` | Kalbos ir jų dviraidžiai kodai |
| [RelationType](terms/RelationType.md) | — | — | `id` | — | `3` | Sąsajos tipas (sinonimas; susijęs, pakeistas, neteiktinas, pasenęs) |
| [Domain](terms/Domain.md) | — | — | `id` | — | `3` | Sritis pagal Tarptautinę standartų klasifikaciją |
| [RelatedTerm](terms/RelatedTerm.md) | — | — | `term, related_term` | — | `3` | Su terminu susieti kiti terminai ir (arba) sinonimai |
| [Attachment](terms/Attachment.md) | — | — | `id` | — | `4` | Grafiniai priedai (JPG formatu) – paveikslai, formulės |
| [TermDomain](terms/TermDomain.md) | — | — | `term, domain` | — | `2` | Taikymo sritis (standartizacija ir metrologija) |
| [Translation](terms/Translation.md) | — | — | `id` | — | `4` | Termino atitikmenys kitomis kalbomis |
| [Term](terms/Term.md) | — | — | `id` | — | `11` | Termino straipsnis (tinkamumo kategorija, sukirčiuotas terminas, apibrėžtis, pastabos, simbolis, straipsnio nr. standarte, pagrindinis žodis) |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/terms (https://data.gov.lt/datasets/996/)

---
type: Dataset
title: "Lietuvių kalbos vartosenos patarimai"
description: "Rinkinyje pateikti Lietuvių kalbos instituto (LKI) sudaryto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/) 1997–2005 metų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai"
tags: [gov, lki, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2765/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvių kalbos vartosenos patarimai

- **Namespace:** `datasets/gov/lki/lietuviu_kalbos_patarimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2765/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai`[^dcat]
- **Portal Title (`@lt`):** Lietuvių kalbos vartosenos patarimai[^dcat]
- **Portal Title (`@en`):** Lithuanian Language Use Tips[^dcat]
- **Issued (`dct:issued`):** `2024-09-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-08-27` .. `2024-08-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikti Lietuvių kalbos instituto (LKI) sudaryto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/) 1997–2005 metų duomenys. Rinkinį sudaro dvi lentelės: pirmojoje pateikti žmonėms rūpimi klausimai apie taisyklingą lietuvių kalbos vartoseną bei Lietuvių kalbos instituto darbuotojų atsakymai į šiuos klausimus, antrojoje – žmonių pateiktų klausimų esminių žodžių ryšiai su kitais žodžiais. Svarbu paminėti, kad šiuo metu Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas nebepildomas ir nuo 2005 metų perduotas Valstybinei lietuvių kalbos komisijai (VLKK). Taigi, šiuo metu Lietuvoje pagrindinis kalbos konsultacijų šaltinis yra VLKK (https://www.vlkk.lt/konsultacijos). Kadangi kalbos patarimai nuolat atsinaujina, kai kurie LKI kurtame Kalbos konsultacijų banke pateikti atsakymai jau gali būti nebeaktualūs ir nesutampantys su VLKK Kalbos konsultacijų banko atsakymais. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection contains data from THE Computer Bank for Language Advice (https://kkb.lki.lt/) 1997-2005 compiled by the Lithuanian Institute of Language (LKI). The collection consists of two tables: the first contains questions of concern to people about correct use of the Lithuanian language and answers to these questions from the staff of the Lithuanian Language Institute, and the second contains links between the key words of the questions put by people and other words. It is important to mention that the Computer Bank of Language Consultations of the Lithuanian Language Institute is no longer filled in and has been transferred to the State Commission for Lithuanian Language (VLKK) since 2005. Thus, the main source of linguistic consultations in Lithuania is currently VLKK (https://www.vlkk.lt/konsultacijos). As language advice is constantly updated, some of the answers provided by THE Language Advice Bank, which has been created, may no longer be relevant and coincide with THOSE of THE VLKK Language Advice Bank. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KlausimasAtsakymas](lietuviu_kalbos_patarimai/KlausimasAtsakymas.md) | Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Klausimai ir atsakymai. | `4` | `iraso_id` | — | `8` | Lentelėje pateikti klausimai ir atsakymai iš Lietuvių kalbos instituto kurto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/). |
| [ZodisRysys](lietuviu_kalbos_patarimai/ZodisRysys.md) | Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Esminių žodžių ryšiai su kitais žodžiais. | `4` | `iraso_id` | — | `5` | Lentelėje pateikti Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/) esminių žodžių ryšiai su kitais žodžiais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai (https://data.gov.lt/datasets/2765/)

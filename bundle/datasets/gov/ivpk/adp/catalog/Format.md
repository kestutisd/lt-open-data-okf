---
type: Table
title: "Format — Duomenų formatai"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Format (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Format"
tags: [gov, ivpk, format, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L81"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L81"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Format — Duomenų formatai

- **Model:** `datasets/gov/ivpk/adp/catalog/Format`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L81](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L81)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Format` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | Identifikatorius | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | Kada sukurta | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | Kada pakeista | — |
| `version` | `integer` | — | `4` | `open` | — | Keitimo versija | — |
| `extension` | `string` | — | `5` | `open` | `dct:identifier` | Failo plėtinys | Failo plėtinys didžiosiomis raidėmis. |
| `mimetype` | `string` | — | `2` | `open` | `dcat:mediaType` | Formato media tipas | Standartine MIME/Type forma. |
| `rating` | `integer` | — | `4` | `open` | — | Brandos lygis | Duomenų brandos lygis remiantis 5stardata.info skale. |
| `title` | `string` | — | `2` | `open` | `dct:title` | Formato pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rating` | `1` | — | — | Mašininiu būdu nenuskaitomi | — |
| `rating` | `2` | — | — | Nuosavybiniai formatai | — |
| `rating` | `3` | — | — | Atviri formatai | — |
| `rating` | `4` | — | — | Duomenys su identifikatoriais | — |
| `rating` | `5` | — | — | Standartiniai duomenys | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `adms` | `https://www.w3.org/ns/adms#` |
| `dc` | `http://purl.org/dc/elements/1.1/` |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `dct` | `http://purl.org/dc/terms/` |
| `dctype` | `http://purl.org/dc/dcmitype/` |
| `dqv` | `http://www.w3.org/ns/dqv#` |
| `earl` | `http://www.w3.org/ns/earl#` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `geosparql` | `http://www.opengis.net/ont/geosparql#` |
| `locn` | `http://www.w3.org/ns/locn#` |
| `oa` | `http://www.w3.org/ns/oa#` |
| `odrl` | `http://www.w3.org/ns/odrl/2/` |
| `org` | `http://www.w3.org/ns/org#` |
| `owl` | `http://www.w3.org/2002/07/owl#` |
| `prov` | `http://www.w3.org/ns/prov#` |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `sdmx-attribute` | `http://purl.org/linked-data/sdmx/2009/attribute#` |
| `sdo` | `https://schema.org/` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `time` | `http://www.w3.org/2006/time#` |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` |
| `w3cgeo` | `http://www.w3.org/2003/01/geo/wgs84_pos#` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mimetype` | — | — | — | `open` | — | — | Šiuo metu media tipas pateikiamas laisva forma arba visai nepateikiamas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L81 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L81)

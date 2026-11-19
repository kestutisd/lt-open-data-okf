---
type: Table
title: "Dataset"
description: "Spinta table datasets/gov/ivpk/adp/catalog/Dataset (32 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Dataset"
tags: [gov, ivpk, dataset, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L238"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L238"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dataset

- **Model:** `datasets/gov/ivpk/adp/catalog/Dataset`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L238)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/Dataset` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `5` | `open` | `dct:identifier` | — | — |
| `created` | `datetime` | — | `5` | `open` | `dct:created` | — | — |
| `modified` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `catalog` | `ref` | [Catalog](Catalog.md) (`level=4 UUID`: `catalog._id`) | `4` | `open` | — | — | — |
| `description` | `string` | — | `2` | `open` | `dct:description` | — | — |
| `internal_id` | `string` | — | `5` | `open` | `dct:identifier` | Rinkinio ID išoriniame kataloge | — |
| `language` | `string` | — | `2` | `open` | `dct:language` | Kalba kuria pateikti duomenys | Dviejų raidžių kalbos kodai, atskirti kableliais. |
| `licence` | `ref` | [Licence](Licence.md) (`level=2` scalar) | `2` | `open` | `dct:license` | — | — |
| `creator` | `ref` | [Organization](Organization.md) (`level=5 UUID`: `creator._id`) | `5` | `open` | `dct:creator` | — | Duomenų šaltinio autorius |
| `contributor` | `ref` | [Organization](Organization.md) (`level=0` scalar) | `0` | `open` | `dct:contributor` | — | Kiti autoriai prisidėję prie duomenų kūrimo |
| `publisher` | `ref` | [Organization](Organization.md) (`level=0` scalar) | `0` | `open` | `dct:publisher` | — | Duomenų platintojas |
| `priority_score` | `integer` | — | `4` | `open` | — | Prioriteto balas | Prioriteto balas, nuo 1 iki 100. |
| `published` | `datetime` | — | `5` | `open` | `dct:issued` | Kada paskelbta | — |
| `slug` | `string` | — | `4` | `open` | — | — | — |
| `spatial_coverage` | `string` | — | `1` | `open` | `dct:spatial` | — | — |
| `spatial_resolution` | `number` | `m` | `0` | `open` | `dcat:spatialResolutionInMeters` | — | — |
| `status` | `string` | `enum: Status` | `4` | `open` | — | — | — |
| `tags` | `string` | — | `2` | `open` | `dcat:keyword` | Žymės | Atskirtos kableliu. |
| `temporal_coverage` | `string` | — | `2` | `open` | `dct:temporal` | — | — |
| `temporal_resolution` | `ref` | [Frequency](Frequency.md) (`level=0` scalar) | `0` | `open` | `dcat:temporalResolution` | — | — |
| `title` | `string` | — | `4` | `open` | `dct:title` | — | — |
| `uuid` | `string` | — | `4` | `open` | `dct:identifier` | — | — |
| `catalog2` | `ref` | [Catalog](Catalog.md) (`level=4 UUID`: `catalog2._id`) | `4` | `open` | — | — | — |
| `access_rights` | `string` | — | `2` | `open` | `dct:rights` | — | — |
| `category` | `ref` | [Category](Category.md) (`level=4 UUID`: `category._id`) | `4` | `open` | `dcat:theme` | — | — |
| `distribution_conditions` | `string` | — | `1` | `open` | `odrl:hasPolicy` | — | — |
| `description_en` | `string` | — | `5` | `open` | `dct:description` | — | — |
| `last_update` | `datetime` | — | `5` | `open` | `dct:modified` | — | — |
| `title_en` | `string` | — | `5` | `open` | `dct:title` | — | — |
| `structure` | `file` | — | `3` | `open` | — | Struktūra | [Duomenų struktūros aprašas](https://atviriduomenys.readthedocs.io/dsa/index.html). |
| `frequency` | `ref` | [Frequency](Frequency.md) (`level=5 UUID`: `frequency._id`) | `5` | `open` | `dct:accrualPeriodicity` | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `status` | `'INVENTORED'` | — | — | Atlikta inventorizacija | — |
| `status` | `'PRIORITIZED'` | — | — | Numatitas prioritetas | — |
| `status` | `'FINANCING'` | — | — | Skirtas finansavimas | — |
| `status` | `'METADATA'` | — | — | Pateikti metaduomenys | — |
| `status` | `'HAS_DATA'` | — | — | Atverti duomenys | — |

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

# Related References

- [ISO 639 Language Codes Reference](../../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L238 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L238)

---
type: Table
title: "RequestStructure — Pageidaujamos duomenų struktūros laukas"
description: "Teikiant prašymus gauti duomenis yra galimybė pateikti kokių konkrečių duomenų laukų reikia arba trūksta duomenų rinkinyje."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestStructure"
tags: [gov, ivpk, requeststructure, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L201"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L201"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# RequestStructure — Pageidaujamos duomenų struktūros laukas

Teikiant prašymus gauti duomenis yra galimybė pateikti kokių konkrečių duomenų laukų reikia arba trūksta duomenų rinkinyje. Šioje lentelėje saugomi prašomi atverti duomenų laukai.[^manifest]

- **Model:** `datasets/gov/ivpk/adp/catalog/RequestStructure`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L201](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L201)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/RequestStructure` (`deployed`)[^manifest]
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
| `data_notes` | `string` | — | `2` | `open` | `dct:description` | Pastabos | Duomenų struktūros apraše `comment` eilutė. |
| `data_title` | `string` | — | `2` | `open` | — | Duomenų lauko antraštė | Duomenų struktūros apraše `title`. |
| `data_type` | `string` | — | `1` | `open` | — | Duomenų lauko tipas | Duomenų struktūros apraše `type`. |
| `dictionary_title` | `string` | — | `1` | `open` | — | Duomenų kodinis pavadinimas | Duomenų struktūros apraše `model/property` arba `uri`. |
| `request` | `ref` | [Request](Request.md) (`level=4 UUID`: `request._id`) | `4` | `open` | — | Poreikis duomenų rinkiniui | — |

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
| `dictionary_title` | — | `type` | — | `open` | — | — | Nėra susiejim su struktūros aprašu, laisvas tekstas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv#L201 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L201)

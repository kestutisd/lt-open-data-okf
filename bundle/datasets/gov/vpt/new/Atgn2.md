---
type: Table
title: "Atgn2 — Pirkimų ataskaita už mažos vertės viešuosius pirkimus, atliktus gynybos ir saugumo srityje"
description: "Spinta table datasets/gov/vpt/new/Atgn2 (54 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atgn2"
tags: [gov, vpt, atgn2, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L238"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L238"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atgn2 — Pirkimų ataskaita už mažos vertės viešuosius pirkimus, atliktus gynybos ir saugumo srityje

- **Model:** `datasets/gov/vpt/new/Atgn2`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L238)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atgn2` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `title` | `string` | — | `3` | `open` | — | — | — |
| `published_date` | `datetime` | — | `3` | `open` | — | — | — |
| `authority_org_nr` | `string` | — | `3` | `open` | — | — | — |
| `tender_id` | `integer` | — | `3` | `open` | — | — | — |
| `form_name` | `string` | — | `3` | `open` | — | — | — |
| `published` | `integer` | — | `3` | `open` | — | — | — |
| `eps_ref_nr` | `string` | — | `3` | `open` | — | — | — |
| `procurement_type` | `string` | — | `3` | `open` | — | — | — |
| `law_article` | `integer` | — | `3` | `open` | — | — | — |
| `law_paragraph` | `integer` | — | `3` | `open` | — | — | — |
| `law_sub_paragraph` | `integer` | — | `3` | `open` | — | — | — |
| `total_contract_value` | `string` | — | `3` | `open` | — | — | — |
| `procurement_report` | `string` | — | `3` | `open` | — | — | — |
| `reporting_calendar_year` | `string` | — | `3` | `open` | — | — | — |
| `official_name_1` | `string` | — | `3` | `open` | — | — | — |
| `legal_entity_code_1` | `string` | — | `3` | `open` | — | — | — |
| `postal_address_1` | `string` | — | `3` | `open` | — | — | — |
| `town_1` | `string` | — | `3` | `open` | — | — | — |
| `postal_code_1` | `string` | — | `3` | `open` | — | — | — |
| `country_1` | `string` | — | `3` | `open` | — | — | — |
| `url_general_1` | `string` | — | `3` | `open` | — | — | — |
| `url_buyer_1` | `string` | — | `3` | `open` | — | — | — |
| `other_information_1` | `string` | — | `3` | `open` | — | — | — |
| `code_of_contracting_authority_or_entity` | `string` | — | `3` | `open` | — | — | — |
| `is_procurement_power_granted_to_another_authority` | `integer` | — | `3` | `open` | — | — | — |
| `official_name_2` | `string` | — | `3` | `open` | — | — | — |
| `legal_entity_code_2` | `string` | — | `3` | `open` | — | — | — |
| `postal_address_2` | `string` | — | `3` | `open` | — | — | — |
| `town_2` | `string` | — | `3` | `open` | — | — | — |
| `postal_code_2` | `string` | — | `3` | `open` | — | — | — |
| `url_general_2` | `string` | — | `3` | `open` | — | — | — |
| `url_buyer_2` | `string` | — | `3` | `open` | — | — | — |
| `other_information_2` | `string` | — | `3` | `open` | — | — | — |
| `code_of_authorised_organisation` | `string` | — | `3` | `open` | — | — | — |
| `total_value_of_concluded_goods_contracts` | `number` | — | `3` | `open` | — | — | — |
| `total_value_of_concluded_services_contracts` | `number` | — | `3` | `open` | — | — | — |
| `total_value_of_concluded_works_contracts` | `number` | — | `3` | `open` | — | — | — |
| `total_value_of_concluded_contracts` | `number` | — | `3` | `open` | — | — | — |
| `total_number_of_goods_procurements` | `number` | — | `3` | `open` | — | — | — |
| `total_number_of_services_procurements` | `number` | — | `3` | `open` | — | — | — |
| `total_number_of_works_procurements` | `number` | — | `3` | `open` | — | — | — |
| `total_number_of_procurements` | `number` | — | `3` | `open` | — | — | — |
| `secret_number` | `number` | — | `3` | `open` | — | — | — |
| `confidential_number` | `number` | — | `3` | `open` | — | — | — |
| `restricted_number` | `number` | — | `3` | `open` | — | — | — |
| `total_number` | `number` | — | `3` | `open` | — | — | — |
| `secret_value` | `number` | — | `3` | `open` | — | — | — |
| `confidential_value` | `number` | — | `3` | `open` | — | — | — |
| `restricted_value` | `number` | — | `3` | `open` | — | — | — |
| `total_value_` | `number` | — | `3` | `open` | — | — | — |
| `additional_info` | `string` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L238 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L238)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)

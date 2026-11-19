---
type: Table
title: "Atgn1 — AtGn-1 tipinė forma"
description: "Viešojo pirkimo arba pirkimo, atlikto gynybos ir saugumo srityje, procedūrų ataskaita"
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1"
tags: [gov, vpt, atgn1, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atgn1 — AtGn-1 tipinė forma

Viešojo pirkimo arba pirkimo, atlikto gynybos ir saugumo srityje, procedūrų ataskaita[^manifest]

- **Model:** `datasets/gov/vpt/new/Atgn1`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1` (`deployed`)[^manifest]
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
| `procurement_number` | `integer` | — | `3` | `open` | — | — | — |
| `procurement_procedure_number` | `string` | — | `3` | `open` | — | — | — |
| `procurement_object_name` | `string` | — | `3` | `open` | — | — | — |
| `procurement_design_name` | `string` | — | `3` | `open` | — | — | — |
| `design_contest_value` | `string` | — | `3` | `open` | — | — | — |
| `procurement_financed_by_funds` | `integer` | — | `3` | `open` | — | — | — |
| `procurement_financed_by_eu` | `integer` | — | `3` | `open` | — | — | — |
| `project_code` | `string` | — | `3` | `open` | — | — | — |
| `project_name` | `string` | — | `3` | `open` | — | — | — |
| `via_public_procurement_information_system` | `integer` | — | `3` | `open` | — | — | — |
| `carried_out_via_central_system_utilities` | `string` | — | `3` | `open` | — | — | — |
| `carried_out_via_central_system_public` | `string` | — | `3` | `open` | — | — | — |
| `carried_out_via_central_system_reason` | `string` | — | `3` | `open` | — | — | — |
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
| `is_procurement_concluded_to_framework_agreement` | `integer` | — | `3` | `open` | — | — | — |
| `type_of_contract` | `string` | — | `3` | `open` | — | — | — |
| `cpv_main_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_main_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_2` | `string` | — | `3` | `open` | — | — | — |
| `number_of_parts` | `integer` | — | `3` | `open` | — | — | — |
| `type_of_award_procedure` | `string` | — | `3` | `open` | — | — | — |
| `atg_procurement_proc_type_negotiated_wo_publication` | `string` | — | `3` | `open` | — | — | — |
| `atg_utility_proctype_comp_dialogues` | `string` | — | `3` | `open` | — | — | — |
| `procurement_no` | `integer` | — | `3` | `open` | — | — | — |
| `contract_award_criteria` | `string` | — | `3` | `open` | — | — | — |
| `most_economical_advantage` | `string` | — | `3` | `open` | — | — | — |
| `lowest_price` | `string` | — | `3` | `open` | — | — | — |
| `is_claim_submitted` | `integer` | — | `3` | `open` | — | — | — |
| `any_legay_claims` | `integer` | — | `3` | `open` | — | — | — |
| `total_value_of_part_in_framework_agreement` | `number` | — | `3` | `open` | — | — | — |
| `is_procurement_related_to_classified_information` | `integer` | — | `3` | `open` | — | — | — |
| `during_procurement_procedure` | `integer` | — | `3` | `open` | — | — | — |
| `during_contract_performance` | `integer` | — | `3` | `open` | — | — | — |
| `other` | `integer` | — | `3` | `open` | — | — | — |
| `other_information` | `string` | — | `3` | `open` | — | — | — |
| `classified_info_type` | `string` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |
| `country_2` | `string` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.
- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)

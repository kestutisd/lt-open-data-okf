---
type: Table
title: "Atkn1 — Koncesijos suteikimo procedūrų ataskaita"
description: "Spinta table datasets/gov/vpt/new/Atkn1 (44 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1"
tags: [gov, vpt, atkn1, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L294"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L294"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atkn1 — Koncesijos suteikimo procedūrų ataskaita

- **Model:** `datasets/gov/vpt/new/Atkn1`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L294](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L294)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1` (`deployed`)[^manifest]
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
| `concession_number` | `integer` | — | `3` | `open` | — | — | — |
| `title_2` | `string` | — | `3` | `open` | — | — | — |
| `design_contest_value` | `string` | — | `3` | `open` | — | — | — |
| `concession_financed_by_funds` | `integer` | — | `3` | `open` | — | — | — |
| `project_code` | `string` | — | `3` | `open` | — | — | — |
| `project_name` | `string` | — | `3` | `open` | — | — | — |
| `number_of_contracting_authority` | `integer` | — | `3` | `open` | — | — | — |
| `is_concession_power_granted_to_another_authority` | `integer` | — | `3` | `open` | — | — | — |
| `official_name_1` | `string` | — | `3` | `open` | — | — | — |
| `legal_entity_code_1` | `string` | — | `3` | `open` | — | — | — |
| `postal_address_1` | `string` | — | `3` | `open` | — | — | — |
| `town_1` | `string` | — | `3` | `open` | — | — | — |
| `postal_code_1` | `string` | — | `3` | `open` | — | — | — |
| `country_1` | `string` | — | `3` | `open` | — | — | — |
| `url_general_1` | `string` | — | `3` | `open` | — | — | — |
| `other_information_1` | `string` | — | `3` | `open` | — | — | — |
| `type_of_contract` | `string` | — | `3` | `open` | — | — | — |
| `cpv_main_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_main_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_2` | `string` | — | `3` | `open` | — | — | — |
| `number_of_parts` | `integer` | — | `3` | `open` | — | — | — |
| `type_of_award_procedure` | `string` | — | `3` | `open` | — | — | — |
| `atk_proc_type_comp_dialogue_or_award_wo_comp_pub` | `string` | — | `3` | `open` | — | — | — |
| `atk_proc_type_comp_wo_prior_pub` | `string` | — | `3` | `open` | — | — | — |
| `concession_no` | `integer` | — | `3` | `open` | — | — | — |
| `tenderer_excluded` | `integer` | — | `3` | `open` | — | — | — |
| `is_qualification_stipulated` | `integer` | — | `3` | `open` | — | — | — |
| `justification_in_concession` | `string` | — | `3` | `open` | — | — | — |
| `is_claim_submitted` | `integer` | — | `3` | `open` | — | — | — |
| `any_legay_claims` | `integer` | — | `3` | `open` | — | — | — |
| `additional_info` | `string` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.
- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L294 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L294)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)

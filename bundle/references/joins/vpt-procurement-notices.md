---
type: Reference
title: "VPT Public Procurement Notices & Contracts Join Reference"
description: "Canonical join reference for Viešųjų pirkimų tarnyba (vpt/new, vpt/old, vpt/sutartys): Atn1 UUID child joins, CPV division/group normalization, buyer/supplier JAR links, and pre-2015 LTL contract values."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new"
tags: [join, vpt, procurement, cpv, jar]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: vpt-manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv, old.csv & sutartys.csv"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: std-cpv
    resource: "https://publications.europa.eu/resource/celex/32008R0213"
    title: "Commission Regulation (EC) No 213/2008 on the Common Procurement Vocabulary (CPV / BVPŽ)"
    author: "team:eu-publications-office"
    last_modified: "2008-03-15T00:00:00Z"
---

# VPT Public Procurement Notices & Contracts Join Reference

Public procurement data from **Viešųjų pirkimų tarnyba (VPT)** spans three core Spinta datasets — modern CVP IS notices ([datasets/gov/vpt/new](../../datasets/gov/vpt/new.md)), legacy CVP IS notices and lookup tables ([datasets/gov/vpt/old](../../datasets/gov/vpt/old.md)), and contract registries ([datasets/gov/vpt/sutartys](../../datasets/gov/vpt/sutartys.md)).[^vpt-manifest]

## 1. Parent-Child Notice Joins in `datasets/gov/vpt/new`

- **Notice Families (`Atn1`, `Atn2`, `Atn3`, `Atgn1`, `Atgn2`, `Atkn1`):** Each notice form family in [datasets/gov/vpt/new](../../datasets/gov/vpt/new.md) has a parent notice table (such as [vpt/new/Atn1](../../datasets/gov/vpt/new/Atn1.md)) and normalized child list tables (such as [vpt/new/Atn1ContractList](../../datasets/gov/vpt/new/Atn1ContractList.md), [vpt/new/Atn1PartOfObjectPurchaseList](../../datasets/gov/vpt/new/Atn1PartOfObjectPurchaseList.md), `Atn1TendererList`).[^vpt-manifest]
- **`level = 4` UUID Foreign Keys:** Child list tables link back to their parent notice via `type: ref`, `level: 4` columns (`atn1`, `atn2`, `atn3`, `atgn1`, `atkn1`). On `https://get.data.gov.lt`, filter or join using `atn1._id = Atn1._id` rather than raw integer `id`.[^vpt-manifest]

## 2. CPV / BVPŽ Classification Joins

- **Code Normalization:** Procurement columns (`cpv_main_1`, `cpv_codes_1`, [vpt/new/CvpCode](../../datasets/gov/vpt/new/CvpCode.md) `code`, `vpt/old` `acpv_kodas` / `mcpv_kodas`) may store 8-digit codes (`45233120`), 8-digit + check digit (`45233120-6`), or comma/space-separated lists.[^vpt-manifest][^std-cpv]
- **Division & Group Rollups:** Strip any `-Y` check digit (`code[:8]`), then take `code[:2]` (`03`–`98`) for the 45 statutory CPV divisions or `code[:3]` for the 272 CPV groups in [BVPŽ / CPV viešųjų pirkimų kodai](../cpv-bvpz-kodai.md).[^std-cpv]

## 3. Buyer & Supplier JAR Joins and Multi-Year Currency Rules

- **Contracting Authority & Supplier Codes:** Buyer codes (`authority_org_nr`, `legal_entity_code_1`) and supplier codes (`code`, `selected_tenderer`) in VPT notices are `string` columns (`level = 3`) without enforced Spinta `ref` links to `JuridinisAsmuo` because suppliers include foreign companies and natural persons. Filter to 9-digit Lithuanian codes before joining to [JAR Legal Entities](jar-legal-entities.md).[^vpt-manifest]
- **String-Typed Values & Historical LTL Notices:** Several value fields in `vpt/new` (`total_contract_value`, `total_value_of_part`, `value_in_eur`) are typed as `string` in the DSA schema, and legacy `vpt/old` / pre-`2015-01-01` records can contain nominal `LTL` amounts — verify currency metadata and convert `LTL` amounts solely via [Statutory LTL to EUR Currency Conversion](../../computations/ltl-to-eur-conversion.md) (see [Lithuanian Currency History](../lt-valiutos-istorija.md)).[^vpt-manifest]

[^vpt-manifest]: atviriduomenys/manifest — `datasets/gov/vpt/new.csv`, `old.csv`, and `sutartys.csv` (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv)
[^std-cpv]: Commission Regulation (EC) No 213/2008 on the Common Procurement Vocabulary (CPV / BVPŽ) (https://publications.europa.eu/resource/celex/32008R0213)

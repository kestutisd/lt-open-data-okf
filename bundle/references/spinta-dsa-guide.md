---
type: Reference
title: "Spinta DSA & Lithuanian Open Data API Architecture Reference (VSSA & VDA)"
description: "Architectural reference for VSSA get.data.gov.lt Spinta DSA levels 0–5, access tiers, RQL syntax, get_data_gov_lt.in deployment, CSV path traps, and VDA api.dataportal.gov.lt Iceberg endpoints."
resource: "https://atviriduomenys.readthedocs.io/latest/dsa/index.html"
tags: [spinta, dsa, rql, vssa, vda, architecture, reference]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: spinta-dsa
    resource: "https://atviriduomenys.readthedocs.io/latest/dsa/index.html"
    title: "Spinta Dataset Structure Attributes (DSA) Specification (VSSA)"
    author: "team:vssa"
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/tree/ec54998dcea52a0d26dc1c172eacec438d47e727"
    title: "atviriduomenys/manifest — Lithuanian Open Data Spinta DSA Catalog"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/edp/dcat-ap.rdf"
    title: "data.gov.lt DCAT-AP Open Data Portal Metadata Feed (VDA)"
    author: "team:vda"
  - id: dataportal-api
    resource: "https://api.dataportal.gov.lt/openapi.json"
    title: "VDA State Data Lakehouse Analytical API OpenAPI 3.0.4 Specification"
    author: "team:vda"
  - id: dataportal-ns
    resource: "https://api.dataportal.gov.lt/namespaces"
    title: "VDA State Data Lakehouse Live Namespace Directory (GET /namespaces)"
    author: "team:vda"
---

# Spinta DSA & Lithuanian Open Data API Architecture Reference (VSSA & VDA)

> **Unofficial / Unverified Bundle Notice:** This OKF v0.3 knowledge bundle is generated deterministically from public `atviriduomenys/manifest` DSA CSV schemas, `data.gov.lt` DCAT-AP metadata, and EU/ISO statutory acts. Neither **Valstybės skaitmeninių sprendimų agentūra (VSSA)** nor **Valstybės duomenų agentūra (VDA)** has reviewed this bundle (`0` `human:` verifications; inferred `trust_tier = "unverified"`).[^manifest][^spinta-dsa]

## 1. Two Distinct Lithuanian Open Data APIs (`get.data.gov.lt` vs `api.dataportal.gov.lt`)

Lithuanian open data is cataloged on `data.gov.lt` (DCAT-AP RDF)[^dcat] and served across two technically distinct public API platforms (**Lietuvos atvirų duomenų ekosistemoje veikia du techniškai skirtingi API sluoksniai**):[^spinta-dsa][^dataportal-api]

1. **VSSA Spinta REST API (`https://get.data.gov.lt/<dataset>/<Model>`):**
   - Operated by **Valstybės skaitmeninių sprendimų agentūra (VSSA)** (formerly *Informacinės visuomenės plėtros komitetas* — historical namespace code `ivpk`).[^manifest][^spinta-dsa]
   - Every record carries a Spinta-generated UUID `_id` and revision hash `_revision`. Supports JSON (`.json`), JSONL, CSV (`.csv`), and RDF outputs plus Spinta RQL filtering.[^spinta-dsa]
2. **VDA Analytical Lakehouse API (`https://api.dataportal.gov.lt`):**
   - Operated by **Valstybės duomenų agentūra (VDA)** (formerly *Lietuvos statistikos departamentas* — namespace code `lsd`), exposing Apache Iceberg tables via `GET /namespaces/{namespace}/tables/{tableName}/schema` and `POST /namespaces/{namespace}/tables/{tableName}/query`.[^dataportal-api]
   - **9-Digit JAR Namespace & `_id` Incompatibility:** Calling `GET https://api.dataportal.gov.lt/namespaces` returns **9-digit publisher JAR codes** as `{namespace}` (e.g., `188659752`) and `snake_case` `{tableName}` identifiers, with flattened scalar foreign keys and 20-digit integer `_id` values. **Never join `api.dataportal.gov.lt` integer `_id` values to `get.data.gov.lt` UUID `_id` values.**[^dataportal-api][^dataportal-ns]

## 2. Spinta DSA Maturity Levels (`level` `0`–`5`) & Foreign-Key Serialization

On `https://get.data.gov.lt`, how a `ref` foreign-key column serializes in JSON and CSV responses depends strictly on the property's **DSA maturity `level`** — **even when `TargetModel[field]` is written in the manifest CSV**:[^spinta-dsa]

| DSA `level` | Meaning (LT / EN) | `get.data.gov.lt` JSON / CSV Serialization | Join Rule |
| --- | --- | --- | --- |
| `5` | Semantinė sąveika / Semantic linked data | `{"_id": "<UUID>"}` / `<col>._id` | Join via `<col>._id = Target._id` (same UUID mechanism as `level=4`).[^spinta-dsa] |
| `4` | Susieti duomenys / Linked internal `Ref` | `{"_id": "<UUID>"}` / `<col>._id` | **Two-step UUID join:** resolve target `_id` first (e.g., [datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo.md) -> [datasets/gov/vmi/ja_mokesciai/Moketojas](../datasets/gov/vmi/ja_mokesciai/Moketojas.md)).[^spinta-dsa] |
| `3` | Identifikatoriai (`ExternalRef`) | `{"<pk>": "..."}` / `<col>.<pk>` | Join directly on the declared natural primary key `<col>.<pk> = Target.<pk>`.[^spinta-dsa] |
| `2` | Vienodos reikšmės ir vienetai / Standardized values | Scalar value | Unlinked scalar key; normalize types/padding and do not assume enforced FK integrity.[^spinta-dsa] |
| `1` | Pirminė struktūra / Raw source dump | Scalar value | Raw source field without standardized units or referential integrity.[^spinta-dsa] |
| `0` | Projektas / Draft schema (`status: draft`) | Unpublished / draft | Preliminary schema design (`status: draft` in OKF frontmatter).[^spinta-dsa] |

## 3. Spinta `access` Tiers (Open Data vs Restricted Columns)

In Spinta DSA, **`public` does NOT mean unrestricted open data**:[^spinta-dsa]
- **`open`:** True open data available anonymously without authorization or purpose restrictions (`get.data.gov.lt` serves `open` columns anonymously).[^spinta-dsa]
- **`public`:** Restricted to authorized recipients bound by terms of use and GDPR *purpose limitation* (*tikslo apribojimas*).[^spinta-dsa]
- **`protected`:** Inter-institutional system-to-system exchange only (omitted from anonymous API responses).[^spinta-dsa]
- **`private`:** Internal system use only (omitted from anonymous API responses).[^spinta-dsa]
- **`(inherited)` vs `—`:** Higher dimensions (`dataset`, `model`) frequently leave `access` blank in CSV rows while properties declare `open`, or properties inherit `access` from their parent `model` / `resource` / `dataset`.[^manifest][^spinta-dsa]

## 4. Spinta RQL Query Syntax (`get.data.gov.lt`)

- **Functions:** `?limit(20)`, `?select(_id,ja_kodas,ja_pavadinimas)`, `?sort(ja_kodas)`, `?sort(-reg_data)`.[^spinta-dsa]
- **Filtering:** `?ja_kodas=188659752`, `?metai>=2024&menuo=12`, `?mm_kodas._id="<UUID>"`.[^spinta-dsa]
- **Pagination Trap:** Spinta uses cursor tokens via `_page.next` (`?page("<token>")`). Passing unknown `key=value` query parameters such as `?page=1` or `?offset=10` is parsed as a column equality filter and fails with `HTTP 400 PropertyNotFound`.[^spinta-dsa]

## 5. Saugykla Deployment (`get_data_gov_lt.in`) & Path-vs-Namespace Trap

1. **Active Deployment (`get_data_gov_lt.in`):** Out of `1100` CSV schemas in `atviriduomenys/manifest`, `988` are listed in `get_data_gov_lt.in` (deployed on `get.data.gov.lt`, carrying `resource:` and tag `deployed`), while `112` are schema-only or externally hosted (e.g., [datasets/gov/regitra/jtp/TransportoPriemone](../datasets/gov/regitra/jtp/TransportoPriemone.md) — returning `HTTP 404` on `get.data.gov.lt`, omitting frontmatter `resource:`, and tagged `undeployed`).[^manifest]
2. **CSV Path vs Declared `dataset` Namespace (`~14%`):** `151` of `1100` CSV files declare an internal `dataset` namespace that differs from the CSV filename (for example, `datasets/gov/vmi/ja_sumoketi_mokesciai.csv` declares `datasets/gov/vmi/ja_mokesciai`), `4` CSV files define multiple datasets, and upstream namespace typos such as [datasasets/gov/ivpk/svetainiu_atitikties_vertinimas](../datasasets/gov/ivpk/svetainiu_atitikties_vertinimas.md) (`[sic]`) must be preserved verbatim to match Spinta paths.[^manifest]

## 6. Cross-Register Join & Classification References in This Bundle

- **Legal Entities (JAR):** [JAR Legal Entities Join Reference](joins/jar-legal-entities.md)
- **Address Hierarchy & LKS-94 Geometry (AR):** [AR Address Hierarchy & LKS-94 Reference](joins/ar-address-hierarchy.md)
- **Public Procurement (VPT & CPV):** [VPT Procurement Notices Join Reference](joins/vpt-procurement-notices.md) & [CPV / BVPŽ Vocabulary](cpv-bvpz-kodai.md)
- **Economic Activities (EVRK 2 vs 2025-01-01 EVRK 2.1):** [EVRK 2 / NACE Rev. 2 & EVRK 2.1 Reference](evrk-nace-sekcijos.md)
- **Languages (ISO 639):** [ISO 639 Language Codes](iso-639-kalbu-kodai.md)
- **Currency History & Sanctioned Conversion:** [Lithuanian Currency History (1 EUR = 3.45280 LTL)](lt-valiutos-istorija.md) & [Statutory LTL to EUR Currency Conversion](../computations/ltl-to-eur-conversion.md)

[^spinta-dsa]: Spinta Dataset Structure Attributes (DSA) Specification (VSSA) (https://atviriduomenys.readthedocs.io/latest/dsa/index.html)
[^manifest]: atviriduomenys/manifest — Lithuanian Open Data Spinta DSA Catalog (https://github.com/atviriduomenys/manifest/tree/ec54998dcea52a0d26dc1c172eacec438d47e727)
[^dcat]: data.gov.lt DCAT-AP Open Data Portal Metadata Feed (VDA) (https://data.gov.lt/edp/dcat-ap.rdf)
[^dataportal-api]: VDA State Data Lakehouse Analytical API OpenAPI 3.0.4 Specification (https://api.dataportal.gov.lt/openapi.json)
[^dataportal-ns]: VDA State Data Lakehouse Live Namespace Directory (https://api.dataportal.gov.lt/namespaces)

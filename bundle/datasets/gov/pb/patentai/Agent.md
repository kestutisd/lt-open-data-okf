---
type: Table
title: "Agent"
description: "Spinta table datasets/gov/pb/patentai/Agent (2 columns)."
tags: [gov, pb, agent, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L59"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L59"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Agent

- **Model:** `datasets/gov/pb/patentai/Agent`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L59)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sequence`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sequence` | `integer` | — | `3` | `open` | — | Atstovo numeris | — |
| `rep_type` | `string` | — | `3` | `open` | — | Atstovo tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L59 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L59)

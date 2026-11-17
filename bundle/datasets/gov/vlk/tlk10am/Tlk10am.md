---
type: Table
title: "Tlk10am — Ligų sąrašas (TLK-10-AM)"
description: "Ligų klasifikacija."
resource: "https://get.data.gov.lt/datasets/gov/vlk/tlk10am/Tlk10am"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/tlk10am.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/tlk10am.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tlk10am — Ligų sąrašas (TLK-10-AM)

Ligų klasifikacija. TLK-10-AM – Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos modifikacija (TLK-10-AM) – Sisteminis ligų sąrašas

- **Model:** `datasets/gov/vlk/tlk10am/Tlk10am`[^manifest]
- **Dataset:** [datasets/gov/vlk/tlk10am](../tlk10am.md) (`datasets/gov/vlk/tlk10am`)
- **Manifest CSV:** [datasets/gov/vlk/tlk10am.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/tlk10am.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/tlk10am/Tlk10am`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `code` | `string` | — | `4` | `open` | — | — | Diagnozės kodas pagal tarptautinę statistinę ligų ir sveikatos sutrikimų klasifikaciją, dešimtąjį leidimą, Australijos modifikaciją (TLK-10-AM) |
| `tlk10amcode` | `string` | — | `4` | `open` | — | — | Diagnozės kodas pagal tarptautinę statistinę ligų ir sveikatos sutrikimų klasifikaciją, dešimtąjį leidimą, Australijos modifikaciją (TLK-10-AM) |
| `name` | `string` | — | `4` | `open` | — | — | Diagnozės pavadinimas pagal tarptautinę statistinę ligų ir sveikatos sutrikimų klasifikaciją, dešimtąjį leidimą, Australijos modifikaciją (TLK-10-AM) |
| `section_code` | `string` | — | `2` | `open` | — | — | Diagnozės kodų poskyrio grupės |
| `section_name` | `string` | — | `2` | `open` | — | — | Diagnozės kodų poskyrio pavadinimas |
| `chapter_code` | `string` | — | `2` | `open` | — | — | Skyriui priklausanti kodų grupė |
| `chapter_name` | `string` | — | `2` | `open` | — | — | Skyriaus pavadinimas |
| `valid_from` | `date` | — | `4` | `open` | — | — | Diagnozės kodo galiojimo pradžios data |
| `valid_to` | `date` | — | `4` | `open` | — | — | Diagnozės kodo galiojimo pabaigos data |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `section_code` | `create(property: "section", type: "ref", ref: "Section")` | `property` | `4` | `open` | — | — | — |
| `section_code` | `update(property: "section.code", type: "")` | `property` | `4` | `open` | — | — | — |
| `section_name` | `update(property: "section.name", type: "")` | `property` | `4` | `open` | — | — | — |
| `chapter_code` | `create(property: "chapter", type: "ref", ref: "Chapter")` | `property` | `4` | `open` | — | — | — |
| `chapter_code` | `update(property: "chapter.code", type: "")` | `property` | `4` | `open` | — | — | — |
| `chapter_name` | `update(property: "chapter.name", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/tlk10am.csv

---
type: Table
title: "PurchaseContract — Projekto pirkimo plano pirkimo sutartis"
description: "Spinta table datasets/gov/finmin/sutartys/PurchaseContract (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseContract"
tags: [gov, finmin, purchasecontract, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L415"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L415"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PurchaseContract — Projekto pirkimo plano pirkimo sutartis

- **Model:** `datasets/gov/finmin/sutartys/PurchaseContract`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L415](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L415)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseContract` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `purchase_contract_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_contract_id` | `string` | — | `4` | `open` | — | Pirkimo sutarties identifikatorius | — |
| `purchase` | `ref` | [Purchase](Purchase.md) (`level=4 UUID`: `purchase._id`) | `4` | `open` | — | Pirkimo identifikatorius | — |
| `sfmis_no` | `string` | — | `4` | `open` | — | SFMIS sutarties numeris | — |
| `submitted` | `date` | `D` | `4` | `open` | — | Pateikimo ĮI data | — |
| `state` | `string` | — | `3` | `open` | — | Būsena | — |
| `purchase_no` | `string` | — | `4` | `open` | — | Pirkimo numeris | — |
| `when` | `date` | `D` | `4` | `open` | — | Pirkimo sutarties data | — |
| `amount` | `number` | — | `2` | `open` | — | Pirkimo sutarties suma, susijusi su projektu | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `expense` | `number` | — | `2` | `open` | — | Tinkamų finansuoti išlaidų suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `supplier` | `string` | — | `2` | `open` | — | Tiekėjo pavadinimas | Fiziniams ir panašiems asmenims vertės pašalintos |
| `supplier_code` | `string` | — | `2` | `open` | — | Tiekėjo JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `deadline` | `date` | `D` | `4` | `open` | — | Pirkimo sutarties įvykdymo termino pabaigos data | — |
| `ext` | `boolean` | — | `4` | `open` | — | Sutarties pratęsimo galimybė | — |
| `verbal` | `boolean` | — | `4` | `open` | — | Požymis, ar žodinė sutartis | — |
| `end_purchase` | `string` | — | `2` | `open` | — | Požymis, ar pirkimas baigtas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L415 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L415)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

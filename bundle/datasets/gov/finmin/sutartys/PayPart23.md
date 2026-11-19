---
type: Table
title: "PayPart23 — Projekto mokėjimo prašymo dalis Nr. 2 arba Nr. 3"
description: "Spinta table datasets/gov/finmin/sutartys/PayPart23 (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayPart23"
tags: [gov, finmin, paypart23, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L177"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L177"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayPart23 — Projekto mokėjimo prašymo dalis Nr. 2 arba Nr. 3

- **Model:** `datasets/gov/finmin/sutartys/PayPart23`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L177](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L177)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayPart23` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_part23_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_part23_id` | `string` | — | `4` | `open` | — | Mokėjimo prašymo dalies identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) (`level=4 UUID`: `payment._id`) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `number` | `string` | — | `3` | `open` | — | Mokėjimo prašymo dalies numeris – MPD2/MPD3 | — |
| `state` | `string` | — | `3` | `open` | — | MPD2/MPD3 būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | MPD2/MPD3 būsenos data | — |
| `state_decided` | `date` | `D` | `4` | `open` | — | MPD2/MPD3 būsenos sprendimo data | — |
| `paid_decided` | `date` | `D` | `4` | `open` | — | MPD2/MPD3 būsenos „Apmokėta“ sprendimo data | — |
| `method` | `string` | — | `3` | `open` | — | MPD2/MPD3 apmokėjimo būdas | — |
| `request_amount` | `number` | — | `2` | `open` | — | MPD2/MPD3 prašoma suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `confirm_amount` | `number` | — | `2` | `open` | — | MPD2/MPD3 patvirtinta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `fin` | `number` | — | `2` | `open` | — | MPD2/MPD3 finansavimas | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `paid_fin` | `number` | — | `2` | `open` | — | MPD2/MPD3 AV išmokamas finansavimas | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `declare_by` | `date` | `D` | `4` | `open` | — | MPD2/MPD3 deklaruotinumo EK data | — |
| `declare_amount` | `number` | — | `2` | `open` | — | MPD2/MPD3 deklaruotina suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `declared_amount` | `number` | — | `2` | `open` | — | MPD2/MPD3 deklaruota suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |
| `paid_amount` | `number` | — | `2` | `open` | — | MPD2/MPD3 apmokėta suma | Sumai konfidencialumo tikslais pridėta triukšmo, sudarančio iki 33 % sumos. Triukšmo koeficientas vienodas visiems to paties projekto duomenims |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `request_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `confirm_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `fin` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paid_fin` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `declare_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `declared_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paid_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L177 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L177)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

---
type: Table
title: "IrStatistika — Įgaliojimų registro statistika"
description: "Spinta table datasets/gov/rc/ir/statistika/IrStatistika (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/statistika/IrStatistika"
tags: [gov, rc, irstatistika, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/statistika.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/statistika.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2166/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/statistika"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IrStatistika — Įgaliojimų registro statistika

- **Model:** `datasets/gov/rc/ir/statistika/IrStatistika`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) statistika](../statistika.md) (`datasets/gov/rc/ir/statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/statistika.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/statistika.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/statistika/IrStatistika` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais užregistruotas (arba baigia galioti) įgaliojimas | — |
| `ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis, kurį užregistruotas (arba baigia galioti) įgaliojimas | — |
| `ireg_ntpi_igaliojimu_kiekis` | `integer` | — | `3` | `open` | — | Įgaliojimų, kuriuos registravo notarai, konsuliniai pareigūnai ir CK 2.138 str. 2 dalyje nurodyti asmenys, kiekis per ketvirtį | — |
| `isreg_ntpi_igaliojimu_kiekis` | `integer` | — | `3` | `open` | — | Baigusių galioti įgaliojimų, kuriuos registravo notarai, konsuliniai pareigūnai ir CK 2.138 str. 2 dalyje nurodyti asmenys, kiekis per ketvirtį | — |
| `ireg_itpsi_igaliojimu_kiekis` | `string` | — | `3` | `open` | — | Įgaliojimų, kurie registruoti savitarnos portale, kiekis per ketvirtį | — |
| `isreg_itpsi_igaliojimu_kiekis` | `string` | — | `3` | `open` | — | Baigusių galioti įgaliojimų, kurie registruoti savitarnos portale, kiekis per ketvirtį | — |
| `igaliotojas_fa_kiekis` | `integer` | — | `3` | `open` | — | Įgaliotojų fizinių asmenų kiekis | — |
| `igaliotojas_ja_kiekis` | `integer` | — | `3` | `open` | — | Įgaliotojų juridinių asmenų kiekis | — |
| `igaliotojas_perse_kiekis` | `string` | — | `3` | `open` | — | Įgaliotojų juridinių asmenų pats iš savęs (lot. Per se) kiekis | — |
| `igaliotasis_fa_kiekis` | `integer` | — | `3` | `open` | — | Įgaliotų fizinių asmenų kiekis | — |
| `igaliotasis_ja_kiekis` | `integer` | — | `3` | `open` | — | Įgaliotų juridinių asmenų kiekis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/statistika.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/statistika.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/statistika (https://data.gov.lt/datasets/2166/)

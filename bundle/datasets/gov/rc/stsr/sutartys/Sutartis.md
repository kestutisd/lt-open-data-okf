---
type: Table
title: "Sutartis — Duomenys apie sutartis (sutarčių rūšys ir kiti duomenys: data, sutarties šalių požymiai, daikto rūšis)"
description: "Spinta table datasets/gov/rc/stsr/sutartys/Sutartis (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/sutartys/Sutartis"
tags: [gov, rc, sutartis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/sutartys.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2134/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sutartis — Duomenys apie sutartis (sutarčių rūšys ir kiti duomenys: data, sutarties šalių požymiai, daikto rūšis)

- **Model:** `datasets/gov/rc/stsr/sutartys/Sutartis`[^manifest]
- **Dataset:** [STSR duomenys apie sutartis](../sutartys.md) (`datasets/gov/rc/stsr/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/stsr/sutartys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/sutartys/Sutartis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Sutarties identifikavimo kodas šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `3` | `open` | — | Sutarties tipo aprašymas šiame duomenų rinkinyje | — |
| `turto_tipas` | `ref` | [TurtoTipas](../klasifikatoriai/TurtoTipas.md) (`level=4 UUID`: `turto_tipas._id`) | `4` | `open` | — | Turto tipas | — |
| `ireg_ketv` | `date` | `Q` | `4` | `open` | — | Sutarties įregistravimo data (metai - ketvirtis) | — |
| `isreg_ketv` | `date` | `Q` | `4` | `open` | — | Sutarties išregistravimo data (metai - ketvirtis) | — |
| `terminas_metai` | `date` | `Y` | `4` | `open` | — | Galutinis atsiskaitymo terminas (metai) | — |
| `pabaigos_aprasymas` | `string` | — | `3` | `open` | — | Sutarties pabaigos pagrindo aprašymas | — |
| `gav_amnt_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties gavėjo asmens tipas | — |
| `gav_sal_kodas` | `integer` | — | `2` | `open` | — | Sutarties gavėjo valstybės kodas | — |
| `gav_sal_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties gavėjo valstybės pavadinimas | — |
| `dav_amnt_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties davėjo asmens tipas | — |
| `dav_sal_kodas` | `integer` | — | `2` | `open` | — | Sutarties davėjo valstybės kodas | — |
| `dav_sal_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties davėjo valstybės pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gav_amnt_pavadinimas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo | — |
| `gav_amnt_pavadinimas` | `"LR juridinis asmuo"` | — | — | LR juridinis asmuo | — |
| `gav_amnt_pavadinimas` | `"Užsienio juridinis asmuo"` | — | — | Užsienio juridinis asmuo | — |
| `dav_amnt_pavadinimas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo | — |
| `dav_amnt_pavadinimas` | `"LR juridinis asmuo"` | — | — | LR juridinis asmuo | — |
| `dav_amnt_pavadinimas` | `"Užsienio juridinis asmuo"` | — | — | Užsienio juridinis asmuo | — |
| `dav_amnt_pavadinimas` | `"Užsienio juridinis iš JAR"` | — | — | Užsienio juridinis iš JAR | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/sutartys.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sutartys.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sutartys (https://data.gov.lt/datasets/2134/)

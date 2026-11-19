---
type: Table
title: "Skundas — Lygių galimybių pažeidimų skundai"
description: "Rinkinyje pateikiami asmenų gauti skundai dėl lygių galimybių pažeidimo: registracijos, uždarymo datos, teisinis pagrindas, sritis, uždarymo priežastis, respondentas ir su juo susijusi informacija, taip pat subjektas."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/skundai/Skundas"
tags: [gov, lgkt, skundas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/skundai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lgkt/skundai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skundas — Lygių galimybių pažeidimų skundai

Rinkinyje pateikiami asmenų gauti skundai dėl lygių galimybių pažeidimo: registracijos, uždarymo datos, teisinis pagrindas, sritis, uždarymo priežastis, respondentas ir su juo susijusi informacija, taip pat subjektas. Rinkinyje duomenys nuo 2015 metų gruodžio iki dabar.[^manifest]

- **Model:** `datasets/gov/lgkt/skundai/Skundas`[^manifest]
- **Dataset:** [datasets/gov/lgkt/skundai](../skundai.md) (`datasets/gov/lgkt/skundai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgkt/skundai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/skundai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/skundai/Skundas` (`deployed`)[^manifest]
- **Provider:** `lgkt` — Lygių galimybių kontrolieriaus tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registarcijos_data` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `uzdarymo_data` | `date` | `D` | `4` | `open` | — | Skundo pabaigos data | — |
| `teisinis_terminas` | `string` | — | `4` | `open` | — | Teisinio termino pavadinimas | — |
| `sritis` | `string` | — | `4` | `open` | — | Skundo srities pavadinimas | — |
| `posritis` | `string` | — | `4` | `open` | — | Skundo srities posrities pavadinimas | — |
| `uzdarymo_priezastis` | `string` | — | `4` | `open` | — | Sprendimo kodas ir aprašymas | — |
| `respondentas` | `string` | — | `4` | `open` | — | Respondentas/pranešėjas - Vardas pavardė, arba juridinio asmens pavadinimas | — |
| `respondento_kodas` | `string` | — | `4` | `open` | — | Respondento: asmens, arba juridinio asmens kodas | — |
| `respondento_tipas` | `string` | — | `4` | `open` | — | Respondento tipas: F -moteris, M -vyras, J -juridinis; | — |
| `respondento_teisnis_statusas` | `string` | — | `4` | `open` | — | Respondento teisinis statusas | — |
| `respondento_statusas` | `string` | — | `4` | `open` | — | Respondento socialinis statusas | — |
| `respondento_tautybe` | `string` | — | `4` | `open` | — | Respondento tautybė | — |
| `respondento_miestas` | `string` | — | `2` | `open` | — | Respondento miestas | — |
| `respondento_savivaldybe` | `string` | — | `2` | `open` | — | Respondento savivaldybė | — |
| `subjektas` | `string` | — | `4` | `open` | — | Subjektas - Vardas pavardė, arba juridinio asmens pavadinimas | — |
| `subjekto_kodas` | `string` | — | `4` | `open` | — | Subjekto: asmens, arba juridinio asmens kodas | — |
| `subjekto_tipas` | `string` | — | `4` | `open` | — | Subjekto tipas: F -moteris, M -vyras, J -juridinis; | — |
| `subjekto_teisnis_statusas` | `string` | — | `4` | `open` | — | Subjekto teisinis statusas | — |
| `subjekto_miestas` | `string` | — | `2` | `open` | — | Subjekto miestas | — |
| `subjekto_savivaldybe` | `string` | — | `2` | `open` | — | Subjekto savivaldybė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `respondento_tipas` | `"F"` | — | — | Moteris | — |
| `respondento_tipas` | `"M"` | — | — | Vyras | — |
| `respondento_tipas` | `"J"` | — | — | Juridinis asmuo | — |
| `respondento_teisnis_statusas` | `"Kita"` | — | — | Kita | — |
| `respondento_teisnis_statusas` | `"VšĮ"` | — | — | Viešoji įstaiga | — |
| `respondento_teisnis_statusas` | `"Valstybinė"` | — | — | Valstybinė | — |
| `respondento_teisnis_statusas` | `"Savivaldybė"` | — | — | Savivaldybė | — |
| `respondento_teisnis_statusas` | `"Privati"` | — | — | Privati | — |
| `respondento_statusas` | `"Negalią turintis(-i)"` | — | — | Negalią turintis(-i) | — |
| `respondento_statusas` | `"Nuteistasis(-oji)"` | — | — | Nuteistasis(-oji) | — |
| `respondento_statusas` | `"Dirbantis(-i)"` | — | — | Dirbantis(-i) | — |
| `respondento_statusas` | `"Bedarbis(-ė)"` | — | — | Bedarbis(-ė) | — |
| `respondento_statusas` | `"Pensininkas(-ė)"` | — | — | Pensininkas(-ė) | — |
| `subjekto_tipas` | `"F"` | — | — | Moteris | — |
| `subjekto_tipas` | `"M"` | — | — | Vyras | — |
| `subjekto_tipas` | `"J"` | — | — | Juridinis asmuo | — |
| `subjekto_teisnis_statusas` | `"Kita"` | — | — | Kita | — |
| `subjekto_teisnis_statusas` | `"VšĮ"` | — | — | Viešoji įstaiga | — |
| `subjekto_teisnis_statusas` | `"Valstybinė"` | — | — | Valstybinė | — |
| `subjekto_teisnis_statusas` | `"Savivaldybė"` | — | — | Savivaldybė | — |
| `subjekto_teisnis_statusas` | `"Privati"` | — | — | Privati | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teisinis_terminas` | `"update(property: ""teisinis_terminas[]"", type: ""array"", source: ""teisinis_terminas"")"` | `property` | `4` | — | — | — | — |
| `uzdarymo_priezastis` | `"update(property: ""uzdarymo_priezastis[]"", type: ""array"", source: ""uzdarymo_priezastis"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/skundai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/skundai.csv#L6)

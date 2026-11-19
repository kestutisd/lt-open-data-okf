---
type: Table
title: "Objektas — Apribojusių savo galimybę lošti asmenų registro objektų prašymai"
description: "Nuo 2017 m. gegužės 1 d. asmenų prašymai neleisti lošti ir dalyvauti nuotoliniuose lošimuose registruojami Apribojusių savo galimybę lošti asmenų registre"
resource: "https://get.data.gov.lt/datasets/gov/lpt/registro_objektas/Objektas"
tags: [gov, lpt, objektas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registro_objektas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lpt/registro_objektas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2688/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lpt/registro_objektas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Objektas — Apribojusių savo galimybę lošti asmenų registro objektų prašymai

Nuo 2017 m. gegužės 1 d. asmenų prašymai neleisti lošti ir dalyvauti nuotoliniuose lošimuose registruojami Apribojusių savo galimybę lošti asmenų registre[^manifest]

- **Model:** `datasets/gov/lpt/registro_objektas/Objektas`[^manifest]
- **Dataset:** [Apribojusių savo galimybę lošti asmenų registro objektų prašymai](../registro_objektas.md) (`datasets/gov/lpt/registro_objektas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lpt/registro_objektas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registro_objektas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/registro_objektas/Objektas` (`deployed`)[^manifest]
- **Provider:** `lpt` — Lošimų priežiūros tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `registro_objekto_kodas` | `string` | — | `4` | `open` | — | Registro objekto unikalus identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Asmens unikalus identifikatorius | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lyties pavadinimas | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `asmens_losimu_miestai` | `string` | — | `4` | `open` | — | Asmens pažymėti miestai, kur lošia dažniausiai - pildant paraišką pasirinkti miestai - statistikai | — |
| `asmens_losimu_rusys` | `string` | — | `4` | `open` | — | Asmens pažymėtos lošimų rūšys, kur lošia dažniausiai - pildant paraišką pasirinktos rūšys - statistikai | — |
| `registracijos_data` | `date` | `D` | `4` | `open` | — | Registracijos data | — |
| `registracijos_priezastis` | `string` | — | `3` | `open` | — | Registracijos priežastis | — |
| `periodo_pabaiga` | `date` | `D` | `4` | `open` | — | Periodo pabaiga | — |
| `periodo_keitimo_priezastis` | `string` | — | `3` | `open` | — | Periodo keitimo priežasties pavadinimas | — |
| `pasalinimo_data` | `date` | `D` | `4` | `open` | — | Pašalinimo data | — |
| `pasalinimo_priezastis` | `string` | — | `3` | `open` | — | Pašalinimo priežastis | — |
| `pozymis_archyvuota` | `boolean` | — | `4` | `open` | — | Požymis ar archyvuota | — |
| `prasymo_numeris` | `string` | — | `4` | `open` | — | Prašymo numeris | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |
| `prasymo_tipas` | `string` | — | `3` | `open` | — | Prašymo tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `asmens_losimu_miestai` | `"update(property: ""asmens_losimo_miestai[]"", type: ""array"", source: ""Asmens_losimo_miestai"")"` | `property` | `4` | — | — | — | — |
| `asmens_losimu_rusys` | `"update(property: ""asmens_losimu_rusys[]"", type: ""array"", source: ""Asmens_losimu_rusys"")"` | `property` | `4` | — | — | — | — |
| `registracijos_priezastis` | `"update(property: ""registracijos_priezastis[]"", type: ""array"", source: ""Registracijos_priezastis"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/registro_objektas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/registro_objektas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lpt/registro_objektas (https://data.gov.lt/datasets/2688/)

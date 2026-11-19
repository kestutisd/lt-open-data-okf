---
type: Table
title: "Artefaktas — Lietuvių tautosakos archyvo įrašų kolekcija"
description: "Rinkinyje pateikiami Lietuvių Literatūros ir Tautosakos Instituto tautosakos archyvinė medžiagos duomenys."
resource: "https://get.data.gov.lt/datasets/gov/llti/tautosaka/Artefaktas"
tags: [gov, llti, artefaktas, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/llti/archyvas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2836/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/tautosaka"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Artefaktas — Lietuvių tautosakos archyvo įrašų kolekcija

Rinkinyje pateikiami Lietuvių Literatūros ir Tautosakos Instituto tautosakos archyvinė medžiagos duomenys. Lietuvių tautosakos archyvo duomenų bazė talpina duomenis iš Lietuvių tautosakos archyvo - didžiausios ir seniausios lietuvių folkloro saugyklos Lietuvoje ir pasaulyje. Ši folkloro saugykla paveldėjo duomenis iš Lietuvių mokslo draugijos, gyvavusios 1907–1940 Vilniuje, Lietuvių tautosakos archyvo, veikusio 1935–1939 Kaune, ir kitų fondų. Rinkinio objektas - į archyvą įtrauktas rankraštis, vaizdo arba garso įrašas ar kito pobūdžio artefaktas. Duomenys apima artefaktus nuo XIXa. pabaigos iki šių dienų. Pateikiami duomenys apie fizinius artefakto parametrus, inventorizavimą, klasifikaciją, sudarytojus, fiksavimo vietą ir kt. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/llti/tautosaka/Artefaktas`[^manifest]
- **Dataset:** [Lietuvių tautosakos archyvo įrašų kolekcija](../tautosaka.md) (`datasets/gov/llti/tautosaka`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/archyvas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/tautosaka/Artefaktas` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `signatura` | `string` | — | `3` | `open` | — | Signatūros pavadinimas | — |
| `kolekcija` | `string` | — | `4` | `open` | — | Kolekcijos pavadinimas | — |
| `saugotojas` | `string` | — | `4` | `open` | — | Įrašo saugojimo vieta | — |
| `rusys` | `string` | — | `4` | `open` | — | Kolekcijos įrašo rūšis(-ys) | — |
| `klasifikacija` | `string` | — | `4` | `open` | — | Kolekcijos įrašo klasifikacija(-os) | — |
| `fiks_vieta` | `string` | — | `4` | `open` | — | Duomenų užrašymo arba dokumento sudarymo vieta | — |
| `orig_antraste_lt` | `string` | — | `4` | `open` | — | Tautosakos rinkinio ar įrašo originalus pavadinimas | — |
| `arch_antraste_lt` | `string` | — | `4` | `open` | — | Archyvo antraštės pavadinimas | — |
| `kalbos` | `string` | — | `4` | `open` | — | Rankraščio arba įrašo kalba(os) | — |
| `sudarymo_metai` | `integer` | — | `4` | `open` | — | Rankraščio arba įrašo sudarymo metai | — |
| `sudarytojai` | `string` | — | `4` | `open` | — | Artefakto sudarytojas | — |
| `gauta_is` | `string` | — | `3` | `open` | — | Asmuo arba asmenys iš kurių gautas rankraštis arba įrašas. | — |
| `inv_data` | `integer` | — | `4` | `open` | — | Artefakto inventorizavimo data | — |
| `fiz_parametrai_lt` | `string` | — | `4` | `open` | — | Artefakto fiziniai parametrai | — |
| `anotacija_lt` | `string` | — | `4` | `open` | — | Rankraščio arba įrašo apibūdinimas | — |
| `turinio_vnt` | `integer` | `U` | `4` | `open` | — | Bendras artefaktą sudarančių tautosakos archyvo vienetų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rusys` | `"update(property: ""rusys[]"", type: ""array"", source: ""Rusys"")"` | `property` | `4` | — | — | — | — |
| `klasifikacija` | `"update(property: ""klasifikacija[]"", type: ""array"", source: ""Klasifikacija"")"` | `property` | `4` | — | — | — | — |
| `orig_antraste_lt` | `update(property: "orig_antraste_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `arch_antraste_lt` | `update(property: "arch_antraste_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `kalbos` | `"update(property: ""kalbos[]"", type: ""array"", source: ""Kalbos"")"` | `property` | `4` | — | — | — | — |
| `sudarytojai` | `"update(property: ""kalbos[]"", type: ""array"", source: ""Kalbos"")"` | `property` | `4` | — | — | — | — |
| `fiz_parametrai_lt` | `update(property: "fiz_parametrai_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `anotacija_lt` | `update(property: "anotacija_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/archyvas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/tautosaka (https://data.gov.lt/datasets/2836/)

---
type: Table
title: "MirusiujuToksikologinisRezultatas — Toksikologinių tyrimų rezultatai"
description: "\"Duomenys atspindi toksikologinių tyrimų rezultatus mirties atvejais, kai medžiagų buvo rasta."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai/MirusiujuToksikologinisRezultatas"
tags: [gov, lsd, mirusiujutoksikologinisrezultatas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MirusiujuToksikologinisRezultatas — Toksikologinių tyrimų rezultatai

"Duomenys atspindi toksikologinių tyrimų rezultatus mirties atvejais, kai medžiagų buvo rasta. Toksikologinės medžiagos nebūtinai lėmė asmens mirtį."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai/MirusiujuToksikologinisRezultatas`[^manifest]
- **Dataset:** [Toksikologinių tyrimų rezultatai mirties atvejais](../mirusiuju_toksikologiniai.md) (`datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai/MirusiujuToksikologinisRezultatas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius" |
| `mirties_id` | `string` | — | `4` | `open` | — | Unikalus asmens mirties įrašo identifikatorius | — |
| `t_rez` | `string` | — | `4` | `open` | — | "Tyrimo rezultatas: 0 Nerasta, 1 Pėdsakai, 2 Rasta, 3 Koncentracija" | — |
| `m_konc` | `number` | — | `4` | `open` | — | Rastos medžiagos koncentracija | — |
| `mk_vienetai` | `string` | — | `4` | `open` | — | "Koncentracijos vienetai: 1 Procentai, 2 Promilės, 3 mg/l" | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Rastos medžiagos pavadinimas | — |
| `gr_pavadinimas` | `string` | — | `4` | `open` | — | Medžiagų grupės pavadinimas | — |
| `tipo_pavadinimas` | `string` | — | `4` | `open` | — | Medžiagų tipo pavadinimas | — |
| `lytis` | `string` | — | `4` | `open` | — | Mirusiojo lytis | — |
| `mirties_metai` | `integer` | — | `4` | `open` | — | Metai mirties metu | — |
| `gyv_tipas` | `string` | — | `4` | `open` | — | Mirusiojo gyvenamosios vietovės tipas | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Asmens amžiaus grupė mirties metu | — |
| `mirties_priezastis` | `string` | — | `4` | `open` | — | "Mirties priežasties grupė, suformuota pagal TLK-10 klasifikaciją" | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirusiuju_toksikologiniai.csv#L6)

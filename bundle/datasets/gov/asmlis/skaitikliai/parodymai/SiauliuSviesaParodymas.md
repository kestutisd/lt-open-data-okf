---
type: Table
title: "SiauliuSviesaParodymas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“ skaitiklių parodymų įrašai."
description: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas"
tags: [gov, asmlis, siauliusviesaparodymas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SiauliuSviesaParodymas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“...

**Dataset Context:** Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai. Viena eilutė atitinka vieną skaitiklio deklaravimo įrašą. Duomenų rinkinį sudaro dvi lentelės, kuriose pateikiami skaitiklių parodymų ir patalpų, kurioms priskirtas skaitiklis įrašai. Lentelėse galima rasti skaitiklio tipą, laikotarpį, kuriuo atlikta deklaracija, skaitiklių vertes nuo ir iki, patapos plotą, tūri ir apytiksles koordinates. Koordinatės „triukšminamos“ naudojant 50 metrų standartinio nuokrypio parametrą. Priklausomai nuo savivaldybės ar įstaigos, duomenų aprėptis gali skirtis, tačiau duomenis numatyta atnaujinti kas mėnesį.[^manifest]

- **Model:** `datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”...](../parodymai.md) (`datasets/gov/asmlis/skaitikliai/parodymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai/SiauliuSviesaParodymas` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `skaitliuko_id` | `string` | — | `4` | `open` | — | Skaitiklio identifikatorius | — |
| `skaitliuko_tipas` | `string` | — | `4` | `open` | — | Skaitiklio tipas | — |
| `periodas` | `date` | `D` | `4` | `open` | — | Deklaruotų duomenų periodas | — |
| `nuo` | `number` | — | `4` | `open` | — | Data nuo | — |
| `iki` | `number` | — | `4` | `open` | — | Data iki | — |
| `skirtumas` | `number` | — | `4` | `open` | — | Skirtumas | — |
| `matavimo_vienetai` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L6)

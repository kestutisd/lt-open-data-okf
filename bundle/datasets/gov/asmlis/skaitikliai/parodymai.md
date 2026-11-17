---
type: Dataset
title: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai."
description: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai"
tags: [gov, asmlis, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai.

Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai. Viena eilutė atitinka vieną skaitiklio deklaravimo įrašą. Duomenų rinkinį sudaro dvi lentelės, kuriose pateikiami skaitiklių parodymų ir patalpų, kurioms priskirtas skaitiklis įrašai. Lentelėse galima rasti skaitiklio tipą, laikotarpį, kuriuo atlikta deklaracija, skaitiklių vertes nuo ir iki, patapos plotą, tūri ir apytiksles koordinates. Koordinatės „triukšminamos“ naudojant 50 metrų standartinio nuokrypio parametrą. Priklausomai nuo savivaldybės ar įstaigos, duomenų aprėptis gali skirtis, tačiau duomenis numatyta atnaujinti kas mėnesį.

- **Namespace:** `datasets/gov/asmlis/skaitikliai/parodymai`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/parodymai`
- **Parent Namespace (`ns`):** MOKESTA ir ASMLIS sistemos (`datasets/gov/asmlis`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SiauliuSviesaParodymas](parodymai/SiauliuSviesaParodymas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“ skaitiklių parodymų įrašai. | `4` | `vda_prime_key` | — | 9 | — |
| [SiauliuEnergijaParodymas](parodymai/SiauliuEnergijaParodymas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“ skaitiklių parodymų įrašai. | `4` | `vda_prime_key` | — | 9 | — |
| [SimnoKomunalininkasParodymas](parodymai/SimnoKomunalininkasParodymas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Simno komunalininkas“ skaitiklių parodymų įrašai. | `4` | `vda_prime_key` | — | 9 | — |
| [SilutesSTParodymas](parodymai/SilutesSTParodymas.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šilutės šilumos tinklai“ skaitiklių parodymų įrašai. | `4` | `vda_prime_key` | — | 9 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv

---
type: Table
title: "Pacientas — Pacientai"
description: "Lentelė „Pacientai“. Lentelę sudaro: paciento asmens kodas bei jo validacijos požymis, paciento gimimo metai iš atskiro gimimo datos stulpelio ir gimimo metai bei lytis iš tinkamo asmens kodo."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Pacientas"
tags: [gov, rvul, pacientas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L58"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L58"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientas — Pacientai

Lentelė „Pacientai“. Lentelę sudaro: paciento asmens kodas bei jo validacijos požymis, paciento gimimo metai iš atskiro gimimo datos stulpelio ir gimimo metai bei lytis iš tinkamo asmens kodo. Vienas lentelės įrašas atitinka vieną asmens kodo ir gimimo metų iš gimimo datos stulpelio kombinaciją. Besikartojantys asmens kodai yra fiktyvios reikšmės, įvestos nežinant tikrojo paciento asmens kodo. Tokiais atvejais atskirti unikalius asmenis padeda gimimo metai. Įrašai su besikartojančiais asmens kodais ir tuščiais gimimo metais iš stulpelio buvo pašalinti. Lentelėje įtraukta lytis tik iš tinkamo asmens kodo, kadangi pirminiuose duomenyse nebuvo atskiro paciento lyties stulpelio.[^manifest]

- **Model:** `datasets/gov/rvul/hops/Pacientas`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L58)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Pacientas` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Paciento asmens kodas | — |
| `paciento_asm_k_val` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `paciento_gim_m` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `vda_paciento_gim_m_ak` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš asmens kodo | — |
| `vda_paciento_lytis_ak` | `string` | — | `4` | `open` | — | Paciento lytis iš asmens kodo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_asm_k_val` | `"Tinkamas"` | — | — | Tinkamas | — |
| `paciento_asm_k_val` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `paciento_asm_k_val` | `"Yra ne skaitmenų"` | — | — | Yra ne skaitmenų | — |
| `paciento_asm_k_val` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `paciento_asm_k_val` | `"Netinkama gimimo data"` | — | — | Netinkama gimimo data | — |
| `paciento_asm_k_val` | `"Netinkamas pirmas skaitmuo"` | — | — | Netinkamas pirmas skaitmuo | — |
| `vda_paciento_lytis_ak` | `"M"` | — | — | Moteris | — |
| `vda_paciento_lytis_ak` | `"V"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L58 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L58)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)

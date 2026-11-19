---
type: Table
title: "JurbarkoLigonine — Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys"
description: "Informacinėje sistemoje „CEDARA“ kaupiami Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/JurbarkoLigonine"
tags: [gov, radiologija, jurbarkoligonine, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L374"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L374"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# JurbarkoLigonine — Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys

Informacinėje sistemoje „CEDARA“ kaupiami Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys. Duomenų rinkinyje pateikiami duomenys nuo 1998 metų. Vienas įrašas atitinka vieną tyrimo atvaizdą (visų tyrimo atvaizdų identifikatoriai unikalūs). Duomenų rinkinį sudaro: šifruotas paciento asmens kodas, asmens kodo validumo požymis, šifruoti paciento ir tyrimo studijos identifikatoriai, paciento gimimo metai ir lytis tiek iš gimimo datos arba lyties stulpelių, tiek iš validaus asmens kodo, šifruotas tyrimo serijos identifikatorius, tirta paciento kūno dalis, paciento lateralumas tyrimo serijos metu, tyrimo serijos modalumas, protokolas, tyrimo atvaizdo šifruotas identifikatorius, paciento kūno padėtis tyrimo atvaizde ir fotometrinė interpretacija. Paciento gimimo metų reikšmės iš gimimo datos stulpelio iki 1800 m. laikomos analitiškai tolygiomis nesamoms reikšmėms. Duomenų teikėjas – VšĮ Jurbarko ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/JurbarkoLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L374](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L374)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/JurbarkoLigonine` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `vda_paciento_asm_k_val` | `string` | — | `4` | `open` | — | Paciento asmens kodo validumas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento identifikatorius | — |
| `tyrimo_uid` | `string` | — | `4` | `open` | — | Pseudonimizuotas tyrimo studijos identifikatorius | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš gimimo datos stulpelio | — |
| `vda_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš validaus asmens kodo | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis iš lyties stulpelio | — |
| `vda_lytis` | `string` | — | `4` | `open` | — | Paciento lytis iš validaus asmens kodo | — |
| `tyrimo_serijos_uid` | `string` | — | `4` | `open` | — | Pseudonimizuotas tyrimo serijos identifikatorius | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tyrimo serijos metu tirta paciento kūno dalis | — |
| `paciento_lateralumas` | `string` | — | `4` | `open` | — | Paciento lateralumas tyrimo serijos metu | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_protokolas` | `string` | — | `4` | `open` | — | Tyrimo serijos protokolas | — |
| `atvaizdo_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas tyrimo atvaizdo identifikatorius | — |
| `paciento_padetis` | `string` | — | `4` | `open` | — | Paciento kūno padėtis tyrimo atvaizdo metu | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Tyrimo atvaizdo fotometrinė interpretacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vda_paciento_asm_k_val` | `"Tinkamas"` | — | — | Tinkamas | — |
| `vda_paciento_asm_k_val` | `"Netinkamas"` | — | — | Netinkamas | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"K"` | — | — | Kita | — |
| `vda_lytis` | `"M"` | — | — | Moteris | — |
| `vda_lytis` | `"V"` | — | — | Vyras | — |
| `tyrimo_serijos_modalumas` | `"CR"` | — | — | Kompiuterinė radiografija | — |
| `tyrimo_serijos_modalumas` | `"OT"` | — | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"PR"` | — | — | Prezentacijos būsena | — |
| `tyrimo_serijos_modalumas` | `"IO"` | — | — | Intraoralinė radiografija | — |
| `tyrimo_serijos_modalumas` | `"DX"` | — | — | Skaitmeninė radiografija | — |
| `tyrimo_serijos_modalumas` | `"CT"` | — | — | Kompiuterinė tomografija | — |
| `fotometrine_interpretacija` | `"MONOCHROME1"` | — | — | Vienspalvis atvaizdas, kurio pikselio minimali vertė po transformacijų atitinka baltą | — |
| `fotometrine_interpretacija` | `"MONOCHROME2"` | — | — | Vienspalvis atvaizdas, kurio pikselio minimali vertė po transformacijų atitinka juodą | — |
| `fotometrine_interpretacija` | `"RGB"` | — | — | Atvaizdas, naudojantis raudonos, žalios, mėlynos spalvų komponentes | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L374 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L374)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)

---
type: Table
title: "Irasas — Civilinių orlaivių registro duomenys"
description: "Rinkinyje pateikiami duomenys registruotus ir jau išregistruotus civilnius orlaivius Lietuvos Respublikoje."
resource: "https://get.data.gov.lt/datasets/gov/tka/registras/Irasas"
tags: [gov, tka, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/tka/cor.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tka/cor.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Irasas — Civilinių orlaivių registro duomenys

Rinkinyje pateikiami duomenys registruotus ir jau išregistruotus civilnius orlaivius Lietuvos Respublikoje. Duomenys apima laikotarpį nuo 1991m. iki šių dienų. Nurodoma orlaivio kategorija, rūšis, tipas, keleivių skaičius, maksimali pakilimo masė, oro sraigto tipas, orlaivio bazė ir jos adresas. Papildomai taip pat nurodyti orlaivio savininko ir naudotojo tipai.

- **Model:** `datasets/gov/tka/registras/Irasas`[^manifest]
- **Dataset:** [Civilinių orlaivių registro duomenys](../registras.md) (`datasets/gov/tka/registras`)
- **Manifest CSV:** [datasets/gov/tka/cor.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tka/cor.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tka/registras/Irasas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | `Valstybės Duomenų Agentūros įrašo unikalus identifikatorius` | — | — |
| `duomenu_sviezumas` | `date` | `D` | `4` | `open` | `Duomenų atnaujinimo data` | — | — |
| `registracijos_nr` | `string` | — | `4` | `open` | `Orlaivio registracijos numeris, susidedantis iš orlaivio nacionalinio ženklo (LY) ir registracijos ženklo, kurį sudaro 3 didžiosios lotyniškos raidės.` | — | — |
| `statusas` | `string` | — | `4` | `open` | `Orlaivio registravimo būsena` | — | — |
| `kategorija` | `string` | — | `4` | `open` | `Orlaivio kategorija pagal klasifikatorių` | — | — |
| `rusis` | `string` | — | `4` | `open` | `Orlaivio rūšis` | — | — |
| `tipas` | `string` | — | `4` | `open` | `Orlaivio tipas` | — | — |
| `savininko_tipas` | `string` | — | `4` | `open` | `Požymis, ar orlaivio savininkas yra fizinis ar juridinis asmuo.` | — | — |
| `naudotojo_tipas` | `string` | — | `4` | `open` | `Požymis, ar orlaivio naudotojas yra fizinis ar juridinis asmuo.` | — | — |
| `pagaminimas` | `date` | `D` | `4` | `open` | `Orlaivio pagaminimo metai` | — | — |
| `pirma_registracija` | `date` | `D` | `4` | `open` | `Pirmo registravimo Lietuvoje data` | — | — |
| `paskutine_registracija` | `date` | `D` | `4` | `open` | `Orlaivio paskutinio registravimo data` | — | — |
| `tsppp_galiojimas` | `date` | `D` | `4` | `open` | `Tinkamumo skristi pažymėjimo patikros pasirašymo data` | — | — |
| `baze` | `string` | — | `4` | `open` | `Numatoma orlaivio bazavimosi vieta` | — | — |
| `bazes_adresas` | `string` | — | `4` | `open` | `Bazės adresas` | — | — |
| `geometrija` | `geometry(point, 3346)` | `m` | `4` | `open` | `Bazės adreso koordinatės (LKS)` | — | — |
| `keleiviu_sk` | `integer` | `U` | `4` | `open` | `Orlaivio keleivių skaičius` | — | — |
| `mkm` | `integer` | `kg` | `4` | `open` | `Sertifikuota maksimali pakilimo masė (kg)` | — | — |
| `oro_sraigtas` | `string` | — | `4` | `open` | `Informacija apie oro sraigtą` | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `"Registravimas panaikintas"` | — | — | — | — |
| `statusas` | `"Registruotas"` | — | — | — | — |
| `savininko_tipas` | `"Juridinis asmuo"` | — | — | — | — |
| `savininko_tipas` | `"Fizinis asmuo"` | — | — | — | — |
| `savininko_tipas` | `"Galimai fizinis asmuo"` | — | — | — | — |
| `naudotojo_tipas` | `"Juridinis asmuo"` | — | — | Žymima, kai naudotojo kodas atitinka juridinio asmens kodo taisykles | — |
| `naudotojo_tipas` | `"Galimai fizinis asmuo"` | — | — | Žymima, kai naudotojo kodas atitinka fizinio asmens kodo taisykles | — |
| `naudotojo_tipas` | `"Fizinis asmuo"` | — | — | Žymima, kai naudotojo kodas neatitinka nei fizinio, nei juridinio asmens kodo validacijos taisyklių. Tai apima atvejus, kai orlaivis naudojamas kelių fizinių/juridinių asmenų arba asmenų iš užsienio valstybių. | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/tka/cor.csv

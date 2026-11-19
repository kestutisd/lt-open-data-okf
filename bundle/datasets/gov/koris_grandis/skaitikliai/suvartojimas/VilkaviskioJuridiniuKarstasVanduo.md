---
type: Table
title: "VilkaviskioJuridiniuKarstasVanduo — UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka juridiniai asmenys"
description: "Deklaruotas vandens ir šilumos suvartojimas"
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioJuridiniuKarstasVanduo"
tags: [gov, koris_grandis, vilkaviskiojuridiniukarstasvanduo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L35"
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L35"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VilkaviskioJuridiniuKarstasVanduo — UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka juridiniai asmenys

**Dataset Context:** Deklaruotas vandens ir šilumos suvartojimas[^manifest]

- **Model:** `datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioJuridiniuKarstasVanduo`[^manifest]
- **Dataset:** [Suvartojimas](../suvartojimas.md) (`datasets/gov/koris_grandis/skaitikliai/suvartojimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L35)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioJuridiniuKarstasVanduo` (`deployed`)[^manifest]
- **Provider:** `koris_grandis` — Komunaliniai suvartojimo įrašai sistemoje „GRANDIS“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Namo, daugiabučio ar kito pastato identifikatorius | — |
| `pastato_ar_dalies_id` | `string` | — | `4` | `open` | — | Namo, buto arba kitos pastato dalies identifikatorius | — |
| `apskaitos_tasko_id` | `string` | — | `4` | `open` | — | Apskaitos taško (skaitiklio vietos) identifikatorius | — |
| `moketojo_kategorija` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo kategorija | — |
| `moketojo_teisines_formos_tipas` | `string` | — | `4` | `open` | — | Įmonės teisinės formos tipas pagal Registrų centro Juridinių asmenų registro teisinių formų klasifikatorių | — |
| `moketojo_jar_kodas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo kodas Juridinių asmenų registre | — |
| `moketojo_jar_kodo_tinkamumas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo kodo tinkamumas pagal Juridinių asmenų registro formatą | — |
| `pvm_moketojo_kodas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo turimas pridėtinės vertės mokėtojo kodas | — |
| `moketojas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo pavadinimas | — |
| `apskaitos_menuo` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio mėnuo | — |
| `deklaravimo_data` | `date` | `D` | `4` | `open` | — | Skaitiklio rodmenų deklaravimo data | — |
| `deklaruotas_suvartojimas_m3` | `number` | — | `4` | `open` | — | Deklaruotas skaitiklio rodmenų skirtumas nuo praėjusio apskaitos laikotarpio, m3 | — |
| `pateikimo_budas` | `string` | — | `4` | `open` | — | Skaitiklio rodmenų pateikimo būdas | — |
| `ar_gyvenamas` | `string` | — | `4` | `open` | — | Požymis, nurodantis, ar namo, buto arba kitos pastato dalies patalpų paskirtis yra gyvenamoji (1 – taip, 0 – ne) | — |
| `gyvenanciu_zmoniu_skaicius` | `number` | — | `4` | `open` | — | Name, bute ar kitoje pastato dalyje gyvenančių žmonių skaičius | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena (Nedalyvauja – nesudalyvavo periodo uždaryme; Dalyvauja – sudalyvavo periodo uždaryme; Ištrintas) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `moketojo_kategorija` | `"Biudžetinės įstaigos"` | — | — | Biudžetinės įstaigos | — |
| `moketojo_kategorija` | `"Įmonės"` | — | — | Įmonės | — |
| `moketojo_teisines_formos_tipas` | `"Viešasis"` | — | — | Viešasis | — |
| `moketojo_teisines_formos_tipas` | `"Privatus"` | — | — | Privatus | — |
| `moketojo_jar_kodo_tinkamumas` | `"Tinkamas"` | — | — | Tinkamas | — |
| `moketojo_jar_kodo_tinkamumas` | `"Tuščia reikšmė"` | — | — | Tuščia reikšmė | — |
| `moketojo_jar_kodo_tinkamumas` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `moketojo_jar_kodo_tinkamumas` | `"Yra ne skaitmenų"` | — | — | Yra ne skaitmenų | — |
| `moketojo_jar_kodo_tinkamumas` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `pateikimo_budas` | `"Importuota"` | — | — | Importuota | — |
| `pateikimo_budas` | `"Įvesta"` | — | — | Įvesta | — |
| `pateikimo_budas` | `"Neįvesta"` | — | — | Neįvesta | — |
| `busena` | `"Nedalyvauja"` | — | — | Nedalyvauja | — |
| `busena` | `"Dalyvauja"` | — | — | Dalyvauja | — |
| `busena` | `"Ištrintas"` | — | — | Ištrintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L35 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L35)

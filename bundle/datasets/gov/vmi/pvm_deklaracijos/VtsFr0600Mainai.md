---
type: Table
title: "VtsFr0600Mainai — FR0600_DUOMENYS"
description: "Spinta table datasets/gov/vmi/pvm_deklaracijos/VtsFr0600Mainai (30 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/pvm_deklaracijos/VtsFr0600Mainai"
tags: [gov, vmi, vtsfr0600mainai, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmi/pvm_deklaracijos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1163/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/pvm_deklaracijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VtsFr0600Mainai — FR0600_DUOMENYS

- **Model:** `datasets/gov/vmi/pvm_deklaracijos/VtsFr0600Mainai`[^manifest]
- **Dataset:** [Pridėtinės vertės mokesčio deklaracijų duomenų rinkinys](../pvm_deklaracijos.md) (`datasets/gov/vmi/pvm_deklaracijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/pvm_deklaracijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/pvm_deklaracijos/VtsFr0600Mainai` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokestinis_laikotarpis` | `date` | `M` | `4` | `open` | — | Mokestinis laikotarpis iki (laikotarpio pabaigos data) | — |
| `sekcija_pagal_ekonomines_veiklos_rusiu_klasifikatoriu` | `string` | — | `4` | `open` | — | Deklaracijoje nurodyta pagrindinė vykdomos veiklos rūšis pagal Ekonominės veiklos rūšių klasifikatorių, patvirtintą Statistikos departamento generalinio direktoriaus 2007 m. spalio 31 d. įsakymu Nr.DĮ-226 (Žin., 2007, Nr.119-4877, toliau - EVRK) | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis. Taip pat veikla nenustatoma, kai veiklos kodas nėra atpažįstamas. |
| `skyrius_pagal_ekonomines_veiklos_rusiu_klasifikatoriu` | `string` | — | `4` | `open` | — | Pagrindinė vykdomos veiklos rūšis pagal EVRK. Imama iš klasifikatoriaus, jei pavyko identifikuoti pagal deklaracijoje įrašytą kodą | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis. Taip pat veikla nenustatoma, kai veiklos kodas nėra atpažįstamas. |
| `apskritis` | `string` | — | `4` | `open` | — | Deklaracijai priskirtos apskrities pavadinimas | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis. |
| `mokesciu_moketoju_skaicius` | `integer` | — | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |
| `pvm_apmokestinami_sandoriai` | `number` | — | `4` | `open` | — | PVM apmokestinami tiekimai (18, 9, 5 procentais) | — |
| `pvm_apmokestinami_sandoriai_kai_pvm_isskaito_pirkejas` | `number` | — | `4` | `open` | — | PVM apmokestinami sandoriai, kai PVM išskaito pirkėjas (PVM įstatymo 96 str. nustatytais atvejais) | — |
| `pvm_neapmokestinami_sandoriai` | `number` | — | `4` | `open` | — | PVM neapmokestinami tiekimai | — |
| `suvartojimas_privatiems_poreikiams` | `number` | — | `4` | `open` | — | Suvartojimas privatiems poreikiams | — |
| `ilgalaikio_materialiojo_turto_pasigaminimas` | `number` | — | `4` | `open` | — | Ilgalaikio materialiojo turto pasigaminimas | — |
| `sandoriu_kuriems_taikoma_spec_apmokestinimo_schema_marza` | `number` | — | `4` | `open` | — | Tiekimų, kuriems taikoma speciali apmokestinimo schema, marža | — |
| `prekiu_eksportas_0_proc` | `number` | — | `4` | `open` | — | Patiektos ir už Europos Sąjungos ribų išgabentos prekės (eksportas, PVM – 0 procentų) | — |
| `es_pvm_moketojams_patiektos_prekes_0_proc` | `number` | — | `4` | `open` | — | Europos Sąjungos valstybių narių PVM mokėtojams patiektos ir iš Lietuvos Respublikos išgabentos prekės (PVM – 0 procentų) | — |
| `kiti_pvm_apmokestinami_sandoriai_0_proc` | `number` | — | `4` | `open` | — | Kitos patiektos prekės ir suteiktos paslaugos, apmokestinamos 0 procentų | — |
| `uz_lietuvos_ribu_ivyke_sandoriai_ne_pvm_objektas_lietuvoje` | `number` | — | `4` | `open` | — | Už Lietuvos Respublikos ribų patiektos prekės ir suteiktos paslaugos, kurių pirkimo (importo) PVM atskaitomas | — |
| `is_es_isigytos_prekes` | `number` | — | `4` | `open` | — | Iš Europos Sąjungos valstybių narių įsigytos prekės, kurių įsigijimo vieta Lietuvos Respublikoje | — |
| `is_es_isigytos_prekes_trikampei_prekybai` | `number` | — | `4` | `open` | — | Iš Europos Sąjungos valstybių narių įsigytos prekės, kurios iš karto patiektos kitos Europos Sąjungos valstybės narės PVM mokėtojams (trikampė prekyba) | — |
| `is_uzsienio_valstybiu_isigytos_paslaugos` | `number` | — | `4` | `open` | — | Iš užsienio valstybių įsigytos paslaugos | — |
| `is_ju_isigytos_is_es_pvm_moketoju` | `number` | — | `4` | `open` | — | Iš ES valstybių narių PVM mokėtojų įsigytos paslaugos | — |
| `isigytu_prekiu_ir_paslaugu_pirkmo_pvm` | `number` | — | `4` | `open` | — | Įsigytų prekių ir paslaugų pirkmo PVM | — |
| `sumoketas_importo_pvm` | `number` | — | `4` | `open` | — | Sumokėtas importo PVM | — |
| `importo_pvm_kurio_iskaityma_kontroliuoja_vmi` | `number` | — | `4` | `open` | — | Importo PVM, kurio įskaitymą kontroliuoja VMI | — |
| `standartinio_tarifo_pardavimo_pvm` | `number` | — | `4` | `open` | — | Standartinio tarifo pardavimo PVM | — |
| `procentu_9_pardavimo_pvm` | `number` | — | `4` | `open` | — | 9 procentų pardavimo PVM | — |
| `procentu_5_pardavimo_pvm` | `number` | — | `4` | `open` | — | 5 procentų pardavimo PVM | — |
| `pardavimo_pvm_pagal_95_str` | `number` | — | `4` | `open` | — | Pardavimo PVM (PVM įstatymo 95 str. nustatytais atvejais) | — |
| `pardavimo_pvm_pagal_96_str` | `number` | — | `4` | `open` | — | Pardavimo PVM (PVM įstatymo 96 str. nustatytais atvejais) | — |
| `is_es_isigytu_prekiu_pardavimo_pvm` | `number` | — | `4` | `open` | — | Pirkėjo apskaičiuotas iš kitų Europos Sąjungos valstybių narių įsigytų prekių pardavimo PVM | — |
| `atskaitomas_pvm` | `number` | — | `4` | `open` | — | Atskaitomas pirkimo ir importo PVM | — |
| `moketinas_i_biudzeta_arba_grazintinas_is_biudzeto_pvm` | `number` | — | `4` | `open` | — | Mokėtinas į biudžetą arba grąžintinas iš biudžeto (-) PVM | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/pvm_deklaracijos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/pvm_deklaracijos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/pvm_deklaracijos (https://data.gov.lt/datasets/1163/)

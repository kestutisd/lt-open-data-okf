---
type: Table
title: "Medikamentas — Veterinariniai vaistai"
description: "Lietuvoje registruoti veterinariniai vaistai – jų sudėtis, paskirtis, gamintojas ir registracijos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vmvt/medikamentai/Medikamentas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/medikamentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/medikamentai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Medikamentas — Veterinariniai vaistai

Lietuvoje registruoti veterinariniai vaistai – jų sudėtis, paskirtis, gamintojas ir registracijos duomenys

- **Model:** `datasets/gov/vmvt/medikamentai/Medikamentas`[^manifest]
- **Dataset:** [Duomenys apie Lietuvoje registruotus veterinarinius vaistus](../medikamentai.md) (`datasets/gov/vmvt/medikamentai`)
- **Manifest CSV:** [datasets/gov/vmvt/medikamentai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/medikamentai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/medikamentai/Medikamentas`
- **Primary Key (`ref`):** `med_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `med_id` | `string` | — | `4` | `open` | — | Unikalus vaisto identifikatorius | — |
| `atcvet_kodas` | `string` | — | `4` | `open` | — | ATCvet kodas, naudojamas veterinariniams vaistams klasifikuoti pagal jų terapinį poveikį | — |
| `medikamento_pavadinimas` | `string` | — | `4` | `open` | — | Veterinarinio vaisto pavadinimas | — |
| `veiklioji_medziaga` | `string` | — | `4` | `open` | — | Vaisto sudėtyje esančios veikliosios medžiagos (-ų) pavadinimas (-ai) | — |
| `gyvunu_rusys` | `string` | — | `4` | `open` | — | Gyvūnų rūšis (-ys), kuriai (-ioms) skirtas veterinarinis vaistas | — |
| `vaisto_forma` | `string` | — | `4` | `open` | — | Veterinarinio vaisto farmacinė forma | — |
| `indikacijos` | `string` | — | `4` | `open` | — | Veterinarinio vaisto indikacijų aprašymas | — |
| `naudojimo_budas` | `string` | — | `4` | `open` | — | Veterinarinio vaisto naudojimo būdas (-ai) | — |
| `islauka` | `string` | — | `4` | `open` | — | Laikotarpis, per kurį draudžiama naudoti gyvūno produkciją po veterinarinio vaisto vartojimo. Nurodoma pagal gyvūnų rūšį | — |
| `med_registracijos_numeris` | `string` | — | `4` | `open` | — | Veterinarinio vaisto registracijos numeris | — |
| `med_registracijos_data` | `date` | `D` | `4` | `open` | — | Data, kada veterinarinio vaisto registracijos statusas įsigaliojo | — |
| `registracijos_statusas` | `string` | — | `4` | `open` | — | Veterinarinio vaisto registracijos statusas | — |
| `vaisto_klasifikacija` | `string` | — | `4` | `open` | — | Veterinarinio vaisto teisinis statusas, nurodantis receptinį ar nereceptinį pobūdį | — |
| `med_registruotojas` | `string` | — | `4` | `open` | — | Veterinarinio vaisto registruotojo pavadinimas | — |
| `med_reg_salis` | `string` | — | `4` | `open` | — | Veterinarinio vaisto registruotojo šalis | — |
| `med_reg_salies_kodas` | `string` | — | `4` | `open` | — | Dviejų raidžių ISO 3166-1 alfa-2 šalies kodas | — |
| `pakuociu_id` | `string` | — | `4` | `open` | — | Pakuočių identifikatoriai, atitinkantys konkrečias registruotas pakuočių formas | — |
| `pakuociu_pavadinimai` | `string` | — | `4` | `open` | — | Registruotų pakuočių pavadinimai, aprašantys pakuotės tipą ir dydį. Kelios pakuotės išvardintos per kablelį | — |
| `pakuociu_kiekiai` | `string` | — | `4` | `open` | — | Kiekvienos registruotos pakuotės vienetų skaičius (pvz., tablečių, ampulių, flakonų skaičius pakuotėje). Kelios pakuotės išvardintos per kablelį | — |
| `pakuociu_vienetai` | `string` | — | `4` | `open` | — | Pakuotėje esančių vienetų tipas (pvz., Tabletė, Flakonas, Ampulė, Pipetė). Kelios pakuotės išvardintos per kablelį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/medikamentai.csv

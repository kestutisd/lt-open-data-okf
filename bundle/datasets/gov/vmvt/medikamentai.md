---
type: Dataset
title: "Duomenys apie Lietuvoje registruotus veterinarinius vaistus"
description: "Duomenų rinkinys apima Lietuvoje registruotų veterinarinių vaistų informaciją, sudarytą remiantis Valstybinės maisto ir veterinarijos tarnybos (VMVT) administruojamu Veterinarinių vaistų registru."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/medikamentai"
tags: [gov, vmvt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/medikamentai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/medikamentai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/5343/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/medikamentai"
    author: "team:vda"
    last_modified: "2026-05-07T00:00:00Z"
---

# Duomenys apie Lietuvoje registruotus veterinarinius vaistus

- **Namespace:** `datasets/gov/vmvt/medikamentai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/medikamentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/medikamentai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/medikamentai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/5343/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė maisto ir veterinarijos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/medikamentai`[^dcat]
- **Portal Title (`@lt`):** Veterinarinių vaistų registracijos ir sudėtinės informacijos duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Set of data on registration and composite information of veterinary medicinal products[^dcat]
- **Issued (`dct:issued`):** `2026-05-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-05-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-05-07` .. `2026-05-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys apima Lietuvoje registruotų veterinarinių vaistų informaciją, sudarytą remiantis Valstybinės maisto ir veterinarijos tarnybos (VMVT) administruojamu Veterinarinių vaistų registru. Šis registras yra oficialus šaltinis, kuriame kaupiami duomenys apie visus Lietuvoje leidžiamus veterinarinius vaistus – tiek Europos Komisijos centralizuota tvarka registruotus (EU/...), tiek nacionaline tvarka registruotus (LT/...) preparatus. Apie kiekvieną vaistą rinkinyje pateikiama ši informacija: Sudėtis ir klasifikacija – veikliosios medžiagos pavadinimas lietuvių kalba ir Anatominis terapinis cheminis (ATCvet) klasifikacijos kodas, leidžiantis vaistus grupuoti pagal jų terapinį poveikį ir veikliosios medžiagos savybes. Paskirtis – indikacijos, t. y. ligos ar būklės, kurioms gydyti ar profilaktikai skirtas vaistas; vaisto paskirties gyvūnų rūšys (pvz., šuo, katė, galvijas, kiaulė, arklys, avis); vartojimo būdas (pvz., leisti į raumenis, naudoti su geriamuoju vandeniu) ir išlauka – laikotarpis, per kurį po vaisto vartojimo draudžiama naudoti gyvūno produkciją (mėsą, pieną, kiaušinius), nurodomas atskirai pagal gyvūno rūšį ir produkto tipą. Farmacinė forma – vaisto forma (pvz., tabletė, injekcinis tirpalas, užlašinamasis tirpalas, geriamoji suspensija). Registracijos duomenys – oficialus registracijos numeris; registracijos įsigaliojimo data; registracijos statusas (pvz., galioja, negalioja); vaisto klasifikacija (receptinis ar nereceptinis), registruotojo pavadinimas; šalis ir šalies kodas pagal ISO 3166-1 alfa-2 standartą. Pakuočių informacija – registruotų pakuočių identifikatoriai;, pavadinimai; kiekiai ir vienetų tipai (pvz., tabletė, flakonas, ampulė, pipetė). Vienas vaistas gali turėti kelias registruotas pakuočių formas, kurios išvardintos per kablelį. Duomenų rinkinys atnaujinamas kiekvieną dieną. Visi duomenys pateikiami atsižvelgiant į teisės aktų keliamus duomenų atvėrimo reikalavimus. Duomenų teikėjas – Valstybinės maisto ir veterinarijos tarnyba. Nuoroda į veterinarinių vaistų registrą: https://vetvaistai.vmvt.lt/. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Medikamentas](medikamentai/Medikamentas.md) | Veterinariniai vaistai | `4` | `med_id` | — | `20` | Lietuvoje registruoti veterinariniai vaistai – jų sudėtis, paskirtis, gamintojas ir registracijos duomenys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/medikamentai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/medikamentai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/medikamentai (https://data.gov.lt/datasets/5343/)

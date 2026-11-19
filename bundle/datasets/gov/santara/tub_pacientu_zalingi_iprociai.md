---
type: Dataset
title: "\"Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai.\""
description: "\"Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis."
resource: "https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai"
tags: [gov, santara, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2871/"
    title: "data.gov.lt DCAT-AP — datasets/gov/santara/tub_pacientu_zalingi_iprociai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# "Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai."

"Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis. Duomenų valdytojas - Nacionalinio visuomenės sveikatos centro prie Sveikatos apsaugos ministerijos (NVSC). Duomenų tvarkytojas - Vilniaus universiteto ligoninė Santaros klinikos (VULSK). Viena duomenų rinkinio eilutė atspindi vieną pacientą kuriam buvo diagnozuota tuberkuliozės liga. Duomenys apima visos Lietuvos tuberkuliozės liga sirgusius bei sergančius asmenis ir informacinėje sistemoje yra kaupiami nuo 2013 m. Atkreipiame dėmesį, kad paciento identifikacinis kodas nebūtinai reiškia unikalų paciento įrašą - vienas pacientas gali turėti kelis identifikacinius kodus, dėl gyvenamosios vietos pasikeitimo, dėl šios priežasties unikalius pacientų įrašus rekomenduojama nustatyti pagal paciento vardo, pavardės, gimimo datos, asmens kodo ir asmens kodo validacijos stulpelius. Taip pat pažymime kad paciento diagnozė gali kisti, paciento gydymo metu ar atliekant papildomus tyrimus. Be to, Pasaulio sveikatos organizacijos (PSO) tuberkuliozės duomenų kaupimo rekomendacijos keitėsi 1996, 1998, 2000, 2014 metais ir galėjo paveikti duomenų surinkimo metodikas bei surinktų duomenų kokybę.Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/santara/tub_pacientu_zalingi_iprociai`[^manifest]
- **Manifest CSV:** [datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai` (`deployed`)[^manifest]
- **Provider:** `santara` — VUL Santaros klinikos *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2871/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai`[^dcat]
- **Portal Title (`@lt`):** Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai[^dcat]
- **Portal Title (`@en`):** Adverse habits of patients diagnosed with tuberculosis[^dcat]
- **Issued (`dct:issued`):** `2024-12-19`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-25` .. `2026-07-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie pacientus, kuriems buvo diagnozuota tuberkuliozė (TB), jų žalingus įpročius, diagnozes ir mirtis. Duomenų valdytojas – Nacionalinis visuomenės sveikatos centras prie Sveikatos apsaugos ministerijos (NVSC). Duomenų tvarkytojas – VšĮ Vilniaus universiteto ligoninė Santaros klinikos (VULSK). Viena duomenų rinkinio eilutė atitinka vieną pacientą, kuriam buvo diagnozuota tuberkuliozė. Duomenys informacinėje sistemoje kaupiami nuo 1996 m. ir apima visus Lietuvoje užregistruotus tuberkulioze sirgusius bei sergančius asmenis. Informacija gaunama iš teisės aktais patvirtintų TB atvejo registravimo formų, kurių turinys, atsižvelgiant į Pasaulio sveikatos organizacijos (PSO) ekspertų rekomendacijas, keitėsi 2000 m., 2014 m., ir 2018 m. Pažymime, kad dėl šių pokyčių tuberkuliozės atvejo registravimo definicijų turinys taip pat laikui bėgant kito, todėl būtina atkreipti dėmesį į registravimo metu galiojusias metodikas. Svarbu paminėti, kad paciento identifikacinis kodas nebūtinai reiškia unikalų paciento įrašą – vienas pacientas gali turėti kelis identifikacinius kodus dėl gyvenamosios vietos pasikeitimo ar dėl patekimo į įkalinimo įstaigą, todėl unikalius pacientų įrašus rekomenduojama nustatyti pagal paciento vardo, pavardės, asmens kodo ir asmens kodo validacijos stulpelius. Be to, gydymo metu, gavus laboratorinių tyrimų rezultatus, paciento diagnozė gali kisti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides data from the Tuberculosis State Information System (TVIS) on patients diagnosed with tuberculosis (TB), their harmful habits, diagnoses and deaths. The controller is the National Public Health Centre under the Ministry of Health (NVSC). Data processor – Vilnius University Hospital Santara Clinic (VULSK). One line of the dataset corresponds to one patient who has been diagnosed with tuberculosis. Data have been accumulated in the information system since 1996 and include all persons with tuberculosis and diseases registered in Lithuania. The information comes from legal forms of TB case registration, the content of which changed in 2000, 2014 and 2018 in line with the recommendations of experts from the World Health Organisation (who). We note that these changes have also resulted in changes in the content of the TB case registration definitions over time, and it is therefore necessary to take into account the methodologies in force at the time of registration. It is important to note that the patient ID does not necessarily mean a unique patient record – one patient may have multiple identification codes due to a change of residence or access to a prison facility, so it is recommended to set unique patient records based on the validation columns of the patient's name, surname, personal number and personal number. In addition, the patient's diagnosis may vary with the results of laboratory tests during treatment. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TubPacientoZalingasIprotis](tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis.md) | "Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai." | `4` | `paciento_id` | — | `20` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/santara/tub_pacientu_zalingi_iprociai (https://data.gov.lt/datasets/2871/)

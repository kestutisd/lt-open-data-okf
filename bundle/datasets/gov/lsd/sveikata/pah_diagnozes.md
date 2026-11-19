---
type: Dataset
title: "\"Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys\""
description: "\"Rinkinyje pateikiami asmenų, kuriems įrašyta plaučių arterinės hipertenzijos (PAH) diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai), duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes"
tags: [gov, lsd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes"
    author: "team:vda"
    last_modified: "2026-05-06T00:00:00Z"
---

# "Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys"

"Rinkinyje pateikiami asmenų, kuriems įrašyta plaučių arterinės hipertenzijos (PAH) diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai), duomenys. Rinkinį sudaro trys lentelės: 1) Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip pagrindinė, lydinti arba skyriaus diagnozė. Pateikiama jų gimimo data (metų tikslumu), kiekvieno PAH diagnozės kodo pirmo įrašymo data, mirties data (mėnesio tikslumu) bei pagrindinė mirties priežastis, 2) PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas, 3) Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. Pateikiama recepto išrašymo data (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas, požymis, ar vaistas išduotas, savivaldybė, kurioje veikiančioje įstaigoje išduotas vaistas (nustatoma pagal įstaigos filialą, kuriame dirba išdavęs specialistas tuo metu). Duomenų šaltiniai: SVEIDRA – Privalomojo sveikatos draudimo informacinė sistema, ambulatorinių paslaugų apskaitos posistemė (APAP), stacionarinių paslaugų apskaitos posistemė (SPAP), ESPBI IS – Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinė sistema, E. recepto posistemė, Mirties atvejų ir jų priežasčių valstybės registras."[^manifest]

- **Namespace:** `datasets/gov/lsd/sveikata/pah_diagnozes`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3888/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes`[^dcat]
- **Portal Title (`@lt`):** Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys[^dcat]
- **Portal Title (`@en`):** Treatment data for patients with pulmonary arterial hypertension[^dcat]
- **Issued (`dct:issued`):** `2025-08-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-05-06`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-08-19` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami asmenų, kuriems įrašyta plaučių arterinės hipertenzijos (PAH) diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai), duomenys. Rinkinį sudaro trys lentelės: 1) Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a), kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a), kaip pagrindinė, lydinti arba skyriaus diagnozė. Pateikiama jų gimimo data (gyviems pacientams metų tikslumu, mirusiems mėnesio tikslumu), kiekvieno PAH diagnozės kodo pirmo įrašymo data, mirties data (mėnesio tikslumu) bei pagrindinė mirties priežastis, 2) PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas, riociguatas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas. 3). Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. Pateikiama recepto išrašymo data (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas, požymis, ar vaistas išduotas, savivaldybė, kurioje veikiančioje įstaigoje išduotas vaistas (nustatoma pagal įstaigos filialą, kuriame dirba išdavęs specialistas tuo metu). Duomenų šaltiniai: SVEIDRA – Privalomojo sveikatos draudimo informacinė sistema, ambulatorinių paslaugų apskaitos posistemė (APAP), stacionarinių paslaugų apskaitos posistemė (SPAP), ESPBI IS – Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinė sistema, E. recepto posistemė, Mirties atvejų ir jų priežasčių valstybės registras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The kit contains data for individuals with a diagnosis of pulmonary arterial hypertension (PAH) (I27 .0, I27 .2, I27 .8 TLK-10-AM codes). The kit consists of three tables: (1) Persons with PAH diagnosis (I27 .0, I27 .2, I27 .8 TLK-10-AM codes) on the VLK SVEIDRA Outpatient Treatment Statistical Card (F025/a) as the main diagnosis, or on the Statistical Card (F066/a) as the main, accompanying or department diagnosis. Their date of birth (year precision), date of first entry of each PAH diagnostic code, date of death (month precision) and main cause of death, 2) Date of first and last prescription for PAH specific treatment (ambrisentan, bosentan, iloprost, sildenafil, treprostinil, macitentan, selexypagne), drug ATC code, common name, 3) All valid diagnostics of L.27, IX-10. The date of prescription (with noise up to 5 days), the ATC code of the medicinal product, the general name, the indication of whether the medicinal product has been dispensed, the municipality in which the medicinal product was dispensed (determined by the branch of the institution where the issuing professional is employed at that time) shall be provided. Data sources: SVEIDRA – Compulsory Health Insurance Information System, Outpatient Services Accounting Subsystem (APAP), Inpatient Service Accounting Subsystem (SPAP), ESPBI IS – Information System for Electronic Health Services and Cooperation Infrastructure, E-prescription Subsystem, State Register of Death Cases and Their Reasons[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PAHDiagnoze](pah_diagnozes/PAHDiagnoze.md) | "Asmenys, kuriems diagnozuota PAH" | `4` | `vda_prime_key` | — | `9` | "Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip... |
| [PAHSpecReceptas](pah_diagnozes/PAHSpecReceptas.md) | PAH specifiniam gydymui skiriamų vaistų receptai | `4` | `vda_prime_key` | — | `6` | "PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir... |
| [PAHVisiReceptai](pah_diagnozes/PAHVisiReceptai.md) | "Visi galiojantys receptai, išrašyti nurodant PAH diagnozę" | `4` | `vda_prime_key` | — | `9` | "Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes (https://data.gov.lt/datasets/3888/)

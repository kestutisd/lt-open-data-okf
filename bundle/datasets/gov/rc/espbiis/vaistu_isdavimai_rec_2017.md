---
type: Dataset
title: "Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistema"
description: "e.Sveikatos (ESPBIIS) e.Recepto posistemės duomenys apie vaistinių išduotus, pagal gydytojo receptą paskirtus, vaistus."
resource: "https://get.data.gov.lt/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2557/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017"
    author: "team:vda"
    last_modified: "2026-05-21T00:00:00Z"
---

# Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistema

- **Namespace:** `datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2557/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017`[^dcat]
- **Portal Title (`@lt`):** ESPBI IS e. Recepto posistemės duomenys apie vaistinių išduotus receptinius vaistus[^dcat]
- **Portal Title (`@en`):** Espbiis_i Ship Pharmaceuticals[^dcat]
- **Issued (`dct:issued`):** `2024-03-05`[^dcat]
- **Last Modified (`dct:modified`):** `2026-05-21`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-03-05` .. `2026-05-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

e.Sveikatos (ESPBIIS) e.Recepto posistemės duomenys apie vaistinių išduotus, pagal gydytojo receptą paskirtus, vaistus. Terminas „VAISTAS“ šiame duomenų rinkinyje naudojamas kaip bendrinis pavadinimas visiems su receptu skiriamiems medicininiams produktams (vaistinis preparatas, medicinos pagalbos priemonė (MPP), vardinis vaistas, ekstemporalus vaistas, kitos priemonės). Duomenų nuasmeninimo kriterijai: 1. Jeigu per ketvirtį vienam TLK-10-AM kodui išrašytų receptų skaičius yra mažesnis nei 10, duomenų rinkinyje pateikiamas tik dirbtinis išrašyto recepto identifikatorius, recepto išrašymo metai bei ketvirtis ir diagnozės (TLK-10-AM klasifikatoriaus), pagal kurią išrašytas receptas, kodas bei pavadinimas. 2. Jeigu per ketvirtį vienam TLK-10-AM kodui vienoje savivaldybėje, kurioje yra receptą išrašiusi gydymo įstaiga, išrašytų receptų skaičius yra mažesnis nei 5, įstaigos, kurioje buvo išrašytas receptas, savivaldybė nenurodoma. 3. Jeigu per ketvirtį vienam TLK-10-AM kodui vienoje savivaldybėje, kurioje pacientas yra deklaravęs gyvenamąją vietą, išrašytų receptų skaičius yra mažesnis nei 5, paciento deklaruotos gyvenamosios vietos savivaldybė nenurodoma. 4. Jeigu per ketvirtį vienoje savivaldybėje, kurioje yra receptą išrašiusi gydymo įstaiga, receptus išrašiusių gydytojų, turinčių tą pačią kvalifikaciją, skaičius yra mažesnis nei 3, gydytojo kvalifikacija nenurodoma.[^dcat]

### Portal Description (`@en`)

ESPBI IS e-prescription subsystem data on medicines issued according to a doctor's prescription. Criteria for data anonymisation: 1. If the number of prescriptions issued per TLK-10-AM code is less than 10 per quarter, the dataset shall contain only the artificial identifier of the prescription issued, the year and quarter of the prescription and the code and name of the diagnosis (TLK-10-AM classification) used for the prescription. 2. If within a quarter the number of prescriptions issued per TLK-10-AM code in one municipality where the medical institution which wrote the prescription is located is less than 5, the municipality of the institution where the prescription was issued shall not be indicated. 3. If within a quarter the number of prescriptions issued for one TLK-10-AM code in one municipality where the patient has declared his place of residence is less than 5, the municipality of the place of residence declared by the patient shall not be indicated. 4. If, within a quarter, the number of doctors who have written prescriptions in one municipality where the medical institution has written the prescription is less than 3, the doctor's qualification shall not be specified.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VaistoIsdavimas](vaistu_isdavimai_rec_2017/VaistoIsdavimas.md) | ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus pagal 2017 m. išrašytus receptus | `4` | `dirbt_isdavimo_id` | — | `12` | ESPBI IS e. recepto posistemės duomenys apie skiriamus vaistus*. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2017 (https://data.gov.lt/datasets/2557/)

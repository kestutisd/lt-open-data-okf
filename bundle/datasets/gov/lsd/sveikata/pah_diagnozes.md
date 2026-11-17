---
type: Dataset
title: "Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys"
description: "Rinkinyje pateikiami asmenų, kuriems įrašyta plaučių arterinės hipertenzijos (PAH) diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai), duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys

Rinkinyje pateikiami asmenų, kuriems įrašyta plaučių arterinės hipertenzijos (PAH) diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai), duomenys.

Rinkinį sudaro trys lentelės:

1) Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip pagrindinė diagnozė, arba stacionare gydomo asmens statistinė kortelėje (F066/a) kaip pagrindinė, lydinti arba skyriaus diagnozė. Pateikiama jų gimimo data (metų tikslumu), kiekvieno PAH diagnozės kodo pirmo įrašymo data, mirties data (mėnesio tikslumu) bei pagrindinė mirties priežastis,

2) PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas,

3) Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. Pateikiama recepto išrašymo data (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas, požymis, ar vaistas išduotas, savivaldybė, kurioje veikiančioje įstaigoje išduotas vaistas (nustatoma pagal įstaigos filialą, kuriame dirba išdavęs specialistas tuo metu).

Duomenų šaltiniai: SVEIDRA – Privalomojo sveikatos draudimo informacinė sistema, ambulatorinių paslaugų apskaitos posistemė (APAP), stacionarinių paslaugų apskaitos posistemė (SPAP), ESPBI IS – Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinė sistema, E. recepto posistemė, Mirties atvejų ir jų priežasčių valstybės registras.

- **Namespace:** `datasets/gov/lsd/sveikata/pah_diagnozes`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PAHDiagnoze](pah_diagnozes/PAHDiagnoze.md) | Asmenys, kuriems diagnozuota PAH | `4` | `vda_prime_key` | — | 9 | Asmenys, kuriems buvo įrašyta PAH diagnozė (I27.0, I27.2, I27.8 TLK-10-AM kodai) VLK SVEIDRA ambulatorinio gydymo statistinėje kortelėje (F025/a) kaip... |
| [PAHSpecReceptas](pah_diagnozes/PAHSpecReceptas.md) | PAH specifiniam gydymui skiriamų vaistų receptai | `4` | `vda_prime_key` | — | 6 | PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir... |
| [PAHVisiReceptai](pah_diagnozes/PAHVisiReceptai.md) | Visi galiojantys receptai, išrašyti nurodant PAH diagnozę | `4` | `vda_prime_key` | — | 9 | Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv

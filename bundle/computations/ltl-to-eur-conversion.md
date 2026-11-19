---
type: Attested Computation
title: "Statutory LTL to EUR Currency Conversion"
description: "Converts historical Lithuanian litas (LTL) amounts to euros (EUR) using the irrevocable EU conversion rate 3.45280 and Council Regulation (EC) No 1103/97 half-up cent rounding."
tags: [currency, eur, ltl, conversion, statutory]
runtime: python
parameters:
  - { name: ltl_amount, type: number, required: true }
executor:
  resource: "/references/executors/ltl_to_eur.py"
  receipt: [ltl_amount, rate_used, unrounded_eur, eur_amount, computation_sha256]
attester:
  resource: "/references/attesters/ltl_to_eur_attester.py"
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: std-eur
    resource: "https://publications.europa.eu/resource/celex/32014R0851"
    title: "Council Regulation (EU) No 851/2014 amending Regulation (EC) No 2866/98 as regards the conversion rate to the euro for Lithuania"
    author: "team:eu-publications-office"
    last_modified: "2014-07-23T00:00:00Z"
  - id: std-eur-1103
    resource: "https://publications.europa.eu/resource/celex/31997R1103"
    title: "Council Regulation (EC) No 1103/97 on certain provisions relating to the introduction of the euro (Articles 4–5)"
    author: "team:eu-publications-office"
    last_modified: "1997-06-19T00:00:00Z"
  - id: std-lt-euro-law
    resource: "https://www.e-tar.lt/portal/lt/legalAct/dad7f330cca211e387b1ebf12f4d03f3"
    title: "Lietuvos Respublikos euro įvedimo Lietuvos Respublikoje įstatymas (2014-04-17 Nr. XII-828)"
    author: "team:lr-seimas"
    last_modified: "2014-04-17T00:00:00Z"
---

# Computation

```python
from decimal import Decimal, ROUND_HALF_UP

LTL_PER_EUR_RATE = Decimal("3.45280")
EUR_CENT = Decimal("0.01")


def convert_ltl_to_eur(ltl_amount: Decimal | int | float | str) -> Decimal:
    amount = Decimal(str(ltl_amount))
    return (amount / LTL_PER_EUR_RATE).quantize(EUR_CENT, rounding=ROUND_HALF_UP)
```

Sanctioned conversion of historical Lithuanian litas (`LTL`, `1993-06-25` – `2014-12-31`) monetary amounts into euros (`EUR`, effective `2015-01-01`) under **Council Regulation (EU) No 851/2014** (`1 EUR = 3.45280 LTL`),[^std-eur] **Council Regulation (EC) No 1103/97** Articles 4–5 (prohibiting inverse rate truncation or intermediate rounding and mandating commercial half-up cent rounding `ROUND_HALF_UP`),[^std-eur-1103] and the **Law on the Adoption of the Euro in the Republic of Lithuania (No. XII-828)**.[^std-lt-euro-law] See [Lithuanian Currency History](../references/lt-valiutos-istorija.md) for historical `SUR`, `LTT`, `LTL`, and `EUR` validity windows.

# Attestation Rules

The consumer-side attester at [`/references/attesters/ltl_to_eur_attester.py`](../references/attesters/ltl_to_eur_attester.py) verifies every receipt emitted by [`/references/executors/ltl_to_eur.py`](../references/executors/ltl_to_eur.py) without network calls or LLMs:

1. **Exact 6-Significant-Figure Statutory Rate:** `receipt["rate_used"]` must equal the exact string `"3.45280"` (any rounded inverse factor such as `0.28962` or truncated `3.45` fails attestation).[^std-eur][^std-eur-1103]
2. **Code Provenance (`computation_sha256`):** Canonicalized `# Computation` code SHA-256 must match `receipt["computation_sha256"]`.
3. **Decimal Half-Up Fidelity (`ROUND_HALF_UP`):** Recomputes `(Decimal(str(receipt["ltl_amount"])) / Decimal("3.45280")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` (avoiding IEEE-754 float drift and Python `round()` banker's `ROUND_HALF_EVEN`) and checks exact equality against both `receipt["eur_amount"]` and `claimed_value`.[^std-eur-1103][^std-lt-euro-law]

# Examples

```bash
python references/executors/ltl_to_eur.py 1000 --json
python references/attesters/ltl_to_eur_attester.py --receipt '{"ltl_amount":"1000","rate_used":"3.45280","unrounded_eur":"289.6200185356811862835959222","eur_amount":289.62,"eur_decimal":"289.62","computation_sha256":"8148194b64fdc4db1509edf19ae2bfd2d912f72cd518848476f9f5abd919cb87"}' --claimed 289.62 --sanctioned-code computations/ltl-to-eur-conversion.md
```

[^std-eur]: Council Regulation (EU) No 851/2014 amending Regulation (EC) No 2866/98 as regards the conversion rate to the euro for Lithuania (https://publications.europa.eu/resource/celex/32014R0851)
[^std-eur-1103]: Council Regulation (EC) No 1103/97 on certain provisions relating to the introduction of the euro, Articles 4–5 (https://publications.europa.eu/resource/celex/31997R1103)
[^std-lt-euro-law]: Lietuvos Respublikos euro įvedimo Lietuvos Respublikoje įstatymas, 2014-04-17 Nr. XII-828 (https://www.e-tar.lt/portal/lt/legalAct/dad7f330cca211e387b1ebf12f4d03f3)

#!/usr/bin/env python3
# Copyright 2026 Lithuanian Open Data OKF Bundle Contributors
# SPDX-License-Identifier: Apache-2.0

"""Deterministic Python executor for Statutory LTL to EUR Currency Conversion.

Implements Council Regulation (EU) No 851/2014 (1 EUR = 3.45280 LTL) and
Council Regulation (EC) No 1103/97 Articles 4-5 (6 significant figures and
half-up cent rounding). Pure Python 3.9+ standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from typing import Any

LTL_PER_EUR_RATE = Decimal("3.45280")
EUR_CENT = Decimal("0.01")

SANCTIONED_CODE = """from decimal import Decimal, ROUND_HALF_UP

LTL_PER_EUR_RATE = Decimal("3.45280")
EUR_CENT = Decimal("0.01")


def convert_ltl_to_eur(ltl_amount: Decimal | int | float | str) -> Decimal:
    amount = Decimal(str(ltl_amount))
    return (amount / LTL_PER_EUR_RATE).quantize(EUR_CENT, rounding=ROUND_HALF_UP)"""


def canonicalize_code(code: str) -> str:
    """Strip blank lines and comment lines for deterministic SHA-256 hashing."""
    lines = []
    for raw_line in code.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return "\n".join(lines)


COMPUTATION_SHA256 = hashlib.sha256(canonicalize_code(SANCTIONED_CODE).encode("utf-8")).hexdigest()


def convert_ltl_to_eur(ltl_amount: Decimal | int | float | str) -> Decimal:
    """Convert `ltl_amount` to EUR rounded half-up to 0.01 EUR."""
    amount = Decimal(str(ltl_amount))
    return (amount / LTL_PER_EUR_RATE).quantize(EUR_CENT, rounding=ROUND_HALF_UP)


def execute(ltl_amount: Decimal | int | float | str) -> dict[str, Any]:
    """Execute the sanctioned LTL-to-EUR conversion and return an OKF v0.3 receipt."""
    if isinstance(ltl_amount, bool) or ltl_amount is None:
        raise ValueError(f"Invalid ltl_amount: {ltl_amount!r}")
    raw_str = str(ltl_amount).strip()
    if not raw_str:
        raise ValueError("ltl_amount must not be empty")
    try:
        with localcontext() as ctx:
            ctx.prec = 28
            amount = Decimal(raw_str)
            if not amount.is_finite():
                raise ValueError(f"ltl_amount must be finite, got {ltl_amount!r}")
            unrounded = amount / LTL_PER_EUR_RATE
            rounded = unrounded.quantize(EUR_CENT, rounding=ROUND_HALF_UP)
    except InvalidOperation as exc:
        raise ValueError(f"Cannot parse ltl_amount {ltl_amount!r} as Decimal") from exc

    return {
        "ltl_amount": format(amount, "f"),
        "rate_used": "3.45280",
        "unrounded_eur": format(unrounded, "f"),
        "eur_amount": float(rounded),
        "eur_decimal": format(rounded, ".2f"),
        "computation_sha256": COMPUTATION_SHA256,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert historical Lithuanian litas (LTL) to euros (EUR) at 1 EUR = 3.45280 LTL."
    )
    parser.add_argument("ltl_amount", help="Nominal LTL amount to convert (e.g. 345.28 or 1000).")
    parser.add_argument("--json", action="store_true", help="Emit JSON receipt (default output format).")
    args = parser.parse_args(argv)
    try:
        receipt = execute(args.ltl_amount)
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

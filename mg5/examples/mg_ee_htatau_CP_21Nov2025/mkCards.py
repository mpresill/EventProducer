import os
import itertools

# ------------------------------------------------------------
# USER CONFIGURATION
# ------------------------------------------------------------

TEMPLATE_FILE = "template.mg5"
OUTPUT_DIR = "generated_cards"

# Operator name → operator string to append
OPERATORS = {
    "ceHRe":    "smeft 100",
    "ceHIm":    "smeftcpv 45",
    "cHB":      "smeft 8",
    "cHBtil":   "smeftcpv 5",
    "cHW":      "smeft 7",
    "cHWtil":   "smeftcpv 4",
    "cHWB":     "smeft 9",
    "cHWBtil":  "smeftcpv 6",
}

# ------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------

def load_template():
    with open(TEMPLATE_FILE, "r") as f:
        return f.read()

def append_operator_settings(card_text, operator_values):
    """
    Append at the end of the template:
       set <OPERATOR> <VALUE>
    for all operators provided in operator_values dict.
    """
    append_lines = ["", "# ---- SMEFT OPERATOR OVERRIDES ----"]
    for op_name, value in operator_values.items():
        tag = OPERATORS[op_name]  # e.g. 'smeft 100'
        append_lines.append(f"set {tag} {value}")

    return card_text + "\n" + "\n".join(append_lines) + "\n"

def write_card(name, content):
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w") as f:
        f.write(content)

# ------------------------------------------------------------
# MAIN GENERATION LOGIC
# ------------------------------------------------------------

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    template = load_template()

    # -------------------------------
    # 1) Single operator ±1
    # -------------------------------
    for op in OPERATORS:
        for val, sval in [(1, "p1"), (-1, "m1")]:
            operator_values = {op: val}  # only one operator modified
            card = append_operator_settings(template, operator_values)

            filename = f"card_{op}_{sval}.mg5"
            write_card(filename, card)
            print("Generated:", filename)

    # ------------------------------------
    # 2) Pairs of operators = +1 together
    # ------------------------------------
    for op1, op2 in itertools.combinations(OPERATORS.keys(), 2):
        operator_values = {op1: 1, op2: 1}
        card = append_operator_settings(template, operator_values)

        filename = f"card_{op1}__{op2}_p1_p1.mg5"
        write_card(filename, card)
        print("Generated:", filename)

    print("\nAll cards generated inside:", OUTPUT_DIR)

import json, re, pathlib

BUILD = pathlib.Path("/home/yunshan/Documents/KTHAnteckningar/DD2395_AIGuide/.study_guide_build")
OUT = pathlib.Path("/home/yunshan/Documents/KTHAnteckningar/DD2395_AIGuide/study_guide.tex")

tmpl = (BUILD / "TEMPLATE_v2.tex").read_text()
preamble = tmpl.split("% --- BEGIN REPEATING SECTION FOR EACH QUESTION TYPE ---")[0]

cluster = json.loads((BUILD / "cluster.json").read_text())["question_types"]

SHORT_NAMES = [
    "Custom hash-function analysis",
    "Cache/timing side channels",
    "Memory-safety exploits",
    "Bell-LaPadula access control",
    "Protocol flaw analysis",
    "Concept true/false",
    "Custom block-cipher modes",
    "Web attacks (XSS/CSRF/SQLi)",
    "Password storage analysis",
    "DoS construction/countermeasures",
    "Social-engineering scenarios",
]

def san(s: str) -> str:
    s = s.replace("\u2014", "---").replace("\u2013", "--")
    s = re.sub(r"\\q\{([^{}]*)\}", r"``\1''", s)
    s = s.replace("$\\&M' = \\&M + r$", "\\&M' = \\&M + r")
    return s

def esc_kw(s: str) -> str:
    if "^" in s:
        return "$" + s.replace("^", "^") + "$"
    for a, b in [("&", "\\&"), ("%", "\\%"), ("$", "\\$"), ("#", "\\#"),
                 ("_", "\\_"), ("~", "\\textasciitilde")]:
        s = s.replace(a, b)
    return s

def texstr(x):
    if isinstance(x, str):
        return san(x)
    raise TypeError(type(x))

parts = [preamble.rstrip(), ""]

for i, qt in enumerate(cluster):
    sch = json.loads((BUILD / "v2" / f"scheme_{i:02d}.json").read_text())
    n = i + 1
    out = []
    out.append(f"\\section{{Question Type {n}: {san(qt['name'])}}}")
    out.append("")
    out.append("\\subsection*{Theory Background}")
    out.append("")
    out.append("\n\n".join(texstr(p) for p in sch["theory_paragraphs"]))
    out.append("")
    out.append("\\begin{theorybox}")
    out.append("\\begin{tightitem}")
    for b in sch["theory_cheatsheet"]:
        out.append(f"\\item {texstr(b)}")
    out.append("\\end{tightitem}")
    out.append("\\end{theorybox}")
    out.append("")
    out.append("\\subsection*{How to Identify}")
    out.append("")
    kws = ", ".join(f"``{esc_kw(k)}''" for k in sch["identify_keywords"])
    out.append(
        f"Use this scheme when the problem provides {texstr(sch['identify_givens'])} "
        f"and asks you to produce the following: {texstr(sch['identify_target'])} "
        f"Look for keywords like: \\textit{{{kws}}}."
    )
    out.append("")
    out.append(f"\\begin{{schemebox}}{{{texstr(sch['strategy_name'])}}}")
    out.append("\\begin{enumerate}[label=\\textbf{Step \\arabic*:}, leftmargin=*]")
    for st in sch["algorithm"]:
        out.append(f"    \\item \\textbf{{{texstr(st['action'])}:}} {texstr(st['detail'])}")
    out.append("\\end{enumerate}")
    out.append("\\end{schemebox}")
    out.append("")
    out.append("\\begin{trapbox}")
    out.append("\\begin{itemize}")
    for j, v in enumerate(sch["variations"], 1):
        out.append(f"    \\item \\textbf{{Variation {j} ({texstr(v['name'])}):}} {texstr(v['detail'])}")
    out.append("\\end{itemize}")
    out.append("\\end{trapbox}")
    out.append("")
    out.append("\\subsection*{Worked Example (Mapped to Scheme)}")
    out.append("")
    out.append(f"\\textbf{{Problem (original practice question):}} {texstr(sch['original_problem'])}")
    out.append("")
    out.append("\\textbf{Solution:}")
    out.append("\\begin{itemize}")
    for st in sch["original_steps"]:
        out.append(f"    \\item \\textit{{Applying {texstr(st['step_ref'])}:}} {texstr(st['work'])}")
    out.append("\\end{itemize}")
    out.append("")
    refs = ", ".join(san(r) for r in sch["practice_refs"])
    out.append(f"\\textit{{For more practice, see past-exam instances:}} {refs}")
    out.append("")
    parts.append("\n".join(out))

cov = ["\\section*{Coverage Note}", "",
       "The eleven question types below cover the recurring patterns found across the analyzed DD2395 exams and re-exams.",
       "\\begin{itemize}"]
for i, qt in enumerate(cluster):
    cov.append(f"    \\item \\textbf{{Question Type {i+1} ({SHORT_NAMES[i]}):}} appeared in approximately {qt['frequency']} analyzed exam questions.")
cov.append("\\end{itemize}")
cov.append("")
cov.append("\\end{document}")
parts.append("\n".join(cov))

OUT.write_text("\n".join(parts) + "\n")
print("sections written:", len(cluster))

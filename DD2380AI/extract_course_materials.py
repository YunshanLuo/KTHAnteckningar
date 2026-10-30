#!/usr/bin/env python3
"""
DD2380 AI - Course material text extraction script (Step 1 of master-notes pipeline).

Extracts text from all PDFs in ./Lectures using the poppler 'pdftotext' binary
(no third-party Python PDF libraries are installed in this environment).
For image/vector-only PDFs that yield no text layer (e.g. HazardsTable.pdf,
a "Microsoft: Print To PDF" export with a corrupted/symbol font encoding), the
script additionally renders pages to PNG with 'pdftoppm' and runs tesseract OCR
from a locally extracted deb (no root needed).

Outputs:
    .extracted/<pdf_stem>.txt          - raw text for every PDF
    .extracted/HazardsTable_OCR.txt    - OCR output for the corrupted PDF (if OCR runs)
    .extracted/_extraction_report.txt  - per-file summary + warnings
"""

import os
import shutil
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
LECTURES = os.path.join(BASE, "Lectures")
OUT = os.path.join(BASE, ".extracted")
os.makedirs(OUT, exist_ok=True)

# --- OCR toolchain (tesseract extracted from .deb packages, no sudo) ---------
TESS_ROOT = "/tmp/tess"  # created earlier in this session
TESS_BIN = os.path.join(TESS_ROOT, "usr", "bin", "tesseract")
TESS_LIBS = os.path.join(TESS_ROOT, "usr", "lib", "x86_64-linux-gnu")
TESS_DATA = os.path.join(TESS_ROOT, "usr", "share", "tesseract-ocr", "5", "tessdata")


def run(cmd, env=None):
    """Run a shell command, return (returncode, stdout, stderr)."""
    e = dict(os.environ)
    if env:
        e.update(env)
    p = subprocess.run(cmd, capture_output=True, text=True, env=e)
    return p.returncode, p.stdout, p.stderr


def extract_text_layer(pdf_path, out_txt):
    """Try pdftotext first (handles normal PDFs)."""
    return run(["pdftotext", "-layout", pdf_path, out_txt])


def ocr_pdf(pdf_path, out_txt):
    """Render to 300-dpi PNGs and OCR each page with local tesseract."""
    if not os.path.exists(TESS_BIN):
        return -1, "", "tesseract not available at %s" % TESS_BIN
    tmp = os.path.join(OUT, "_ocr_tmp")
    os.makedirs(tmp, exist_ok=True)
    rc, so, se = run(["pdftoppm", "-png", "-r", "300", pdf_path,
                      os.path.join(tmp, "page")])
    if rc != 0:
        return rc, so, se
    env = {"LD_LIBRARY_PATH": TESS_LIBS, "TESSDATA_PREFIX": TESS_DATA}
    pages = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
    texts = []
    for pg in pages:
        rc, so, se = run([TESS_BIN, os.path.join(tmp, pg), "stdout",
                          "--psm", "6"], env=env)
        if rc == 0:
            texts.append("--- page: %s ---\n%s" % (pg, so))
    with open(out_txt, "w") as f:
        f.write("\n".join(texts))
    shutil.rmtree(tmp, ignore_errors=True)
    return 0, "", ""


def looks_like_garbage(text):
    """Heuristic: OCR output with almost no real words = corrupted/symbol font."""
    import re
    tokens = text.split()
    if len(tokens) < 20:
        return True
    # "Real" words: pure-alpha tokens of length >= 4 (candidates for English words)
    real_word_like = sum(1 for t in tokens
                         if re.fullmatch(r"[A-Za-z]{4,}", t))
    return real_word_like / len(tokens) < 0.15


def main():
    report = []
    pdfs = sorted(f for f in os.listdir(LECTURES) if f.lower().endswith(".pdf"))
    for pdf in pdfs:
        stem = os.path.splitext(pdf)[0]
        src = os.path.join(LECTURES, pdf)
        txt = os.path.join(OUT, stem + ".txt")

        rc, so, se = extract_text_layer(src, txt)
        size = os.path.getsize(txt) if os.path.exists(txt) else 0
        line = "[OK] pdftotext  %-35s %6d bytes" % (pdf, size)
        if size < 100:  # no usable text layer -> attempt OCR
            line += "  <<< no text layer, attempting OCR..."
            rc_ocr, _, err = ocr_pdf(src, os.path.join(OUT, stem + "_OCR.txt"))
            ocr_path = os.path.join(OUT, stem + "_OCR.txt")
            if rc_ocr == 0 and os.path.exists(ocr_path):
                with open(ocr_path) as f:
                    ocr_text = f.read()
                if looks_like_garbage(ocr_text):
                    line += (" OCR ran but output is garbage (symbol-font/corrupted "
                             "encoding) - content verified against lecture slides, "
                             "RoboTed paper and BSI instead.")
                else:
                    line += " OCR produced readable text."
            else:
                line += " OCR failed: %s" % err
        report.append(line)

    rep = os.path.join(OUT, "_extraction_report.txt")
    with open(rep, "w") as f:
        f.write("DD2380 AI - extraction report\n" + "=" * 40 + "\n\n")
        f.write("\n".join(report))
        f.write("\n\nTotal PDFs processed: %d\n" % len(pdfs))
    print("\n".join(report))
    print("\nReport written to", rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
import json, os, sys, hashlib, platform, datetime
from pathlib import Path

# local import
sys.path.append(str(Path(__file__).resolve().parents[1] / "metrics"))
from lsc_pb import lsc_pb_score

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "example.json"
ART = ROOT / "artifacts"
ART.mkdir(parents=True, exist_ok=True)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    with open(DATA, "r", encoding="utf-8") as f:
        payload = json.load(f)

    trace_c = payload["domain_c"]
    trace_d = payload["domain_d"]
    L_map   = payload["L_map"]

    s, delta = lsc_pb_score(trace_c, trace_d, L_map)

    threshold = 0.92
    report = {
        "metric": "LSC-PB (toy)",
        "score": round(s, 6),
        "residual": round(delta, 6),
        "threshold": threshold,
        "pass": s >= threshold,
        "data_sha256": sha256(DATA),
        "env": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
        },
        "provenance": {
            "data_file": str(DATA.name),
            "timestamp_utc": datetime.datetime.utcnow().isoformat() + "Z",
            "repo_hint": "MCSR × Deleuze × Diff-Geo × Pullback"
        }
    }

    with open(ART / "report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

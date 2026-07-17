from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("controller_model", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("controller_model", args.controller_model)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to import controller model")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    report = {
        "current_d3a_counterexamples": module.current_d3a_counterexamples(),
        "desired_fault_matrix": module.run_fault_matrix(),
        "desired_randomized_model": module.randomized_model_runs(),
        "mutation_tests": module.mutation_tests(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "counterexamples": len(report["current_d3a_counterexamples"]),
                "admission_fault_cases": len(report["desired_fault_matrix"]["admission"]),
                "drain_fault_cases": len(report["desired_fault_matrix"]["drain"]),
                "randomized": report["desired_randomized_model"],
                "mutation_tests": report["mutation_tests"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

import logging
import pandas as pd
import config
from metrics import detect_continuous_drift
from typing import Dict, Any
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_drift_monitor() -> Dict[str, Any]:
    ref_data = pd.read_csv(config.REF_DATA_PATH)
    live_data = pd.read_csv(config.LIVE_BATCH_DATA_PATH)
    drift_report={}

    for col in config.NUMERICAL_COLUMNS:
        drift_report[col] = detect_continuous_drift(ref_data[col], live_data[col], config.DRIFT_THRESHOLD_P_VALUE)

        if drift_report[col]['drift_detected']:
            logging.warning(f"DRIFT DETECTED in feature: {col}. p-value: {drift_report[col]['p_value']}")
        else:
            logging.info(f"Feature {col} is stable.")
    return drift_report

if __name__ == "__main__":
    report = run_drift_monitor()
    with open("drift_report.json", "w") as f:
        json.dump(report,f, indent=4)
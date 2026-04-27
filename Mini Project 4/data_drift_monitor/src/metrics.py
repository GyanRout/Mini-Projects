from scipy.stats import ks_2samp
import pandas as pd
from typing import Dict, Any

def detect_continuous_drift(ref_series: pd.Series, live_series: pd.Series, threshold: float) -> Dict[str, Any]:
    # Unpack normally, but tell Pylance to ignore the type checking for this specific line
    statistic, p_value = ks_2samp(ref_series, live_series)  # type: ignore
    
    drift_detected = p_value < threshold
    
    return {
        "drift_detected": bool(drift_detected),
        "p_value": float(p_value),
        "ks_statistic": float(statistic)
    }
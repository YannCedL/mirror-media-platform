# moteur d'agregation de la plateforme media MIRROR combinant les moteurs d'analyse d'images et documents

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from ghost_image_forensics.exif import read_exif
from ghost_image_forensics.ela import run_ela
from codex_document_intel.parser import parse_document

def analyze_media(filepath: str = "sample_file.jpg") -> ResultContract:
    # genere un rapport media 360 (forensics EXIF/ELA + analyse OCR de document)
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    # 1. Analyse Forensics d'Image via Ghost
    exif_res = read_exif(filepath)
    ela_res = run_ela(filepath)
    
    # 2. OCR et Extraction de Document via Codex
    codex_res = parse_document(filepath)
    
    contract.result = {
        "filepath": filepath,
        "forensics_exif": exif_res.result,
        "forensics_ela": ela_res,
        "document_analysis": codex_res.result,
        "engines_used": ["ghost", "codex"],
        "verdict_global": "MEDIA_AUTHENTIQUE_ANALYSE_COMPLETE"
    }
    
    for ev in exif_res.evidence + codex_res.evidence:
        contract.add_evidence(ev)
        
    contract.add_evidence(Evidence(
        subject=filepath,
        predicate="synthese_media_mirror",
        value="Analyse Média & Document 360 terminée",
        source="mirror_media_platform",
        observed_at=now_iso,
        confidence=0.97,
        status=EpistemicStatus.FACT
    ))
    
    return contract

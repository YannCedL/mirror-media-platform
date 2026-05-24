# test du rapport media 360 de la plateforme Mirror
from mirror_media_platform.engine import analyze_media

def test_analyse_media_360():
    contract = analyze_media("preuve.jpg")
    assert contract is not None
    assert contract.result["forensics_exif"]["camera_model"] is not None
    assert contract.result["document_analysis"]["word_count"] > 0
    assert len(contract.evidence) >= 2

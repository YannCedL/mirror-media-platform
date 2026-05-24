from mirror_media_platform import analyze_media

def test_analyze_media():
    c = analyze_media("rapport.pdf")
    assert "codex" in c.result["engines_used"]
    assert c.confidence > 0.9

from app import analyze_sentiment

def test_positive():
    assert analyze_sentiment("This is good") == "Positive"

def test_negative():
    assert analyze_sentiment("This is bad") == "Negative"
import re

diacritics = re.compile(r'[\u064b-\u065e\u0670\u0610-\u061a\u06d6-\u06ed]', re.UNICODE)

def clean_arabic(text: str) -> str:
    text = str(text)
    text = re.sub(r"http\S+|www.\S+|[@#]\S+|[A-Za-z0-9]", "", text)
    text = diacritics.sub('', text)
    text = re.sub(r'[إأآ]', 'ا', text)
    text = re.sub(r'[يى]', 'ي', text) 
    text = re.sub(r'[ؤئ]', 'ء', text) 
    text = re.sub(r'ة', 'ت', text)
    text = re.sub(r"[^\u0600-\u06FF\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
from bs4 import BeautifulSoup
import re

def extract_elements(html):
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator=" ").lower()

    emails = list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))
    phones = list(set(re.findall(r"\+?\d[\d\s-]{8,}", text)))

    links = [a.get('href') for a in soup.find_all('a', href=True)]

    return {
        "text": text,
        "emails": emails,
        "phones": phones,
        "links": links
    }
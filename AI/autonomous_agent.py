import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fpdf import FPDF


def save_summary_to_file(summary: str, filename: str = "smartphone_summary.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"[+] Summary saved to {filename}")


def save_summary_to_pdf(summary: str, filename: str = "smartphone_summary.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in summary.split("\n"):
        pdf.multi_cell(0, 10, txt=line)
    pdf.output(filename)
    print(f"[+] PDF saved to {filename}")


def extract_smartphone_reviews():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    url = "https://www.techradar.com/best/best-phones"

    for attempt in range(3):
        try:
            driver.get(url)
            time.sleep(5)  # Wait for the page to load
            break
        except Exception as e:
            print(f"[!] Page load timed out. Retrying...")
            time.sleep(2)
    else:
        print("[x] Failed to load page after retries.")
        driver.quit()
        return []

    reviews = []
    try:
        articles = driver.find_elements(By.CSS_SELECTOR, 'div.listingResult.small article, div.listingResult.large article')
        for article in articles[:5]:
            try:
                title_elem = article.find_element(By.CSS_SELECTOR, 'h3')
                title = title_elem.text.strip()
                link = article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

                # Dummy pros/cons
                pros = "✅ Good performance\n✅ Great battery life"
                cons = "❌ Slightly expensive\n❌ Bulky design"
                reviews.append((f"{title} ({link})", pros, cons))
            except Exception as e:
                print(f"[!] Skipped an article due to error: {e}")
                continue
    except Exception as e:
        print(f"[x] Error extracting articles: {e}")
    finally:
        driver.quit()

    return reviews


def summarize_reviews(reviews):
    summary = "Smartphone Reviews Summary\n\n"
    for title, pros, cons in reviews:
        summary += f"{title}\n{pros}\n{cons}\n\n"
    return summary


def main(instruction):
    if "smartphone" in instruction.lower():
        print("[+] Task: Extracting Smartphone Reviews Summary")
        reviews = extract_smartphone_reviews()
        if not reviews:
            print("[x] No reviews extracted.")
            return
        summary = summarize_reviews(reviews)
        save_summary_to_file(summary)
        save_summary_to_pdf(summary)
        print("[+] Smartphone summary saved and PDF generated.")
    else:
        print("[x] Unrecognized instruction.")


if __name__ == "__main__":
    user_instruction = input("Enter your instruction: ")
    main(user_instruction)

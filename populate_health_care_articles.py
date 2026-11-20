import os
import sys
import re

sys.path.append('/var/www/askharekrishna-platform/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askharekrishna_backend.settings')
import django
django.setup()

from django.utils.text import slugify
from cooking.models import CookingArticle

BOOK_PATH = '/var/www/askharekrishna-platform/backend/media/books/health_care_of_devotees_complete_book.md'

with open(BOOK_PATH, 'r', encoding='utf-8') as f:
    book_text = f.read()

def get_slice(start_pattern, end_pattern):
    try:
        start_idx = book_text.index(start_pattern)
        if end_pattern:
            end_idx = book_text.index(end_pattern, start_idx)
            content = book_text[start_idx:end_idx]
        else:
            content = book_text[start_idx:]
        return content.strip()
    except Exception as e:
        print(f"Error slicing: {start_pattern} -> {end_pattern}: {e}")
        return ""

def format_article_markdown(order, title, content):
    # Ensure clean article structure
    lines = content.splitlines()
    # Strip any top level markdown heading if identical
    while lines and (lines[0].startswith('#') or not lines[0].strip()):
        lines.pop(0)
    cleaned_body = "\n".join(lines).strip()
    
    header = f"# {title}\n\n"
    meta = f"> **Category:** Devotee Health Care | **Part {order} of 30** | *Srila Prabhupada Standard of Direct Clarity*\n\n---\n\n"
    footer = f"\n\n---\n\n*This article is Part {order} of the 'Health Care of Devotees' master curriculum published on cooking.askharekrishna.com.*"
    return header + meta + cleaned_body + footer

article_definitions = [
    {
        'order': 1,
        'title': 'The Sacred Vehicle: Why Devotee Health Care is Authentic Yukta-Vairagya',
        'start': "## Introduction: The Divine Purpose of the Devotee's Body",
        'end': "## Chapter 1: The Divine Blueprint",
    },
    {
        'order': 2,
        'title': "Bhagavad-gita 6.16–17: Lord Krishna's Infallible Science of Regulated Living",
        'start': "### 1.1 The Golden Mean of Eating and Sleeping",
        'end': "### 1.3 The Tripartite Chemistry of Food: Sattva, Rajas, and Tamas",
    },
    {
        'order': 3,
        'title': "The Chemistry of Consciousness: How Sattva, Rajas, and Tamas Enter Through the Tongue (BG 17.8–10)",
        'start': "### 1.3 The Tripartite Chemistry of Food: Sattva, Rajas, and Tamas",
        'end': "### 1.4 The Vaishvanara Fire: Honoring Krishna in the Stomach",
    },
    {
        'order': 4,
        'title': "Respecting the Fire in the Gut: Bhagavad-gita 15.14 and the Sacred Agni",
        'start': "### 1.4 The Vaishvanara Fire: Honoring Krishna in the Stomach",
        'end': "## Chapter 2: Srila Prabhupada's Revolutionary Guidance",
    },
    {
        'order': 5,
        'title': "Srila Prabhupada's Medical Guidance: Timeless Wisdom from Letters and Conversations",
        'start': "## Chapter 2: Srila Prabhupada's Revolutionary Guidance on Devotee Health and Bodily Care",
        'end': "## Chapter 3: The Modern Devotee Health Crisis",
    },
    {
        'order': 6,
        'title': "The Myth of Prasadam Immunity: Distinguishing Spiritual Mercy from Physical Digestion",
        'start': "### 3.1 The Dangerous Myth: \"It is Prasadam, so I Cannot Get Sick\"",
        'end': "### 3.3 Sleep Imbalances: Chronic Deprivation vs. Tamasic Over-Sleeping",
    },
    {
        'order': 7,
        'title': "The Devotee's Digestive Fire: Understanding Agni and Eradicating Toxic Ama",
        'start': "### 4.1 Understanding Agni and Ama",
        'end': "### 4.3 The Sacred Division of the Stomach: Charaka's Golden Proportions",
    },
    {
        'order': 8,
        'title': "The Half-Stomach Rule: Charaka Samhita's Golden Mathematical Formula for Eating",
        'start': "### 4.3 The Sacred Division of the Stomach: Charaka's Golden Proportions",
        'end': "### 4.4 Solar Meal Timings: Breakfast, Lunch, and Dinner in Cosmic Rhythm",
    },
    {
        'order': 9,
        'title': "Solar Meal Timings: Harmonizing Breakfast, Lunch, and Dinner with the Cosmic Sun",
        'start': "### 4.4 Solar Meal Timings: Breakfast, Lunch, and Dinner in Cosmic Rhythm",
        'end': "### 4.5 The Six Tastes (Shad-Rasa) in Krishna Prasadam",
    },
    {
        'order': 10,
        'title': "The Six Tastes (Shad-Rasa) in Krishna Prasadam: Achieving Complete Nutritional and Mental Satisfaction",
        'start': "### 4.5 The Six Tastes (Shad-Rasa) in Krishna Prasadam",
        'end': "### 4.6 Incompatible Food Combinations (Viruddha Ahara): Toxic Culinary Mistakes",
    },
    {
        'order': 11,
        'title': "Incompatible Foods (Viruddha Ahara): Toxic Mistakes in the Devotee Kitchen",
        'start': "### 4.6 Incompatible Food Combinations (Viruddha Ahara): Toxic Culinary Mistakes",
        'end': "### 4.7 Sattvic Superfoods for Devotional Vitality and Ojas",
    },
    {
        'order': 12,
        'title': "Liquid Gold: The Spiritual and Medicinal Science of Pure Desi Cow Ghee and A2 Milk",
        'start': "### 4.7 Sattvic Superfoods for Devotional Vitality and Ojas",
        'end': "### 4.8 Toxic Culinary Ingredients to Expel from Devotee Kitchens",
    },
    {
        'order': 13,
        'title': "White Sugar and Maida: The Silent Destroyers of Devotee Vitality and Sadhana",
        'start': "### 4.8 Toxic Culinary Ingredients to Expel from Devotee Kitchens",
        'end': "### 4.9 Ekadashi and Parana: Scientific Fasting and Cellular Autophagy",
    },
    {
        'order': 14,
        'title': "Ekadashi Done Right: Scientific Fasting, Autophagy, and the Danger of the \"Feast-Fast\"",
        'start': "### 4.9 Ekadashi and Parana: Scientific Fasting and Cellular Autophagy",
        'end': "## Chapter 5: Biological Rhythms, Rest, and Brahma-Muhurta",
    },
    {
        'order': 15,
        'title': "The Architecture of Sleep: Why Nidra is a Foundational Pillar of Devotional Life",
        'start': "### 5.1 Sleep (Nidra) as One of the Three Pillars of Human Existence",
        'end': "### 5.2 The 9:30 PM to 3:30 AM Circadian Goldmine",
    },
    {
        'order': 16,
        'title': "The 9:30 PM to 3:30 AM Circadian Goldmine: Conquering Brahma-Muhurta Without Fatigue",
        'start': "### 5.2 The 9:30 PM to 3:30 AM Circadian Goldmine",
        'end': "### 5.4 The Digital Sunset Protocol: Protecting Melatonin and Brain Waves",
    },
    {
        'order': 17,
        'title': "The Digital Sunset: Protecting Melatonin, Brain Chemistry, and Deep Sleep",
        'start': "### 5.4 The Digital Sunset Protocol: Protecting Melatonin and Brain Waves",
        'end': "### 5.5 Pada-Abhyanga and Sleeping on the Left Side (Vama-Kukshi)",
    },
    {
        'order': 18,
        'title': "Pada-Abhyanga and Left-Side Sleep: Two Ancient Secrets for Deep Rest and Reflux Relief",
        'start': "### 5.5 Pada-Abhyanga and Sleeping on the Left Side (Vama-Kukshi)",
        'end': "## Chapter 6: Ergonomics, Posture, and Physical Health for All Lifestyles",
    },
    {
        'order': 19,
        'title': "Ergonomics for Devotee Knowledge Workers: Protecting the Spine During Coding, Writing, and Study",
        'start': "### 6.1 The Spectrum of Devotional Occupations",
        'end': "### 6.3 Preventing and Reversing \"Text Neck\", Lumbar Herniation, and Eye Strain",
    },
    {
        'order': 20,
        'title': "Preventing \"Text Neck\" and Lumbar Herniation: Daily Physical Therapy for Sitting Sadhana",
        'start': "### 6.3 Preventing and Reversing \"Text Neck\", Lumbar Herniation, and Eye Strain",
        'end': "### 6.4 Heavy Physical Workers, Kitchen Cooks, Pujaris, and Book Distributors",
    },
    {
        'order': 21,
        'title': "Heavy Lifting in Krishna's Service: Injury Prevention for Kitchen Cooks and Book Distributors",
        'start': "### 6.4 Heavy Physical Workers, Kitchen Cooks, Pujaris, and Book Distributors",
        'end': "### 6.5 Daily Functional Exercise: Walking, Suryanamaskar, and Spinal Mobility",
    },
    {
        'order': 22,
        'title': "The Sacred Morning Walk: Srila Prabhupada's Daily Functional Fitness Formula",
        'start': "### 6.5 Daily Functional Exercise: Walking, Suryanamaskar, and Spinal Mobility",
        'end': "## Chapter 7: Prevention is Supreme – Dinacharya (Daily Routine) and Seasonal Care",
    },
    {
        'order': 23,
        'title': "Dinacharya: The Vedic Morning Purification Sequence for Unshakable Health",
        'start': "### 7.1 The Vedic Morning Purification Sequence",
        'end': "## Chapter 8: Simple Natural Remedies for Common Devotee Ailments",
    },
    {
        'order': 24,
        'title': "Langhanam Parama Aushadham: The Art of Therapeutic Fasting for Acute Illness",
        'start': "### 8.5 The Science of Therapeutic Fasting (Langhana)",
        'end': "## Chapter 9: Digital Detox, Regulated Entertainment, and Mind Control",
    },
    {
        'order': 25,
        'title': "Natural Home Pharmacy: Ayurvedic Kitchen Remedies for Gas, Acidity, and Bloating",
        'start': "### 8.1 Digestive Disorders",
        'end': "### 8.2 Respiratory Ailments",
    },
    {
        'order': 26,
        'title': "Respiratory Resilience: Conquering Colds, Coughs, and Sinusitis with Tulasi, Ginger, and Steam",
        'start': "### 8.2 Respiratory Ailments",
        'end': "### 8.4 Nervous and Mental Exhaustion",
    },
    {
        'order': 27,
        'title': "Overcoming Burnout and Anxiety: Ashwagandha, Brahmi, and Nadi Shodhana for Mental Peace",
        'start': "### 8.4 Nervous and Mental Exhaustion",
        'end': "### 8.5 The Science of Therapeutic Fasting (Langhana)",
    },
    {
        'order': 28,
        'title': "The Dopamine Trap: How Social Media Feeds Destroy Attention Span and Spiritual Taste",
        'start': "### 9.1 How Sensory Contamination Enters the Subconscious Mind",
        'end': "### 9.3 Establishing Sacred Phone-Free Boundaries in Devotional Life",
    },
    {
        'order': 29,
        'title': "Sacred Digital Boundaries: Establishing Phone-Free Zones for Japa, Prasadam, and Temple Worship",
        'start': "### 9.3 Establishing Sacred Phone-Free Boundaries in Devotional Life",
        'end': "## Chapter 10: The Devotee's Master 24-Hour Daily Health Routine",
    },
    {
        'order': 30,
        'title': "The Master 24-Hour Devotee Routine: A Practical Blueprint from Brahma-Muhurta to Rest",
        'start': "## Chapter 10: The Devotee's Master 24-Hour Daily Health Routine",
        'end': "## Appendix: Master Blueprint for 30 Standalone Articles",
    },
]

MAIN_TOPIC = "Health Care of Devotees"

# Delete any existing test articles under this topic
CookingArticle.objects.filter(mainTopic=MAIN_TOPIC).delete()

created_count = 0
for art_def in article_definitions:
    raw_content = get_slice(art_def['start'], art_def['end'])
    if not raw_content:
        print(f"Warning: Empty slice for order {art_def['order']}")
        continue

    formatted = format_article_markdown(art_def['order'], art_def['title'], raw_content)
    slug = slugify(f"health-care-{art_def['order']}-{art_def['title']}")[:280]

    article_obj = CookingArticle.objects.create(
        mainTopic=MAIN_TOPIC,
        subTopic=art_def['title'],
        article=formatted,
        slug=slug,
        order=art_def['order'],
        language='en'
    )
    created_count += 1
    print(f"[{created_count}/30] Created Article #{article_obj.order}: {article_obj.subTopic[:50]}... ({len(article_obj.article)} chars)")

print(f"\nSuccessfully populated all {created_count} articles under mainTopic='{MAIN_TOPIC}'!")

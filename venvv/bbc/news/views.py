from django.shortcuts import render

news_list = [
    {
        "id": 1,
        "title": "Markets Rally on Inflation Data",
        "text": "Global stock markets rallied after new inflation data suggested price pressures are easing. Investors responded positively across major indexes.",
        "label": "business",
        "sentiment": "positive",
        "summary": "Stocks rose globally after encouraging inflation data.",
        "keywords": ["stocks", "inflation", "markets"],
        "split": "train"
    },
    {
        "id": 2,
        "title": "New AI Model Improves Accuracy",
        "text": "A technology company unveiled a new artificial intelligence model that outperforms previous systems in accuracy and efficiency.",
        "label": "technology",
        "sentiment": "positive",
        "summary": "A new AI model shows improved performance.",
        "keywords": ["AI", "machine learning", "technology"],
        "split": "train"
    },
    {
        "id": 3,
        "title": "Government Faces Budget Debate",
        "text": "Lawmakers debated spending priorities as the government prepares to finalize its annual budget.",
        "label": "politics",
        "sentiment": "neutral",
        "summary": "Government officials debate national budget plans.",
        "keywords": ["budget", "government", "policy"],
        "split": "train"
    },
    {
        "id": 4,
        "title": "Team Wins Championship Final",
        "text": "The underdog team won the championship final after a dramatic overtime finish.",
        "label": "sports",
        "sentiment": "positive",
        "summary": "An underdog team claimed the championship title.",
        "keywords": ["championship", "sports", "victory"],
        "split": "train"
    },
    {
        "id": 5,
        "title": "Doctors Warn About Poor Sleep",
        "text": "Health experts warn that chronic sleep deprivation can lead to long-term physical and mental health problems.",
        "label": "health",
        "sentiment": "negative",
        "summary": "Experts warn of health risks from lack of sleep.",
        "keywords": ["sleep", "health", "doctors"],
        "split": "train"
    },
    {
        "id": 6,
        "title": "Oil Prices Fall",
        "text": "Oil prices declined due to increased supply and weaker global demand.",
        "label": "business",
        "sentiment": "negative",
        "summary": "Oil prices dropped amid supply concerns.",
        "keywords": ["oil", "energy", "prices"],
        "split": "validation"
    },
    {
        "id": 7,
        "title": "Cyberattacks Increase Worldwide",
        "text": "Cybersecurity firms report a sharp increase in attacks targeting financial institutions.",
        "label": "technology",
        "sentiment": "negative",
        "summary": "Cyberattacks on banks are rising.",
        "keywords": ["cybersecurity", "attacks", "banks"],
        "split": "validation"
    },
    {
        "id": 8,
        "title": "Election Campaign Intensifies",
        "text": "Political parties intensified campaigning efforts ahead of the upcoming election.",
        "label": "politics",
        "sentiment": "neutral",
        "summary": "Election campaigns gain momentum.",
        "keywords": ["election", "campaign", "politics"],
        "split": "validation"
    },
    {
        "id": 9,
        "title": "Star Player Suffers Injury",
        "text": "A star player will miss the rest of the season after suffering a serious injury.",
        "label": "sports",
        "sentiment": "negative",
        "summary": "Injury sidelines a star athlete.",
        "keywords": ["injury", "player", "season"],
        "split": "validation"
    },
    {
        "id": 10,
        "title": "Mental Health Awareness Rises",
        "text": "Public awareness campaigns are increasing focus on mental health and wellness.",
        "label": "health",
        "sentiment": "positive",
        "summary": "Mental health awareness is growing.",
        "keywords": ["mental health", "awareness", "wellness"],
        "split": "validation"
    },
    {
        "id": 11,
        "title": "Tech Stocks Decline",
        "text": "Technology stocks fell amid concerns over future earnings growth.",
        "label": "business",
        "sentiment": "negative",
        "summary": "Tech stocks declined due to earnings concerns.",
        "keywords": ["stocks", "technology", "markets"],
        "split": "test"
    },
    {
        "id": 12,
        "title": "AI Used in Hospitals",
        "text": "Hospitals are increasingly adopting AI tools to assist with medical diagnoses.",
        "label": "technology",
        "sentiment": "positive",
        "summary": "Hospitals adopt AI for diagnostics.",
        "keywords": ["AI", "healthcare", "diagnosis"],
        "split": "test"
    },
    {
        "id": 13,
        "title": "Foreign Policy Talks Held",
        "text": "World leaders met to discuss foreign policy and international security.",
        "label": "politics",
        "sentiment": "neutral",
        "summary": "Leaders discussed global security issues.",
        "keywords": ["foreign policy", "security", "leaders"],
        "split": "test"
    },
    {
        "id": 14,
        "title": "Runner Wins City Marathon",
        "text": "An unexpected runner won the annual city marathon, surprising spectators.",
        "label": "sports",
        "sentiment": "positive",
        "summary": "An underdog won the city marathon.",
        "keywords": ["marathon", "runner", "sports"],
        "split": "test"
    },
    {
        "id": 15,
        "title": "New Nutrition Guidelines Released",
        "text": "Health authorities released updated nutrition guidelines emphasizing balanced diets.",
        "label": "health",
        "sentiment": "positive",
        "summary": "New nutrition guidelines promote balanced diets.",
        "keywords": ["nutrition", "diet", "health"],
        "split": "test"
    }
]


def home(request):
    return render(request,'newshome.html',{'news':news_list})

def news(request):
    return render(request,'newslist.html')

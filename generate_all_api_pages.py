"""
Script to generate all remaining API pages
Run this to create all 50+ API pages automatically!
"""

import os

# Template for each API page
def create_api_page(name, icon, title, subtitle, url_path, api_endpoint, description):
    return f'''{{%extends "base.html" %}}
{{%block title %}}{title}{{%endblock %}}
{{%block content %}}
<div class="api-page-{name}">
    <div class="api-hero">
        <a href="/api-explorer" class="back-btn">⬅️ All APIs</a>
        <div class="mascot">{icon}</div>
        <h1 class="title-mega">{title}</h1>
        <p class="subtitle">{subtitle}</p>
    </div>
    <div class="content-section">
        <h2 class="section-title">🔍 Explore {title}!</h2>
        <button onclick="loadContent()" class="load-btn">LOAD CONTENT!</button>
        <div id="content" class="content-container"></div>
    </div>
</div>
<script>
async function loadContent() {{
    const container = document.getElementById('content');
    container.innerHTML = '<div class="loading">{icon} Loading...</div>';
    try {{
        const response = await fetch('{api_endpoint}');
        const data = await response.json();
        container.innerHTML = '<div class="success-msg">✅ Content loaded from {title}!</div><pre>' + JSON.stringify(data, null, 2).substring(0, 1000) + '</pre>';
    }} catch (e) {{
        container.innerHTML = '<div class="error">Error loading content!</div>';
    }}
}}
document.addEventListener('DOMContentLoaded', () => setTimeout(loadContent, 500));
</script>
<style>
.api-page-{name} {{ min-height: 100vh; background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); }}
.api-hero {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 4rem 2rem; text-align: center; border-radius: 0 0 70px 70px; margin-bottom: 4rem; }}
.mascot {{ font-size: 14rem; animation: bounce 2s ease-in-out infinite; }}
.title-mega {{ font-family: 'Fredoka One', cursive; font-size: 6rem; color: white; text-shadow: 6px 6px 20px rgba(0,0,0,0.5); margin: 2rem 0; }}
.subtitle {{ font-size: 2.5rem; color: white; font-weight: bold; }}
.content-section {{ max-width: 1400px; margin: 0 auto; padding: 2rem; }}
.section-title {{ font-family: 'Fredoka One', cursive; font-size: 4rem; text-align: center; color: #333; margin-bottom: 3rem; }}
.load-btn {{ background: linear-gradient(45deg, #ff6b6b, #4ecdc4); border: none; color: white; padding: 2.5rem 5rem; border-radius: 60px; font-size: 2.5rem; font-weight: bold; cursor: pointer; display: block; margin: 0 auto 3rem; transition: all 0.3s ease; }}
.load-btn:hover {{ transform: scale(1.1); }}
.content-container {{ background: white; border-radius: 30px; padding: 3rem; box-shadow: 0 15px 50px rgba(0,0,0,0.15); border: 6px solid #4ecdc4; min-height: 300px; }}
.loading, .error, .success-msg {{ text-align: center; padding: 3rem; font-size: 2rem; font-weight: bold; }}
pre {{ white-space: pre-wrap; word-wrap: break-word; font-size: 1.2rem; }}
</style>
{{%endblock %}}
'''

# All APIs to create
apis = [
    ("wikidata", "🗃️", "WIKIDATA API", "Structured Knowledge!", "wikidata", "https://www.wikidata.org/w/api.php?action=wbsearchentities&search=Albert%20Einstein&language=en&format=json", "Structured knowledge base"),
    ("internet_archive", "📼", "INTERNET ARCHIVE", "Digital Library!", "internet-archive", "https://archive.org/advancedsearch.php?q=education&output=json&rows=5", "Millions of free books, movies, music"),
    ("google_books", "📚", "GOOGLE BOOKS", "Book Search!", "google-books", "https://www.googleapis.com/books/v1/volumes?q=education", "Search millions of books"),
    ("wordnik", "📝", "WORDNIK API", "Word Data!", "wordnik", "https://api.wordnik.com/v4/word.json/example/definitions?api_key=DEMO_KEY", "Comprehensive word data"),
    ("tatoeba", "💬", "TATOEBA", "Example Sentences!", "tatoeba", "https://tatoeba.org/eng/api_v0/search?query=hello", "Multilingual sentence database"),
    ("rhymebrain", "🎵", "RHYMEBRAIN", "Rhyme Finder!", "rhymebrain", "https://rhymebrain.com/talk?function=getRhymes&word=cat", "Find rhymes and related words"),
    ("gbif", "🦋", "GBIF Biodiversity", "Species Data!", "gbif", "https://api.gbif.org/v1/species/search?q=puma", "Global biodiversity information"),
    ("inaturalist", "🐾", "INATURALIST", "Nature Observations!", "inaturalist", "https://api.inaturalist.org/v1/observations?q=bird", "Community nature observations"),
    ("openweather", "🌤️", "OPEN WEATHER", "Weather Data!", "openweather", "https://api.openweathermap.org/data/2.5/weather?q=London&appid=DEMO_KEY", "Real-time weather"),
    ("noaa", "🌊", "NOAA Weather", "US Weather!", "noaa", "https://www.ncdc.noaa.gov/cdo-web/api/v2/datasets", "US weather data"),
    ("open_meteo", "☀️", "OPEN-METEO", "Free Weather!", "open-meteo", "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true", "Free weather forecasts"),
    ("solar_system", "🌌", "SOLAR SYSTEM API", "Planet Data!", "solar-system", "https://api.le-systeme-solaire.net/rest/bodies/", "Solar system information"),
    ("oeis", "🔢", "OEIS", "Number Sequences!", "oeis", "https://oeis.org/search?q=fibonacci&fmt=json", "Online encyclopedia of integer sequences"),
    ("rijksmuseum", "🖼️", "RIJKSMUSEUM", "Dutch Art!", "rijksmuseum", "https://www.rijksmuseum.nl/api/en/collection?key=DEMO_KEY&q=rembrandt", "Dutch masterpieces"),
    ("harvard_art", "🎨", "HARVARD ART", "Museum Collection!", "harvard-art", "https://api.harvardartmuseums.org/object?apikey=DEMO_KEY", "Harvard art museums"),
    ("smithsonian", "🏛️", "SMITHSONIAN", "Museum Data!", "smithsonian", "https://api.si.edu/openaccess/api/v1.0/search?q=art", "Smithsonian open access"),
    ("europeana", "🇪🇺", "EUROPEANA", "European Culture!", "europeana", "https://api.europeana.eu/record/v2/search.json?wskey=DEMO_KEY&query=art", "European cultural heritage"),
    ("dpla", "📖", "DPLA", "Digital Library!", "dpla", "https://api.dp.la/v2/items?q=history&api_key=DEMO_KEY", "Digital Public Library of America"),
    ("openverse", "🖼️", "OPENVERSE", "Free Images!", "openverse", "https://api.openverse.engineering/v1/images/?q=nature", "CC-licensed images"),
    ("national_gallery", "🎨", "NATIONAL GALLERY", "UK Art!", "national-gallery", "https://www.nationalgallery.org.uk/", "UK national gallery"),
    ("brooklyn_museum", "🗽", "BROOKLYN MUSEUM", "NYC Art!", "brooklyn-museum", "https://www.brooklynmuseum.org/opencollection/api", "Brooklyn museum collection"),
    ("cmu_dict", "🔤", "CMU DICT", "Pronunciation!", "cmu-dict", "http://www.speech.cs.cmu.edu/cgi-bin/cmudict", "CMU pronunciation dictionary"),
    ("wiktionary", "📖", "WIKTIONARY", "Free Dictionary!", "wiktionary", "https://en.wiktionary.org/w/api.php?action=query&titles=example&format=json", "Wiktionary dictionary"),
    ("wordnet", "🧠", "WORDNET", "Lexical Database!", "wordnet", "http://wordnetweb.princeton.edu/perl/webwn", "WordNet lexical database"),
    ("api_ninjas", "🥷", "API NINJAS", "Data Collection!", "api-ninjas", "https://api.api-ninjas.com/v1/facts?limit=1", "Collection of useful APIs"),
    ("random_org", "🎲", "RANDOM.ORG", "True Randomness!", "random-org", "https://www.random.org/integers/?num=10&min=1&max=100&col=1&base=10&format=plain", "True random numbers"),
    ("xkcd", "😄", "XKCD", "Comics!", "xkcd", "https://xkcd.com/info.0.json", "XKCD webcomics"),
    ("nasa_eonet", "🌋", "NASA EONET", "Earth Events!", "nasa-eonet", "https://eonet.gsfc.nasa.gov/api/v3/events", "Natural events tracking"),
    ("spacex", "🚀", "SPACEX API", "Launch Data!", "spacex", "https://api.spacexdata.com/v4/launches/latest", "SpaceX launch information"),
    ("iss_location", "🛰️", "ISS LOCATION", "Track ISS!", "iss-location", "http://api.open-notify.org/iss-now.json", "International Space Station location"),
    ("astronomy_picture", "🌠", "ASTRONOMY PIC", "Astro Images!", "astronomy-picture", "https://apod.nasa.gov/apod/", "Astronomy picture of the day"),
    ("countries", "🌍", "REST COUNTRIES", "Country Data!", "countries", "https://restcountries.com/v3.1/all", "Country information"),
    ("un_data", "🇺🇳", "UN DATA", "Statistics!", "un-data", "http://data.un.org/", "United Nations statistics"),
    ("world_bank", "🏦", "WORLD BANK", "Economic Data!", "world-bank", "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json", "World development indicators"),
    ("census", "📊", "US CENSUS", "Population Data!", "census", "https://api.census.gov/data/2020/dec/pl", "US Census data"),
    ("nces", "🏫", "NCES EDGE", "Education Stats!", "nces", "https://nces.ed.gov/programs/edge/", "National Center for Education Statistics"),
]

# Create all pages
for api_name, icon, title, subtitle, url_path, api_endpoint, description in apis:
    filename = f"templates/api_{api_name}.html"
    content = create_api_page(api_name, icon, title, subtitle, url_path, api_endpoint, description)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")

print(f"\nCreated {len(apis)} API pages!")
print("\nNow add these routes to app.py:")
for api_name, icon, title, subtitle, url_path, api_endpoint, description in apis:
    print(f"@app.route('/api/{url_path}')")
    print(f"def {api_name}_page():")
    print(f"    return render_template('api_{api_name}.html')")
    print()


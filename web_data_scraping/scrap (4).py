import requests
import json
import csv

with open(r'concert.csv', 'w') as f:

  header = [
    "Name",
    "Location",
    "Image",
    "Datetime",
    "URL",
    "Lineup"
  ]
  writer = csv.writer(f)
  writer.writerow(header)
     

  page = 0
  while page < 10000:
    print("Get data from page: ", page)
    headers = { 
      'authority': 'www.ticketmaster.com',
      'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
      'x-tm-ff': '{"nfl-branding":"true","event-updates-filters":"true","id-widget-new-ca-backend":"true","events-web":"true","video-module-adp":"true","branding":"true","seo-url":"true","lineup-images":"true","id-widget-new-ca":"true","native-ad-position-homepage-desktop":"8","monetate-decision":"true","aurora-navbar":"true","ursa-ilm":"true","guides":"true","hp-ui-updates":"true","reviews":"true","imperative-calls":"true","adhesion-ad-cap":"1","virtual-badge":"true","language-topnav":"true","no-index":"true","end-date-publicvisibility":"true","write-review-button":"true","dynamic-hostname":"https://www.ticketmaster.com","improved-search-hp-variant":"1","islanders-homeaway":"true","artist-offers":"true","event-updates-search":"true","venue-images-cms":"true","pc-home":"true","monetatestg":"true","adp-venue-ilm":"true","id-widget":"true","hamburger-new":"true","nfl-sell":"true","see-tickets-cta":"true","vdp-city-list":"true","next-renderer-green":"true","native-ad-position-category":"6","improved-search-hp":"true","event-schema-markup-warnings":"true","native-ad-position-homepage":"3","adhesion-ad":"true","favorites":"true","ff4j-tags":"true","my-account-flyout":"true","hero":"true","id-widget-new-us":"true","id-widget-new-us-backend":"true","sign-in-popup":"true","seo-vdp-questions":"true","srp-gql":"true","default-calendar-view":"true","onsale-badge":"true","ursa-country":"true","usabilla-hamburger":"true","event-status-info-ln":"true","vdp-hotels-tab":"true","vdp-hotels-tab-uber":"true","suppress-reviews":"true","pc-domains":"CA,US","event-updates-filters-default":"all","ual":"true","standalone-login":"true","native-ad-position":"true","from-the-client":"true","events-web-size":"10","event-new-tab":"true","home-away-filters":"true","ss-autocorrect":"true","presale":"true","info-module":"true","search-suggest-gql":"true","native-ad-position-adp":"4","calendar-status-badge":"true","www-migration":"true","pc":"true","cbrk":"true","simplified-artist-filters":"true","event-status-badge":"true","venue-seating-charts":"true","hero-homepage":"true","hero-category":"true","amex-smart-widget":"true","event-updates-info":"true","improved-search-ui-mw":"true","country-domain":"US","ccpa":"true"}',
      'detectedlanguage': 'en-US',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
      'iswebview': 'false',
      'content-type': 'application/json',
      'accept': '*/*',
      'x-tm-device': 'Desktop',
      'x-tm-session-id': '3bd325a5-5c23-4877-92b9-eb1290f1e1e5',
      'referer': 'https://www.ticketmaster.com/discover/concerts?geoHash=drt2&radius=50&sort=date%2Casc&unit=miles&daterange=all'
    }
                
    out = requests.get("https://www.ticketmaster.com/api/next/graphql?operationName=CategorySearch&variables=%7B%22locale%22%3A%22en-us%22%2C%22sort%22%3A%22date%2Casc%22%2C%22page%22%3A"+str(page)+"%2C%22size%22%3A10%2C%22lineupImages%22%3Atrue%2C%22withSeoEvents%22%3Atrue%2C%22radius%22%3A%2250%22%2C%22geoHash%22%3A%22drt2%22%2C%22unit%22%3A%22miles%22%2C%22segmentId%22%3A%22KZFzniwnSyZfZ7v7nJ%22%2C%22localeStr%22%3A%22en-us%22%2C%22type%22%3A%22event%22%2C%22includeDateRange%22%3Atrue%2C%22includeTBA%22%3A%22yes%22%2C%22includeTBD%22%3A%22yes%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%225664b981ff921ec078e3df377fd4623faaa6cd0aa2178e8bdfcba9b41303848b%22%7D%7D", headers=headers);
    
    print(out.text)
    exit()

    y = json.loads(out.text)
    
    if y['data']['products'] != None:
      for one in y['data']['products']['items']:
        location = one['venues'][0]['name']+" - "+one['venues'][0]['city']['name']+", "+one['venues'][0]['state']['stateCode']
        lineup = []
        if one['attractions'] != None:
          for two in one['attractions']:
            lineup.append(two['name'])
        
        data = [
          one['name'],
          one['genreName'],
          location,
          one['imagesFiltered'][0]['url'],
          one['datesFormatted']['venueDateTime'],
          one['url'],
          "|".join(lineup)
        ]
        
        writer = csv.writer(f)
        writer.writerow(data)
    
    else:
      break;

    page = page+1
    
  

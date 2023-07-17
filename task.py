import csv
from serpapi import GoogleSearch
from pytube import YouTube

def get_channel_link(video_link):
    
    try:
        video = YouTube(video_link)
        channel_link = video.channel_url

        return channel_link
    except:
        return video_link
    
    
def google_search_crawler():
    query = 'site:youtube.com openinapp.co'
    links = []
    params = {
        'q': query,
        'num': 100,  # Number of results per page (maximum allowed by SerpApi)
        'api_key': 'eee2eb2b96e849cdd1010627b25569cd59b971bbd6a72ee966b05c7f98a66741'
    }
    
    pages = 0
    while len(links) < 10000:
        search = GoogleSearch(params)
        results_json = search.get_dict()
        #print(results_json)
        if 'organic_results' in results_json:
            for result in results_json['organic_results']:
                link = result['link']
                if link.startswith('https://www.youtube.com/'):
                    if 'c/' in link:
                        links.append(link)
                    else:
                        channel_link = get_channel_link(link)
                        if channel_link:
                            links.append(channel_link)
                    if (len(links)%100==0):
                        print(len(links))
                    if len(links) >= 10000:
                        break

        if 'next' in results_json.get('pagination', {}):
            params['start'] = pages
            pages += 100
            print(pages)
        else:
            break
    
    return links

def save_results_to_csv(results):
    file_path = r'D:\listed task\youtube_links.csv'  # Replace with your desired file path
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['YouTube Links'])
        writer.writerows([[link] for link in results])
    print("Results saved to youtube_links.csv")
# Run the crawler and save the results
search_results = google_search_crawler()
save_results_to_csv(search_results)




'''import csv
from serpapi import GoogleSearch

def google_search_crawler():
    query = 'site:youtube.com openinapp.co'
    results = []
    params = {
        'q': query,
        'num': 10000,  # Number of results per page (maximum allowed by SerpApi)
        'api_key': 'eee2eb2b96e849cdd1010627b25569cd59b971bbd6a72ee966b05c7f98a66741'
    }

    while len(results) < 10000:
        search = GoogleSearch(params)
        results_json = search.get_dict()
        if 'organic_results' in results_json:
            for result in results_json['organic_results']:
                link = result['link']
                if link.startswith('https://www.youtube.com/c/'):
                    results.append(link)
                    if len(results) >= 10000:
                        break

        if 'next' in results_json.get('pagination', {}):
            params['start'] = results_json['pagination']['next']
        else:
            break
    print(results)
    return results

def save_results_to_csv(results):
    file_path = r'D:\listed task\youtube_links.csv'  # Replace with your desired file path
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['YouTube Links'])
        writer.writerows([[link] for link in results])
    print("Results saved to youtube_links.csv")

# Run the crawler and save the results
search_results = google_search_crawler()
save_results_to_csv(search_results)'''

"""import csv
from serpapi import GoogleSearch

def google_search_crawler():
    query = 'site:youtube.com openinapp.co'
    results = []
    params = {
        'q': query,
        'num': 100,  # Number of results per page (maximum allowed by SerpApi)
        'api_key': 'eee2eb2b96e849cdd1010627b25569cd59b971bbd6a72ee966b05c7f98a66741'
    }

    while len(results) < 10000:
        search = GoogleSearch(params)
        results_json = search.get_dict()
        if 'organic_results' in results_json:
            for result in results_json['organic_results']:
                link = result['link']
                if link.startswith('https://www.youtube.com/'):
                    results.append(link)
                    if len(results) >= 10000:
                        break

        if 'next' in results_json.get('pagination', {}):
            params['start'] = results_json['pagination']['next']
        else:
            break
    print(results)
    return results
    
def save_results_to_csv(results):
    file_path = r'D:\listed task\youtube_links.csv'  # Replace with your desired file path
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['YouTube Links'])
        writer.writerows([[link] for link in results])
    print("Results saved to youtube_links.csv")
# Run the crawler and save the results
search_results = google_search_crawler()
save_results_to_csv(search_results)
"""
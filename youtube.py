import urllib.request as r
import re
def yvideo(url):
    search_url = 'https://qdownloader.io/download?url={}'.format(r.quote(url))
    # search_url = search_url.replace()
    # print(search_url)
    # print(search_url.split('/') )
    # print(len(search_url.split('/') ))
    # search_url = "https://qdownloader.io/download?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DqmeXgtzr-Xg"
    request=r.Request(search_url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})

    with r.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)

    import bs4 
    soup = bs4.BeautifulSoup(data, "html.parser")
    t = soup.select('.col-md-8 td a' )
    # print(t)
    url = t[0]['href']
    t = soup.select('.info.col-md-4 img' )
    # print(t)
    img = t[0]['src']
    url = re.search(r'.*&title',url).group()[:-6]
    return url,img



# search_url = 'https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D'.format(r.quote(keyword))
print(yvideo("https://www.youtube.com/watch?v=qmeXgtzr-Xg")[0])
# //ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a
# //ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a

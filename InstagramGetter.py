from bs4 import BeautifulSoup
from requests_html import HTMLSession
# from fake_useragent import UserAgent
# import requests

class InstagramGetter():
    def __init__(self) -> None:
        pass
    
    def getImageviaPage(self, page_url:str, image_url : str) -> str:
        """_summary_

        Args:
            page_url (str): Right Click the post -> copy link

        Returns:
            str: Image Direct URL
        """
        
        image_id = image_url.split('/p/')[-1]
        
        session = HTMLSession()
        r = session.get(page_url)
        r.html.render(sleep=5)
        
        soup = BeautifulSoup(r.html.raw_html, "html.parser")
        a_result = soup.find("a", {"href" : f"/p/{image_id}"})
        
        print(f"/p/{image_id}")
        
        if a_result is None:
            raise Exception("Not Found")
        
        results = a_result.find("img")
        source_link = results["src"]
        return source_link
    
    def getImageviaPost(self, image_url : str) -> str:
        session = HTMLSession()
        r = session.get(image_url)
        r.html.render(sleep = 5)
        
        soup = BeautifulSoup(r.html.raw_html, "html.parser")
        div_tag = soup.find("div", {"class" : "_aagv"})
        result = div_tag.find("img")["src"]
        
        return result

# url = "https://www.instagram.com/nisathletics/"

# session = HTMLSession()
# # response = requests.get(url)
# # response_text = response.text
# r = session.get(url)
# r.html.render(sleep=5)

# # print(r.html.raw_html)

# soup = BeautifulSoup(r.html.raw_html, "html.parser")

# # {"href" : "/p/CkhroEih1AD/"}
# a_result = soup.find("a", {"href" : "/p/CkhroEih1AD/"})

# results = a_result.find("img")

# source_link = results["src"]

# print(source_link)

if __name__ == "__main__":
    getter = InstagramGetter()
    # print(getter.getImageviaPage("https://www.instagram.com/nisathletics/", "https://www.instagram.com/p/CkPmWbEhccd/"))
    print(getter.getImageviaPost("https://www.instagram.com/p/Ckhq6F6Bb1F/"))
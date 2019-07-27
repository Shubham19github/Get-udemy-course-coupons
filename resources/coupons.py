# required packages
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup as BS
from flask_restful import Resource


class Coupons(Resource):

    url = None

    def get(self, keyword: str):

        if(keyword == 'new'):
            url = 'https://www.real.discount/new/'
        else:
            url = 'https://www.real.discount/trending/'

        nextUrlLinks, courseNames = self.scrapRealDiscount(url)

        p = Pool(12)
        courses = p.starmap(self.udemyLink, zip(courseNames, nextUrlLinks))

        p.terminate()
        p.join()

        return courses

    
    def udemyLink(self, courseName, nextUrlLink):

        courses = {}

        try:
            realPage = requests.get(nextUrlLink, headers={'Connection': 'close'})

            # parsing html data
            courseSoup = BS(realPage.text, 'html.parser')

            # getting all 12 blocks of courses in one page 
            courseLinks = courseSoup.find_all('a', {"class": "btn"})

            for udemyUrl in courseLinks:
                if 'https://www.udemy.com/' in udemyUrl['href']:
                    courses[courseName] = 'https://www.udemy.com/' + udemyUrl['href'].split('https://www.udemy.com/')[-1]

            return courses

        except:
            pass

    
    def scrapRealDiscount(self, url):

        try:
            # getting html from url
            response = requests.get(url, headers={'Connection': 'close'})

            # parsing html data
            soup = BS(response.text, 'html.parser')

            # getting all 12 blocks of courses in one page 
            courseBlocks = soup.find_all('div', {"class": "white-block-content"})

            # to store urls to scrap for udemy coupons
            nextUrlLinks = []
            courseNames = []

            for block in courseBlocks:

                # finding 'a' element inside each div
                links = block.find_all('a')

                for link in links:
                    # getting all 12 links of real.discount and course name in one page
                    if 'https://www.real.discount/offer/' in link['href']:
                        nextUrlLinks.append(link['href'])
                        courseNames.append(link.text.replace('.', '').replace('  ',''))

            return nextUrlLinks, courseNames

        except:
            pass

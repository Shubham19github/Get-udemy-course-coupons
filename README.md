# Get-udemy-course-coupons
Flask api that does web scrapping to extract udemy coupons for free courses.

It uses **[this](https://www.real.discount/)** link to extract udemy coupons link.

### Dependencies
- Python
- BeautifulSoup
- requests
- flask_restful
- flask
- multiprocessing

**Clone this Repository and run following command:**
> python app.py

There are two end points:
- /coupons/new **(For new Courses)**
- /coupons/trending **(For Trending Courses)**

### It returns 12 courses name and respective free udemy link

**NOTE: On Single api request, it scrappes 13(1 + 12) webpages. So depending upon your network, it may take around an average of 7-8 seconds. I have used multiprocessing to reduce it to this spped. Otherwise, It takes much longer time.**

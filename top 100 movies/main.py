from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page=response.text
# print(movie_page)
soup=BeautifulSoup(movie_page,"html.parser")
all_title_tag=soup.find_all(name="h3",class_="title")
print(all_title_tag)
article_texts=[]
for t in all_title_tag:
    text=t.getText()
    article_texts.append(text)
print(article_texts)
article_texts.reverse()
print(article_texts)
textfile = open("movies.txt", "w")
for element in article_texts:
    textfile.write(element + "\n")
textfile.close()

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


# response=requests.get("https://news.ycombinator.com/")
# yc_web_page=(response.text)
#
# soup=BeautifulSoup(yc_web_page,"html.parser")
# # print(soup.title.string)
# all_title_tag=soup.find_all(name="a",class_="titlelink")
# # print(all_title_tag)
# article_texts=[]
# article_links=[]
# for t in all_title_tag:
#     text=t.getText()
#     article_texts.append(text)
#     link=t.get("href")
#     article_links.append(link)
#
# article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
# max_upvote=max(article_upvotes)
# print(max_upvote)
# index_max=article_upvotes.index(max_upvote)
# print(index_max)
# max_title=article_texts[index_max]
# max_link=article_links[index_max]
# print(max_title)
# print(max_link)




# import lxml

# with open("website.html", encoding="utf-8") as file:
#    contents = file.read()
#
# soup= BeautifulSoup(contents,"html.parser")
# print(soup.title.string)
# all_anchor_tag=soup.find_all(name="a")
# print(all_anchor_tag)
#
# # for text in all_anchor_tag:
# #    # print(text.getText())
# #    print(text.get("href"))
#
# heading=soup.find(name="h1",id="name")
# print(heading)
#
# section=soup.find(name="h3",class_="heading")
# print(section)
#
# url=soup.select_one(selector="p a")
# print(url)
#
# name=soup.select_one(selector="#name")
# print(name)
#
# all=soup.select(".heading")
# print(all)
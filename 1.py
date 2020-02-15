from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import requests
def get_links():
    header={"User-Agent":"BaiduSpider"}
    init_url="https://www.zhihu.com/"
    url=urljoin(init_url,"/explore")
    request = requests.get(url,headers=header)
    question_regex = re.compile(r"^/question")
    special_regex = re.compile(r"^/special")
    soup = BeautifulSoup(request.text,"html.parser")
    links_question=dict()
    links_special=dict()
    for a_q in soup.find_all("a",{"href":question_regex}):
        links_question[a_q.string]=urljoin(init_url,a_q.attrs["href"])
    for a_q in soup.find_all("a",{"href":special_regex}):
        links_special[a_q.string]=urljoin(init_url,a_q.attrs["href"])
    return links_question,links_special
if __name__ == "__main__":
    links_question,links_special=get_links()
    with open("问题与专题.txt","w",encoding="utf-8") as f:
        f.write("问题：\n")
        for key,value in links_question.items():
            f.write(f"{key}:{value}\n")
        f.write("专题：/n")
        for key,value in links_special.items():
            f.write(f"{key}:{value}\n")
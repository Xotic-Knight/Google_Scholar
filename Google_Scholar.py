from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd

def eric(user_input):#function for site 1
    uc=user_input.split()
    str="+".join(uc)
    uclient=urlopen('https://eric.ed.gov/?q='+str)#url
    page_html=uclient.read()
    Soup=BeautifulSoup(page_html,'html.parser')
    containers=Soup.find_all('div',class_='r_i')

    l=[]
    for i in range(containers.__len__()):
        e=list()
        if containers[i].find('div',class_='r_t'):
            e.append(containers[i].find('div',class_='r_t').text)#Heading
        else:
            e.append("NaN")
        if containers[i].find('div',class_='r_a'):
            e.append(containers[i].find('div',class_='r_a').text)#Author
        else:
            e.append("NaN")
        if containers[i].find('div',class_='r_d'):
            e.append(containers[i].find('div',class_='r_d').text)#Description
        else:
            e.append("NaN")
        if containers[i].find('div',class_='keywords'):
            e.append(containers[i].find('div',class_='keywords').text)#Keywords
        else:
            e.append("NaN")
        l.append(e)
    df=pd.DataFrame(l,columns=['Heading','Author','Description','Keywords'])
    df.to_csv('GS1.csv',index=False)
    print(df)
def arxiv(user_input):#function for site2
    uc = user_input.split()
    str = "+".join(uc)
    uclient = urlopen('https://arxiv.org/search/?query=' +str+ '&searchtype=all&source=header')#url
    page_html = uclient.read()
    Soup = BeautifulSoup(page_html, 'html.parser')
    containers=Soup.find_all('li',class_='arxiv-result')
    l=[]
    for i in range(containers.__len__()):
        e=list()
        if containers[i].find('p',class_='title is-5 mathjax'):
            e.append(containers[i].find('p',class_='title is-5 mathjax').text)#Heading
        else:
            e.append("NaN")
        if containers[i].find('p',class_='authors'):
            e.append(containers[i].find('p',class_='authors').text)#Author
        else:
            e.append("NaN")
        if containers[i].find('span',class_='abstract-full has-text-grey-dark mathjax'):
            e.append(containers[i].find('span',class_='abstract-full has-text-grey-dark mathjax').text)#Abstract
        else:
            e.append('NaN')
        if containers[i].find('p',class_='is-size-7'):
            q=containers[i].find('p',class_='is-size-7').text #Submitted
            w=q.split(';')
            e.append(w[0])
        else:
            e.append("NaN")
        if containers[i].find('p',class_='is-size-7'):
            q=containers[i].find('p',class_='is-size-7').text #Originally Announced
            w=q.split(';')
            e.append(w[1])
        else:
            e.append('NaN')
        l.append(e)
    df1=pd.DataFrame(l,columns=['Heading','Author','Abstract','Submitted','Originally Announced'])
    df1.to_csv('GS2.csv',index=False)
    print(df1)
user_input = input('Enter Something You Want To Search')
print('From Eric Website: ')
eric(user_input)
print('From Arxiv Website: ')
arxiv(user_input)

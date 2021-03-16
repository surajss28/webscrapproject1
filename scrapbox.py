from bs4 import BeautifulSoup
import requests
import csv

with open('box.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml') # to parse the html file using lxml parser

# print(soup.prettify()) # to display the html file content. pretiffy method is for making indentation clear

headline = soup.find('h1',class_='center').text  # accessing the text of h1 heading tag
# print(headline)

title = soup.find('div',class_='container').h3.text # to print the container class heading
# print(title) 

description = soup.find('div',class_='container').p.text  # to accessing the desription of the places
# print(description)

link = soup.find('iframe',class_='youtube-player')['src']
# print(link)
vid_id = link.split('/')[4]
# print(vid_id)
yt_link = f'https://youtube.com/watch?v={vid_id}'   # to get the youtube link and process it
# print(yt_link)   




# To print all the content and writing in the csv file

csv_file = open('place_scrap.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'title', 'description', 'video_link'])


headline = soup.find('h1',class_='center').text  # accessing the text of h1 heading tag
print(headline)
print()

for data in soup.find_all('div',class_='container'):
    title = data.h3.text
    print(title)

    description = data.p.text
    print(description)
    try:
        link = data.find('iframe',class_='youtube-player')['src']
        vid_id = link.split('/')[4]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
        print(yt_link)
    except Exception as e:
        print("None")
    print()

    csv_writer.writerow([headline, title, description, yt_link])

csv_file.close



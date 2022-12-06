import csv
import requests
import xml.etree.ElementTree as ET
  
def loadRSS():
  
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
  
    # creating HTTP response object from given url
    resp = requests.get(url)
  
    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)
          
  
def parseXML(xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    book1 = []
    book2 = []
    book3 = []
  


    for child in root:
        #print(child.tag)
        if child.tag=='AddOrder':
            if(child.attrib['book']=='book-1'):
                temp = child.attrib['volume'] + '@' + child.attrib['price']
                book1.append(tuple([child.attrib['operation'],temp]))
            elif(child.attrib['book']=='book-2'):
                temp = child.attrib['volume'] + '@' + child.attrib['price']
                book2.append(tuple([child.attrib['operation'],temp]))
            elif(child.attrib['book']=='book-3'):
                temp = child.attrib['volume'] + '@' + child.attrib['price']
                book3.append(tuple([child.attrib['operation'],temp]))

    print("book: book1")
    #print(len(book1))
    for i in range(0,len(book1)):
        s=""
        if book1[i][0] == 'BUY':
            if i+1 < len(book1) and book1[i+1][0] == 'SELL':
                s = str(book1[i][1]) + "--" + str(book1[i+1][1])
                i = i+1
            else:
                s = str(book1[i][1]) + "--"
        else:
            s = " "*9 + "--" + str(book1[i][1])
        print(s)
    
    print("book: book2")
    for i in range(0,len(book2)):
        s=""
        if book2[i][0] == 'BUY':
            if i+1 < len(book2) and book2[i+1][0] == 'SELL':
                s = str(book2[i][1]) + "--" + str(book2[i+1][1])
                i = i+1
            else:
                s = str(book2[i][1]) + "--"
        else:
            s = " "*9 + "--" + str(book2[i][1])
        print(s)
    
    print("book: book3")
    for i in range(0,len(book3)):
        s=""
        if book3[i][0] == 'BUY':
            if i+1 < len(book3) and book3[i+1][0] == 'SELL':
                s = str(book3[i][1]) + "--" + str(book3[i+1][1])
                i = i+1
            else:
                s = str(book3[i][1]) + "--"
        else:
            s = " "*9 + "--" + str(book3[i][1])
        print(s)

    # iterate news items
    # for item in root.findall('./channel/item'):
  
    #     # empty news dictionary
    #     news = {}
  
    #     # iterate child elements of item
    #     for child in item:
  
    #         # special checking for namespace object content:media
    #         if child.tag == '{http://search.yahoo.com/mrss/}content':
    #             news['media'] = child.attrib['url']
    #         else:
    #             news[child.tag] = child.text.encode('utf8')
  
    #     # append news dictionary to news items list
    #     newsitems.append(news)
      
    # # return news items list
    # return newsitems
  
  
def savetoCSV(newsitems, filename):
  
    # specifying the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
  
    # writing to csv file
    with open(filename, 'w') as csvfile:
  
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        # writing headers (field names)
        writer.writeheader()
  
        # writing data rows
        writer.writerows(newsitems)
  
      
def main():
    # load rss from web to update existing xml file
    #loadRSS()
  
    # parse xml file
    newsitems = parseXML('orders.xml')
  
    # store news items in a csv file
    #savetoCSV(newsitems, 'topnews.csv')
      
      
if __name__ == "__main__":
  
    # calling main function
    main()
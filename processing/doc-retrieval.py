import os.path
import urllib.request
import json

from process import multiprocessing_main_integrated


def getDocument(url: str):
    """
    :param url: url to html page to text-transform
    :return: json
    """

    # download html
    basename = os.path.basename(url)
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    f = open("TestFiles/"+ basename + ".html" , 'w', encoding="utf8")
    f.write(html)
    f.close()

    # process downloaded html
    multiprocessing_main_integrated("TestFiles", "Test_Output")

    # return output as json
    with open("Test_Output/" + basename + "_output.txt", "r") as read_file:
        data = json.load(read_file)
    return data




# print(getDocument("http://50.116.50.126:8001/html/2"))

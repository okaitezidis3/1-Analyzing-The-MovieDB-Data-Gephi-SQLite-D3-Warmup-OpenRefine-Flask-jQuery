import requests
import json
import csv
import sys
import collections
from time import sleep

#For Q1.b
def print_to_csv(filename, data):
    """
    [Summary]: Append 300 data points with attributes ['id'] and ['title'] to a csv file
    -----------------------------------------------------------------------------
    [Arguments]: Filename(str): The name of the csv file that the data will be appended
                 data(dictionary): The data that will be appended in order to extract ['id'] and ['title']
    -----------------------------------------------------------------------------
    [Returns]:
    """
    with open(filename, 'a+', newline='') as f:
        fieldnames = ["column1","column2"]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        for i in range(len(data)):
            if len(open(filename).readlines()) ==300:
                break
            thewriter.writerow({"column1" : data[i]['id'], 'column2':data[i]['title']})
#Reference https://www.youtube.com/watch?v=s1XiCh-mGCA

#For Q1.c
def print_similar_movies_to_csv(filename, data,movie_id,d):
    """
    [Summary]: Append similar movies with attributes ['id'] to a csv file
    -----------------------------------------------------------------------------
    [Arguments]: Filename(str): The name of the csv file that the data will be appended
                 data(dictionary): The data that will be appended in order to extract ['id']
                 movie_id(str): The movie_id of the movie that we search for similars
                 d(defaultdictionary(int)): Dictionary for checking duplicate pairs
    -----------------------------------------------------------------------------
    [Returns]:
    """
    with open(filename, 'a+', newline='') as f:
    #print(d)
        fieldnames = ["column1","column2"]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        #Check for duplicate values
        if (d[(movie_id, data['id'])] == 0 and d[(data['id'], movie_id)] == 0):
            if (movie_id < data['id']):
                thewriter.writerow({"column1" : movie_id, 'column2':data['id']})
            else:
                thewriter.writerow({"column1" : data['id'], 'column2':movie_id})



#Reference https://www.youtube.com/watch?v=s1XiCh-mGCA


#Q1.c
def read_csv_write_similar_movies(filename,api_key):
    """
    [Summary]: Read all the movies ['id'] from the filename
    -----------------------------------------------------------------------------
    [Arguments]: Filename(str): The name of the csv file that the data will be appended
                 Api_key(str): The api_key
    -----------------------------------------------------------------------------
    [Returns]:
    """
    d = collections.defaultdict(int)
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            movie_id = int((row[0]))
            url = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"/similar?api_key="+api_key+"&page=1"
            payload = "{}"
            response = requests.request("GET", url, data=payload)
            sleep(0.26)   #Sleep, 40 requests per 10 seconds are allowed
            dictionary_of_results = response.json()
            results_in_dictionary_of_results = dictionary_of_results['results']
            min_similar = min(len(results_in_dictionary_of_results), 5) #find the minimum between 5 and number of similar movies
            for similar_movie_number in range(min_similar):
                print_similar_movies_to_csv("movie_ID_sim_movie_ID.csv", results_in_dictionary_of_results[similar_movie_number],movie_id,d)
                d[(movie_id,results_in_dictionary_of_results[similar_movie_number]['id'])] += 1
                d[(results_in_dictionary_of_results[similar_movie_number]['id'],movie_id)] += 1

#reference https://pythonprogramming.net/reading-csv-files-python-3/


api_key = sys.argv[1]
open("movie_ID_name.csv","w").close()
open("movie_ID_sim_movie_ID.csv","w").close()


#Use the api in order to request information about 300 comedy movies by descending popularity
for num_page in range(1,17):
#Url for Comedy movies (id = 35), descending popularity

    url = "https://api.themoviedb.org/3/discover/movie?api_key="+api_key+"&sort_by=popularity.desc&primary_release_date.gte=2000-01-01&page="+str(num_page)+"&with_genres=35"
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    dictionary_of_results = response.json()
    results_in_dictionary_of_results = dictionary_of_results['results']
    print_to_csv("movie_ID_name.csv",results_in_dictionary_of_results)

#Q1c
read_csv_write_similar_movies("movie_ID_name.csv",api_key)













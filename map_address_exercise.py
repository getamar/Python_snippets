
import json
import googlemaps
import csv

''' Problem : To get the address from a list and find the distance between each address and save the time & distance in 
    a csv file
    
    1. Prepare a list with postcode/address
    2. Use google API/json to find the distance using the address
    3. Decode the result for the distance with mode as 'WALK'
    4. Make a list with A,B,distance,time
    5. Iterate for various places 
    6. Save all the details into a csv file
    
    following imports/Library required
    1. import csv
    2. import googlemaps
    3. import json
'''
Address_list = ['ME8 7UE', 'ME7 1BB','ME7 4RF', ' ME7 4NN', 'ME8 0RU']
data_list = []

#geocode_results = gmaps.geocode('20 Ropemaker St, London EC2Y 9AR')

gmaps = googlemaps.Client(key='AIzaSyCCfnTSQ3g_QEQll192QDRKIV6dB9uw9hI')

for i in range(0,5):
    for j in range(i+1,5):
        distance_matrix_results = gmaps.distance_matrix(Address_list[i],Address_list[j], mode = 'walking')
        json_format = json.dumps(distance_matrix_results, sort_keys=True, indent = 4, separators=(',' , ':'))
        t = distance_matrix_results['rows'][0]['elements'][0]['duration']['text']
        d = distance_matrix_results['rows'][0]['elements'][0]['distance']['text']
        data_list.append([Address_list[i],Address_list[j],t,d])

for i in data_list:
    print "Distance from %s to %s is %s and time taken for walking is %s\n" %(i[0],i[1],i[3],i[2])


with open('google_map_time_distance.csv','wb') as csvfile:
    csv_fh = csv.writer(csvfile, delimiter=';')
    for i in data_list:
        csv_fh.writerow(i)







# -*- coding: utf-8 -*-
"""
create data for the psagot tirgul
"""
import numpy as np
import datetime
import pandas as pd
import random
import math
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
###############################################
#############   CONSTANTS    ##################
###############################################
GRAND_PARENTS = 160000
CHILDREN_MAX = 10
GRANDPA_AGES = (65,80)
PARENTS_AGES = (40, 50)
CHILDREN_AGES = (10, 25)
FATHER_TERRORIST_PROB = 0.2
BROTHER_TERRORIST_IF_FATHER_PROB = 0.5
BROTHER_TERRORIST_IF_NOT_FATHER_PROB = 0.1
UNEMPLOYED_PROB = 0.1
MAX_SALARY = 10000
MIN_SALARY = 1500
PHONE_TO_TERRORIST_PROB = 0.9
SHORT_CONVERSATION_PROB = 0.5
TERRORIST_IF_CALLED_TERRORIST_PROB = 0.3
WAS_NEAR_TERRORIST_PLACE_PROB = 0.2

LONG_LAT_GAZA = [(31.57163253231525, 34.4948730384931), 
                 (31.527746270968645, 34.54019164200872),
                 (31.457251058320786, 34.454223616048694),
                 (31.4513935845821, 34.38143919222057),
                 (31.337686158836156, 34.25234983675181),
                 (31.29897081266501, 34.28256223909557)]
                 
LONG_LAT_LEBANON = [(33.89287539708619, 35.50355528946966),
                    (33.88079113845614, 35.52319335518404),
                    (33.87189785496681, 35.49919509678148)
                    ]

SUSPRECT_GRANDPARENT = 10000
SUSPECTS_PARENTS = 15000

def generate_random_point(points_list):
    points_num = len(points_list)
    alphas = np.array(np.random.random(points_num))
    alphas= alphas/alphas.sum()
    # normalize points so that sum will be 1:
    new_long = 0
    new_lat = 0
    for i in range(len(alphas)):
        new_long += alphas[i]*points_list[i][0]
        new_lat += alphas[i]*points_list[i][1]
    return (new_long, new_lat)

def create_terrorists_places():
    # create 10 places that terrorists arrested in:
    places = []
    for i in range(10):
        places.append(generate_random_point(LONG_LAT_GAZA))
    return places

def geodetic_distance(p1, p2):
    """
    p1 and p2 are points of the form (long, lat)
    the function will return the distance in km between them
    """
    earth_radius = 6371
    phi1 = p1[1]/180 * math.pi
    phi2 = p2[1]/180 * math.pi
    lambda1 = p1[0]/180 * math.pi
    lambda2 = p2[0]/180 * math.pi
    delta_phi = phi1-phi2
    delta_lambda = lambda1-lambda2
    a = math.sin(delta_phi/2)*math.sin(delta_phi/2) + \
        math.cos(phi1)*math.cos(phi2)* \
        math.sin(delta_lambda/2)* math.sin(delta_lambda/2)
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earth_radius*c
    
def get_locations_near_terrorists(terrorists_places, total_locations):
    """
    randomize total_locations locations in radious of 1km near one of the places
    in the terrorists places list
    """
    ret_locations = []
    # generate total_locations/len(terroritst_places) places near each
    # terrorists place:
    for place in terrorists_places:
        for i in range(int(math.ceil(float(total_locations)/len(terrorists_places)))):
            one_long_to_km = geodetic_distance(place, (place[0]+0.1, place[1]))/0.1
            one_lat_to_km = geodetic_distance(place, (place[0], place[1]+0.1))/0.1
            c_long = random.random()*0.5/one_long_to_km
            c_lat = random.random()*0.5/one_lat_to_km
            random_place = (place[0]+c_long, place[1] + c_lat)
            ret_locations.append(random_place)
    return ret_locations
    
def dist_to_closest_point(point, list_of_points):
    """
    return the minimal distance between the point and list_of_points
    """
    min_dist = float("inf")
    for other_point in list_of_points:
        min_dist = min(min_dist, geodetic_distance(point, other_point))
    return min_dist
    
def get_locations_far_from_terrorists(terrorist_places, total_locations):
    """
    randomize location that are far at lear 1 km from all the places in terrorist
    places.
    """
    ret_locations = []
    for i in range(total_locations):
        random_point = generate_random_point(LONG_LAT_GAZA)
        while dist_to_closest_point(random_point, terrorist_places) < 1:
            random_point = generate_random_point(LONG_LAT_GAZA)
        ret_locations.append(random_point)
    return ret_locations

# 10 popular places where terrorist founds in                    
TERRORIST_PLACES = create_terrorists_places()
LOCATIONS_NEAR_TERRORISTS = get_locations_near_terrorists(TERRORIST_PLACES, 1500)
LOCATIONS_FAR_FROM_TERRORISTS = get_locations_far_from_terrorists(TERRORIST_PLACES, 2500)
LOCATIONS_WITH_NEAR_TERRORISTS = list(set(LOCATIONS_NEAR_TERRORISTS).union(LOCATIONS_FAR_FROM_TERRORISTS))

TERRORIST_IF_FATHER_BROTHER_YOUNG_PROB = 0.8
TERRORIST_IF_FATHER_BROTHER_NOT_YOUNG_PROB = 0.5
TERRORIST_IF_FATHER_NOT_BROTHER_YOUNG_PROB = 0.3
TERRORIST_IF_FATHER_BOT_BROTHER_NOT_YOUNG_PROB = 0.5
TERRORIST_IF_NOT_FATHER_BROTHER_YOUNG_PROB = 0.3
TERRORIST_IF_NOT_FATHER_BROTHER_NOT_YOUNG_PROB = 0.05
TERRORIST_IF_NOT_FATHER_NOT_BROTHER = 0.03
TERRORIST_IF_OLD_RICH = 0.01
TERRORIST_IF_CALLED_TO_TERRORIST_ADDITION = 0.2
CALL_NEAR_TERRORIST_ADDITION = 0.1
###############################################
############   FUNCTIONS   ####################
###############################################

    
    
def create_grand_parents():
    curr_id = 1000000
    ret = {}
    for i in range(curr_id, curr_id + GRAND_PARENTS):
        age = GRANDPA_AGES[0] + np.random.random()* \
            (GRANDPA_AGES[1] - GRANDPA_AGES[0])
        birth_date = datetime.datetime(2016, 8, 1) - \
                datetime.timedelta(days = age*365)
        ret[i] = {'id': i, 'father_id': i - 200000, 'mom_id': i - 400000,
                    'birth_date': birth_date}
    return ret
    
def create_parents(grand_parents):
    ret = {}
    parents_ids = range(2000000, 3000000)
    np.random.shuffle(parents_ids)
    grandparents_ids = range(1000000, 1000000 + GRAND_PARENTS)
    np.random.shuffle(grandparents_ids)
    curr_parent_id = 0
    for i in range(0, len(grandparents_ids), 2):
        grandpa_id = grandparents_ids[i]
        grandma_id = grandparents_ids[i+1]
        childrens_num = int(np.random.random()*CHILDREN_MAX)
        for child in range(childrens_num):
            parent_id = parents_ids[curr_parent_id]
            curr_parent_id += 1
            age = PARENTS_AGES[0] + np.random.random()* \
                (PARENTS_AGES[1] - PARENTS_AGES[0])
            birth_date = datetime.datetime(2016, 8, 1) - \
                datetime.timedelta(days = age*365)
            ret[parent_id] = {"id": parent_id,
                                "father_id": grandpa_id,
                                "mom_id": grandma_id,
                                "birth_date": birth_date}
    return ret
    
def create_childrens(parents):
    ret = {}
    childrens_ids = range(3000000, 4000000)
    np.random.shuffle(childrens_ids)
    parents_ids = parents.keys()
    np.random.shuffle(parents_ids)
    curr_children_id = 0
    for i in range(0, len(parents_ids)-1, 2):
        father_id = parents_ids[i]
        mom_id = parents_ids[i+1]
        childrens_num = int(np.random.random()*CHILDREN_MAX)
        for child in range(childrens_num):
            child_id = childrens_ids[curr_children_id]
            curr_children_id += 1
            age = CHILDREN_AGES[0] + np.random.random()* \
                (CHILDREN_AGES[1] - CHILDREN_AGES[0])
            birth_date = datetime.datetime(2016, 8, 1) - \
                datetime.timedelta(days = age*365)
            ret[child_id] = {"id": child_id,
                                "father_id": father_id,
                                "mom_id": mom_id,
                                "birth_date": birth_date}
    return ret 

            
def create_db_1(grand_parent, parents, childrens):
    ids = grand_parent.keys()
    ids.extend(parents.keys())
    ids.extend(childrens.keys())
    dicts_list = grand_parents.values()
    dicts_list.extend(parents.values())
    dicts_list.extend(childrens.values())
    ret = pd.DataFrame(dicts_list, index = ids)
    return ret
    
def extract_births_dates_dict(db1):
    """
    return a dictionary that maps each id to its birth date
    """
    ids = list(db1['id'])
    births_dates = list(db1['birth_date'])
    ret_dict = {}
    for i in range(len(ids)):
        ret_dict[ids[i]] = births_dates[i]
    return ret_dict
    
def sort_by_age(ids_list, birth_dates_dict):
    """
    sort the ids in the list from olgest to youngest
    """
    candidates_tuples = []
    for candidate_id in ids_list:
        candidates_tuples.append((birth_dates_dict[candidate_id], candidate_id))
    candidates_tuples.sort()
    return [candidate_id for (birth_date, candidate_id) in candidates_tuples]
    
def get_sons(candidates_list, db1):
    """
    receives list of candidates ids and db1 and return a dictionary that 
    maps for each candidate id, the ids of the sons of him as a list of 
    ids (empty list if he has no sons). the sons should be ordered from th
    oldest to the youngest
    """
    # extract birth_dates dict:
    births_dates_dict = extract_births_dates_dict(db1)
    db1_grouped_by_father = db1.groupby('father_id').groups
    candidates_sons = {}
    counter = 0
    without_sons_counter = 0
    for candidate_id in candidates_list:
        counter += 1
        if candidate_id not in db1_grouped_by_father: #candidate has no sons:
            without_sons_counter +=1
            candidates_sons[candidate_id] = []
        else:    
            candidate_sons = db1_grouped_by_father[candidate_id]
            # now we should sort the candidates sons from the oldest to the
            # youngest:
            candidate_sons = sort_by_age(candidate_sons, births_dates_dict)
            candidates_sons[candidate_id] = candidate_sons
    return candidates_sons
        
def create_suspects_list(grand_parents, parents, db1):
    """
    return 2 arguments: suspects list, arrest_table (dictionary)
    """
    arrests_list = {}
    suspects_list = []
    candidates = list(random.sample(grand_parents.keys(), SUSPRECT_GRANDPARENT))
    candidates.extend(list(random.sample(parents.keys(), SUSPECTS_PARENTS)))
    candidates_sons = {}
    for candidate in candidates:
        candidates_sons[candidate] = []
    candidates_sons = get_sons(candidates, db1)
    # we generate suspects from their parents (while updating the terrorist
    # list):
    
    # what is should do in here?
    # for each candidate, gets its son lists. 
    # in prob 0.2 add it to the terrorist list
    # now, randomize a son of him and add it to the candidates list
    # if the father is a terrorist make its oldest son a terrorist with prob 0.5
    # and otherwise make it oldest sun a terrorist with prob 0.1
    brother_terrorist_counter = 0
    father_counter = 0
    fathers_ids = []
    brothers_ids = []
    for candidate_id in candidates:
        coin_flip_father, coin_flip_brother = random.random(), random.random()
        try:
            oldest_son = candidates_sons[candidate_id][0]
        except: # candidate has no sons:
            oldest_son = -1
            
        if oldest_son != -1: # add only candidates that has children
            if coin_flip_father < FATHER_TERRORIST_PROB:
                father_counter += 1
                arrests_list[candidate_id] = random.choice(TERRORIST_PLACES)
                fathers_ids.append(candidate_id)
                if coin_flip_brother < BROTHER_TERRORIST_IF_FATHER_PROB:
                    brother_terrorist_counter +=1
                    arrests_list[oldest_son] = random.choice(TERRORIST_PLACES)
                    brothers_ids.append(oldest_son)
            else: # father not a terrorist:
                if coin_flip_brother < BROTHER_TERRORIST_IF_NOT_FATHER_PROB:
                    brother_terrorist_counter += 1
                    arrests_list[oldest_son] = random.choice(TERRORIST_PLACES)
                    brothers_ids.append(oldest_son)
            # add a random son of the candidate to the suspects list:
            suspects_list.append(random.choice(candidates_sons[candidate_id]))
    return suspects_list, arrests_list, fathers_ids, brothers_ids
    
def get_phones_dict(phones_df):
    ids = list(phones_df['id'])
    phones = list(phones_df['phone'])
    ret_dict = {}
    for i in range(len(ids)):
        ret_dict[ids[i]] = phones[i]
    return ret_dict
    
###############################################
#########    DB1    CREATION    ###############
###############################################
# keys are ids and values are dictionary with keys: id, father_id, mom_id,
# and birth_date
grand_parents = create_grand_parents()
parents = create_parents(grand_parents)
childrens = create_childrens(parents)
db1 = create_db_1(grand_parents, parents, childrens)

db1.to_csv("C:/Users/zilberman/Desktop/db1.csv")
###############################################
##########  DB2     CREATION      #############
###############################################

# create terrorist dbs and suspects list at the same time:
suspects_list, arrests_table, fathers_ids, brothers_ids = create_suspects_list(grand_parents, parents, db1)

# inserts to arrests_table person that are not from the family of the suspects
# too (for diversity):
candidates = np.random.choice(list(db1.index), 5000)
# insert first 5K to the arrest table:
for i in range(5000):
    # with 90% chance, arrested in terrorist place and 10% chance in random
    # place:
    coin_flip = np.random.random()
    if coin_flip > 0.9: # generate random point
        arrest_place = generate_random_point(LONG_LAT_GAZA)
    else: # one of terrorist places
        arrest_place = random.choice(TERRORIST_PLACES)
    arrests_table[candidates[i]] = arrest_place
    
# save arrests table as csv to disk:
arrested_ids = []
arrests_longitude = []
arrests_latitude = []
for arrest_id in arrests_table.keys():
    arrested_ids.append(arrest_id)
    arrests_longitude.append(arrests_table[arrest_id][0])
    arrests_latitude.append(arrests_table[arrest_id][1])

arrests_df = pd.DataFrame({"arrested_id": arrested_ids, 
                           "arrest_longitude": arrests_longitude,
                           "arrest_latitude": arrests_latitude})
                           
arrests_df.to_csv("C:/Users/zilberman/Desktop/db2.csv")

##############################################################
###############    DB3 CREATION  #############################
##############################################################

# for each suspect make it with prob 0.1 unemployed, and with prob 0.9
# make its salary uniform between 1500 to 10000 nis in month:

salaries_list = []
for suspect_id in suspects_list:
    if random.random() < UNEMPLOYED_PROB: # unemployed
        pass
    else: # employed
        salaries_list.append((suspect_id, random.randint(MIN_SALARY, MAX_SALARY)*12))
        
salaries_df = pd.DataFrame({"suspect_id": [tup[0] for tup in salaries_list],
                            "annual_salary": [tup[1] for tup in salaries_list]})

# save salaries_df to disk:
salaries_df.to_csv("C:/Users/zilberman/Desktop/db3.csv")


##############################################################
###############    DB4 CREATION  #############################
##############################################################

total_phones = len(db1.index)
phones_list = random.sample(range(1000000, 9999999), total_phones)
phones_list = map(lambda phone: "050-{0}".format(phone), phones_list)

phones_df = pd.DataFrame({"id": list(db1.index),
                          "phone": phones_list})

phones_df.to_csv("C:/Users/zilberman/Desktop/db4.csv")                          

##############################################################
###############    DB5 CREATION  #############################
##############################################################
# phone calls is a list of tuples of the form: 
# (suspect_id, out_phone number, in_phone number, total_time(secs), gps_location of out_phone)
# for each phone we randomize between 50 to 150 calls in the last month (uniformly)
# for x% percentage of the population, a call is between 10 secs to 120 secs
# uniformly and for the rest its 120 secs to 1hour (3600 secs)
phone_calls = []
id_to_phone_dict = get_phones_dict(phones_df)
arrested_ids = arrests_table.keys()
population_ids = list(db1.index)

for suspect_id in suspects_list:
    suspect_called_to_terrorist = (random.random() < PHONE_TO_TERRORIST_PROB)
    suspect_phone = id_to_phone_dict[suspect_id]
    was_near_terrorist_place = (random.random() < WAS_NEAR_TERRORIST_PLACE_PROB)
    # first randomize calls to non-arrested people
    for i in range(random.randint(5, 15)): # number of calls is random between 50 and 150
        other_person = random.choice(population_ids)
        while (other_person == suspect_id):
            other_persion = random.choice(population_ids)
        if not suspect_called_to_terrorist:
            while (other_person in arrested_ids) or (other_person == suspect_id): # make sure call is to no arrested
                other_person = random.choice(population_ids)
        # randomize call duration:
        if random.random() < SHORT_CONVERSATION_PROB: 
            call_duration = random.randint(10, 120)
        else:
            call_duration = random.randint(120, 3600)
        # radomize out and in phones:
        out_phone = suspect_phone
        in_phone = id_to_phone_dict[other_person]
        if random.random() < 0.5: #flip between in and out phones
            out_phone, in_phone = in_phone, out_phone
        if was_near_terrorist_place:
            phone_loc = random.choice(LOCATIONS_WITH_NEAR_TERRORISTS)
        else:
            phone_loc = random.choice(LOCATIONS_FAR_FROM_TERRORISTS)
        # add call to phone calls:
        phone_calls.append((suspect_id, out_phone, in_phone, call_duration,
                            phone_loc))
        # if the other person is a suspect, add it to the calls list to:
        if other_person in suspects_list:
            phone_calls.append((other_person, in_phone, out_phone, call_duration,
                                random.choice(LOCATIONS_WITH_NEAR_TERRORISTS)))
id_to_calls_dict = {}
for suspect_id in suspects_list:
    id_to_calls_dict[suspect_id] = []
for call in phone_calls:
    suspect_id = call[0]
    in_phone = call[1]
    out_phone = call[2]
    call_duration = call[3]
    call_location = call[4]
    suspect_phone = id_to_phone_dict[suspect_id]
    if in_phone == suspect_phone:
        call_type = "in-call"
        other_phone = out_phone
    else:
        call_type = "out-call"
        other_phone = in_phone
    id_to_calls_dict[suspect_id].append((other_phone, call_type, call_duration,
                                call_location))

# create file for each suspect with his calls:
for suspect_id in suspects_list:
    with open("C:/Users/zilberman/Desktop/db5/{0}_calls.csv".format(suspect_id), 'wb') as f:
        f.write("phone_number,call_type,call_duration,call_location_longitude,call_location_latitude\r\n")
        calls_list = id_to_calls_dict[suspect_id]
        for call in calls_list:
            f.write("{0},{1},{2},{3},{4}\r\n".format(call[0], call[1], call[2],
                    call[3][0],call[3][1]))
                    
                    
#######################################################
#############   CREATE LABELED DATA    ################
#######################################################
# now for the hardest part: create labeled data from which we will create
# the train and tests:
# prepare convenient data structures to access:
id_to_birth_date_dict = {}
births_dates = list(db1['birth_date'])
for i in range(len(population_ids)):
    person_id = population_ids[i]
    id_to_birth_date_dict[person_id] = \
        (datetime.datetime.now() - births_dates[i]).days / 365.0
        
id_to_father_dict = {}
fathers_ids = list(db1['father_id'])
for i in range(len(population_ids)):
    person_id = population_ids[i]
    id_to_father_dict[person_id] = fathers_ids[i]
    
suspects_fathers = []
for suspect_id in suspects_list:
    suspects_fathers.append(id_to_father_dict[suspect_id])    
id_to_sons = get_sons(suspects_fathers, db1)
id_to_sons.update(get_sons(suspects_list, db1))
    
id_to_oldest_brother_dict = {}
for suspect_id in suspects_list:
    id_to_oldest_brother_dict[suspect_id] = id_to_sons[id_to_father_dict[suspect_id]][0]

id_to_salary_dict = {}
for tup in salaries_list:
    id_to_salary_dict[tup[0]] = tup[1]/12.0
for suspect_id in suspects_list:
    if suspect_id not in id_to_salary_dict:
        id_to_salary_dict[suspect_id] = 0

id_to_salary_per_person = {}
for suspect_id in suspects_list:
    number_of_children = len(id_to_sons[suspect_id])
    if number_of_children > 0:
        id_to_salary_per_person[suspect_id] = id_to_salary_dict[suspect_id]/number_of_children
    else:
        id_to_salary_per_person[suspect_id] = float("inf")
        
id_to_near_terrorist_count = {}
for suspect_id in suspects_list:
    id_to_near_terrorist_count[suspect_id] = 0
for call in phone_calls:
    caller_id = call[0]
    call_location = call[4]
    if dist_to_closest_point(call_location, TERRORIST_PLACES) < 1:
        id_to_near_terrorist_count[caller_id] += 1
        
phone_to_id_dict = {}
for person_id in id_to_phone_dict.keys():
    phone_to_id_dict[id_to_phone_dict[person_id]] = person_id
        
id_to_terrorist_calls = {}
for suspect_id in suspects_list:
    id_to_terrorist_calls[suspect_id] = False
    suspect_calls = id_to_calls_dict[suspect_id]
    for call in suspect_calls:
        other_person_id = phone_to_id_dict[call[0]]
        call_duration = call[2]
        if (call_duration < 120) and (other_person_id in arrested_ids):
            id_to_terrorist_calls[suspect_id] = True
        



# label data:
suspects_labels = []
for suspect_id in suspects_list:
    suspect_age = id_to_birth_date_dict[suspect_id]
    if suspect_age < 25:
        is_father_terrorist = (id_to_father_dict[suspect_id] in arrested_ids)
        is_brother_terrorist = (id_to_oldest_brother_dict[suspect_id] in arrested_ids)
        if is_father_terrorist:
            if is_brother_terrorist:
                if suspect_age >= 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BROTHER_NOT_YOUNG_PROB
                else: #suspect_age < 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BROTHER_YOUNG_PROB
            else:
                if suspect_age >= 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BOT_BROTHER_NOT_YOUNG_PROB
                else:
                    terrorist_prob = TERRORIST_IF_FATHER_NOT_BROTHER_YOUNG_PROB
        else: # father not a terrorist
            if is_brother_terrorist:
                if suspect_age < 18:
                    terrorist_prob = TERRORIST_IF_NOT_FATHER_BROTHER_YOUNG_PROB
                else:
                    terrorist_prob = TERRORIST_IF_NOT_FATHER_BROTHER_NOT_YOUNG_PROB
            else: # brother not a terrorist
                terrorist_prob = TERRORIST_IF_NOT_FATHER_NOT_BROTHER
        # if suspect is only child of his father, probability for terrorism
        # reduced by factor 3:
        if len(id_to_sons[id_to_father_dict[suspect_id]]) == 1:
            terrorist_prob = terrorist_prob/3.0
    else: # suspect is older than 25 years old
        salary_per_person = id_to_salary_per_person[suspect_id]
        if salary_per_person >= 1000:
            terrorist_prob = TERRORIST_IF_OLD_RICH
        else:
            near_terrorist_calls = id_to_near_terrorist_count[suspect_id]
            # more calls near terrorist_places = more probability to be a
            # terrorist
            terrorist_prob = CALL_NEAR_TERRORIST_ADDITION * near_terrorist_calls
        if id_to_terrorist_calls[suspect_id]:
            terrorist_prob += TERRORIST_IF_CALLED_TO_TERRORIST_ADDITION
    # now that we have terrorist prob we can label our suspects_list
    if random.random() < terrorist_prob:
        suspects_labels.append(True)
    else:
        suspects_labels.append(False)

labeled_data = pd.DataFrame({"suspect_id": suspects_list, "is_terrorist": suspects_labels},
                            index = suspects_list)
                            
suspects_list_shuffled = [suspect_id for suspect_id in suspects_list]
random.shuffle(suspects_list_shuffled)

train_suspects = labeled_data.loc[suspects_list_shuffled[:9000]]
test_suspects = labeled_data.loc[suspects_list_shuffled[9000:]]

train_suspects.to_csv("C:/Users/zilberman/Desktop/train_data.csv")
test_suspects.to_csv("C:/Users/zilberman/Desktop/test_data.csv")

################################################################
##########    SANITY CHECKS   ##################################
################################################################
# first check how a perfect model perform in terms of auc and roc curve:
test_suspects_probs = []
for suspect_id in list(test_suspects.index):
    suspect_age = id_to_birth_date_dict[suspect_id]
    if suspect_age < 25:
        is_father_terrorist = (id_to_father_dict[suspect_id] in arrested_ids)
        is_brother_terrorist = (id_to_oldest_brother_dict[suspect_id] in arrested_ids)
        if is_father_terrorist:
            if is_brother_terrorist:
                if suspect_age >= 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BROTHER_NOT_YOUNG_PROB
                else: #suspect_age < 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BROTHER_YOUNG_PROB
            else:
                if suspect_age >= 18:
                    terrorist_prob = TERRORIST_IF_FATHER_BOT_BROTHER_NOT_YOUNG_PROB
                else:
                    terrorist_prob = TERRORIST_IF_FATHER_NOT_BROTHER_YOUNG_PROB
        else: # father not a terrorist
            if is_brother_terrorist:
                if suspect_age < 18:
                    terrorist_prob = TERRORIST_IF_NOT_FATHER_BROTHER_YOUNG_PROB
                else:
                    terrorist_prob = TERRORIST_IF_NOT_FATHER_BROTHER_NOT_YOUNG_PROB
            else: # brother not a terrorist
                terrorist_prob = TERRORIST_IF_NOT_FATHER_NOT_BROTHER
        # if suspect is only child of his father, probability for terrorism
        # reduced by factor 3:
        if len(id_to_sons[id_to_father_dict[suspect_id]]) == 1:
            terrorist_prob = terrorist_prob/3.0
    else: # suspect is older than 25 years old
        salary_per_person = id_to_salary_per_person[suspect_id]
        if salary_per_person >= 1000:
            terrorist_prob = TERRORIST_IF_OLD_RICH
        else:
            near_terrorist_calls = id_to_near_terrorist_count[suspect_id]
            # more calls near terrorist_places = more probability to be a
            # terrorist
            terrorist_prob = CALL_NEAR_TERRORIST_ADDITION * near_terrorist_calls
        if id_to_terrorist_calls[suspect_id]:
            terrorist_prob += TERRORIST_IF_CALLED_TO_TERRORIST_ADDITION
    # now that we have terrorist prob we can label our suspects_list
    test_suspects_probs.append(terrorist_prob)

fpr, tpr, thresholds = roc_curve(list(test_suspects['is_terrorist']),
                                test_suspects_probs, pos_label=True)
perfect_auc = auc(fpr, tpr)
%matplotlib qt 
plt.figure()
plt.plot(fpr, tpr, label='ROC perfect_estimator (area = %0.2f)' % perfect_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
# second, build class for learning with students csv. put a csv with perfect
# features (i.e. all the features we thought about) and see how the different
# models are performed:

#now we will create perfect predictor features for each suspect. then we will
# index will be suspects_list
suspects_ages = []
for suspect_id in suspects_list:
    suspects_ages.append(id_to_birth_date_dict[suspect_id])
father_terrorist = []
for suspect_id in suspects_list:
    father_terrorist.append(id_to_father_dict[suspect_id] in arrested_ids)
brother_terrorist = []
for suspect_id in suspects_list:
    brother_terrorist.append(id_to_oldest_brother_dict[suspect_id] in arrested_ids)
lonely_son = []
for suspect_id in suspects_list:
    lonely_son.append(len(id_to_sons[id_to_father_dict[suspect_id]]) == 1)
salaries_per_person = []
for suspect_id in suspects_list:
    salary_per_person = id_to_salary_per_person[suspect_id]
    if salary_per_person > 100000:
        salary_per_person = 100000
    salaries_per_person.append(salary_per_person)
times_near_terror_places = []
for suspect_id in suspects_list:
    times_near_terror_places.append(id_to_near_terrorist_count[suspect_id])
talked_with_terrorist = []
for suspect_id in suspects_list:
    talked_with_terrorist.append(id_to_terrorist_calls[suspect_id])
    
features_df = pd.DataFrame({"age":suspects_ages,
                            "father_terrorist": father_terrorist,
                            "brother_terrorist": brother_terrorist,
                            "lonely_son": lonely_son,
                            "salary_per_person": salaries_per_person,
                            "times_near_terrorist": times_near_terror_places,
                            "talked_with_terrorist": talked_with_terrorist},
                            index = suspects_list)
                            
features_train_df = features_df.loc[train_suspects.index]
features_test_df = features_df.loc[test_suspects.index]
train_labels = train_suspects['is_terrorist']
test_labels = test_suspects['is_terrorist']

clf = RandomForestClassifier(n_estimators = 1000).fit(features_train_df, train_labels)
rf_probs = [tup[1] for tup in clf.predict_proba(features_test_df)]

fpr, tpr, thresholds = roc_curve(list(test_labels),
                               rf_probs, pos_label=True)
rf_auc = auc(fpr, tpr)
%matplotlib qt 
plt.figure()
plt.plot(fpr, tpr, label='ROC random forest (area = %0.2f)' % rf_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
# describe that targil and domain knowledge and for summary show the optimal 
# model, its performance and the different learning models performances:




#####################################################################
##########   CREATE DIRTY_DATA   for the data cleaning part  ########
#####################################################################

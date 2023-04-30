
#dict()  bara zakhire sazi dadeha hastesh 

# weekdays = {
#     'sun': 'sunday',
#     'mon': 'monday',
#     'fri': 'friday'
#     #'sun': 'monday'    #morede tekrari dar dict hazf mishe  
# }

#print(weekdays['mon']) #dar dict esme moteghaier ro ke benevisi va [] bezari khodesh neshon mide behet kodom key ro mikhay neshon bedei faghat




#print(weekdays.get('sun', "somthing is wrong")) #in ravashe nesbate be ravesh bala kheili behtare  chon age eshtebah neveshti none ro behet neshon mide ya mitoni ye meesage mese balal barash benevisi va be carbar neshon bedi 





# test = {
#     'name': 'saghar',
#     'age': '34',
#     'from': 'iran' 
# }

#test['name']= "sara"  #age bekhaym mored jadid esafe konim va ghadimi ro taghir bedim az in ravaesh estefade mkonim 

#test['email'] = "saghi.abazari@gmail.com" #ba in ravesh ye krey jadid minevisim 

#print(test.get('sAghar',"somthing is wrong"))
#test.pop("saghar")





#haghe dar dict


# test = {
#      'name': 'saghar',
#      'age': '34',
#      'from': 'iran' 
#  }

#for i,x in test.items(): #bara inke ham key ham value ro bebinim az in ravesh dar for estefade mikonim 
    #print(i,":",x)



# for i in test.values(): #bara be dast ovordan faghat values
#     print(i)
    

# for i in test.keys(): #bara be dast ovordan faghat keys
#     print(i)
    
#for i in test:
    #print(test[i]) #in ye ravesh ke ham key ham values be dast miad ke niaz nis az meyhod use konim 
    


# test = {
#      'name': 'saghar',
#      'age': '34',
#      'from': 'iran' 
#  }

# test.update({'tel':'09169817944','car':"BMW"})
#dar dict az remove nemitoni use koni , mitoni az pop use koni ke yeki ro pak mikone az dict 
#pop, popitem(),del ,clear
# del test['age']
# print(test)


# test = {
#     "user1":{
#         "name":{"firstname":"sara","lastname":"abazari"},
#          "age": 16,
#          "from": "ahwaz"
#          },
#     "user2":{
#         "name":"amin",
#         "age":25
#         },
#     "from":{
#         "live":{"life":"usa"}
#     }
       
# }


# print(test["user2"]['from']['live']['life'])






test = {
    "user1":{
       "name": {"firstname":"saghar","lastname":"abazari"},
    },
    "user2":{
       "name": {"firstname":"amin","lastname":"hajipour"},
       
    },
    "user3":{
       "from":{"live":"iran"}
    }
       
}


print(test["user3"]['from']['live'])
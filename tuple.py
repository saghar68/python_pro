#test = (1,2,3, 'nima','saghar','musa', 12, 14)
#test2 = list(test)
#test2[3] = 'ayaan'
#test = tuple(test2)
#print(test)



#age bekhaym hazf nakonim faghat ezafe konim ye movred ro 



#test = (23,'nima','musa','saghi', 2,3,4)
#test2 = list[test]
#test2.clear()
#test = tuple(test2)
#print(test)


#tuple khodesh chan ta metode dare 



test = (12, "ali","sara", 2)
#print(test.index("ali"))
#print(test.index("ali"))

#ma inja khastim ali avali ro neshon nade pas az in ravash estefade kardim 
#print(test.index("ali", 3))

#inam vaghti test ro bekhaym pak konim kolan
#del test
#print(test)

#unpack kardan 
#ba in kar ma name moteghaier ro etesal dadim be in abcd, vaghti setare bezarim masalan b moteghaiere khodesho bar midare c ham hamintor vali a chon setare dare baghie chiza ke monde ro bar midare 
(a, b, c, d) = test
(a,*b) = test
print(a)
print(b)
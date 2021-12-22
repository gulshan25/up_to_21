ss='have a nice DAY'
print('original text   : ' +ss )
print('upper case      :  ' +ss.upper())
print('lower case      :  ' +ss.lower())
print('capitalize case : ' +ss.capitalize())
print('title case      : ' +ss.title())
print('swap case       :    ' +ss.swapcase())
print('count a         :    ' +str (ss.count('a')))
print('count A         :    ' +str (ss.count('A')))
print('count total number of character   :    ' +str (len(ss)))
print('center          :    ' +ss.center(50))
print('center          :    ' +ss.center(50,'#'))
print('replace         :    ' +ss.replace('nice','good'))
print('find            :    ' +str (ss.find('nice')))
print('index            :    ' +str (ss.index('nice')))

print('find            :    ' +str (ss.find('Nice')))
#print('index            :    ' +str (ss.index('Nice'))) ValueError: substring not found
print('split           :    ' +str (ss.split())) #return list[]
print(dir(ss)) 



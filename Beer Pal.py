from autocorrect import spell
from PIL import Image
from pytesseract import image_to_string
import pyscreenshot as Imagegrab
import cv2


alphanum ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&#' "
image = Image.open("Bar Menu 6.jpg")
wineDictionary = {}
beerDictionary = {
            'A':{
                'abita amber':[128,4.5],
                'abita golden':[125,4.2],
                'abita jockamo ipa':[190,6.5],
                'abita light':[118,4.0],
                'abita purple haze':[128,4.20],
                'abita restoration':[167,5.0],
                'abita turbodog':[168,5.60],
                'amstel light':[99,4.10],
                'anchor porter':[209,5.60],
                'anchor steam':[153,4.90],
                'augustiner amber lager':[135,4.30]
                },
            'B':{
                "bass ale":[156,5.00],
                "beach bum blonde ale":[163,5.4],
                "beck's":[143,5.00],
                "beck's light":[64,2.30],
                "blatz beer":[153,4.80],
                "blue moon belgian white":[164,5.36],
                "blue moon full moon winter ale": [180,5.52],
                "blue moon harvest moon pumpkin ale":[180,5.76],
                "blue moon honey moon summer ale":[157,5.12],
                "blue moon rising moon spring ale":[161,5.40],
                "blue point toasted lager":[175,5.30],
                "boddington's ale":[148,4.70],
                "brooklyn black chocolate stout":[320,10.00],
                "brooklyn brown ale":[190,5.60],
                "brooklyn east india pale ale":[200,6.90],
                "brooklyn lager":[170,5.20],
                "brooklyn monster":[305,10.10],
                "brooklyn pennant pale ale":[160,5.00],
                "brooklyn pilsner":[155,5.10],
                "brooklyn summer ale":[150,5.00],
                "brooklyn winter ale":[205,6.10],
                "bud american ale":[182,5.30],
                "bud ice":[123,5.50],
                "bud light":[110,4.20],
                "bud light chelada clamato":[151,4.20],
                "bud light lime":[116,4.20],
                "bud light platinum":[137,6.0],
                "budweiser":[145,5.00],
                "budweiser chelada":[186,5.00],
                "budweiser select":[99,4.30],
                "budweiser select 55":[55,2.40],
                "busch":[114,4.30],
                "busch ice":[136,5.90],
                "busch light":[95,4.10]
                },
            'C':{
                "carling black label":[138, 4.30],
                "coors banquet":[147,5.00],
                "coors extra gold":[152,4.97],
                "coors light":[102,4.20],
                "corona extra":[149,4.60],
                "corona familiar":[154,4.80],
                "corona light":[99,4.10],
                "corona premier":[90,4.00],
                "cristal (peru)":[132,4.60],
                "cusquena":[141,4.80]
                },
            'D':{
                "deschutes black butte porter":[192,5.20],
                "deschutes fresh squeezed ipa":[225,6.40],
                "deschutes inversion ipa":[228,6.80],
                "deschutes mirror pond ale":[170,5.00],
                "dogfish head 120 minute ipa":[450,18.00],
                "dogfish head 60 minute ipa":[209,6.00],
                "dogfish head 90 minute ipa":[294,9.00],
                "dogfish head midas touch":[307,9.00],
                "dogfish head red & white":[310,10.00],
                "dogfish head shelter pale ale":[168,5.00]
                },
            'E':{
                "efes pils":[170,5.00],
                },
            'F':{
                "firestone dba":[166,5.00],
                "flying dog doggie style pale ale":[150,5.50],
                "flying dog double dog":[313,11.50],
                "flying dog gonzo":[271,9.20],
                "flying dog horn dog":[314,10.20],
                "flying dog in heat wheat":[138,4.70],
                "flying dog kerberos tripel":[238,8.50],
                "flying dog old scratch amber lager":[154,5.50],
                "flying dog raging bitch":[221,8.30],
                "flying dog road dog":[163,6.00],
                "flying dog snake dog ipa":[188,7.10],
                "flying dog tire bite golden ale":[129,5.10],
                "foster's":[146,5.00],
                "foster's premium ale":[161,5.50],
                },
            'G':{
                "genesee beer":[148,4.50],
                "genesee cream ale":[162,5.10],
                "genesee ice":[156,5.90],
                "genesee red":[148,4.90],
                "george killian's irish red":[168,5.40],
                "grolsch amber ale":[160,5.40],
                "grolsch blonde lager":[120,2.80],
                "grolsch light lager":[97,3.60],
                "grolsch premium lager":[142,5.00],
                "guinness draught":[125,4.27],
                "guinness extra stout":[153,5.00],
                },
            'H':{
                "hamm's beer":[142,4.70],
                "hamm's special light":[110,3.80],
                "harbin":[144,4.60],
                "harp lager":[155,5.20],
                "heineken":[150,5.00],
                "heineken light":[99,4.20],
                "hiland light":[97,4.00],
                "hoegaarden belgian white":[153,4.90],
                },
            'I':{
                "irish red ale":[196,5.70],
                "iron city":[140,4.50],
                "iron city light":[95,4.15],
                },
            'J':{
                "jose cuervo especial":[768, 40],
                "jack and diet coke":[195, 10],
                },
            'K':{
                "keystone ice":[142,5.90],
                "keystone light":[104,4.13],
                "keystone premium":[111,4.43],
                "king cobra":[134,6.0],
                "kirin":[147,5.00],
                "kirin light":[95,3.20],
                },
            'L':{
                "lagunitas brown shugga":[335,9.70],
                "lagunitas hop stoopid":[285,8.00],
                "lagunitas ipa":[194,6.20],
                "lagunitas little sumpin' sumpin' ale":[230,7.50],
                "lech":[143,4.90],
                "leinenkugel amber light":[110,4.14],
                "leinenkugel creamy dark":[170,4.94],
                "leinenkugel honey weiss":[149,4.92],
                "leinenkugel light":[105,4.19],
                "leinenkugel northwoods lager":[163,4.94],
                "leinenkugel original":[152,4.67],
                "leinenkugel red":[166,4.94],
                "leinenkugel sunset wheat":[165,4.90],
                "long island iced tea":[529,23.8],
                "lowenbrau dark":[160,5.00],
                "lowenbrau special beer":[160,5.20],
                },
            'M':{
                "magic hat #9":[153,5.10],
                "makers mark":[880, 45.5],
                "michael shea's":[145,4.62],
                "michelob amberbock":[155,5.20],
                "michelob beer" :[164,5.00],
                "michelob dunkelweisse":[167,5.50],
                "michelob golden draft":[152,4.70],
                "michelob golden draft light":[110,4.10],
                "michelob honey lager":[174,4.90],
                "michelob light":[123,4.30],
                "michelob pale ale":[187,5.60],
                "michelob porter":[187,5.90],
                "michelob ultra":[95,4.20],
                "michelob ultra amber":[95,4.00],
                "michelob ultra lime cactus":[95,4.00],
                "michelob ultra pure gold":[85,3.80],
                "mickey's ice":[157,5.80],
                "miller fortune":[186,6.90],
                "miller genuine draft":[140,4.60],
                "miller high life":[141,4.60],
                "miller high life light":[107,4.10],
                "miller lite":[96,4.20],
                "miller64":[64,2.80],
                "milwaukee's best (premium)":[142,4.80],
                "milwaukee's best ice (beast ice)":[173,5.90],
                "milwaukee's best light":[96,4.10],
                "modelo especial":[145,4.40],
                "molson canadian":[136,5.00],
                "molson canadian 67":[67,3.00],
                "molson canadian light":[113,3.90],
                "molson ice":[160,5.60],
                },
            'N':{
                "natty daddy":[183,8.00],
                "natural ice":[130,5.90],
                "natural light":[95,4.20],
                "negra modelo":[170,5.40],
                "new belgium 1554":[205,5.60],
                "new belgium 2 below":[200,6.60],
                "new belgium abbey":[200,7.00],
                "new belgium blue paddle":[140,4.80],
                "new belgium fat tire":[160,5.20],
                "new belgium mothership wit":[155,4.80],
                "new belgium skinny dip":[110,4.20],
                "new belgium sunshine wheat":[145,4.80],
                "new belgium trippel":[215,7.80],
                "new planet tread lightly ale":[125,5.00],
                "newcastle brown ale":[150,4.70],
                },
            'O':{
                "old milwaukee beer":[145,4.60],
                "old milwaukee light":[110,3.82],
                "olympia premium lager":[146,4.70],
                "ommegang three philosophers":[290,9.70],
                },
            'P':{
                "pabst blue ribbon":[144,4.74],
                "pabst extra light low alcohol":[67,2.50],
                "pacifico":[145,4.40],
                "peroni nastro azzurro":[149,5.10],
                "pete's wicked ale":[174,5.30],
                "pilsner urquell":[156,4.40],
                "presidente":[147,5.00],
                },
            'Q':{
                "placeholder":[1,2,3],
                },
            'R':{
                "red bridge":[160,4.80],
                "red dog":[147,5.00],
                "red stripe":[153,4.90],
                "redd's apple ale":[165,5.00],
                "redhook esb":[179,5.77],
                "redhook ipa":[188,6.50],
                "redhook slim chance":[125,3.90],
                "rock bottom illuminator doppelback":[288,6.67],
                "rogue dead guy ale":[216,6.80],
                "rolling rock extra pale":[142,4.60],
                "rolling rock green light":[83,3.70],
                "rolling rock premium beer":[132,4.50],
                "russian river pliny the elder":[236,8.00],
                },
            'S':{
                "sam adams black lager":[191,4.90],
                "sam adams blackberry witbier":[176,5.50],
                "sam adams boston ale":[188,5.40],
                "sam adams boston lager":[175,5.00],
                "sam adams brown ale":[159,5.35],
                "sam adams cherry wheat":[180,5.40],
                "sam adams coastal wheat":[167,5.30],
                "sam adams cream stout":[190,4.90],
                "sam adams hefeweizen":[182,5.40],
                "sam adams honey porter":[192,5.45],
                "sam adams imperial double bock":[320,9.50],
                "sam adams imperial stout":[316,9.20],
                "sam adams imperial white":[328,10.30],
                "sam adams ipa":[175,5.93],
                "sam adams irish red":[180,5.50],
                "sam adams light":[119,4.30],
                "sam adams octoberfest":[180,5.40],
                "sam adams pale ale":[160,5.40],
                "sam adams scotch ale":[200,5.40],
                "sam adams summer ale":[160,5.30],
                "sam adams white ale":[175,5.40],
                "sam adams winter lager":[200,5.80],
                "schaefer beer":[142,4.60],
                "schlitz beer":[146,4.70],
                "schlitz light":[110,4.20],
                "sculpin ipa":[228,7.00],
                "shipyard light":[97,3.90],
                "shock top":[168,5.20],
                "sierra nevada anniversary ale":[190,5.90], 
                "sierra nevada bigfoot":[330,9.60],
                "sierra nevada celebration ale":[214,6.80],
                "sierra nevada draft ale":[157,5.00],
                "sierra nevada early spring beer":[190,5.90],
                "sierra nevada harvest ale":[215,6.70],
                "sierra nevada india pale ale":[231,6.90],
                "sierra nevada pale ale":[175,5.60],
                "sierra nevada pale bock":[218,7.00],
                "sierra nevada porter":[194,5.60],
                "sierra nevada stout":[225,5.80],
                "sierra nevada summerfest":[158,5.00],
                "sierra nevada wheat beer":[153,4.40],
                "signature stroh beer":[153,4.80],
                "smithwick's":[150,4.50],
                "smuttynose fineskind ipa":[200,6.90],
                "sol cerveza":[128,4.20],
                "southpaw light":[123,5.00],
                "st. pauli girl":[148,4.90],
                "st. pauli girl special dark":[150,4.80],
                "stella artois":[154,5.20],
                "stone pale ale":[188,5.64],
                "strauss endless summer light":[110,3.30],
                "stroh's beer":[149,4.60],
                "stroh's light":[113,4.40],
                },
            'T':{
                "tsingtao":[157,4.80],
                "tuborg deluxe dark export":[163,5.10],
                "tuborg export quality":[156,5.00],
                "tyskie":[149,5.30],
                },
            'U':{
                "placeholder":[1,2],
                },
            'V':{
                "victoria":[135,4.04],
                },
            'W':{
                "weinhard's amber light":[135,4.20],
                "weinhard's blonde lager":[161,5.10],
                "weinhard's hefeweizen":[151,4.90],
                "weinhard's pale ale":[147,4.60],
                "weinhard's private reserve":[150,4.80],
                "widmer hefeweizen":[159,4.90],
                "winter's bourbon cask ale":[165,6.00],
                "wyder's apple cider":[150,5.00],
                "wyder's pear cider":[136,5.00],
                },
            'X':{
                "placeholder":[1,2],
                },
            'Y':{
                "yuengling lager":[140,4.50],
                "yuengling light lager":[99,3.80],
                "yuengling lord chesterfield ale":[158,5.40],
                "yuengling oktoberfest":[168,5.40],
                "yuengling porter":[160,4.70],
                "yuengling porter":[160,4.70],
                "yuengling premium beer":[141,4.50],

                },
            'Z':{
                "placeholder":[1,2],
                },
            }

def readText(string):
    print(string)
def getText(image):
    return image_to_string(image)

def createList(string):
    item = ""
    lst=[]
    ignoreChar = False
    for char in string:
        if (char != '\n' and char in alphanum):
            if (ignoreChar == False):
                item+=char
        elif (char == ',' or char == '|' or char == '/' or char =='-' or char =='$'):
            ignoreChar = True
        elif (char == '\n'):
            ignoreChar = False
            if (len(item)) > 1:
                lst.append(item)
                item=""
    lst.append(item)
    return lst

def cleanUp(lst):
    newLst = []
    for item in lst:
        if item[-1] == " ":
            newLst.append(item[:-1])
        else:
            newLst.append(item)
    return newLst

def collectInfo(lst):
    foundBeers={}
    for item in lst:
        print (item)
        if (item[0].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            for beer in beerDictionary[(item[0].upper())]:
                if (item.lower() == beer):
                    info=beerDictionary[(item[0].upper())][beer]
                    foundBeers[beer] = beerDictionary[(item[0].upper())][beer]
                    display(beer, info)
                else:
                    #print("Item: ", item, " not in database.") 
                    newItem = spell(item.lower())
                    #print(newItem)
    return foundBeers

def display(beer, lst):
    print (str(beer).upper()+":")
    if (lst[1]>=35):
        print ("Calories (per 1.5 oz.): "+str(lst[0])/8)
        print ("Alcohol By Volume: "+str(lst[1])+"%")
        print ("Efficiency Score: "+str(lst[1]/lst[0]))
        print ("------------------------------")
    else:
        print ("Calories (per 12 oz.): "+str(lst[0]))
        print ("Alcohol By Volume: "+str(lst[1])+"%")
        print ("Efficiency Score: "+str(lst[1]/lst[0]))
        print ("------------------------------")

def sortEfficiency(lst):
    for beer in lst:
        calories = beerDictionary[beer[0].upper()][beer][0]
        abv = beerDictionary[beer[0].upper()][beer][1]
        efficiency = (abv*100)/calories
        
        
testDic = {'a':[6,0],'b':[6,0],'c':[6,0],'d':[5,0],'e':[9,0],'f':[7,0],'g':[8,0],'h':[3,0],'i':[4,0],'j':[1,0],'k':[11,0]}
def sortCalories(dic):
    drinkList = []
    for item in dic:
        drinkList.append(item)
    j = 0
    i = 1
    end = (len(drinkList))
    while (j < len(drinkList)-1):
        if (i < end):
            if (dic[drinkList[j]][0] > dic[drinkList[i]][0]):
                temp = drinkList[i]
                drinkList[i]=drinkList[j]
                drinkList[j] = temp
                i+=1
            else:
                i+=1
        else:
            j+=1
            i=j+1
    return drinkList

def sortABV(dic):
    drinkList = []
    for item in dic:
        drinkList.append(item)
    j = 0
    i = 1
    end = (len(drinkList))
    while (j < len(drinkList)-1):
        if (i < end):
            if (dic[drinkList[j]][1] < dic[drinkList[i]][1]):
                temp = drinkList[i]
                drinkList[i]=drinkList[j]
                drinkList[j] = temp
                i+=1
            else:
                i+=1
        else:
            j+=1
            i=j+1
    return drinkList

def SortEfficiency(dic):
    drinkList = []
    for item in dic:
        drinkList.append(item)
    j = 0
    i = 1
    end = (len(drinkList))
    while (j < len(drinkList)-1):
        if (i < end):
            if ((dic[drinkList[j]][1]/dic[drinkList[j]][0]) < (dic[drinkList[i]][1]/dic[drinkList[i]][0])):
                temp = drinkList[i]
                drinkList[i]=drinkList[j]
                drinkList[j] = temp
                i+=1
            else:
                i+=1
        else:
            j+=1
            i=j+1
    return drinkList

def search(beer):
    itemFound = False
    for drink in beerDictionary[(beer[0].upper())]:
        if (beer.lower() == drink):
            info=beerDictionary[(beer[0].upper())][drink]
            display(drink, info)
            itemFound = True
    if (not itemFound):
        print("Item: ", beer, " not in database.") 

#print sortEfficiency(SortEfficiency(
#print(sortCalories(testDic))
print display((sortCalories(collectInfo(createList(getText(image))))))
#print (cleanUp(createList(getText(image))))
#print (collectInfo(cleanUp(createList(getText(image)))))
#beer = input("Name of the beer? ")
#print (search(beer))

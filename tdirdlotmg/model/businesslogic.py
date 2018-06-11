import random
import pandas as pd

# slotlist=["aa","ab","ac","ad","ae"]
# exitdf=pd.read_csv("slotdata.csv")
# Total_no_slot=5
# car=""

def car_entry(slotdatapath,slotlist,exitdf,Total_no_slot,car):
    templist=exitdf['car_slotid'].values
    templen=len(templist)
    avial_slot=Total_no_slot-templen
    datadict={}
    datadict["car_id"]=car
    print ("avilable slot size:%s"%avial_slot)
    noslot=0
    if avial_slot!=0:
        secure_random = random.SystemRandom(Total_no_slot)
        print(secure_random)
        car_slotid=secure_random.choice(slotlist)
        if car_slotid not in templist:
            datadict["car_slotid"]=car_slotid
            dfg=pd.DataFrame(datadict, index=['i',])
            dfg.to_csv(slotdatapath,mode='a',index=False,header=False)
        return avial_slot,car_slotid
    else:
        return avial_slot,noslot

def car_exit(slotdatapath,remove_car,exitdf):
    exitdf= exitdf[exitdf.car_slotid != remove_car]
    exitdf.to_csv(slotdatapath,index=False)
    avial_slot=len(exitdf)
    return remove_car,avial_slot



#Exit car
# remove_car=input("car id: ")
# exitdf= exitdf[exitdf.car_slotid != remove_car]
# exitdf.to_csv("slotdata.csv",index=False)







# This is a method to help you convert one range for another.  
#There are no checks to ensure that the old limits and 
#new limits are porportional, as in the old lower limt is less than the old upper limit and likewise for the new limits.

def convert_range(OldValue, OldMax, OldMin, NewMax, NewMin):
    OldValue = OldValue
    OldMax = OldMax
    OldMin = OldMin
    OldRange = (OldMax - OldMin)
    NewMax = NewMax
    NewMin = NewMin
    NewRange = (NewMax - NewMin)
    portion = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    NewValue = NewMin + portion 

    #print (NewValue)
    return (NewValue)
self.convert_range()

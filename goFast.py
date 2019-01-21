#This may need some tweaking, but I think this is the python version of our old go fast trigger command.

def goFast (stickValue,trigger, maxSpeed):
  zoom =(trigger*((1-maxSpeed)/1))+maxSpeed
  if (zoom == 0)
    zoomZoom = stickValue
  else:
    zoomZoom = stickValue*zoom
  return:
    zoomZoom
self.zomZoom()
      
  

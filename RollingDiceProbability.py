#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import random


# In[6]:


#Returning the succes of an event which is getting 6 in a dice throw
def diceResult(i):
    if i==6:
        return True
    else:
        return False        


# In[7]:


#even turn Anupam-2,4,6...
#odd turn Ankita-1,3,5...
def turnDecide(turn):
    rem=turn%2
    if rem==0:
        turn="Anupam"
    else:
        turn="Ankita"
    return turn;


# In[8]:


#function to randomly generate a number from 1 to 6
def diceRoll():
    numOnDice=random.randint(1,6)
    return numOnDice
    


# In[49]:


#function to create  a probability of winning by a respective candidate when dice is rolled alternatively
def probWin(AWInCounter,BWInCounter,totSuccess):    
    totSuccess=AWInCounter+BWInCounter
    probAWin=AWInCounter/(AWInCounter+BWInCounter)
    probBWin=BWInCounter/(AWInCounter+BWInCounter)
    return(probAWin,probBWin)
   
    


# In[54]:


timesRolled=1000# no of times the dice is rolled
def main():
    AWInCounter=0
    BWInCounter=0
    totSuccess=0
    for i in range(timesRolled):       
        numOnDice=diceRoll()
        if diceResult(numOnDice):
            turn=turnDecide(i)
            if(turn=='Ankita'):
                AWInCounter+=1
            elif(turn=='Anupam'):
                BWInCounter+=1
    probAWin,probBWin=probWin(AWInCounter,BWInCounter,totSuccess)
    print("Probability that Ankita Wins:",probAWin)
    print("Probability that Anupam Wins:",probBWin)
main()


# In[ ]:





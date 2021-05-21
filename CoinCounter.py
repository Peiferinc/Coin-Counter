'''
Created on May 20, 2021

@author: Justin Peifer
'''
print('Greetings, I am a program made to test the probability of a coin streak.')
number=input('What streak number are you looking for the probability of?')
number=int(number)
import random
numberOfStreaks = 0
totalflips=0
totalheads=0
hstreak=0
tstreak=0
totalhstreaks=0
totaltstreaks=0
totalstreaks=0
for experimentNumber in range(10000):
    coin=random.randint(0,1)
    print(coin)
    if coin==0:
        coinflip='tails'
    elif coin==1:
        coinflip='heads'
    print(coinflip)
    if coinflip=='heads':
        hstreak+=1
        tstreak=0
        if hstreak==number:
            totalstreaks+=1
            totalhstreaks+=1
            hstreak=0
    if coinflip=='tails':
        tstreak+=1
        hstreak=0
        if tstreak==number:
            totalstreaks+=1
            totaltstreaks+=1
            tstreak=0
            
    #maybe make a list instead, with 6 coins at a time.
    totalflips+=1
    totalheads+=coin
print('Total number of heads is '+ str(totalheads))
print(f'Which is out of "{totalflips} flips. This makes '+str(totalheads/totalflips*100)+'% heads.')
print(f'There were {totalhstreaks} streaks of heads, with {totaltstreaks} streaks of tails. This made for a total of {totalstreaks} streaks. This means that {(totalstreaks*number)/10000*100}% of the coins were in streaks of {number}.')
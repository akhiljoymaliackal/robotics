import gym
env = gym.make('FrozenLake-v0')
env.reset()

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3


print "initial"
env.render()
print "******"
l=[]

count=0

movements=[2,2,1,1,1,2]



for i in range(0,1000):
    for action in movements:


        observation, reward, done, info = env.step(action)
        env.render()
        print observation, reward, done, info
        if done:

            env.reset()
        if reward==1:
            print "Reached goal"



            print i
            count=count+1
        if count>=600:
            l.append(movements)
print count
print l
    #raw_input()

    #raw_input()

#Functions used in preparing Guido's gorgeous lasagna.

#Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum


# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME= int(40)

# TODO: consider defining the 'PREPARATION_TIME' constant

def preparation_time_in_minutes():
    x= int(input('number of layers:'))
    y=2
    return x*y  

print('preparation_time_in_minutes:', preparation_time_in_minutes())
#   y    equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
#a= input('time in the oven:')

 
def bake_time_remaining():
    a= int(input('time in the oven:'))
    return  EXPECTED_BAKE_TIME-a

print('bake_time_remaining:', bake_time_remaining())

#Calculate the bake time remaining.

   # :param elapsed_bake_time: int - baking time already elapsed.
   # :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    #Function that takes the actual minutes the lasagna has been in the oven as
    #an argument and returns how many minutes the lasagna still needs to bake
    #based on the `EXPECTED_BAKE_TIME`

def elapsed_bake_time():
    return EXPECTED_BAKE_TIME-preparation_time_in_minutes()-bake_time_remaining()

print('elapsed bake time:',elapsed_bake_time())
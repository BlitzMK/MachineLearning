# 1 million people have diabetes 
# some have thier eyes effected
# they have to see the doctor every month to catagorize where they fall 1,2, or 3
# some catagories get more medician, must see a doctor, 
# 7 images are needed to be seen by a doctor 
# process takes 2 hours for a doctor 
# 1 doctor can see 3 patients a day 

# 1 = good, 2 =change in dose, 3 means they must need to see a doctor imediatly 
# doctor will see to find 14 features in the eye 7 for each eye 
# predicting the target variable of catagory 

# Find a way to analyze the 7 feature for each eye for the doctor to veiw in an image 



# 1. measure the 7 features of each eye 
# 2. decode those features into the catagory it most belongs
# 3.a cat =1 nothing is needed 
# 3.b cat=2 dosing is changed and no action is needed by a doctor
# 3.c cat=3 patient is called into a meeting with a doctor 


# assuming each of these features are boolean values. either they are there or they are not 
# each catagory has its own condition
# defualt is catagory 1


# function( bool[14] features)
# match features 
#   case(cat1_conditions):
#       exit
#   case(cat2Conditions):
#       catagory 2 actions 
#   case(cat3Conditions):
#       catagory 3 actions
#   defualt: cat 1 actions 
# return 
# String in Python--   A string is a sequence (collection) of characters enclosed in single quotes (' '), double 
#                      quotes (" "), or triple quotes (''' ''' or """ """).
# A string can contain:
#            * Letters (A-Z, a-z)
#            * Numbers (0-9)
#            * Symbols (@, #, $, %, etc.)
#            * Spaces

# Methods of string--
#            * .capitalize()
#            * .lower()
#            * .upper()
#            * .list()
#            * .srip() , etc.  

#NOTE-
#    slice-- [start:stop:step]

#----------------------------------------------------------------------------------------------------------------------

# LIST--

# Even values in list--
val = [1,2,3,4,5,6,7,8,9]
new_list = [ x for x in val if x%2==0]
print(new_list)

# Odd values in list--
val = [1,2,3,4,5,6,7,8,9]
new_list = [ x for x in val if x%2!=0]
print(new_list)

# List Comprehension--
val = [1,2,3,4,5]
new_list = [ a*2 for a in val ]
print(new_list)

#---------------------------------------------------------------------------------------------------------------------------

# TUPLE--  A tuple is an ordered collection of items in Python. It is written inside round brackets () and can store
#          different types of data.
#          Important: A tuple is immutable, which means its values cannot be changed after it is created.
#       Syntax=   tuple_name = (value1, value2, value3)

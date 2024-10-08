#Selecting Columns and Custom Slicing Ndarrays
#Select every row for the columns at indices 1, 4, and 7. Assign the result to columns_1_4_7
columns_1_4_7 = taxi[:,[1, 4, 7]]
#Select the columns at indices 5 to 8 inclusive for the row at index 99. Assign the result to row_99_columns_5_to_8
row_99_columns_5_to_8 = taxi[99, 5: 9]
#Select the rows at indices 100 to 200 inclusive for the column at index 14. Assign the result to rows_100_to_200_column_14.
rows_100_to_200_column_14 = taxi[100:201, 14]


#Vector Operations
#From the provided taxi ndarray:
#Add the fare_amount and fees_amount arrays element-wise. Assign the result to a new variable called fare_and_fees
fare_amount = taxi[:, 9]
fees_amount = taxi[:, 10]
fare_and_fees = fare_amount + fees_amount
print(fare_and_fees)


#Boolean Indexing with 2D Ndarrays
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]
                ])
bool_1 = [True, False, True, True ]
bool_2 = [True, False, True]
print(arr[bool_1]) # row filtering
print(arr[:,bool_2]) # column filtering

c = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]
                ])
c[c[:, 1] > 2, 1] = 99
print(c)
print(c[:, 1])
print(c[:, 1] > 2)
''' The Boolean operation c[:, 1] > 2 selects the the second column of c for comparison and creates a 1D Boolean array based on the values of that column being > 2 or not. We then use the resulting Boolean array as the row index for assignment and we use 1 as the column index for assignment. This ensures we select the proper rows and columns before we assign the value of 99 to them (c[c[:, 1] > 2, 1] = 99). This way, only the second column will (possibly) have its values changed, and all other columns will remain untouched.'''

#the explanation of the concept
row_idx_for_assignment = array[:, col_idx_for_comparison] == value_for_comparison
array[row_idx_for_assignment, col_idx_for_assignment] = new_value

array[array[:, col_idx_for_comparison] == value_for_comparison, col_idx_for_assignment] = new_value

#Example case
#the extended way
x = taxi[:, 5]
x_bool = x == 5
x_need = taxi[x_bool, 5]
x_count = x_need.shape[0]


#the streamlined way of boolean assignment
jfk = taxi[taxi[:, 5] == 2, 5]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:, 5] == 3, 5]
laguardia_count= laguardia.shape[0]

newark = taxi[taxi[:, 5] == 5, 5]
newark_count = newark.shape[0]

busiest_airport = 'laguardia'

# Create the variables trip_distance_miles, trip_length_seconds, and trip_length_hours as shown above in the Learn section.
trip_distance_miles = taxi[:, 7]
trip_length_seconds = taxi[:, 8]
trip_length_hours = trip_length_seconds / 3600
trip_mph = trip_distance_miles / trip_length_hours
print(trip_mph[:10])


# extract the first 5 rows only
taxi_first_five = taxi[:5]
print(taxi_first_five)
# select columns: fare_amount, fees_amount, tolls_amount, and tip_amount
fare_components = taxi_first_five[:, 9:13]
fare_sums = fare_components.sum(axis = 1)
fare_totals = taxi_first_five[:, 13]
print('fare total : ', fare_totals, '\n', 'fare sums', fare_sums)


#Boolean Arrays : Use vectorized Boolean operations to do the following
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
#Evaluate whether the elements in array a are less than 3. Assign the result to a_bool
a_bool = a < 3
#Evaluate whether the elements in array b are equal to "blue". Assign the result to b_bool
b_bool = b == 'blue'
#Evaluate whether the elements in array c are greater than 100. Assign the result to c_bool
c_bool = c > 100

# numpy-clone

I'm currently learning about machine learning, and it seemed useful to reimplement some numpy functions, and later on some PyTorch functions in order to learn how it actually works.

Current Functionality:

#### Create an array

`arr = clone.Array([1, 2, 3])`

#### Print entire array

`print(arr)` output: [1, 2, 3]

#### Get value at index

`print(arr[2])` output: 3

#### Set value at index

`arr[2] = 5` arr = [1, 2, 5]

#### Get size of array

`print(arr.size)` output: 3

#### Add two arrays

`arr2 = clone.Array([4, 5, 6]) + arr` arr2 = [5, 7, 11]

#### Subtract two arrays

`arr3 = arr - arr2` arr3 = [-4, -5, -6]

#### Multiply two arrays

`arr4 = arr * arr3` arr4 = [-4, -10, -30]

#### Divide two arrays

`arr5 = arr / arr` arr5 = [1, 1, 1]

#### Increase size of array, and fill excess with value (defualt is zero)

`arr.increase_size(5, fill_value=2)` arr = [1, 2, 5, 2, 2]

#### Append value to array

`arr.append(15)` arr = [1, 2, 5, 2, 2, 15]

#### Return sum of all elements in array

`print(arr.sum())` output: 27

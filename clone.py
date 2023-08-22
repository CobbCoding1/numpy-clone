class Array():
    def __init__(self, data, ndim=0):
        self.data = data
        self.size = len(data)

    def compare_type_and_size(self, other):
        if isinstance(other, Array) and len(self) == len(other):
            return(True)
        else:
            return(False)

    def __getItem__(self, index):
        return(self.data[index])

    def __setItem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return(self.size)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if self.compare_type_and_size(other):
            new_data = [x + y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        elif len(self) != len(other):
            raise ValueError("Arrays must have the same length")
        else:
            raise TypeError("An Array cannot be added to a non-Array type!")

    def __sub__(self, other):
        if self.compare_type_and_size(other):
            new_data = [x - y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        elif len(self) != len(other):
            raise ValueError("Arrays must have the same length")
        else:
            raise TypeError("An Array cannot be added to a non-Array type!")

    def __mul__(self, other):
        if self.compare_type_and_size(other):
            new_data = [x * y for x, y in zip(self.data, other.data)]
            return Array(new_data) 
        elif len(self) != len(other):
            raise ValueError("Arrays must have the same length!")
        else:
            raise TypeError("An Array cannot be added to a non-Array type!")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_data = [x / other for x in self.data]
            return Array(new_data)
        elif self.compare_type_and_size(other):
            new_data = [x / y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        elif len(self) != len(other):
            raise ValueError("Arrays must have the same length!")
        else:
            raise TypeError("An array cannot be added to a non-Array type!")

arr1 = Array([1, 2, 3])
arr2 = Array([2, 4, 6])

print(arr1)
        
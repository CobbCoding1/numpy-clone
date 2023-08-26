from types import NoneType


class Array():
    def __init__(self, data, ndim=0):
        self.data = data
        self.size = len(data)
        if self.size != 0:
            self.shape = self.calculate_shape(data)

    def calculate_shape(self, data):
        shape = []
        while isinstance(data, list):
            shape.append(len(data))
            data = data[0]
        return(tuple(shape))

    def compare_type_and_size(self, other):
        if isinstance(other, Array) and len(self) == len(other):
            return(True)
        elif not isinstance(other, Array):
            return(TypeError)
        else:
            return(ValueError)

    def handle_errors(self, error, operation):
        if error == ValueError:
            raise ValueError("Arrays must have the same length")
        elif error == TypeError:
            raise TypeError(f"An Array cannot be {operation} a non-Array type!")

    def increase_size(self, new_size, fill_value=0):
        if(new_size < self.size):
            raise IndexError("Cannot reduce the size of the array through extension")
        diff = new_size - len(self)
        self.data.extend([fill_value] * diff)
        self.size = new_size

    def append(self, value):
        self.data.append(value)
        self.size += 1

    def sum(self):
        value = 0
        for elem in self.data:
            if not isinstance(elem, (int, float)):
                raise TypeError("Sum can only be calculated on arrays of types of int or float")
            value += elem 
        return(value)

    def mean(self):
        value = 0
        for elem in self.data:
            if not isinstance(elem, (int, float)):
                raise TypeError("Mean can only be calculated on arrays of types of int or float")
            value += elem
        return(value/self.size)

    def product(self):
        value = 1
        for elem in self.data:
            if not isinstance(elem, (int, float)):
                raise TypeError("Product can only be calculated on arrays of types of int or float")
            value *= elem
        return(value)

    def __getitem__(self, index):
        if isinstance(index, slice):
            if isinstance(index.stop, NoneType):
                if(index.start >= self.size):
                    raise IndexError("Array slice index out of range")
                else:
                    return(self.data[index])
            if(index.stop > self.size or index.stop == 0):
                raise IndexError("Array slice index out of range")
            else:
                return(self.data[index])
        else:
            if(index > self.size):
                raise IndexError("Array index out of range")
            return(self.data[index])

    def __setitem__(self, index, value):
        if(index >= self.size):
            raise IndexError("Array index out of range")
        self.data[index] = value

    def __len__(self):
        return(self.size)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        if len(self.shape) == 1:
            compared = self.compare_type_and_size(other)
            if compared == True:
                new_data = [x + y for x, y in zip(self.data, other.data)]
                return Array(new_data)
            else:
                return(self.handle_errors(compared, "added to"))
        else:
            return "Not implemented yet"

    def __sub__(self, other):
        if len(self.shape) == 1:
            compared = self.compare_type_and_size(other)
            if compared == True:
                new_data = [x - y for x, y in zip(self.data, other.data)]
                return Array(new_data)
            else:
                return(self.handle_errors(compared, "subtracted from"))
        else:
            return "Not implemented yet"

    def __mul__(self, other):
        if len(self.shape) == 1:
            compared = self.compare_type_and_size(other)
            if compared == True:
                new_data = [x * y for x, y in zip(self.data, other.data)]
                return Array(new_data) 
            else:
                return(self.handle_errors(compared, "multiplied by"))
        else:
            return self.matmul(other)
    
    def matmul(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape Error")
        r = Array([]) 
        m = Array([])
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                sums = 0
                for k in range(len(other.data)):
                    sums = sums + (self.data[i][k] * other.data[k][j])
                r.append(sums)
            m.append(r)
            r = Array([])
        return m

    def __truediv__(self, other):
        if len(self.shape) == 1:
            if isinstance(other, (int, float)):
                new_data = [x / other for x in self.data]
                return Array(new_data)
            
            compared = self.compare_type_and_size(other)
            if compared == True:
                new_data = [x / y for x, y in zip(self.data, other.data)]
                return Array(new_data)
            else:
                return(self.handle_errors(compared, "divided by"))
        else:
            return "Not implemented yet"

    # Aliases
    average = mean

if __name__ == "__main__":
    arr1 = Array([[1, 0], [0, 1]])
    arr2 = Array([1, 2])
    print(arr2.shape, arr1.shape)

    arr3 = arr2 * arr1
    print(arr3)

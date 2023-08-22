from types import NoneType


class Array():
    def __init__(self, data, ndim=0):
        self.data = data
        self.size = len(data)

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
        compared = self.compare_type_and_size(other)
        if compared == True:
            new_data = [x + y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        else:
            return(self.handle_errors(compared, "added to"))

    def __sub__(self, other):
        compared = self.compare_type_and_size(other)
        if compared == True:
            new_data = [x - y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        else:
            return(self.handle_errors(compared, "subtracted from"))

    def __mul__(self, other):
        compared = self.compare_type_and_size(other)
        if compared == True:
            new_data = [x * y for x, y in zip(self.data, other.data)]
            return Array(new_data) 
        else:
            return(self.handle_errors(compared, "multiplied by"))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_data = [x / other for x in self.data]
            return Array(new_data)
        
        compared = self.compare_type_and_size(other)
        if compared == True:
            new_data = [x / y for x, y in zip(self.data, other.data)]
            return Array(new_data)
        else:
            return(self.handle_errors(compared, "divided by"))


if __name__ == "__main__":
    arr1 = Array([1, 2, 3])
    arr2 = Array([2, 4, 6])

    print(arr1[1:3])
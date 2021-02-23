import data as dt
import suggest as sg


# Test #1
print("1. Loading data: ")
a = dt.load()

if a is None:
    print("fail")


# Test 2
print("2. Preparing data: ")
b = dt.prepare(a)

if b is None:
    print("fail")
else:
    assert (b['Julia']['Ilhabela/SP'] == 1.0), "fail, value not equal"


# Test 3
assert sg.psimilar(9) == 0.1, "fail, percentual"
assert sg.euclidian([4,8],[1,4]) == 5, "fail, distance euclidian"


# Test 4
assert round(sg.similar(b, 'Evelyn', 'Antonio'),2) == 6.93, "fail, distanct between users"


# Test 5
t5 = sg.getsimilaruser(b, 'Evelyn')
assert round(t5['Antonio'],4) == 0.1261, "fail, users similars"

# Test 6
t6 = sg.getsuggest(b, 'Luis')
assert round(t6['Ilhabela/SP'], 2) == 2.65, "fail, suggestions"


from Rectangle import SpaceOfRectangle , CheckSpace


def test_area():
    rectangle1 = SpaceOfRectangle(10,50)

    assert rectangle1.area() == 500

    rectangle2 = SpaceOfRectangle(0,50)

    assert rectangle2.area() == 0

def test_check_False():
    rec1 = SpaceOfRectangle(10,0)

    assert CheckSpace(rec1).Check() == False


#ّpip install pytest
#pytest
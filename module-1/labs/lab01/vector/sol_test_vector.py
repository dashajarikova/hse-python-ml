import unittest

try:
    from sol_vector import Vector
except (ModuleNotFoundError, ImportError):
    from vector import Vector


class TestVector(unittest.TestCase):

    def test_inheritance(self):
        self.assertTrue(issubclass(Vector, list))
        self.assertIsInstance(Vector([1, 2, 3]), list)

    def test_repr(self):
        v = Vector([1, 2, 3])

        self.assertEqual(str(v), "Vector([1, 2, 3])")
        self.assertEqual(repr(v), str(v))

        v = Vector([1.0, 2, 3.0])

        self.assertEqual(str(v), "Vector([1.0, 2, 3.0])")
        self.assertEqual(repr(v), str(v))

    def test_add(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a + a, Vector([2, 4, 6, 8]))
        self.assertEqual(b + a, Vector([4, 6, 8, 10]))
        self.assertEqual(a + 1, Vector([2, 3, 4, 5]))
        self.assertEqual(b + 3.1, Vector([6.1, 7.1, 8.1, 9.1]))

        self.assertRaises(TypeError, a.__add__, "a")

    def test_sub(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a - a, Vector([0, 0, 0, 0]))
        self.assertEqual(b - a, Vector([2, 2, 2, 2]))
        self.assertEqual(a - 1, Vector([0, 1, 2, 3]))
        self.assertEqual(b - 3.0, Vector([0.0, 1.0, 2.0, 3.0]))

        self.assertRaises(TypeError, a.__sub__, "a")

    def test_mul(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a * a, Vector([1, 4, 9, 16]))
        self.assertEqual(b * a, Vector([3, 8, 15, 24]))
        self.assertEqual(a * 2, Vector([2, 4, 6, 8]))
        self.assertEqual(b * (- 3.0), Vector([-9.0, -12.0, -15.0, -18.0]))

    def test_truediv(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a / a, Vector([1.0, 1.0, 1.0, 1.0]))
        self.assertEqual(b / a, Vector([3.0, 2.0, 1.6666666666666667, 1.5]))
        self.assertEqual(a / 2, Vector([0.5, 1.0, 1.5, 2.0]))
        self.assertEqual(
            b / (- 3.0),
            Vector([-1.0, -1.3333333333333333, -1.6666666666666667, -2.0])
        )

        self.assertRaises(TypeError, a.__truediv__, "a")

    def test_floordiv(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a // a, Vector([1, 1, 1, 1]))
        self.assertEqual(b // a, Vector([3, 2, 1, 1]))
        self.assertEqual(a // 2, Vector([0, 1, 1, 2]))
        self.assertEqual(
            b // (- 3.0),
            Vector([-1.0, -2.0, -2.0, -2.0])
        )

        self.assertRaises(TypeError, a.__floordiv__, "a")

    def test_pow(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a ** 2, Vector([1, 4, 9, 16]))
        self.assertEqual(b ** 2, Vector([9, 16, 25, 36]))
        self.assertEqual(
            pow(a, 0.5),
            Vector([1.0, 1.4142135623730951, 1.7320508075688772, 2.0])
        )
        self.assertEqual(
            pow(b, 1.5),
            Vector(
                [
                    5.196152422706632, 8.0,
                    11.180339887498949, 14.696938456699069
                ]
            )
        )

        self.assertRaises(TypeError, a.__pow__, "a")

    def test_abs(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(abs(a - b), 4.0)
        self.assertEqual(abs(a),  5.477225575051661)
        self.assertEqual(abs(b), 9.273618495495704)

    def test_neg(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(- a - b, Vector([-4, -6, -8, -10]))
        self.assertEqual(- a * 2, Vector([-2, -4, -6, -8]))
        self.assertEqual(- b - 1, Vector([-4, -5, -6, -7]))

    def test_argmax(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a.argmax(), 3)
        self.assertEqual(b.argmax(), 3)
        self.assertEqual((- a - b).argmax(), 0)
        self.assertEqual((- a * 2).argmax(), 0)
        self.assertEqual(Vector([2, -2, 3]).argmax(), 2)

    def test_argmin(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([3, 4, 5, 6])

        self.assertEqual(a.argmin(), 0)
        self.assertEqual(b.argmin(), 0)
        self.assertEqual((- a - b).argmin(), 3)
        self.assertEqual((- a * 2).argmin(), 3)
        self.assertEqual(Vector([2, -2, 3]).argmin(), 1)

    def test_ndim(self):
        self.assertEqual(Vector([1, 2, 3]).ndim(), len(Vector([1, 2, 3])))
        self.assertEqual(
            Vector([1, 2, 3, 4]).ndim(), len(Vector([1, 2, 3, 4]))
        )
        self.assertEqual(Vector([]).ndim(), len(Vector([])))
        self.assertEqual(Vector([1, 2]).ndim(), len(Vector([1, 2])))
        self.assertEqual(Vector([5, 5]).ndim(), 2)


if __name__ == "__main__":
    unittest.main()

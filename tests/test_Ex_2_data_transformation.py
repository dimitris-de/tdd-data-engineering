import unittest
from hypothesis import given, strategies as st # type: ignore
from src.Ex_2_data_transformation import calculate_mean, calculate_sum, normalize_column


class TestDataTransformation(unittest.TestCase):

    #This line instructs Hypothesis to generate test inputs for your test function.
    #Hypothesis is a powerful testing library for Python that enables property-based testing.
    # Instead of writing specific test cases, you define general properties that your code should satisfy, 
    # and Hypothesis generates a wide range of inputs to test these properties.
    # Reduces the need to manually write multiple test cases with different inputs

    @given(st.lists(
        st.floats(
            min_value=-1e6,
            max_value=1e6,
            allow_nan=False,
            allow_infinity=False
        ),
        min_size=1  # Ensure at least one element to avoid division by zero
    ))
    def test_normalize_column(self, numbers):
        """
        Test normalize_column with a wide range of float inputs within a reasonable range.
        """
        result = normalize_column(numbers)
        # Assertions
        self.assertEqual(len(result), len(numbers))
        for value in result:
            if value is not None:
                self.assertGreaterEqual(value, 0.0)
                self.assertLessEqual(value, 1.0)


    def test_calculate_sum(self):
        """
        Test that calculate_sum correctly sums the values.
        """
        data = [1, 2, 3, 4, 5]
        total = calculate_sum(data)
        self.assertEqual(total, 15)

    def test_calculate_mean(self):
        """
        Test that calculate_mean correctly calculates the mean.
        """
        data = [1, 2, 3, 4, 5]
        mean = calculate_mean(data)
        self.assertEqual(mean, 3.0)




if __name__ == '__main__':
    unittest.main()

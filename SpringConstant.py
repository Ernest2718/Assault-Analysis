"""
Ernest Lee Mitchell
Wright State University
November 12, MMXXV
"""

"""
This code computes the total spring stiffness for a cluster of springs
in parallel or in series.
"""

class Spring_Constant_Calculator:
    """
    A class to compute the equivalent spring stiffnesses for series and parallel mechanical circuits.
    """
    # Initialize the class.
    def __init__(self, stiffness):
        """
        Initializes the Spring_Constant_Calculator with a list or tuple of stiffness values.
        Args:
            stiffness (list or tuple): A collection of individual stiffness values (floats or ints).
        Returns:
            The total stiffness.
        """
        self.stiffness = stiffness

    # Compute parallel stiffness if springs are in parallel.
    def parallel_stiffness(self):
        """
        Calculates the total spring stiffnesses in parallel.
        Formula: k_total = k1 + k2 + k3 + ... + kn

        Implementation in main method:
        Create an instance for parallel calculation.
            parallel_stiffness = [k1, ... , kn] # Values in Newton/meter.
            parallel_calc = Spring_Constant_Calculator(parallel_stiffness)
            k_parallel = parallel_calc.parallel_stiffness()
        """
        total_stiffness = sum(self.stiffness)
        # Return sum parallel stiffness.
        return total_stiffness

    # Compute series stiffness if springs are in series.
    def series_stiffness(self):
        """
        Calculates the total spring stiffnesses in series.
        Formula: 1/k_total = 1/k1 + 1/k2 + 1/k3 + ... + 1/kn

        Implementation in main method:
        Create an instance for series calculation.
            series_stiffness = [k1, ... , kn] # Values in Newton/meter.
            series_calc = Spring_Constant_Calculator(series_stiffness)
            k_series = series_calc.series_stiffness()
        """
        # Calculate the sum of the reciprocals (compliance, square second/kilogram).
        sum_of_reciprocals = 0 # Initialize sum of reciprocals.
        for r in self.stiffness:
            if r == 0:
                # Handle cases where a spring stiffness is 0 N/m.
                return 0.0
            # Update summation.
            sum_of_reciprocals += 1 / r
        
        # The total spring constant is the reciprocal of the sum of reciprocals
        if sum_of_reciprocals == 0:
            return 0.0
        total_stiffness = 1 / sum_of_reciprocals
        # Return sum series stiffness.
        return total_stiffness
    
"""
Ernest Lee Mitchell
Wright State University
November 1, MMXXV
"""

"""
This code features dictionary that converts US customary standard to the metric standard of measurement.
"""

class UStoMetricConverter:
    """
    A class to convert common US customary units to metric units.

    Implementation in main method:
    Create an instance for UStoMtetricConverter.
        converter = UStoMetricConverter()
        <conversion> = converter.<us_customary_to_metric>
    """
    # Conversion factors (based on 1 unit of US customary.)
    # Stored as: Dictionary featuring the following conversion factors: {unit_name: factor_to_base_metric_unit}
    _conversion_factors = {
        'inch_to_cm': 2.54,
        'foot_to_m': 0.3048,
        'yard_to_m': 0.9144,
        'mile_to_km': 1.60934,
        'pound_to_kg': 0.453592,
        'gallon_to_l': 3.78541,
        'ounce_to_g': 28.3495,
        'fahrenheit_to_celsius_offset': -32,
        'fahrenheit_to_celsius_factor': 5/9
    }

    # Helper method for any conversion.
    def _convert(self, value, factor_key):
        """Internal helper method for simple conversions."""
        factor = self._conversion_factors.get(factor_key)
        if factor is None:
            raise ValueError(f"Conversion factor for '{factor_key}' not found.")
        return value * factor

    # I: Length Conversions.
    # Inches to centimeters.
    def inches_to_cm(self, inches):
        """Converts inches to centimeters."""
        return self._convert(inches, 'inch_to_cm')
    
    # Feet to meters.
    def feet_to_meters(self, feet):
        """Converts feet to meters."""
        return self._convert(feet, 'foot_to_m')

    # Yards to meters.
    def yards_to_meters(self, yards):
        """Converts yards to meters."""
        return self._convert(yards, 'yard_to_m')
    
    # Miles to kilometers.
    def miles_to_km(self, miles):
        """Converts miles to kilometers."""
        return self._convert(miles, 'mile_to_km')

    # II: Weight/Mass Conversions.
    # Pounds mass to kilograms.
    def pounds_to_kg(self, pounds):
        """Converts pounds to kilograms."""
        return self._convert(pounds, 'pound_to_kg')

    # Ounces to grams.
    def ounces_to_grams(self, ounces):
        """Converts ounces to grams."""
        return self._convert(ounces, 'ounce_to_g')

    # III: Volume Conversions
    # Gallons to liters.
    def gallons_to_liters(self, gallons):
        """Converts gallons (US liquid) to liters."""
        return self._convert(gallons, 'gallon_to_l')
        
    # IV: Temperature Conversion
    # Degree Fahrenheit to degree Celcius.
    def fahrenheit_to_celsius(self, fahrenheit):
        """Converts Fahrenheit to Celsius."""
        offset = self._conversion_factors['fahrenheit_to_celsius_offset']
        factor = self._conversion_factors['fahrenheit_to_celsius_factor']
        return (fahrenheit + offset) * factor
    
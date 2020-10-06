import conversions as con
import unittest
class conversionTest(unittest.TestCase):
    def testConversions(self):
        self.assertEqual(con.convertCelsiusToKelvin(300.00), 0)
        self.assertEqual(con.convertCelsiusToKelvin(1.00), 0)
        self.assertEqual(con.convertCelsiusToKelvin(135.00), 0)
        self.assertEqual(con.convertCelsiusToKelvin(95.00), 0)
        self.assertEqual(con.convertCelsiusToKelvin(32.00), 0)

        self.assertEqual(con.convertCelsiusToFahrenheit(300.00), 0)
        self.assertEqual(con.convertCelsiusToFahrenheit(0.00), 0)
        self.assertEqual(con.convertCelsiusToFahrenheit(25.00), 0)
        self.assertEqual(con.convertCelsiusToFahrenheit(36.50), 0)
        self.assertEqual(con.convertCelsiusToFahrenheit(150.00), 0)

        self.assertEqual(con.convertKelvinToFahrenheit(300.00), 0)
        self.assertEqual(con.convertKelvinToFahrenheit(0.00), 0)
        self.assertEqual(con.convertKelvinToFahrenheit(25.00), 0)
        self.assertEqual(con.convertKelvinToFahrenheit(36.50), 0)
        self.assertEqual(con.convertKelvinToFahrenheit(150.00), 0)

        self.assertEqual(con.convertKelvinToCelsius(300.00), 0)
        self.assertEqual(con.convertKelvinToCelsius(0.00), 0)
        self.assertEqual(con.convertKelvinToCelsius(25.00), 0)
        self.assertEqual(con.convertKelvinToCelsius(36.50), 0)
        self.assertEqual(con.convertKelvinToCelsius(150.00), 0)

        self.assertEqual(con.convertFahrenheitToKelvin(300.00), 0)
        self.assertEqual(con.convertFahrenheitToKelvin(0.00), 0)
        self.assertEqual(con.convertFahrenheitToKelvin(25.00), 0)
        self.assertEqual(con.convertFahrenheitToKelvin(36.50), 0)
        self.assertEqual(con.convertFahrenheitToKelvin(150.00), 0)

        self.assertEqual(con.convertFahrenheitToCelsius(300.00), 0)
        self.assertEqual(con.convertFahrenheitToCelsius(0.00), 0)
        self.assertEqual(con.convertFahrenheitToCelsius(25.00), 0)
        self.assertEqual(con.convertFahrenheitToCelsius(36.50), 0)
        self.assertEqual(con.convertFahrenheitToCelsius(150.00), 0)

if __name__ == '__main__':
    unittest.main()

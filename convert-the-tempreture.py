class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Far = celsius * 1.80 + 32.00
        Kelvin = celsius + 273.15
        return [Kelvin,Far]

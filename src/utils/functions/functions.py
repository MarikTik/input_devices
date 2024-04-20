from ..type_hints import number_t, range_t

def map(value: number_t, from_low: number_t, from_high: number_t, to_low: number_t, to_high: number_t) -> number_t:
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low


def range_adjust(value, blindspot_range: range_t, bounds: range_t, zero: number_t = None) -> number_t:
     if zero is None:
            zero = (bounds[0] + bounds[1]) / 2

     blindspot_start, blindspot_end = blindspot_range
     bounds_start, bounds_end = bounds
     if blindspot_start <= value <= blindspot_end:
         return 0
     
     elif value < blindspot_start:
         return map(value, bounds_start, blindspot_start, bounds_start, zero - 1)
     
     return map(value, blindspot_end, bounds_end, zero + 1, bounds_end)
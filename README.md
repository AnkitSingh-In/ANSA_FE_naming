# ANSA_FE_naming
## Assign names to FE based on your preference or customer specific request.

Bleow are some examples that common naming convension follow in industries.
Let say you have a CAD name in follwing format: 
first_8_digits.version_number-gate_number program_number(product_name).product_unique_id
### e.g.1 
    CAD naming = BDE84572.002-2458 VFI(FUEL-CAP).8426
    Based on above CAD name we want to assigne name to its correspoding FE base on folling points.
    1. Replace every punctuation, spaces with '_'
    2. Add Nodel thickness in end with 'mm' as suffix.

### Senario 1
    FE_naming = first_8_digits_user_provided_distigusers_thickness
    
### Senario 2
    FE_naming = fullname_thickness
    

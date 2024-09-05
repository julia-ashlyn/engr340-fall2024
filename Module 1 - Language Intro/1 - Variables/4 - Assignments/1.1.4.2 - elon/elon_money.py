"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###
P = 33000000000
N_1 = 10
N_2 = 20
R_1 = 3.96
R_2 = 4.32

# final answer for 10-year
ten_year_final = P * ((1 + (R_1/100)) ** N_1)
print(ten_year_final)

# final answer for 20-year
twenty_year_final = P * ((1 + (R_2/100)) ** N_2)
print(twenty_year_final)
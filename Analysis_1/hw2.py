from whatif import Model
from whatif import get_sim_results_df

class SingleProductSPF(Model):
    """HW2 model"""
    def __init__(self, fixed_cost = 5000, var_cost = 100, selling_price = 115,
                 spf_constant = 4900, spf_linear = -35, spf_quadratic = 0.06):
        self.fixed_cost = fixed_cost
        self.var_cost = var_cost
        self.selling_price = selling_price
        self.spf_constant = spf_constant
        self.spf_linear = spf_linear
        self.spf_quadratic = spf_quadratic

hw2_model = SingleProductSPF()
print(hw2_model)
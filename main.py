from get_data import GetData
from form_input import FormInput
import os

ZILLOW_URL = os.environ['ZILLOW_LINK']


data = GetData(ZILLOW_URL)
housing_data = data.get_info()


get_form = FormInput()
input_data = get_form.input_info(housing_data)




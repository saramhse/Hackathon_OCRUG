  
def onehotnames():
    onehotlist = ['age', 'balance', 'month', 'duration', 'campaign', 'previous',
       'day_bin_(0, 7]', 'day_bin_(7, 14]', 'day_bin_(14, 21]',
       'day_bin_(21, 28]', 'day_bin_(28, 31]', 'pdays_bin_(-2, -1]',
       'pdays_bin_(-1, 0]', 'pdays_bin_(0, 400]', 'pdays_bin_(400, 900]',
       'job_admin.', 'job_blue-collar', 'job_entrepreneur', 'job_housemaid',
       'job_management', 'job_other', 'job_retired', 'job_self-employed',
       'job_services', 'job_student', 'job_technician', 'job_unemployed',
       'marital_divorced', 'marital_married', 'marital_single',
       'education_other', 'education_primary', 'education_secondary',
       'education_tertiary', 'default_no', 'default_yes', 'housing_no',
       'housing_yes', 'loan_no', 'loan_yes', 'contact_cellular',
       'contact_other', 'contact_telephone', 'poutcome_DNE',
       'poutcome_failure', 'poutcome_other', 'poutcome_success']
    return onehotlist